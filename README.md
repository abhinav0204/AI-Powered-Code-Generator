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

git clone https://github.com/your-username/AI-Powered-Code-Generator.git

2. Install required libraries:

pip install openai tenacity


3. Set up your Azure OpenAI API credentials in the script.

## Usage

1. Open the Jupyter notebook or Databricks notebook.
2. Modify the prompt in the script to generate desired code.
3. Run the notebook to see the generated code with comments.

## Example

Input prompt:
```python
"Write a Python function that calculates the factorial of a number. Include detailed comments."
