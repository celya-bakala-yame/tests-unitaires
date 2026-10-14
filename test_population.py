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
    
@pytest.fixture(scope="module")
def statistiques(
    donnees: list[dict[str, str]],
) -> dict[str, tuple[int, int]]:
    return population.build_dict_departements(donnees)


def test_nombre_departements_statistiques(
    statistiques: dict[str, tuple[int, int]],
) -> None:
    assert len(statistiques) == 103


@pytest.mark.parametrize(
    "code, attendu",
    [
        ("87", (202, 383163)),
        ("77", (514, 1433625)),
        ("21", (713, 553151)),
        ("53", (264, 346208)),
        ("75", (20, 2192485)),
        ("2A", (124, 160294)),
    ],
)
def test_statistiques_departement(
    statistiques: dict[str, tuple[int, int]],
    code: str,
    attendu: tuple[int, int],
) -> None:
    assert population.stat_by_dpt(statistiques, code) == attendu


def test_departement_inconnu(
    statistiques: dict[str, tuple[int, int]],
) -> None:
    assert population.stat_by_dpt(statistiques, "inconnu") == (None, None)
    
@pytest.fixture
def petit_jeu() -> list[dict[str, str]]:
    return [
        {
            "Code Officiel Département": "01",
            "Nom Officiel Département": "Ain",
            "Code Officiel Commune / Arrondissement Municipal": "01001",
            "Nom Officiel Commune / Arrondissement Municipal": "Commune A",
            "Population totale": "120.0",
            "Année de recensement": "2018",
        },
        {
            "Code Officiel Département": "01",
            "Nom Officiel Département": "Ain",
            "Code Officiel Commune / Arrondissement Municipal": "01001",
            "Nom Officiel Commune / Arrondissement Municipal": "Commune A",
            "Population totale": "100.0",
            "Année de recensement": "2015",
        },
        {
            "Code Officiel Département": "01",
            "Nom Officiel Département": "Ain",
            "Code Officiel Commune / Arrondissement Municipal": "01002",
            "Nom Officiel Commune / Arrondissement Municipal": "Commune B",
            "Population totale": "80.0",
            "Année de recensement": "2018",
        },
    ]


def test_departements_sans_doublons(
    petit_jeu: list[dict[str, str]],
) -> None:
    assert population.build_list_departements(petit_jeu) == [
        ("01", "Ain"),
    ]


def test_communes_sans_doublons(
    petit_jeu: list[dict[str, str]],
) -> None:
    assert population.build_list_communes(petit_jeu) == [
        ("01001", "Commune A"),
        ("01002", "Commune B"),
    ]


def test_population_annee_recente(
    petit_jeu: list[dict[str, str]],
) -> None:
    assert population.get_pop_commune(petit_jeu, "01001") == (
        "Commune A", 120, "2018"
    )


def test_agregation_annee_recente(
    petit_jeu: list[dict[str, str]],
) -> None:
    assert population.build_dict_departements(petit_jeu) == {
        "01": (2, 200),
    }


def test_listes_vides() -> None:
    assert population.build_list_departements([]) == []
    assert population.build_list_communes([]) == []


def test_statistiques_vides() -> None:
    assert population.build_dict_departements([]) == {}


def test_recherche_donnees_vides() -> None:
    assert population.get_pop_commune([], "01001") is None
    assert population.stat_by_dpt({}, "01") == (None, None)
    
def test_lecture_csv_temporaire(tmp_path: Path) -> None:
    chemin = tmp_path / "population_test.csv"
    chemin.write_text(
        "Code Officiel Département;Population totale\n"
        "01;120.0\n"
        "02;80.0\n",
        encoding="utf-8",
    )

    resultat = population.read_file(str(chemin))

    assert resultat == [
        {"Code Officiel Département": "01", "Population totale": "120.0"},
        {"Code Officiel Département": "02", "Population totale": "80.0"},
    ]


def test_fichier_inexistant(tmp_path: Path) -> None:
    chemin = tmp_path / "absent.csv"

    with pytest.raises(FileNotFoundError):
        population.read_file(str(chemin))