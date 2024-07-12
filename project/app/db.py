import os 

TORTOISE_ORM = {

    "connections": {"default": os.environ.get("DATABASE_URL")},
    "app": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}