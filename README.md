# Django test project

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
A few example models are already present in crud.models.py. Make sure to make and run migrations when creating new models.

### Linting
Linting is done using flake8. This can be configured in the .flake8 file to conform with the coding standards. I also black formatting to format according to the linting rules.

### Testing
We should also try testing a simple endpoint/service

### Notes
- We may want to use django rest framework, an app to create Rest API's specifically