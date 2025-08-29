# AI-Powered Code Generator

This project uses Azure OpenAI's GPT model to generate Python code with detailed comments based on user prompts.

## Features

- Generates Python code with comprehensive comments
- Utilizes Azure OpenAI's GPT-4 model
- Implements retry mechanism for API calls
- Supports custom prompts for various coding tasks

## Prerequisites

- Python 3.7+
- Azure OpenAI API access
- OpenAI Python library
- Tenacity library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/AI-Powered-Code-Generator.git
```
2. Install required libraries:
```bash
pip install openai tenacity
```

3. Set up your Azure OpenAI API credentials in the script.

## Usage

1. Open the Jupyter notebook or Databricks notebook.
2. Modify the prompt in the script to generate desired code.
3. Run the notebook to see the generated code with comments.

## Example

Input prompt:
```python
"Write a Python function that calculates the factorial of a number."
```

Output:
```python
def factorial(n):
    """Calculate factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

## Command-line Example

For a quick demonstration without Azure OpenAI credentials, run the provided script with a prompt:

```bash
python generate_code.py "function that adds two numbers"
```

This uses a dummy generator and prints placeholder code. Replace the logic in `generate_code.py` with an actual API call once credentials are available.
