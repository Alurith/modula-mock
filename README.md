# modula-mock
Quick and dirty mock of [Modula ERP](https://www.modula.eu/it/wms-software/modula-wms-base/) to test it's API locally.

# How to run
Intall the requirements
```shell
    python -m venv venv
    pip install -r requirements
```
Run the project
``litestar --app src.main:app run --reload --debug``
