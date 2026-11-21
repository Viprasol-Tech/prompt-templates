<div align="center">

<img src="docs/assets/logo.png" alt="Viprasol Tech logo" width="120" />

# prompt-templates

**Reusable, validated prompt templates for everyday LLM tasks.**

_Built and maintained by [Viprasol Tech](https://viprasol.com) — Fintech Experts. Full-Stack Builders._

[![CI](https://img.shields.io/github/actions/workflow/status/Viprasol-Tech/prompt-templates/ci.yml?branch=master&style=flat-square&label=CI)](https://github.com/Viprasol-Tech/prompt-templates/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen?style=flat-square)](pyproject.toml)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230?style=flat-square)](https://github.com/astral-sh/ruff)

</div>

---

`prompt-templates` keeps the prompts you use often (summaries, explanations, code review, translation, Q&A, brainstorming) in one place. Each template lists its variables, and filling one raises a clear error if any are missing, so a half-filled prompt never reaches a model. It is a small Python library and CLI with zero dependencies.

## ✨ Features

- 📚 **8 built-in templates:** `summarize`, `explain`, `analyze`, `generate_ideas`, `code_review`, `translate`, `qa_pair`, `brainstorm`.
- ✅ **Validation:** a missing variable raises `ValueError` and names what is missing.
- 🛡️ **Safe filling:** values containing `{braces}` (code, JSON) are inserted as-is, never re-parsed.
- ➕ **Your own templates** with `add_template`.
- 🖥️ **CLI** (`prompt-templates`) to list, inspect and fill templates from the shell.

## 🚀 Quickstart

```bash
git clone https://github.com/Viprasol-Tech/prompt-templates.git
cd prompt-templates
pip install -e .

prompt-templates --list
prompt-templates --get code_review
prompt-templates --format code_review -v language=Python "code=print(1)" focus=security
```

```text
Review this Python code:

print(1)

Focus on: security
```

## 🐍 Python API

```python
from prompt_templates import PromptLibrary, format_prompt, list_templates

list_templates()["summarize"]
# {'description': 'Summarize text to specific length', 'variables': ['text', 'length']}

format_prompt("translate", text="Bonjour", source="French", target="English")
# 'Translate the following text from French to English:\n\nBonjour'

format_prompt("summarize", text="...")  # ValueError: Missing variables: ['length']

PromptLibrary.add_template("greet", "Say hello to {name}.", ["name"], "Greeting")
format_prompt("greet", name="Asha")  # 'Say hello to Asha.'
```

## ⚙️ CLI options

| Option | Meaning |
|---|---|
| `--list` | List every template with its variables (also the default) |
| `--get NAME` | Show one template's text and variables |
| `--format NAME -v KEY=VALUE ...` | Fill a template and print the prompt |

## 🧪 Development

```bash
pip install -e ".[dev]"
ruff check . && ruff format --check . && pytest
```

## 🤝 Contributing

PRs are welcome. Run `ruff check . && ruff format --check . && pytest` before you open one.

## 📬 Contact — Viprasol Tech Private Limited

- 🌐 Website: [viprasol.com](https://viprasol.com)
- ✉️ Email: [support@viprasol.com](mailto:support@viprasol.com)
- 💬 Telegram: [t.me/viprasol_help](https://t.me/viprasol_help) · 📱 WhatsApp: +91 96336 52112
- 🐙 GitHub: [@Viprasol-Tech](https://github.com/Viprasol-Tech) · 💼 [LinkedIn](https://www.linkedin.com/in/viprasol/) · 𝕏 [@viprasol](https://twitter.com/viprasol)

> *Viprasol Tech builds fintech software, algorithmic trading systems, MT4/MT5 bots, AI voice agents, and B2B SaaS. Need a custom build? [Get in touch](mailto:support@viprasol.com).*

## License

[MIT](LICENSE) © 2026 Viprasol Tech Private Limited
