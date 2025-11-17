# TP3-Calculette
Calculette - Analyse, refactoring, tests, exceptions, SonarCloud et CI/CD

# Etape effectuer durant le projet
## Installation de Pytest

Pytest est un framework de test pour Python qui simplifie l'écriture et l'exécution de tests logiciels pour des projets Python.

### Comment l'utiliser ?

Pour utiliser python il faut avoir des fichiers test ou bien celui par defaut de python qui est __init__.py mais dans ce projet pour nous c'est test_calc.py qui est le fichier de test pour notre fichier de correction de dirtyCalc.py qui est calc.py.

Pour faire le test on execute la commande "pytest" qui ira faire le scan du fichier test et annoncera le pourcentage de qualité du code.

# Problème percu dans le scan

Apres avoir effectuer un scan nous avons eu un rapport disant " Quality Gate Failed ", Failed condition 0% Coverage on New Code (required ≥ 80%)

## Etapes effectuer pour ce problème

- Remarque : Coverage est un fichier à générer sur notre éduteur et c'est le fichier scaner par SonarQube qui veut un fichier coverage.xml

- Pour generer un coverage et l'envoyer à SonarQube : 
1. Installer pytest-cov : pip install pytest-cov
2. Lancer tests avec coverage : pytest --cov=. --cov-report xml
3. Fournir coverage.xml à SonarQube

- Modification dans le fichier YML :
    - name: Install dependencies
        run: |
          pip install -r requirements.txt || true
          pip install pytest pytest-cov

    - name: Run tests with coverage
        run: |
          pytest --cov=. --cov-report xml

- Modification dans sonar-project.properties : sonar.python.coverage.reportPaths=coverage.xml

