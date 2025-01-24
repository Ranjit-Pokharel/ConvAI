# ConvAI

#### Description:  
An **AI Conversational Assistant** short for **ConvAI** built in Python that 
interacts with users in a conversational format. It supports saving and loading conversation history, 
and real-time emoji conversion while typing inputs.

It uses the **Ollama AI model** **llama3.2:1b** for generating responses and provides a seamless experience. 
Below are the key details of the project.

---

### Features:
1. **AI-Powered Conversations**:
   - Communicates with users using the Ollama AI model.
   - Stores and retrieves conversation history from a JSON file.

2. **Real-Time Emoji Conversion**:
   - Converts text to emojis in real-time while the user types their input.

3. **Persistent Memory**:
   - Saves conversations in a JSON file and reloads them when restarted.

2. **Clear Screen Functionality**:
   - Clears the terminal to provide a clutter-free interface.

---

### Design Choices:
1. **Why Ollama AI?**
   - Ollama offers robust conversational capabilities suitable for AI-powered projects.

2. **Why JSON for Memory?**
   - JSON provides a lightweight and human-readable format for saving and retrieving conversation data.
   - JSON can also be use in future for fine tunning ai model.

3. **Real-Time Emoji Conversion**:
   - Adds a fun and engaging element to user interactions.

4. **Use of `prompt_toolkit`**:
   - Enables advanced interactive prompts, enhancing user experience.

---

### How to Run:
1. Install ollama:
    - [https://ollama.com/](https://ollama.com/)
    ```bash
    ollama pull llama3.2:1b
    ```

2. Download convai:
    ```bash
    git clone https://github.com/Ranjit-Pokharel/ConvAI.git
    cd ConvAI/
    python -m venv .env
    source .env/bin/activate
    ```

3. Install all dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the program:
    ```bash
    python main.py
    ```

### Known Issues:
- only tested in Linux base system.
- Missing Dependencies: ollma (visit webside [ollama](https://ollama.com/) to setup **ollama**)