from pydantic_settings import BaseSettings


class Constants:
    BASE_URL = "https://www.kayak.com/api/affiliate/autocomplete/v1/cars"


class Settings(BaseSettings):
    MAP_API_KEY: str

    class Config:
        env_file = ".env.sample"
        case_sensitive = True


constants = Constants()
settings = Settings()
