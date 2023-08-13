import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="fastapi_jwt",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="fastapi_jwt_env",
    load_dotenv=True,
)

settings = settings.from_env("production")
dev_settings = settings.from_env("development")
test_settings = settings.from_env("testing")

print(settings.db)
print(dev_settings.db)
print(test_settings.db)

"""
# How to use this application settings

```
from fastapi_jwt.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export fastapi_jwt_KEY=value
export fastapi_jwt_KEY="@int 42"
export fastapi_jwt_KEY="@jinja {{ this.db.uri }}"
export fastapi_jwt_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
fastapi_jwt_ENV=production fastapi_jwt run
```

Read more on https://dynaconf.com
"""
