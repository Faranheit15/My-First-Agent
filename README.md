# 🤖 CLI-Based AI Coding Assistant

This project is a **CLI (Command Line Interface) coding assistant** powered by LLMs.  
It can:
- Understand natural language prompts.
- Plan steps using Chain-of-Thought reasoning.
- Call tools like **system commands** and **weather API**.
- Automatically create and modify files/folders (e.g., building a To-Do app).
- Simulate an AI-powered terminal experience similar to **Copilot, Cursor IDE, or Codex**.

---

## 🚀 Features
- **Chain-of-Thought prompting**  
  The assistant breaks tasks into `START → PLAN → TOOL → OBSERVE → OUTPUT`.

- **Structured outputs (Pydantic models)**  
  Ensures reliable JSON parsing and type safety.

- **Available tools**
  - `get_weather(city: str)` → Fetches weather info using [wttr.in](https://wttr.in).  
  - `run_command(cmd: str)` → Executes Linux commands directly.

- **Autonomous coding**  
  Can create folders, generate HTML/CSS/JS files, and build mini projects on demand.

---

## 🛠️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/cli-coding-assistant.git
cd cli-coding-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**Requirements:**
- `openai`
- `pydantic`
- `requests`
- `python-dotenv`

### 3. Set up environment variables
Create a `.env` file and add your **Gemini API key**:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the assistant
```bash
python agent.py
```

---

## 💻 Usage Examples

Once running, you can type natural prompts:

### Example 1: Math problem
```
👉🏻 Solve 2 + 3 * 5 / 10
```
Assistant reasoning:
- PLAN: Apply BODMAS
- PLAN: Multiply 3 * 5 = 15
- PLAN: Divide 15 / 10 = 1.5
- PLAN: Add 2 + 1.5 = 3.5  
**Output → 3.5**

---

### Example 2: Weather
```
👉🏻 What is the weather in Delhi?
```
Assistant:
- Uses `get_weather("delhi")`
- Returns weather via wttr.in

---

### Example 3: Build a To-Do App
```
👉🏻 Create a ToDo app using HTML, CSS, and JavaScript in a folder called todo_app
```
Assistant:
- Runs `mkdir todo_app`
- Creates files: `index.html`, `style.css`, `app.js`
- Writes boilerplate code
- You can open the folder in your browser and run the app 🎉

---

## ⚠️ Security Warning
- The `run_command` tool can execute **any Linux command** on your system.  
- **Do NOT run untrusted prompts**, as this may harm your machine.  
- For production, consider replacing it with **structured tools** like:
  - `create_file(filename, content)`
  - `read_file(filename)`
  - `delete_file(filename)`

---

## 📌 Next Steps
- Add safer, structured tools for file operations.
- Extend with more capabilities (e.g., Git commands, Docker, project scaffolding).
- Experiment with RAG (Retrieval-Augmented Generation) for project-specific context.

---

## 👨‍💻 Author
Built as part of the **Full-Stack Generative & Agentic AI with Python** course.

---
