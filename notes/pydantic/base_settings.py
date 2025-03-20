from pydantic_settings import BaseSettings


# Python extension will read the .env file into the environment variables
# Check with powershell `gci env:* | sort-object name`
class Settings(BaseSettings):
    APP_NAME: str
    MY_VAR: str


# Load settings
settings = Settings()

# Print settings
print(settings.model_dump())
