import json

from fastapi.openapi.utils import get_openapi

from main import app


def main():
    with open("./openapi.json", "w") as f:
        json.dump(
            get_openapi(
                title=app.title,
                version=app.version,
                openapi_version=app.openapi_version,
                description=app.description,
                routes=app.routes,
            ),
            f,
            indent=4,
        )
        f.write("\n")


if __name__ == "__main__":
    main()
