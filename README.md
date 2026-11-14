# Prompt Templates

Professional prompt templates for common AI tasks

## Features

- Zero external dependencies (stdlib only)
- Easy-to-use CLI interface
- Professional Python implementation
- MIT licensed

## Installation

```bash
pip install -e .
```

Or clone and install:

```bash
git clone https://github.com/Viprasol-Tech/prompt-templates
cd prompt-templates
pip install -e .
```

## Usage

### Python

```python
from prompt_templates import format_prompt, list_templates

print(list(list_templates()))
print(format_prompt("summarize", text="Some long text", length=10))
```

### CLI

```bash
python -m prompt_templates --list
python -m prompt_templates --get summarize
```

## Documentation

See the source code and docstrings for detailed API documentation.

## License

MIT License - see LICENSE file for details

## About

Part of Viprasol Utilities: https://viprasol.com

Created by Viprasol - Building AI-focused tools for developers.
