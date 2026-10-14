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
    
def test_liste_departements(donnees: list[dict[str, str]]) -> None:
    departements = population.build_list_departements(donnees)

    assert len(departements) == 99
    assert ("15", "Cantal") in departements
    assert departements == sorted(departements)
    assert len(departements) == len(set(departements))


def test_liste_communes(donnees: list[dict[str, str]]) -> None:
    communes = population.build_list_communes(donnees)

    assert len(communes) == 35836
    assert ("02598", "Pernant") in communes
    assert communes == sorted(communes)
    assert len(communes) == len(set(communes))


def test_communes_meme_code_noms_differents(
    donnees: list[dict[str, str]],
) -> None:
    communes = population.build_list_communes(donnees)

    assert ("14713", "Montillières-sur-Orne") in communes
    assert ("14713", "Trois-Monts") in communes