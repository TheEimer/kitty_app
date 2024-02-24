import datetime
import json

from reactpy import event, hooks, html


def log_set(set_data):
    log = True
    with open("workout_log.jsonl", "a+") as f:
        for line in f.readlines():
            loaded_set_data = json.loads(line)
            if (
                set_data["name"] == loaded_set_data["name"]
                and set_data["set_number"] == loaded_set_data["set_number"]
            ):
                log = False
        if log:
            f.write(json.dumps(set_data) + "\n")


def Set(exercise_name, set_number, total_reps, set_total_reps, baseline_data):
    reps, set_reps = hooks.use_state(0)
    result_list = []
    baseline_reps = 0
    if baseline_data["name"] == exercise_name:
        baseline_reps = baseline_data["reps"]
    elif isinstance(baseline_data["name"], list):
        for i, (name, num_set) in enumerate(
            zip(baseline_data["name"], baseline_data["set_number"])
        ):
            if name == exercise_name and int(num_set) == set_number:
                baseline_reps = baseline_data["reps"][i]
                break

    @event(prevent_default=True)
    async def handle_submit(event):
        set_total_reps(reps)

    if total_reps == 0:
        result_list.append(
            html.form(
                {
                    "on_submit": handle_submit,
                    "style": {"display": "inline"},
                },
                html.input(
                    {
                        "type": "text",
                        "id": exercise_name,
                        "name": exercise_name,
                        "placeholder": f"{baseline_reps} reps",
                        "on_change": lambda event: set_reps(event["target"]["value"]),
                    }
                ),
                html.button({"type": "submit"}, "Confirm"),
            )
        )
        result_list.append(
            html.label(
                {"for": exercise_name},
                f"Reps in set {set_number}.",
            )
        )
    else:
        log_set(
            {
                "name": exercise_name,
                "date": datetime.date.today().strftime("%Y-%m-%dT%f"),
                "set_number": set_number,
                "reps": total_reps,
                "weight": 0,
                "time": 0,
            }
        )
        result_list.append(
            html.p(f"Good job! You did {total_reps} reps in set {set_number}.")
        )
    return html.div(*result_list)


def SetKg(exercise_name, set_number, total_reps, set_total_reps, baseline_data):
    reps, set_reps = hooks.use_state(0)
    weight, set_weight = hooks.use_state(0)
    result_list = []
    baseline_reps = 0
    baseline_weight = 0
    if baseline_data["name"] == exercise_name:
        baseline_reps = baseline_data["reps"]
        baseline_weight = baseline_data["weight"]
    elif isinstance(baseline_data["name"], list):
        for i, (name, num_set) in enumerate(
            zip(baseline_data["name"], baseline_data["set_number"])
        ):
            if name == exercise_name and int(num_set) == set_number:
                baseline_reps = baseline_data["reps"][i]
                baseline_weight = baseline_data["weight"][i]
                break

    @event(prevent_default=True)
    async def handle_submit(event):
        set_total_reps(reps)

    if total_reps == 0:
        result_list.append(
            html.form(
                {
                    "on_submit": handle_submit,
                    "style": {"display": "inline"},
                },
                html.input(
                    {
                        "type": "text",
                        "id": exercise_name,
                        "name": exercise_name,
                        "placeholder": f"{baseline_reps} reps",
                        "on_change": lambda event: set_reps(event["target"]["value"]),
                    }
                ),
                html.input(
                    {
                        "type": "text",
                        "id": f"{exercise_name}_weight",
                        "name": f"{exercise_name}_weight",
                        "placeholder": f"{baseline_weight} kg",
                        "on_change": lambda event: set_weight(event["target"]["value"]),
                    }
                ),
                html.button({"type": "submit"}, "Confirm"),
            )
        )
        result_list.append(
            html.label(
                {"for": exercise_name},
                f"Reps and weights in set {set_number}.",
            )
        )
    else:
        log_set(
            {
                "name": exercise_name,
                "date": datetime.date.today().strftime("%Y-%m-%dT%f"),
                "set_number": set_number,
                "reps": total_reps,
                "weight": weight,
                "time": 0,
            }
        )
        result_list.append(
            html.p(
                f"Good job! You did {total_reps} reps with {weight}kg in set {set_number}."
            )
        )
    return html.div(*result_list)


def SetTime(exercise_name, set_number, total_reps, set_total_reps, baseline_data):
    reps, set_reps = hooks.use_state(0)
    result_list = []
    baseline_time = 0
    if baseline_data["name"] == exercise_name:
        baseline_time = baseline_data["time"]
    elif isinstance(baseline_data["name"], list):
        for i, (name, num_set) in enumerate(
            zip(baseline_data["name"], baseline_data["set_number"])
        ):
            if name == exercise_name and int(num_set) == set_number:
                baseline_time = baseline_data["time"][i]
                break

    @event(prevent_default=True)
    async def handle_submit(event):
        set_total_reps(reps)

    if total_reps == 0:
        result_list.append(
            html.form(
                {
                    "on_submit": handle_submit,
                    "style": {"display": "inline"},
                },
                html.input(
                    {
                        "type": "text",
                        "id": exercise_name,
                        "name": exercise_name,
                        "placeholder": f"{baseline_time} seconds",
                        "on_change": lambda event: set_reps(event["target"]["value"]),
                    }
                ),
                html.button({"type": "submit"}, "Confirm"),
            )
        )
        result_list.append(
            html.label(
                {"for": exercise_name},
                f"Total seconds in set {set_number}.",
            )
        )
    else:
        log_set(
            {
                "name": exercise_name,
                "date": datetime.date.today().strftime("%Y-%m-%dT%f"),
                "set_number": set_number,
                "reps": 0,
                "weight": 0,
                "time": total_reps,
            }
        )
        result_list.append(
            html.p(f"Good job! You did {total_reps} seconds in set {set_number}.")
        )
    return html.div(*result_list)
