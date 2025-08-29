"""Simple CLI for AI-Powered Code Generator.

This script demonstrates how to request code generation from a text prompt.
The call to Azure OpenAI is replaced with a dummy implementation so the
example runs without credentials.
"""

from __future__ import annotations

import argparse


def generate_code(prompt: str) -> str:
    """Return placeholder Python code for the given prompt."""
    # TODO: Replace with a call to Azure OpenAI or another LLM service.
    return (
        f"# Generated code for prompt: {prompt!r}\n\n"
        "def example():\n"
        "    \"\"\"This is placeholder code.\"\"\"\n"
        "    pass\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Python code from a prompt (dummy example)."
    )
    parser.add_argument("prompt", help="Describe the code you want.")
    args = parser.parse_args()
    print(generate_code(args.prompt))


if __name__ == "__main__":
    main()
