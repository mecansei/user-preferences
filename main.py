import configparser
import os

configuration = configparser.ConfigParser()
configuration.read("./application.ini")

environment: str = os.getenv("ENVIRONMENT", "DEV")
for key, value in configuration[environment].items():
    os.environ[key.upper()] = str(value)

# Must be here to initiate the env variables before initialize
# all components
from src.web.serverconfig.FlaskConfig import FlaskConfig

if __name__ == "__main__":
    app = FlaskConfig()()
