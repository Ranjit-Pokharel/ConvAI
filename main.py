from ArtificialIntelligence import ArtificialIntelligence
from memory import memory
from user_input import UserInput
import subprocess as sp

MODEL = "llama3.2:1b"
ai = ArtificialIntelligence(model=MODEL)

USERNAME = "KD"
AINAME = "AMO"

system = {
    "role": "system",
    "content": f"Your name is {AINAME}. You are a friendly Human. user name is {USERNAME}."
}

usr = UserInput()

HISTORY_DIR = "history"
history = memory(memory_home_path=HISTORY_DIR)

def main():
    history_file = "history.json"
    while True:
        query = usr.take_usr_input(f"{USERNAME}: ")

        if query == "exit":
            quit()

        if query == "clear":
            result = sp.run(["clear"])
            if result.returncode != 0:
                print("unable to clear screen...")
                continue
            else:
                print("screen is cleared....")
                continue

        ai.conversation_history = history.load(history_file)
        ai.conversation_history.append(system)

        text = ai.stream_chat(query=query)

        print(f"{AINAME}: ", end="")
        for txt in text:
            print(txt, end="", flush=True)

        history.save(ai.conversation_history, history_file)


if __name__ == "__main__":
    main()


