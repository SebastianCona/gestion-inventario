import asyncio
import httpx
from httpx import HTTPStatusError
from textual import on
from textual.app import App
from textual.screen import Screen
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer, Label, Static, Button, Input

from SessionManager import SessionManager

class LoginFormWidget(Screen):
    def compose(self):
        yield Header()
        with Container(classes="form-widget"):
            yield Label("Login Form Menu", classes="form-name")
            with Container(classes="form-main-container"):
                with Vertical(classes="form-menu-container"):
                    yield Label("Email:", classes="form-email-label")
                    yield Input(placeholder="example@email.com", classes="form-email-input", id="email-input")
                    yield Label("Password:", classes="form-passwd-label")
                    yield Input(classes="form-passwd-input", password=True, id="passwd-input")
                    with Horizontal(classes="form-button-container"):
                        yield Button("Submit", classes="submit-button", id="submit")
                        yield Button("Cancel", classes="cancel-button", id="cancel")

        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "#submit":
            # Retrieve user input values
            email = self.query_one("#email-input", Input).value
            passwd = self.query_one("#passwd-input", Input).value

            # Prepare request data
            request_data = {
                "email": email,
                "passwd": passwd
            }

            # Initialize the SessionManager
            sessionmgr = SessionManager(request_data)

            # Define an async function to handle the response
            async def handle_post_request():
                try:
                    # Send POST request and get response
                    response = await sessionmgr.auth_register()
                    # Display the response (e.g., update a widget)
                    output = self.query_one("#output", Static)
                    output.update(f"Success: {response.json()}")
                except HTTPStatusError as e:
                    # Handle HTTP errors
                    output = self.query_one("#output", Static)
                    output.update(f"HTTP Error: {e.response.status_code} - {e.response.text}")
                except Exception as e:
                    # Handle other exceptions
                    output = self.query_one("#output", Static)
                    output.update(f"Error: {e}")

            # Create a new task to run the async function
            asyncio.create_task(handle_post_request())

            

class SignUpFormWidget(Screen):
    def compose(self):
        yield Header()
        with Container(classes="form-widget"):
            yield Label("SignUp Form Menu", classes="form-name")
            with Container(classes="form-main-container"):
                with Vertical(classes="form-menu-container"):
                    yield Label("Username:", classes="form-username-label")
                    yield Input(classes="form-username-input", id="username-input")
                    yield Label("Email:", classes="form-email-label")
                    yield Input(placeholder="example@email.com", classes="form-email-input", id="email-input")
                    yield Label("Password:", classes="form-passwd-label")
                    yield Input(classes="form-passwd-input", password=True, id="passwd-input")
                    with Horizontal(classes="form-button-container"):
                        yield Button("Submit", classes="submit-button", id="submit")
                        yield Button("Cancel", classes="cancel-button", id="cancel")

        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "submit":
            # Retrieve user inputs
            username = self.query_one("#username-input", Input).value
            email = self.query_one("#email-input", Input).value
            password = self.query_one("#passwd-input", Input).value

            # Construct payload
            request_data = {
                "username": username,
                "email": email,
                "password": password,
            }

            # Initialize the SessionManager
            sessionmgr = SessionManager(request_data)

            # Define a function to handle POST request
            async def handle_post_request():
                try:
                    # Send the POST request
                    response = await sessionmgr.auth_register()
                    # Return success message if the request is successful
                    return f"User registered successfully"
                except httpx.HTTPStatusError as e:
                    # Return the error message for HTTP status errors
                    return f"HTTP Error: Status {e.response.status_code} - {e.response.text}"
                except Exception as e:
                    # Return the error message for other unexpected errors
                    return f"Error: An unexpected error occurred - {e}"

            # Create a task to handle the request and capture the result
            result_message = await handle_post_request()  # Ensure this returns a valid string

            # Display the result as a Toast message
            self.notify(
                result_message, 
                severity="success" if "successfully" in result_message else "error"
            )


class AppContainerWidget(Static):
    def compose(self):
        yield Label("ApiClient Menu", id="widget-name")
        with Container(id="child-container"):
            with Vertical(id="menu-container"):
                yield Button("Login", id="login-button")
                yield Button("SignUp", id="signup-button")


class ApiClient(App[None]):

    CSS_PATH = "./ApiClient.tcss"

    SCREENS = {
        "login-button": LoginFormWidget,
        "signup-button": SignUpFormWidget
    }

    def compose(self):
        yield Header()
        yield AppContainerWidget()
        yield Footer()


    @on(Button.Pressed, "#login-button, #signup-button")
    def add_screen_to_stack(self, event: Button.Pressed):
        self.push_screen(event.button.id)

    @on(Button.Pressed, "#cancel")
    def pop_screen_to_stack(self, event: Button.Pressed):
        self.pop_screen()




if __name__ == "__main__":
    ApiClient().run()

