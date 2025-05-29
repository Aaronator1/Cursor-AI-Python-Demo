# Simple Python Demo Project

This is a simple demonstration project that shows basic Python functionality. The project includes:
- Basic arithmetic operations
- String manipulation
- List operations
- Simple function definitions
- ChatGPT Integration (Query the ChatGPT API)

## Setup
1. Make sure you have Python 3.x installed
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Running the Project
To run the basic demo:
```bash
python main.py
```

To use the ChatGPT query tool:
```bash
python chatgpt_query.py
```

## Features
- **Basic Demo** (`main.py`): Demonstrates fundamental Python operations with colorful output
- **ChatGPT Query** (`chatgpt_query.py`): Interactive tool to send queries to ChatGPT and get responses
  - Type your question and press Enter
  - Type 'quit' to exit the program 