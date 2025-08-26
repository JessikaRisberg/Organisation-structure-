# Soltak

Detta projekt utför beräkningar för olika kunder.

## Installation

1. Klona repositoryt:
    ```bash
    git clone <repo-url>
    cd my_project
    ```

2. Skapa och aktivera en virtuell miljö:
    ```bash
    python -m venv env
    source env/bin/activate  # På Windows använd: env\Scripts\activate
    ```

3. Installera beroenden:
    ```bash
    pip install -r requirements.txt
    ```

4. Skapa en `.env`-fil med dina API-nycklar:
    ```plaintext
    # COUSTOMER 1
    COUSTOMER1_API_KEY=din_api_key_for_stenungsund
    # COUSTOMER 2
    COUSTOMER2_API_KEY=din_api_key_for_tjorn
    # COUSTOMER 3
    COUSTOMER3_API_KEY=din_api_key_for_kungalv
    ```

## Användning

För att köra beräkningarna:
```bash
python scripts/run_calculations.py
_____________________________________________________________________-

Structure of project
SOLTAK/
│
├── calculations/
│   ├── __init__.py
│   └── delta_calculations.py
│
├── config/
│   ├── __init__.py
│   ├── coustomer1_config.py
│   ├── coustomer2_config.py
│   ├── coustomer3_config.py
│   └── lynx_client.py
│
├── scripts/
│   ├── __init__.py
│   └── run_calculations.py
│
├── tests/
│   ├── __init__.py
│   ├── test_delta_calculations.py
│   └── test_lynx_client.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
