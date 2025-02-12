# Django test project

## Installation instructions

- Installeer Python 3.13 op je pc;
- Ga naar de GitLab repository (https://git.science.uu.nl/ics/sp/2025/v25a/trusthub) en clone de gehele git repository op gewenste locatie. Deze locatie wordt hierna de root folder genoemd;
- Open de backend in een IDE naar keuze;
- Maak een nieuwe file aan op hetzelfde niveau als de '.env.dist'-file genaamd '.env';
- Neem alle inhoud uit de '.env.dist'-file over en vul alle gegevens waar nog geen waarde voor is aan;
- Open een command line op de locatie van de root folder;
- Zet in de backend folder een virtual environment op door in de cmd ```python -m venv venv``` te typen;
- Run ```venv\Scripts\activate``` om de virtual environment te activeren;
- Gebruik de requirements.txt om alle benodigde packages te downloaden door het volgende commando in de cmd van de root folder te typen: ```pip install -r requirements.txt```
- Installeer en open docker desktop (https://www.docker.com/products/docker-desktop/)
- Creeër een docker-container door in de cmd in de backend folder het volgende commando te typen: ```docker-compose --profile "dev" up -d```;
- In de cmd van de backend, run ```python manage.py migrate``` en vervolgens ```python manage.py runserver```
- Ga naar localhost:8000/example om de voorbeeld endpoints te zien

## Development instructions
- Open the backend in its own vs code window, this will allow vs code to find the right interpreter from the venv.
- Enable the recommended extensions

## Recommended VS code extensions
- Python pack for intellisense (https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- flake8 for linting (https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- black formatter for reformatting based on linting (https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- Django for django specific syntax highlighting (https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)

## Features
### Docker
The project is completely runable in docker. We make use of a compose file to eaily create all containers necessary.
How to run in docker:
    - Install and run the Docker deamon
    - Run the project using ```docker compose up -d```
    - For development you may want to run the backend seperately and we may want to run a database viewer. For this, I have created profiles 'dev' and 'prod'. These can be run using ```docker compose --profile "{profile}" up -d```

### Postgres
A postgres database will be run when composing docker. The username and password and such are loaded from a .env file. The necessary variables can be found in .env.dist.
Run ```python manage.py migrate``` to run migrations and create the necessary tables.

### Models
A few example models are already present in example.models.py. Make sure to make and run migrations when creating new models.

### Linting
Linting is done using flake8. This can be configured in the .flake8 file to conform with the coding standards. I also black formatting to format according to the linting rules.

### Testing
We should also try testing a simple endpoint/service.

### Django rest framework
Library specifiek for rest api's, aangezien wij geen templates hoeven te grebruiken.
Features:
- OAuth
- Serialization
- Automatic documentation