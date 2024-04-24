"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
