"""
Prompt templates - Reusable, optimized prompt library.

Professional prompt templates for common tasks.
"""

from typing import Dict, List, Optional


class PromptTemplate:
    """Single prompt template."""

    def __init__(self, name: str, template: str, variables: List[str], description: str = ""):
        self.name = name
        self.template = template
        self.variables = variables
        self.description = description

    def format(self, **kwargs) -> str:
        """Format template with variables."""
        return self.template.format(**{k: kwargs.get(k, "") for k in self.variables})

    def validate(self, **kwargs) -> bool:
        """Check if all variables provided."""
        return all(k in kwargs for k in self.variables)


class PromptLibrary:
    """Library of prompt templates."""

    TEMPLATES = {
        "summarize": PromptTemplate(
            name="summarize",
            template="Summarize the following text in {length} words:\n\n{text}",
            variables=["text", "length"],
            description="Summarize text to specific length"
        ),
        "explain": PromptTemplate(
            name="explain",
            template="Explain {concept} to a {audience}. Be {tone}.\n\n{context}",
            variables=["concept", "audience", "tone", "context"],
            description="Explain concept to specific audience"
        ),
        "analyze": PromptTemplate(
            name="analyze",
            template="Analyze the following {type}:\n\n{content}\n\nFocus on: {focus}",
            variables=["type", "content", "focus"],
            description="Analyze content with specific focus"
        ),
        "generate_ideas": PromptTemplate(
            name="generate_ideas",
            template="Generate {count} creative ideas for: {topic}\n\nConstraints: {constraints}",
            variables=["topic", "count", "constraints"],
            description="Generate creative ideas"
        ),
        "code_review": PromptTemplate(
            name="code_review",
            template="Review this {language} code:\n\n{code}\n\nFocus on: {focus}",
            variables=["language", "code", "focus"],
            description="Review code with specific criteria"
        ),
        "translate": PromptTemplate(
            name="translate",
            template="Translate the following text from {source} to {target}:\n\n{text}",
            variables=["text", "source", "target"],
            description="Translate between languages"
        ),
        "qa_pair": PromptTemplate(
            name="qa_pair",
            template="Based on: {context}\n\nAnswer this question: {question}",
            variables=["context", "question"],
            description="Q&A based on context"
        ),
        "brainstorm": PromptTemplate(
            name="brainstorm",
            template="Brainstorm ideas for {goal}. Consider: {considerations}",
            variables=["goal", "considerations"],
            description="Brainstorm solutions"
        ),
    }

    @classmethod
    def get(cls, name: str) -> Optional[PromptTemplate]:
        """Get template by name."""
        return cls.TEMPLATES.get(name)

    @classmethod
    def list_templates(cls) -> Dict:
        """List all templates."""
        return {
            name: {
                "description": tmpl.description,
                "variables": tmpl.variables,
            }
            for name, tmpl in cls.TEMPLATES.items()
        }

    @classmethod
    def format_template(cls, name: str, **kwargs) -> str:
        """Format template directly."""
        template = cls.get(name)
        if not template:
            raise ValueError(f"Template '{name}' not found")

        if not template.validate(**kwargs):
            missing = [v for v in template.variables if v not in kwargs]
            raise ValueError(f"Missing variables: {missing}")

        return template.format(**kwargs)

    @classmethod
    def add_template(cls, name: str, template_str: str, variables: List[str], description: str = "") -> None:
        """Add custom template."""
        cls.TEMPLATES[name] = PromptTemplate(name, template_str, variables, description)


def get_template(name: str) -> Optional[PromptTemplate]:
    """Get template."""
    return PromptLibrary.get(name)


def list_templates() -> Dict:
    """List all templates."""
    return PromptLibrary.list_templates()


def format_prompt(name: str, **kwargs) -> str:
    """Format prompt from template."""
    return PromptLibrary.format_template(name, **kwargs)


def process(data: str, **kwargs) -> str:
    """Process function."""
    return f"Available templates: {len(PromptLibrary.TEMPLATES)}"


def main():
    """CLI entry point."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Manage prompt templates")
    parser.add_argument("--list", action="store_true", help="List templates")
    parser.add_argument("--get", help="Get specific template")
    parser.add_argument("--format", help="Format a template")
    parser.add_argument("-v", "--vars", nargs="+", help="Variables for formatting")

    args = parser.parse_args()

    if args.list:
        templates = PromptLibrary.list_templates()
        print("Available Templates:")
        for name, info in templates.items():
            print(f"  {name}: {info['description']}")
            print(f"    Variables: {', '.join(info['variables'])}")

    elif args.get:
        template = PromptLibrary.get(args.get)
        if template:
            print(f"Template: {template.name}")
            print(f"Description: {template.description}")
            print(f"Variables: {', '.join(template.variables)}")
            print(f"\nTemplate:\n{template.template}")
        else:
            print(f"Template '{args.get}' not found")

    else:
        print("Prompt templates ready")
        print(f"Available: {len(PromptLibrary.TEMPLATES)} templates")


if __name__ == "__main__":
    main()
