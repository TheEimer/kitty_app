import datetime

from reactpy import component, html

from src.workout_away import WorkoutAway
from src.workout_home import WorkoutHome

WORKOUTS = {"home": WorkoutHome, "away": WorkoutAway}


@component
def DailyItem(name, message, success_message, checked, set_checked):
    def handle_click(event):
        if checked == 0:
            set_checked(1)
        elif checked == 1:
            set_checked(0)

    if checked == 0:
        item = html.form(
            html.input(
                {"type": "checkbox", "id": name, "name": name, "on_click": handle_click}
            ),
            html.label({"for": name}, message),
        )
    else:
        item = html.div(
            html.input(
                {
                    "type": "checkbox",
                    "id": name,
                    "name": name,
                    "checked": True,
                    "on_click": handle_click,
                }
            ),
            html.label(
                {"for": name},
                success_message,
            ),
            html.span({"style": "padding-left:30px;"}),
        )
    return item


@component
def OptionalItem(name, message, success_message, checked, set_checked):
    def handle_click(event):
        if checked == 0:
            set_checked(1)
        elif checked == 1:
            set_checked(0)

    if checked == 0:
        item = html.div(
            html.form(
                {"style": {"display": "inline", "color": "grey"}},
                html.input(
                    {
                        "type": "checkbox",
                        "id": name,
                        "name": name,
                        "on_click": handle_click,
                    }
                ),
                html.label({"for": name}, f"Optional for today: {message}"),
            )
        )
    else:
        item = html.div(
            html.input(
                {
                    "type": "checkbox",
                    "id": name,
                    "name": name,
                    "checked": True,
                    "on_click": handle_click,
                }
            ),
            html.label(
                {"for": name},
                f"{success_message} You really went above and beyond!",
            ),
            html.span({"style": "padding-left:40px;"}),
        )
    return item


@component
def IrregularItem(
    name,
    message,
    success_message,
    check,
    set_check,
    days,
    workout=False,
    workout_option=None,
    set_option=None,
    baseline_data=None,
):
    if datetime.datetime.today().weekday() in days:
        if workout:
            return WorkoutItem(
                name,
                message,
                success_message,
                check,
                set_check,
                workout_option,
                set_option,
                baseline_data,
            )
        else:
            return DailyItem(name, message, success_message, check, set_check)
    else:
        if workout:
            return OptionalWorkoutItem(
                name,
                message,
                success_message,
                check,
                set_check,
                workout_option,
                set_option,
                baseline_data,
            )
        else:
            return OptionalItem(name, message, success_message, check, set_check)


@component
def CountItem(name, message, success_message, current_count, goal_count, goal_setter):
    def handle_click(event):
        goal_setter(current_count + 1)

    if current_count < 8:
        count_item = html.div(
            html.input({"type": "checkbox", "id": name, "name": name}),
            html.label(
                {"for": name},
                f"{message}: {current_count}/{goal_count}",
            ),
            html.span({"style": "padding-left:50px;"}),
            html.button({"onClick": handle_click}, "+1"),
        )
    else:
        count_item = html.div(
            html.input({"type": "checkbox", "id": name, "name": name, "checked": True}),
            html.label(
                {"for": name},
                success_message,
            ),
        )
    return count_item


@component
def WorkoutItem(
    name,
    message,
    success_message,
    checked,
    set_checked,
    workout_option,
    set_option,
    baseline_data,
):
    workout_names = list(WORKOUTS.keys())

    def start_option(name, event):
        set_checked(2)
        set_option(name)

    from functools import partial

    setters = [partial(start_option, name) for name in workout_names]

    if checked == 0:
        buttons = [html.span({"style": "padding-left:50px;"})]
        for i in range(len(workout_names)):
            buttons.append(
                html.button(
                    {
                        "on_click": setters[i],
                    },
                    f"Start {workout_names[i]}",
                )
            )
        subroutine_item = html.div(
            html.input({"type": "checkbox", "id": name, "name": name}),
            html.label({"for": name}, message),
            html.div(*buttons),
        )
    elif checked == 2:
        subroutine_item = WORKOUTS[workout_option](set_checked, baseline_data)
    else:
        subroutine_item = html.div(
            html.input({"type": "checkbox", "id": name, "name": name, "checked": True}),
            html.label(
                {"for": name},
                success_message,
            ),
            html.span({"style": "padding-left:30px;"}),
        )

    return subroutine_item


@component
def OptionalWorkoutItem(
    name,
    message,
    success_message,
    checked,
    set_checked,
    workout_option,
    set_option,
    baseline_data,
):
    workout_names = list(WORKOUTS.keys())

    def start_option(name, event):
        set_checked(2)
        set_option(name)

    from functools import partial

    setters = [partial(start_option, name) for name in workout_names]

    if checked == 0:
        buttons = [html.span({"style": "padding-left:50px;"})]
        for i in range(len(workout_names)):
            buttons.append(
                html.button(
                    {
                        "on_click": setters[i],
                    },
                    f"Start {workout_names[i]}",
                )
            )
        subroutine_item = html.div(
            {"style": {"color": "grey"}},
            html.input({"type": "checkbox", "id": name, "name": name}),
            html.label({"for": name}, f"Optional for today: {message}"),
            html.div(*buttons),
        )
    elif checked == 2:
        subroutine_item = WORKOUTS[workout_option](set_checked, baseline_data)
    else:
        subroutine_item = html.div(
            html.input({"type": "checkbox", "id": name, "name": name, "checked": True}),
            html.label(
                {"for": name},
                f"{success_message} You really went above and beyond!",
            ),
            html.span({"style": "padding-left:30px;"}),
        )

    return subroutine_item
