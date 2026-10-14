import pytest


@pytest.fixture
def texte() -> str:
    return "hello world"


def test_upper() -> None:
    assert "foo".upper() == "FOO"


def test_isupper() -> None:
    assert "FOO".isupper()
    assert not "Foo".isupper()


def test_split(texte: str) -> None:
    assert texte.split() == ["hello", "world"]


def test_split_argument_invalide(texte: str) -> None:
    with pytest.raises(TypeError):
        texte.split(2)
    
@pytest.mark.parametrize(
    "entree, attendu",
    [
        ("python", "PYTHON"),
        ("Bonjour", "BONJOUR"),
        ("", ""),
        ("123", "123"),
        ("été", "ÉTÉ"),
    ],
)
def test_upper_parametre(entree: str, attendu: str) -> None:
    assert entree.upper() == attendu