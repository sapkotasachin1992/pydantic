# as we know some important creanditials are stored in env file . Now to read those env values we have pydantic settings


from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env")

    API_KEY:str #these are the variables stored in env and name must be same 
    DB_USERNAME:str

setting=Settings()
print(setting.API_KEY)