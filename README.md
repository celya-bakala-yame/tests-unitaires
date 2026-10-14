## Erreurs possibles et points de vigilance

### Écrire un test qui n’est pas exécuté

Une fonction dont le nom ne commence pas par `test_` n’est pas découverte automatiquement comme test par pytest. Une commande qui se termine sans échec ne suffit donc pas : il faut vérifier que les tests attendus ont bien été collectés.

### Confondre afficher et vérifier

Écrire `print(resultat)` permet d’observer une valeur, mais ne vérifie pas qu’elle est correcte. Il faut une assertion comme `assert resultat == attendu` pour que pytest signale une différence.

### Modifier le résultat attendu pour faire passer le test

Lorsqu’un test échoue, le problème peut venir du code, du test ou des données. Il faut revenir à la consigne et calculer le résultat attendu indépendamment avant de corriger quoi que ce soit.

### Tester uniquement les cas habituels

Une fonction peut réussir avec les données du cours et échouer sur une liste vide, un code inconnu ou des doublons. Les cas limites permettent de mieux définir son comportement.

### Dépendre de l’ordre des données

Pour vérifier la sélection de l’année la plus récente, il faut essayer plusieurs ordres de lignes. Sinon, une fonction qui conserve simplement la première ou la dernière occurrence pourrait réussir le test par hasard.

### Modifier une fixture partagée

Une fixture de portée module peut fournir le même objet à plusieurs tests. Si un test modifie cette liste ou ce dictionnaire, les suivants peuvent recevoir des données différentes de celles prévues. Les tests doivent éviter ces modifications ou travailler sur une copie adaptée.

### Confondre réussite des tests et absence de bugs

Des tests réussis confirment les comportements effectivement vérifiés. Ils ne garantissent pas que tous les cas possibles sont couverts. Il faut pouvoir expliquer ce que chaque test détecte et ce qu’il ne vérifie pas.