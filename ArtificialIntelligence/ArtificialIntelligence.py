import ollama

class ArtificialIntelligence:
    def __init__(self, model:str, conversational_history=[]):
        self.model = model
        self.conversation_history = conversational_history

    def chat(self, query:str,):
        self.conversation_history.append(
            {
                "role": "user",
                "content": query.strip()
            }
        )

        respose = ollama.chat(
            model=self.model,
            messages=self.conversation_history,
            keep_alive=-1,
        )

        result = {
            "role": respose['message']['role'],
            "content": respose['message']['content']
        }

        self.conversation_history.append(result)

        return result
    
    def stream_chat(self, query:str):
        self.conversation_history.append(
            {
                "role": "user",
                "content": query.strip()
            }
        )

        strems = ollama.chat(
            model=self.model,
            messages=self.conversation_history,
            stream=True,
            keep_alive=-1,
        )

        full_text = ""
        for chunk in strems:
            text = chunk['message']['content']
            full_text += text
            yield text

        result = {
            "role": chunk['message']['role'],
            "content": full_text
        }

        self.conversation_history.append(result)

        yield "\n"       

    @property
    def model(self,):
        return self._model
    
    @model.setter
    def model(self, model):
        try:
            ollama.show(model)
        except ollama._types.ResponseError:
            raise Exception(f"Ollama model: {model} not installed")
        self._model = model
        

if __name__ == "__main__":
    pass