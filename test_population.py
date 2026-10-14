from pathlib import Path

import pytest

import population


@pytest.fixture(scope="module")
def donnees() -> list[dict[str, str]]:
    chemin = Path(__file__).with_name("population.csv")
    return population.read_file(str(chemin))


def test_lecture_dimensions(donnees: list[dict[str, str]]) -> None:
    assert len(donnees) == 140827
    assert all(len(ligne) == 15 for ligne in donnees)


def test_lecture_preserve_codes(donnees: list[dict[str, str]]) -> None:
    assert donnees[5000]["Code Officiel Département"] == "02"


@pytest.mark.parametrize(
    "code, attendu",
    [
        ("39124", ("Chaumergy", 492, "2018")),
        ("63001", ("Aigueperse", 2790, "2018")),
        ("76005", ("Amfreville-la-Mi-Voie", 3354, "2018")),
        ("74275", ("Talloires-Montmin", 2039, "2018")),
        ("94022", ("Choisy-le-Roi", 46366, "2018")),
    ],
)
def test_population_commune(
    donnees: list[dict[str, str]],
    code: str,
    attendu: tuple[str, int, str],
) -> None:
    assert population.get_pop_commune(donnees, code) == attendu


def test_commune_inconnue(donnees: list[dict[str, str]]) -> None:
    assert population.get_pop_commune(donnees, "00000") is None