from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
import emoji


class UserInput:
    def __init__(self):
        self.bindings = KeyBindings()
        self.session = PromptSession()
        self.usr_input:str = ""

    def take_usr_input(self, prompt):
        # realtime emoji conversion as user type
        @self.bindings.add("<any>")
        def update_input_buffer(event):
            # binding add <any> will capture all the key pressed
            # insert_text is needed to insert the text as we type.
            event.app.current_buffer.insert_text(event.data)

            # converts to emoji as user type
            current_text = self.session.app.current_buffer.text
            updated_text = emoji.emojize(current_text, language="alias")
            self.session.app.current_buffer.text = updated_text

        user_input = self.session.prompt(
            prompt,
            key_bindings=self.bindings,
        )
        return str(user_input).strip()