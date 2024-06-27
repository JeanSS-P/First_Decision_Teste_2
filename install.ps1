virtualenv -p python3 venv;
.\venv\scripts\activate;
pip install -r .\requirements.txt;
pre-commit install;
