"""prompt-templates: reusable, validated prompt templates for common LLM tasks."""

__version__ = "0.2.0"

from .core import (
    PromptLibrary,
    PromptTemplate,
    format_prompt,
    get_template,
    list_templates,
    main,
)

__all__ = [
    "PromptLibrary",
    "PromptTemplate",
    "format_prompt",
    "get_template",
    "list_templates",
    "main",
]
