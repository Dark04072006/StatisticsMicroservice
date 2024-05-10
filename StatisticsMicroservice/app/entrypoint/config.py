from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class Config:
    db_uri: str

    def __post_init__(self) -> None:
        if not self.db_uri:
            raise RuntimeError("DB_URI environment variable is not set")

    @staticmethod
    def load_from_env() -> "Config":
        db_user = getenv("POSTGRES_USER")
        db_password = getenv("POSTGRES_PASSWORD")
        db_host = getenv("POSTGRES_HOST")
        db_port = getenv("POSTGRES_PORT")
        db_name = getenv("POSTGRES_DB")

        if not db_user:
            raise RuntimeError("POSTGRES_USER environment variable is not set")

        if not db_password:
            raise RuntimeError("POSTGRES_PASSWORD environment variable is not set")

        if not db_host:
            raise RuntimeError("POSTGRES_HOST environment variable is not set")

        if not db_port:
            raise RuntimeError("POSTGRES_PORT environment variable is not set")

        if not db_name:
            raise RuntimeError("POSTGRES_DB environment variable is not set")

        db_uri = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

        return Config(db_uri=db_uri)
