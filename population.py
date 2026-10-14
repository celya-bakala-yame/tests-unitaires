# Vos import ici
import csv
import doctest

# le path du fichier de données
FILENAME = "population.csv"


def read_file(filename: str) -> list[dict[str, str]]:
    """retourne les données sous la forme d'une liste de dictionnaires

    Args:
        filename (str): le nom du fichier de données (n lignes)

    Returns:
        list: n-1 dictionnaires dont les clés sont les champs de la première ligne du fichier
        
    >>> data = read_file(FILENAME)
    >>> type(data)
    <class 'list'>
    >>> len(data)
    140827
    >>> type(data[0])
    <class 'dict'>
    >>> len(data[0])
    15
    >>> data[1000]["Nom Officiel Région"]
    'Grand Est'
    >>> data[5000]["Code Officiel Département"]
    '02'
    >>> data[10000]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25000]["Nom Officiel Commune / Arrondissement Municipal"]
    'Baneuil'
    >>> data[50000]["Population totale"]
    '1898.0'
    >>> data[75000]["Année de recensement"]
    '2018'
    >>> data[100000]["Nom Officiel EPCI"]
    'CC de la Région de Bar-sur-Aube'
    >>> data[125000]["Nom Officiel Département"]
    'Charente-Maritime'
    >>> data[1500]["Nom Officiel Région"]
    'Occitanie'
    >>> data[5500]["Code Officiel Département"]
    '25'
    >>> data[10500]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25500]["Nom Officiel Commune / Arrondissement Municipal"]
    'Fontenoy'
    >>> data[50500]["Population totale"]
    '52.0'
    >>> data[75500]["Année de recensement"]
    '2015'
    >>> data[100500]["Nom Officiel EPCI"]
    'CC de Yenne'
    >>> data[125500]["Nom Officiel Département"]
    'Aube'
    """

    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        l = list(reader)

    return l



def build_list_departements(
    data: list[dict[str, str]],
) -> list[tuple[str, str]]:
    """retourne la liste ordonnée des départements contenus dans les données

    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        list: la liste ordonnée des tuples (code dpt, nom dpt)
    
    >>> data = read_file(FILENAME)
    >>> ld = build_list_departements(data)
    >>> type(ld)
    <class 'list'>
    >>> len(ld)
    99
    >>> '15' in ld
    False
    >>> 15 in ld
    False
    >>> 'Cantal' in ld
    False
    >>> ('15', 'Cantal') in ld
    True
    >>> ld[::20]
    [('01', 'Ain'), ('22', "Côtes-d'Armor"), ('40', 'Landes'), ('60', 'Oise'), ('80', 'Somme')]
    >>> ld[5::20]
    [('06', 'Alpes-Maritimes'), ('27', 'Eure'), ('45', 'Loiret'), ('65', 'Hautes-Pyrénées'), ('85', 'Vendée')]
    >>> ld[10::20]
    [('11', 'Aude'), ('30', 'Gard'), ('50', 'Manche'), ('70', 'Haute-Saône'), ('90', 'Territoire de Belfort')]
    >>> ld[15::20]
    [('16', 'Charente'), ('35', 'Ille-et-Vilaine'), ('55', 'Meuse'), ('75', 'Paris'), ('95', "Val-d'Oise")]
    >>> ld[20::20]
    [('22', "Côtes-d'Armor"), ('40', 'Landes'), ('60', 'Oise'), ('80', 'Somme')]
    >>> ld[5]
    ('06', 'Alpes-Maritimes')
    >>> ld[15]
    ('16', 'Charente')
    >>> ld[25]
    ('27', 'Eure')
    >>> ld[35]
    ('35', 'Ille-et-Vilaine')
    >>> ld[45]
    ('45', 'Loiret')
    >>> ld[55]
    ('55', 'Meuse')
    >>> ld[65]
    ('65', 'Hautes-Pyrénées')
    """
    # votre code ici
    departements = set()

    for ligne in data:
        code = ligne["Code Officiel Département"]
        nom = ligne["Nom Officiel Département"]

        if code != "" and nom != "":
            departements.add((code, nom))

    l = sorted(departements)

    return l


