
# fastapi_jwt


## Install

from source
```bash
cd fastapi_jwt
make install
```

from pypi

```bash
pip install fastapi_jwt
```

## Executing


```bash
$ make docker-build
$ make docker-run
```

## CLI

```bash
❯ fastapi_jwt --help
Usage: fastapi_jwt [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  create-user  Create user
  run          Run the API server.
  shell        Opens an interactive shell with objects auto imported
```

### Creating a user

```bash
❯ fastapi_jwt create-user --help
Usage: fastapi_jwt create-user [OPTIONS] USERNAME PASSWORD

  Create user

Arguments:
  USERNAME  [required]
  PASSWORD  [required]

Options:
  --superuser / --no-superuser  [default: no-superuser]
  --help 
```

**IMPORTANT** To create an admin user on the first run:

```bash
fastapi_jwt create-user admin admin --superuser
```


## API

Run with `fastapi_jwt run` and access http://127.0.0.1:8000/docs


**For some api calls you must authenticate** using the user created with `fastapi_jwt create-user`.

## Testing

``` bash
make test
```

## Linting and Formatting

```bash
make lint  # checks for linting errors
make fmt   # formats the code
```


## Configuration


```py
from fastapi_jwt.config import settings
```

## Acessing variables

```py
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Defining variables

### On files

settings.toml

```toml
[development]
dynaconf_merge = true

[development.db]
echo = true
```

> `dynaconf_merge` is a boolean that tells if the settings should be merged with the default settings defined in fastapi_jwt/default.toml.

### As environment variables
```bash
export fastapi_jwt_KEY=value
export fastapi_jwt_KEY="@int 42"
export fastapi_jwt_KEY="@jinja {{ this.db.uri }}"
export fastapi_jwt_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Secrets

There is a file `.secrets.toml` where your sensitive variables are stored,
that file must be ignored by git. (add that to .gitignore)



