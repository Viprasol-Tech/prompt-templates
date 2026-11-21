import pytest

from prompt_templates import PromptLibrary, format_prompt, get_template, list_templates, main


def test_builtin_templates_are_listed_with_variables():
    templates = list_templates()
    assert "summarize" in templates
    assert templates["summarize"]["variables"] == ["text", "length"]


def test_format_prompt_fills_every_variable():
    prompt = format_prompt("translate", text="Bonjour", source="French", target="English")
    assert prompt == "Translate the following text from French to English:\n\nBonjour"


def test_values_with_braces_are_not_reinterpreted():
    prompt = format_prompt("qa_pair", context="dict = {'a': 1}", question="What is {a}?")
    assert "{'a': 1}" in prompt and "What is {a}?" in prompt


def test_missing_variable_raises():
    with pytest.raises(ValueError, match="Missing variables"):
        format_prompt("summarize", text="only text")


def test_unknown_template_raises():
    with pytest.raises(ValueError, match="not found"):
        format_prompt("does-not-exist")
    assert get_template("does-not-exist") is None


def test_add_template_registers_custom_prompt():
    PromptLibrary.add_template("greet", "Say hello to {name}.", ["name"], "Greeting")
    try:
        assert format_prompt("greet", name="Asha") == "Say hello to Asha."
    finally:
        del PromptLibrary.TEMPLATES["greet"]


def test_cli_format(capsys):
    main(["--format", "summarize", "-v", "text=Long report", "length=20"])
    assert capsys.readouterr().out == "Summarize the following text in 20 words:\n\nLong report\n"


def test_cli_list_and_get(capsys):
    main(["--list"])
    assert "code_review:" in capsys.readouterr().out
    main(["--get", "explain"])
    assert "Variables: concept, audience, tone, context" in capsys.readouterr().out


@pytest.mark.parametrize(
    "argv",
    [
        ["--format", "summarize", "-v", "text=x"],
        ["--format", "summarize", "-v", "no-equals"],
        ["--get", "nope"],
    ],
)
def test_cli_errors_exit_nonzero(argv):
    with pytest.raises(SystemExit) as exc:
        main(argv)
    assert exc.value.code == 2
