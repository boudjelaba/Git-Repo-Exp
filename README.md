# Guide — Créer, versionner et développer un projet Flask avec Git et GitHub

### Technologies

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Git](https://img.shields.io/badge/Git-Versioning-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

### Informations sur le dépôt

![Créé le](https://img.shields.io/github/created-at/boudjelaba/Git-Repo-Exp?label=Créé%20le)
[![Status](https://img.shields.io/badge/Status-En%20cours-yellow)]()
[![Current Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/boudjelaba/Git-Repo-Exp/node-chat)
![GitHub language count](https://img.shields.io/github/languages/count/boudjelaba/Git-Repo-Exp)
![License](https://img.shields.io/badge/License-MIT-green)
![Branch](https://img.shields.io/badge/Branch-main-blue)


Exemples de Badges GitHub spécifiques au repo disponibles :

[GitHub Badges Reference](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge?utm_source=chatgpt.com)

---

![CI](https://github.com/<UTILISATEUR>/Git-Repo-Exp/actions/workflows/ci.yml/badge.svg)

> Projet d’exemple pour apprendre Flask, Git, GitHub, les branches `main` / `dev` / `feature/*` et une intégration continue simple.

---

## Table des matières

<!-- TOC START -->
- [Guide — Créer, versionner et développer un projet Flask avec Git et GitHub](#guide--créer-versionner-et-développer-un-projet-flask-avec-git-et-github)
    - [Technologies](#technologies)
    - [Informations sur le dépôt](#informations-sur-le-dépôt)
  - [Table des matières](#table-des-matières)
  - [Introduction](#introduction)
    - [Objectif](#objectif)
    - [Technologies](#technologies-1)
    - [Schéma d'architecture](#schéma-darchitecture)
  - [1. Préparation de l’environnement et création du dossier de projet](#1-préparation-de-lenvironnement-et-création-du-dossier-de-projet)
  - [2. Premier commit du projet](#2-premier-commit-du-projet)
    - [Fichier `.gitignore`](#fichier-gitignore)
    - [Fichier `README.md`](#fichier-readmemd)
    - [Création du dépôt GitHub](#création-du-dépôt-github)
    - [Liaison avec GitHub](#liaison-avec-github)
  - [3. Création de l’application Flask](#3-création-de-lapplication-flask)
    - [Nouvelle structure du projet](#nouvelle-structure-du-projet)
    - [Fichier `app.py`](#fichier-apppy)
    - [Fichier `templates/index.html`](#fichier-templatesindexhtml)
    - [Test local du projet](#test-local-du-projet)
  - [4. Développement d’une fonctionnalité](#4-développement-dune-fonctionnalité)
    - [Création de la branche d'intégration `dev`](#création-de-la-branche-dintégration-dev)
    - [Création d'une branche de fonctionnalité](#création-dune-branche-de-fonctionnalité)
    - [Développement](#développement)
    - [Tester localement](#tester-localement)
    - [Enregistrer les modifications](#enregistrer-les-modifications)
    - [`app.py`](#apppy)
    - [`templates/index.html`](#templatesindexhtml)
      - [`templates/about.html`](#templatesabouthtml)
      - [`static/style.css`](#staticstylecss)
    - [Intégration dans `dev`](#intégration-dans-dev)
    - [Publication de la version stable](#publication-de-la-version-stable)
    - [Workflow de branches](#workflow-de-branches)
  - [6. Intégration continue](#6-intégration-continue)
    - [Pytest en local](#pytest-en-local)
  - [Commandes Git utiles](#commandes-git-utiles)
  - [Version stable](#version-stable)
    - [`requirements.txt`](#requirementstxt)
    - [Workflow GitHub Actions](#workflow-github-actions)
    - [Ajouter un nouveau fichier](#ajouter-un-nouveau-fichier)
  - [Conclusion](#conclusion)
<!-- TOC END -->

---

## Introduction

### Objectif

Ce projet a pour objectif de démontrer :

- la création d'une application Flask simple ;
- la gestion d'un environnement Python ;
- l'utilisation de Git pour le versionnement ;
- l'utilisation de GitHub pour l'hébergement du code ;
- la mise en place d'un workflow basé sur les branches `main`, `dev` et `feature/*`

### Technologies

- Python 3.10+.
- Flask.
- Git.
- GitHub.
- GitHub Actions.

### Schéma d'architecture

```text
Utilisateur
     │
     ▼
 Flask (app.py)
     │
     ▼
 Templates HTML
     │
     ▼
 CSS statique
```

Mermaid :

```mermaid
flowchart TD
    A[Utilisateur]
    B[Flask app.py]
    C[Templates HTML]
    D[CSS statique]

    A --> B
    B --> C
    C --> D
```

## 1. Préparation de l’environnement et création du dossier de projet

Installer les outils nécessaires :

- Python 3.10 ou supérieur.
- Git.
- VS Code.
- Un compte GitHub.

Créer le dossier du projet

```bash
mkdir Git-Repo-Exp
cd Git-Repo-Exp
```

Créer et activer un environnement virtuel :

```bash
python -m venv venv
```

- Linux/macOS : `source venv/bin/activate`
- Windows : `venv\Scripts\activate`

Installer Flask puis générer `requirements.txt` :

```bash
# touch requirements.txt
pip install flask
pip freeze > requirements.txt
```

## 2. Premier commit du projet

Créer les fichiers de base du dépôt :

```text
Git-Repo-Exp/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Fichier `.gitignore`

```gitignore
venv/
.venv/

__pycache__/
*.py[cod]

.pytest_cache/
.coverage

.env

.vscode/
.idea/

.DS_Store
Thumbs.db
```

### Fichier `README.md`

Copier et coller le contenu de ce document dans le `README.md`.

Initialiser Git puis créer le premier commit :

```bash
git init

git add README.md .gitignore LICENSE requirements.txt
git commit -m "chore: initialisation du dépôt"
```

### Création du dépôt GitHub

1. Aller sur [github.com/new](https://github.com/new)
2. Créer un dépôt nommé `Git-Repo-Exp`
3. **Ne pas cocher** : *Add a README*, *.gitignore*, *License*

### Liaison avec GitHub

```bash
git branch -M main

git remote add origin https://github.com/mon-compte/Git-Repo-Exp.git
# Variante SSH :
# git remote add origin git@github.com:mon-compte/Git-Repo-Exp.git

git push -u origin main
```

---

## 3. Création de l’application Flask

### Nouvelle structure du projet

```text
Git-Repo-Exp/
├── .gitignore
├── app.py
├── LICENSE
├── README.md
├── requirements.txt
├── screenshots/
├── static/
└── templates/
    └── index.html
```

### Fichier `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### Fichier `templates/index.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon Projet Exemple</title>
</head>
<body>

    <h1>Page d'accueil du projet Flask</h1>

</body>
</html>
```

### Test local du projet

Lancer l’application :

```bash
python app.py
```

Puis ouvrir :

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

Enregistrer le travail :

```bash
git init
git add .
git commit -m "feat: initialisation du projet Flask"
git push
```

---

## 4. Développement d’une fonctionnalité

### Création de la branche d'intégration `dev`

Après la publication de la première version sur `main`, créer une branche `dev` qui servira à centraliser les développements futurs.

```bash
git switch -c dev
# Publier la branche
git push -u origin dev
```

```mermaid
gitGraph
    commit id: "chore: initialisation du dépôt"
    commit id: "feat: initialisation du projet Flask"
    branch dev
    checkout dev
    branch feature/about-page
    checkout feature/about-page
    commit id: "feat: ajout de la page À propos et du CSS"
    checkout dev
    merge feature/about-page
    checkout main
    merge dev tag: "v1.0.0"
```

### Création d'une branche de fonctionnalité

Créer une branche depuis `dev` :

```bash
git switch dev
git pull origin dev

git switch -c feature/about-page
```

### Développement

Ajouter la fonctionnalité « À propos » et le CSS (voir sections ci-dessous) :

* modifier `app.py` ;
* modifier `templates/index.html` ;
* ajouter `templates/about.html` ;
* ajouter `static/style.css`.

> Après l'ajout de la fonctionnalité « À propos », l'arborescence devient :

  ```text
  Git-Repo-Exp/
  ├── .github/
  │   ├── ISSUE_TEMPLATE/
  │   ├── pull_request_template.md
  │   └── workflows/
  │       └── ci.yml
  ├── .gitignore
  ├── app.py
  ├── LICENSE
  ├── README.md
  ├── requirements.txt
  ├── screenshots/
  │   ├── home.png
  │   └── about.png
  ├── static
  │   └── style.css
  ├── templates
  │      ├── about.html
  │    └── index.html
  └── tests/
      └── test_app.py
  ```

### Tester localement

```bash
python app.py
```

Vérifier :

* [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* [http://127.0.0.1:5000/about](http://127.0.0.1:5000/about)

### Enregistrer les modifications

```bash
git add .
git commit -m "feat: ajout de la page À propos et du CSS"
git push -u origin feature/about-page
```

### `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Accueil</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}">Accueil</a>
        <a href="{{ url_for('about') }}">À propos</a>
    </nav>

    <h1>Page d’accueil du projet Flask</h1>
</body>
</html>
```

#### `templates/about.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>À propos</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}">Accueil</a>
        <a href="{{ url_for('about') }}">À propos</a>
    </nav>

    <h1>À propos</h1>
    <p>Exemple d’application Flask avec Git et GitHub.</p>
</body>
</html>
```

#### `static/style.css`

```css
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    background-color: #f4f4f4;
    color: #333;
}

h1 {
    color: #0066cc;
}

nav {
    margin-bottom: 20px;
}

nav a {
    margin-right: 15px;
    text-decoration: none;
    color: #0066cc;
    font-weight: bold;
}

nav a:hover {
    text-decoration: underline;
}
```

### Intégration dans `dev`

Après validation de la fonctionnalité, ouvrir une Pull Request :

```text
feature/about-page
        │
        ▼
   Pull Request
        │
        ▼
       dev
```

Ou fusionner localement :

```bash
git switch dev
git merge feature/about-page
git push origin dev
```

### Publication de la version stable

Lorsque les développements présents sur `dev` sont validés :

```bash
git switch main
git pull origin main

git merge dev

git tag -a v1.0.0 -m "Version stable 1.0.0"

git push origin main
git push origin v1.0.0
```

Flux recommandé :

```text
feature/about-page
        │
        ▼
   Pull Request
        │
        ▼
       dev
        │
        ▼
   Pull Request
        │
        ▼
      main
```

### Workflow de branches

Organisation recommandée :

```text
main      → branche stable
dev       → branche d’intégration
feature/* → branches de fonctionnalité
```

Exemple de workflow :

```mermaid
gitGraph
    commit id: "Initial commit"
    branch dev
    checkout dev
    commit id: "feat: initialisation du projet Flask"
    branch feature/about-page
    checkout feature/about-page
    commit id: "feat: ajout de la page À propos et du CSS"
    checkout dev
    merge feature/about-page
    checkout main
    merge dev tag: "v1.0.0"
```

```mermaid
gitGraph
    commit id: "feat: initialisation du projet Flask"
    branch dev
    checkout dev
    branch feature/about-page
    checkout feature/about-page
    commit id: "feat: ajout de la page À propos et du CSS"
    checkout dev
    merge feature/about-page
    checkout main
    merge dev tag: "v1.0.0"
```

```text
chore: initialisation du dépôt
    ↓
feat: initialisation du projet Flask
    ↓
création de dev
    ↓
feature/about-page
    ↓
merge dans dev
    ↓
merge dans main + tag v1.0.0
```

## 6. Intégration continue

Le workflow GitHub Actions doit :

- installer les dépendances ;
- vérifier la syntaxe ;
- exécuter les tests si présents.

Exemple de structure :

```text
.github/
└── workflows/
    └── ci.yml
```

### Pytest en local

```bash
python -m pytest
```

```bash
python -m pytest -v
```

## Commandes Git utiles

| Commande | Description |
|---|---|
| `git log --oneline --graph --all` | Historique visuel. |
| `git diff main..dev` | Différences entre branches. |
| `git branch` | Lister les branches locales. |
| `git branch -d feature/about-page` | Supprimer une branche locale. |
| `git push origin --delete feature/about-page` | Supprimer une branche distante. |

## Version stable

Les tags comme `v1.0.0` marquent les versions stables sur `main`.

Exemple :

```bash
git tag -a v1.0.0 -m "Version stable 1.0.0"
git push origin v1.0.0
```

### `requirements.txt`

```txt
flask>=2.0
requests>=2.28
```

### Workflow GitHub Actions

Placer ce fichier dans `.github/workflows/`.

```yaml
name: CI

on:
  push:
    branches: [main, dev, "feature/**"]
  pull_request:
    branches: [main, dev]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Check Flask app imports
        run: python -m compileall app.py

      - name: Install test dependencies
        run: |
          pip install pytest

      - name: Run tests
        run: pytest
```

### Ajouter un nouveau fichier

Créer un fichier :

```text
nom_fichier.extension
```

Puis :

```bash
git add nom_fichier.extension
git commit -m "Ajout du fichier nom_fichier"
git push
```

---

## Conclusion

> À ce stade, on dispose d'une application Flask simple, versionnée avec Git, hébergée sur GitHub et intégrée à une chaîne CI GitHub Actions. Cette structure constitue une excellente base pour apprendre le développement collaboratif et faire évoluer le projet avec de nouvelles fonctionnalités.

---