def build_list_communes(
    data: list[dict[str, str]],
) -> list[tuple[str, str]]:
    """retourne la liste des tuples (code, commune)

    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        list: la liste ordonnée des tuples (code commune, nom commune)
    
    >>> data = read_file(FILENAME)
    >>> lc = build_list_communes(data)
    >>> type(lc)
    <class 'list'>
    >>> len(lc)
    35836
    >>> type(lc[999])
    <class 'tuple'>
    >>> len(lc[999])
    2
    >>> lc[999]
    ('02598', 'Pernant')
    >>> type(lc[999][0])
    <class 'str'>
    >>> type(lc[999][1])
    <class 'str'>
    >>> lc[100:103]
    [('01105', 'Civrieux'), ('01106', 'Cize'), ('01107', 'Cleyzieu')]
    >>> lc[900:903]
    [('02499', 'Montbavin'), ('02500', 'Montbrehain'), ('02501', 'Montchâlons')]
    >>> lc[2000:2003]
    [('06089', 'Opio'), ('06090', 'Pégomas'), ('06091', 'Peille')]
    >>> lc[5000:5003]
    [('14712', 'Troarn'), ('14713', 'Montillières-sur-Orne'), ('14713', 'Trois-Monts')]
    >>> lc[10000:10003]
    [('27522', 'Saint-Christophe-sur-Condé'), ('27523', "Saint-Clair-d'Arcey"), ('27524', 'Sainte-Colombe-la-Commanderie')]
    >>> lc[15000:15003]
    [('39138', 'Chemin'), ('39139', 'Chêne-Bernard'), ('39140', 'Chêne-Sec')]
    >>> lc[20000:20003]
    [('54062', 'Benney'), ('54063', 'Bernécourt'), ('54064', 'Bertrambois')]
    >>> lc[25000:25003]
    [('63001', 'Aigueperse'), ('63002', 'Aix-la-Fayette'), ('63003', 'Ambert')]
    >>> lc[30000:30003]
    [('76002', 'Alvimare'), ('76004', 'Ambrumesnil'), ('76005', 'Amfreville-la-Mi-Voie')]
    >>> lc[-3:]
    [('97502', 'Saint-Pierre'), ('97701', 'Saint-Barthélemy'), ('97801', 'Saint-Martin')]
    """
    # votre code ici
    communes = set()

    for ligne in data:
        code = ligne["Code Officiel Commune / Arrondissement Municipal"]
        nom = ligne["Nom Officiel Commune / Arrondissement Municipal"]

        if code != "" and nom != "":
            communes.add((code, nom))

    l = sorted(communes)

    return l


def get_pop_commune(
    data: list[dict[str, str]],
    code: str,
) -> tuple[str, int, str] | None:
    """retourne la population totale d'une commune pour l'année de recensement la plus récente

    Args:
        data (list): la liste de dictionnaires retournée par read_file()
        code (str) : code de la commune considérée

    Returns:
        (int, str, str): (nom de la commune, population totale, année de recensement concernée)

    >>> data = read_file(FILENAME)
    >>> get_pop_commune(data, '39124')
    ('Chaumergy', 492, '2018')
    >>> get_pop_commune(data, '63001')
    ('Aigueperse', 2790, '2018')
    >>> get_pop_commune(data, '76005')
    ('Amfreville-la-Mi-Voie', 3354, '2018')
    >>> get_pop_commune(data, '74275')
    ('Talloires-Montmin', 2039, '2018')
    >>> get_pop_commune(data, '94022')
    ('Choisy-le-Roi', 46366, '2018')
    >>> get_pop_commune(data, '11151')
    ("Fontiès-d'Aude", 509, '2018')
    >>> get_pop_commune(data, '53210')
    ("Saint-Denis-d'Anjou", 1581, '2018')
    >>> get_pop_commune(data, '30266')
    ('Saint-Jean-de-Maruéjols-et-Avéjan', 897, '2018')
    >>> get_pop_commune(data, '07222')
    ('Saint-Cierge-sous-le-Cheylard', 211, '2018')
    >>> get_pop_commune(data, '00000')
    
    """
    # votre code ici
    t: tuple[str, int, str] | None = None
    annee_plus_recente = ""

    for ligne in data:
        if ligne["Code Officiel Commune / Arrondissement Municipal"] == code:
            annee = ligne["Année de recensement"]

            if annee > annee_plus_recente:
                nom = ligne["Nom Officiel Commune / Arrondissement Municipal"]
                population = int(float(ligne["Population totale"]))

                t = (nom, population, annee)
                annee_plus_recente = annee
        
    return t


