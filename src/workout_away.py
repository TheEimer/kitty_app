from reactpy import component, hooks, html

from src.workout_utils import Set


@component
def WorkoutAway(workout_done_setter, baseline_data):
    away_workout_checklist = [
        html.link(
            {"rel": "stylesheet", "href": "https://cdn.simplecss.org/simple.min.css"}
        ),
        html.h1("Hello Kittycat, this is today's workout!"),
    ]
    chest_done, set_chest_done = hooks.use_state(0)
    nordics_done, set_nordics_done = hooks.use_state(0)
    squat_done, set_squat_done = hooks.use_state(0)
    streching_done, set_stretching_done = hooks.use_state(0)

    nordics = NegativeNordic(set_nordics_done, baseline_data)
    chest = InclinePushup(set_chest_done, baseline_data)
    squat = ShrimpSquat(set_squat_done, baseline_data)
    away_workout_checklist.append(nordics)
    away_workout_checklist.append(chest)
    away_workout_checklist.append(squat)

    def handle_click(event):
        if streching_done == 0:
            set_stretching_done(1)
        elif set_stretching_done == 1:
            set_stretching_done(0)

    streching = html.div(
        html.h3("10 minutes of streching"),
        html.form(
            html.input(
                {
                    "type": "checkbox",
                    "id": "strech",
                    "name": "strech",
                    "on_click": handle_click,
                }
            ),
            html.label({"for": "strech"}, "Stretch for at least 10 minutes"),
        ),
    )
    away_workout_checklist.append(streching)

    if (
        chest_done == 1
        and nordics_done == 1
        and squat_done == 1
        and streching_done == 1
    ):

        def handle_submit(event):
            workout_done_setter(1)

        finish_button = html.div(
            html.button({"on_click": handle_submit}, "Finish Workout"),
        )
        away_workout_checklist.append(finish_button)
    return html.div(*away_workout_checklist)


@component
def NegativeNordic(set_pullup_done, baseline_data):
    pullup_list = [html.h3("Negative Nordic Curls: 3 sets of 8-12 reps")]
    pullup_reps_1, set_pullup_index_1 = hooks.use_state(0)
    pullup_reps_2, set_pullup_index_2 = hooks.use_state(0)
    pullup_reps_3, set_pullup_index_3 = hooks.use_state(0)
    pullup_list.append(
        Set("negative nordic curl", 1, pullup_reps_1, set_pullup_index_1, baseline_data)
    )
    pullup_list.append(
        Set("negative nordic curl", 2, pullup_reps_2, set_pullup_index_2, baseline_data)
    )
    pullup_list.append(
        Set("negative nordic curl", 3, pullup_reps_3, set_pullup_index_3, baseline_data)
    )
    if int(pullup_reps_1) > 0 and int(pullup_reps_2) > 0 and int(pullup_reps_3) > 0:
        set_pullup_done(1)
    return html.div(*pullup_list)


@component
def InclinePushup(set_pullup_done, baseline_data):
    pullup_list = [html.h3("Incline/Knee Pushups: 3 sets of 8-12 reps")]
    pullup_reps_1, set_pullup_index_1 = hooks.use_state(0)
    pullup_reps_2, set_pullup_index_2 = hooks.use_state(0)
    pullup_reps_3, set_pullup_index_3 = hooks.use_state(0)
    pullup_list.append(
        Set("incline push-up", 1, pullup_reps_1, set_pullup_index_1, baseline_data)
    )
    pullup_list.append(
        Set("incline push-up", 2, pullup_reps_2, set_pullup_index_2, baseline_data)
    )
    pullup_list.append(
        Set("incline push-up", 3, pullup_reps_3, set_pullup_index_3, baseline_data)
    )
    if int(pullup_reps_1) > 0 and int(pullup_reps_2) > 0 and int(pullup_reps_3) > 0:
        set_pullup_done(1)
    return html.div(*pullup_list)


@component
def ShrimpSquat(set_pullup_done, baseline_data):
    pullup_list = [html.h3("Beginner Shrimp Squats: 3 sets of 8-12 reps")]
    pullup_reps_1, set_pullup_index_1 = hooks.use_state(0)
    pullup_reps_2, set_pullup_index_2 = hooks.use_state(0)
    pullup_reps_3, set_pullup_index_3 = hooks.use_state(0)
    pullup_list.append(
        Set("shrimp squats", 1, pullup_reps_1, set_pullup_index_1, baseline_data)
    )
    pullup_list.append(
        Set("shrimp squats", 2, pullup_reps_2, set_pullup_index_2, baseline_data)
    )
    pullup_list.append(
        Set("shrimp squats", 3, pullup_reps_3, set_pullup_index_3, baseline_data)
    )
    if int(pullup_reps_1) > 0 and int(pullup_reps_2) > 0 and int(pullup_reps_3) > 0:
        set_pullup_done(1)
    return html.div(*pullup_list)
