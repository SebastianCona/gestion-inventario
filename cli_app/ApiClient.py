from textual import on
from textual.app import App
from textual.screen import Screen
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer, Label, Static, Button, Input

class LoginFormWidget(Screen):
    def compose(self):
        yield Header()
        with Container(classes="form-widget"):
            yield Label("Login Form Menu", classes="form-name")
            with Container(classes="form-main-container"):
                with Vertical(classes="form-menu-container"):
                    yield Label("Email:", classes="form-email-label")
                    yield Input(placeholder="example@email.com", classes="form-email-input")
                    yield Label("Password:", classes="form-passwd-label")
                    yield Input(classes="form-passwd-input", password=True)
                    with Horizontal(classes="form-button-container"):
                        yield Button("Submit", classes="submit-button")
                        yield Button("Cancel", classes="cancel-button", id="pop")

        yield Footer()
            

class SignUpFormWidget(Screen):
    def compose(self):
        yield Header()
        with Container(classes="form-widget"):
            yield Label("Login Form Menu", classes="form-name")
            with Container(classes="form-main-container"):
                with Vertical(classes="form-menu-container"):
                    yield Label("Username:", classes="form-username-label")
                    yield Input(classes="form-username-input")
                    yield Label("Email:", classes="form-email-label")
                    yield Input(placeholder="example@email.com", classes="form-text-input")
                    yield Label("Password:", classes="form-passwd-label")
                    yield Input(classes="form-passwd-input", password=True)
                    with Horizontal(classes="form-button-container"):
                        yield Button("Submit", classes="submit-button")
                        yield Button("Cancel", classes="cancel-button", id="pop")

        yield Footer()


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

    @on(Button.Pressed, "#pop")
    def pop_screen_to_stack(self, event: Button.Pressed):
        self.pop_screen()




if __name__ == "__main__":
    ApiClient().run()

