from reactpy import component, hooks, html

from src.workout_utils import Set, SetKg, SetTime


@component
def WorkoutHome(workout_done_setter, baseline_data):
    chest_done, set_chest_done = hooks.use_state(0)
    row_done, set_row_done = hooks.use_state(0)
    squat_done, set_squat_done = hooks.use_state(0)
    press_done, set_press_done = hooks.use_state(0)
    pullup_done, set_pullup_done = hooks.use_state(0)
    home_workout_checklist = [
        html.link(
            {"rel": "stylesheet", "href": "https://cdn.simplecss.org/simple.min.css"}
        ),
        html.h1("Hello Kittycat, this is today's workout!"),
    ]
    chest_press = ChestPress(set_chest_done, baseline_data)
    row = Row(set_row_done, baseline_data)
    squat = Squat(set_squat_done, baseline_data)
    press = ZPress(set_press_done, baseline_data)
    pullup = Pullup(set_pullup_done, baseline_data)

    home_workout_checklist.append(chest_press)
    home_workout_checklist.append(row)
    home_workout_checklist.append(squat)
    home_workout_checklist.append(press)
    home_workout_checklist.append(pullup)
    if (
        chest_done == 1
        and row_done == 1
        and squat_done == 1
        and press_done == 1
        and pullup_done == 1
    ):

        def handle_submit(event):
            workout_done_setter(1)

        finish_button = html.div(
            html.button({"on_click": handle_submit}, "Finish Workout"),
        )
        home_workout_checklist.append(finish_button)
    return html.div(*home_workout_checklist)


@component
def ChestPress(set_chest_done, baseline_data):
    chest_press_list = [html.h3("Incline Dumbell Chestpress: 3 sets of 8-12 reps")]
    chest_reps_1, set_chest_index_1 = hooks.use_state(0)
    chest_reps_2, set_chest_index_2 = hooks.use_state(0)
    chest_reps_3, set_chest_index_3 = hooks.use_state(0)
    chest_press_list.append(
        SetKg("chestpress", 1, chest_reps_1, set_chest_index_1, baseline_data)
    )
    chest_press_list.append(
        SetKg("chestpress", 2, chest_reps_2, set_chest_index_2, baseline_data)
    )
    chest_press_list.append(
        SetKg("chestpress", 3, chest_reps_3, set_chest_index_3, baseline_data)
    )
    if int(chest_reps_1) > 0 and int(chest_reps_2) > 0 and int(chest_reps_3) > 0:
        set_chest_done(1)
    return html.div(*chest_press_list)


@component
def Row(set_row_done, baseline_data):
    row_list = [html.h3("Inverted Rows: 3 sets of 8-12 reps")]
    row_reps_1, set_row_index_1 = hooks.use_state(0)
    row_reps_2, set_row_index_2 = hooks.use_state(0)
    row_reps_3, set_row_index_3 = hooks.use_state(0)
    row_list.append(Set("row", 1, row_reps_1, set_row_index_1, baseline_data))
    row_list.append(Set("row", 2, row_reps_2, set_row_index_2, baseline_data))
    row_list.append(Set("row", 3, row_reps_3, set_row_index_3, baseline_data))
    if int(row_reps_1) > 0 and int(row_reps_2) > 0 and int(row_reps_3) > 0:
        set_row_done(1)
    return html.div(*row_list)


@component
def Squat(set_squat_done, baseline_data):
    squat_list = [html.h3("Goblet Squats: 3 sets of 8-12 reps")]
    squat_reps_1, set_squat_index_1 = hooks.use_state(0)
    squat_reps_2, set_squat_index_2 = hooks.use_state(0)
    squat_reps_3, set_squat_index_3 = hooks.use_state(0)
    squat_list.append(SetKg("squat", 1, squat_reps_1, set_squat_index_1, baseline_data))
    squat_list.append(SetKg("squat", 2, squat_reps_2, set_squat_index_2, baseline_data))
    squat_list.append(SetKg("squat", 3, squat_reps_3, set_squat_index_3, baseline_data))
    if int(squat_reps_1) > 0 and int(squat_reps_2) > 0 and int(squat_reps_3) > 0:
        set_squat_done(1)
    return html.div(*squat_list)


@component
def ZPress(set_press_done, baseline_data):
    press_list = [html.h3("Z Press: 3 sets of 8-12 reps")]
    press_reps_1, set_press_index_1 = hooks.use_state(0)
    press_reps_2, set_press_index_2 = hooks.use_state(0)
    press_reps_3, set_press_index_3 = hooks.use_state(0)
    press_list.append(SetKg("press", 1, press_reps_1, set_press_index_1, baseline_data))
    press_list.append(SetKg("press", 2, press_reps_2, set_press_index_2, baseline_data))
    press_list.append(SetKg("press", 3, press_reps_3, set_press_index_3, baseline_data))
    if int(press_reps_1) > 0 and int(press_reps_2) > 0 and int(press_reps_3) > 0:
        set_press_done(1)
    return html.div(*press_list)


@component
def Pullup(set_pullup_done, baseline_data):
    pullup_list = [
        html.h3(
            "Negative Pull-Ups: 3 sets, each totalling your one rep max negative time in as many reps as necessary"
        )
    ]
    pullup_reps_1, set_pullup_index_1 = hooks.use_state(0)
    pullup_reps_2, set_pullup_index_2 = hooks.use_state(0)
    pullup_reps_3, set_pullup_index_3 = hooks.use_state(0)
    pullup_list.append(
        SetTime("pullup", 1, pullup_reps_1, set_pullup_index_1, baseline_data)
    )
    pullup_list.append(
        SetTime("pullup", 2, pullup_reps_2, set_pullup_index_2, baseline_data)
    )
    pullup_list.append(
        SetTime("pullup", 3, pullup_reps_3, set_pullup_index_3, baseline_data)
    )
    if int(pullup_reps_1) > 0 and int(pullup_reps_2) > 0 and int(pullup_reps_3) > 0:
        set_pullup_done(1)
    return html.div(*pullup_list)
