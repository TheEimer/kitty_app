import datetime
import json
import os
from pathlib import Path

import uvicorn
from reactpy import component, hooks, html
from reactpy.backend.starlette import configure
from starlette.applications import Starlette

from src.list_utils import CountItem, DailyItem, IrregularItem

if Path("last_workout.jsonl").exists():
    baseline_data_list = []
    with open("last_workout.jsonl", "r") as f:
        for line in f:
            baseline_data_list.append(json.loads(line))
    baseline_data = {
        "reps": [set_data["reps"] for set_data in baseline_data_list],
        "weight": [set_data["weight"] for set_data in baseline_data_list],
        "time": [set_data["time"] for set_data in baseline_data_list],
        "date": [set_data["date"] for set_data in baseline_data_list],
        "set_number": [set_data["set_number"] for set_data in baseline_data_list],
        "name": [set_data["name"] for set_data in baseline_data_list],
    }
else:
    baseline_data = {
        "reps": 0,
        "weight": 0,
        "time": 0,
        "date": 0,
        "set_number": 0,
        "name": "",
    }


@component
def RejList():
    checklist = [
        html.link(
            {"rel": "stylesheet", "href": "https://cdn.simplecss.org/simple.min.css"}
        )
    ]
    water_glasses, set_water = hooks.use_state(0)

    water_counter = CountItem(
        "water",
        "Drink 8 glasses of water",
        "Wow, you've had 8 glasses of water today!",
        water_glasses,
        8,
        set_water,
    )
    checklist.append(water_counter)

    walk_check, set_walk = hooks.use_state(0)
    walk_item = DailyItem(
        "walk",
        "Take a 10 minute relaxing walk",
        "Nice work, I hope you enjoyed your walk!",
        walk_check,
        set_walk,
    )

    selfcare_check, set_selfcare = hooks.use_state(0)
    selfcare_item = DailyItem(
        "selfcare",
        "Do at least one selfcare activity (e.g. read for 10 minutes or take a bath)",
        "I'm glad you're taking care of yourself!",
        selfcare_check,
        set_selfcare,
    )

    fruit_check, set_fruit = hooks.use_state(0)
    fruit_item = DailyItem(
        "fruit",
        "Eat at least three servings of fruit or vegetables",
        "Way to go, you've had your greens & reds today!",
        fruit_check,
        set_fruit,
    )

    bedtime_check, set_bedtime = hooks.use_state(0)
    bedtime_item = IrregularItem(
        "bedtime",
        "Go to bed by 21:30",
        "Good night and sweet dreams, sleepyhead!",
        bedtime_check,
        set_bedtime,
        [0, 1, 2, 3, 4],
    )

    cardio_check, set_cardio = hooks.use_state(0)
    cardio_item = IrregularItem(
        "cardio",
        "Do about 30 minutes of cardio",
        "Awesome, you've done your cardio today!",
        cardio_check,
        set_cardio,
        [2, 5],
    )

    datenight_check, set_datenight = hooks.use_state(0)
    datenight_item = IrregularItem(
        "datenight",
        "Enjoy date night",
        "I hope you had a great time on our date!",
        datenight_check,
        set_datenight,
        [4],
    )

    todo_list_check, set_todo_list = hooks.use_state(0)
    todo_list_item = IrregularItem(
        "todo_list",
        "Make a to-do list for the week",
        "You've got the week handled!",
        todo_list_check,
        set_todo_list,
        [6],
    )

    workout_option, set_option = hooks.use_state("away")
    workout_done, set_workout_done = hooks.use_state(0)
    workout_item = IrregularItem(
        "workout",
        "Do some strength training",
        "Nice, you've done your strength training today!",
        workout_done,
        set_workout_done,
        [1, 3],
        True,
        workout_option,
        set_option,
        baseline_data,
    )

    if workout_done == 2:
        return workout_item

    checklist.append(walk_item)
    checklist.append(selfcare_item)
    checklist.append(fruit_item)

    # Make sure current items are at the top of the list
    optionals = [
        {"days": [6], "item": todo_list_item},
        {"days": [4], "item": datenight_item},
        {"days": [2, 5], "item": cardio_item},
        {"days": [0, 1, 2, 3, 4], "item": bedtime_item},
        {"days": [1, 3], "item": workout_item},
    ]
    for o in optionals:
        if datetime.datetime.today().weekday() in o["days"]:
            checklist.append(o["item"])
    for o in optionals:
        if datetime.datetime.today().weekday() not in o["days"]:
            checklist.append(o["item"])

    return html.div(
        html.h1("Hello Kittycat, this is your daily rejuvination list!"),
        html.ul(*checklist),
    )


todo_list = Starlette()
configure(todo_list, RejList)

if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        todo_list,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        log_level=os.getenv("LOG_LEVEL", "info"),
        #proxy_headers=True,
    )
    # move contents of last_workout.jsonl to workout_log.jsonl with dividers
    if Path("last_workout.jsonl").exists():
        f1 = open("workout_logs.jsonl", "a+")
        f2 = open("last_workout.jsonl", "r")
        f1.write("\n")
        f1.write("*********************************")
        f1.write("\n")
        f1.write(f2.read())
        f1.write("*********************************")
        f1.write("\n")
        f1.close()
        f2.close()

    # move workout_log.jsonl to last_workout.jsonl
    Path("last_workout.jsonl").unlink(missing_ok=True)
    lines_seen = set()
    outfile = open("last_workout.jsonl", "w+")
    for line in open("workout_log.jsonl", "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    Path("workout_log.jsonl").unlink()
