# SETUP

## Setting up project folder

**In root or desired directory**

```bash
mkdir midterm_project/
```

**Access project folder**
```bash
cd midterm_projects/
```

**Open in vscode**
```bash
code .
```

### Create the following folders and files ###
- `.github/workkflows/tests.yml`

- `.vscode`

- `app/`

  - `__init__.py`

  - `calculation.py`

  - `calculator_config.py`

  - `calculator_memento.py`

  - `calculator_repl.py`

  - `calculator.py`

  - `exceptions.py`

  - `history.py`

  - `input_validators.py`

- `tests/`

  - `__init__.py`

  - `test_calculation.py`

  - `test_calculator.py`

  - `test_config.py`

  - `test_exceptions.py`

  - `test_history.py`

  - `test_operations.py`

  - `test_validators.py`

- `.gitignore`

- `LICENSE`

- `main.py`

- `pytest.ini`

- `README.md`

- `requirements.txt`

## Initialization

### First set python version to 3.10 ###
```bash
pyenv local 3.10
```

### Create and activate venv ###
```bash
python3 -m venv venv

source venv/bin/activate
```

### Initialize repository ###
```bash
git init
```

### Add remote github repo ###
```bash
git remote add origin git@github.com:dbalicky/midterm_project.git
```

### Adding, committing, and pushing to github repo ###

### Add folder/files then commit ###
```bash
git add <folder_name/file_name>
```
```bash
git commit -m 'added <file(s)>'
```

### Initial push, then each subsequent push ###
```bash
git push --set-upstream origin main 
```
```bash
git push
```

