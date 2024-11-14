# Test Aotomation Project

![Pytest](https://img.shields.io/badge/Pytest-%20-blue?style=flat-square&logo=pytest)

This test project

## 📋 Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Tests invocation](#tests-invocation)

## 🛠 Requirements

- Python 3.10+
- `pytest` 7.x.x+

## 🚀 Installation
Execute following commands

```shell
python3 -m venv venv 
```

```shell
source venv/bin/activate
```
```shell
pip install -r requirements.txt
```

## 🤖 Test invocation
To start test press green triangle opposite test name or execute this command

```shell
pytest -v tests/test_cat_api.py --html=report.html
```

You can change scope of test suite by changing test file, applying markers etc.