def build_dict_departements(
    data: list[dict[str, str]],
) -> dict[str, tuple[int, int]]:
    """Retourne un dictionnaire dont la clé est le département, et la valeur une liste [nombre de communes, population totale]
    
    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        dict : un dictionnaire dont la clé est le code du dpt (str) et la valeur un tuple (int, int) nombre de communes, population totale
    
    >>> data = read_file(FILENAME)
    >>> dd = build_dict_departements(data)
    >>> type(dd)
    <class 'dict'>
    >>> len(dd)
    103
    >>> dd['18']
    (290, 310910)
    >>> dd['21']
    (713, 553151)
    >>> dd['27']
    (614, 627971)
    >>> dd['53']
    (264, 346208)
    """
    # votre code ici
    communes: dict[tuple[str, str], dict[str, str]] = {}

    for ligne in data:
        code = ligne["Code Officiel Commune / Arrondissement Municipal"]
        nom = ligne["Nom Officiel Commune / Arrondissement Municipal"]
        cle = (code, nom)
        annee = ligne["Année de recensement"]

        if cle not in communes:
            communes[cle] = ligne
        elif annee > communes[cle]["Année de recensement"]:
            communes[cle] = ligne

    d: dict[str, tuple[int, int]] = {}

    for ligne in communes.values():
        departement = ligne["Code Officiel Département"]
        population = int(float(ligne["Population totale"]))

        nombre, total = d.get(departement, (0, 0))
        d[departement] = (nombre + 1, total + population)

    return d



def stat_by_dpt(dd: dict[str, tuple[int, int]], dpt: str) -> tuple[int, int] | tuple[None, None]:
    """Retourne un tuple (nombre de communes, population totale)

    Args :
        dd (dict) : le dictionnaire retourné par build_dict_departements()
        dpt (str) : le département concerné

    Returns :
        tuple : (nombre de communes, population totale)
    
    >>> data = read_file(FILENAME)
    >>> dd = build_dict_departements(data)
    >>> s = stat_by_dpt(dd, '87')
    >>> type(s)
    <class 'tuple'>
    >>> len(s)
    2
    >>> s
    (202, 383163)
    >>> stat_by_dpt(dd, '77')
    (514, 1433625)
    >>> stat_by_dpt(dd, '13')
    (134, 2058818)
    >>> stat_by_dpt(dd, '08')
    (452, 278875)
    >>> stat_by_dpt(dd, '21')
    (713, 553151)
    >>> stat_by_dpt(dd, '2A')
    (124, 160294)
    >>> stat_by_dpt(dd, '34')
    (344, 1179337)
    >>> stat_by_dpt(dd, '53')
    (264, 346208)
    >>> stat_by_dpt(dd, '64')
    (546, 698710)
    >>> stat_by_dpt(dd, '75')
    (20, 2192485)
    >>> stat_by_dpt(dd, '18')
    (290, 310910)
    >>> sbd = stat_by_dpt(dd, 'Corse')

    """
    # votre code ici
    if dpt in dd:
        return dd[dpt]
    return (None, None)

def main() -> None:
    # votre code de test ici
    # le code ci dessous est exécuté avec la commande :
    #   python population.py
    pass
    # Exemples d'appels
    # data = read_file(FILENAME)
    # l = build_list_departements(data)
    # c = build_list_communes(data)
    # p = get_pop_commune(data, '39124')
    # d = build_dict_departements(data)
    # s = stat_by_dpt(d, '77')

    
# Ne pas modifier le code ci-dessous
if __name__ == '__main__':
    dt = True
    # dt = False # Décommenter pour exécuter "main()"
    if dt:
        # la ligne suivante teste la fonction "read_file"
        doctest.run_docstring_examples(read_file, globals(), verbose=True)
    else:
        main()
        
if __name__ == '__main__':
    dt = True
    # dt = False # Décommenter pour exécuter "main()"
    if dt:
        # la ligne suivante teste la fonction "read_file"
        doctest.run_docstring_examples(get_pop_commune, globals(), verbose=True)
    else:
        main()

