# CTF SQLI task

The application requires Python3.10, packages are mentioned
in `requirements.txt`

## Application environment
You should specify some environment variables for the task:
### DB_HOST 
Postgres' database host, default is `localhost`
### DB_NAME 
Postgres database name, default is `pgdb`
### DB_USER
Database username, default is `postgres`
### DB_PASSWORD 
Password to connect to Postgres database default is `pgpassword`


To run this package on your PC, you should to perform an installation:

#### Installation:
```shell
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run locally:
```shell
export PYTHONPATH=src
python -u -m src
```

to run this app via `Docker`:

#### Run via Docker:
```shell
docker-compose -p ctf-sqli up --build
```

### There are also short aliases for both actions:

To run local:
```shell
make run
```

To run via Docker:

```shell
make docker-run
```

This application represents `Structured Query Language Injection` in postgres database.


### main IDEA of a task:
flag-hub -- flag storage for sharing. Anyone can see his own flags, and list of users, you can store your own flag, create, new user if not exist, and see your own flags, but can't see others
you should perform an sql injection to see admin's flag. 
