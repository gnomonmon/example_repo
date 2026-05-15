# example_repo

A minimal Python package for testing GitHub clone and sync workflows.

## Structure

```
example_repo/
├── mypackage/
│   ├── __init__.py
│   ├── calculator.py
│   ├── formatter.py
│   └── utils.py
└── tests/
    ├── test_calculator.py
    ├── test_formatter.py
    └── test_utils.py
```

## Run tests

```bash
pip install -e .
pytest
```
