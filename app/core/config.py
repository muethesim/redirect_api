from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    INLINE_ADS_API_KEY: str
    COMPARETO_ADS_API_KEY: str

    class Config:
        env_file = ".env.sample"
        case_sensitive = True


settings = Settings()
