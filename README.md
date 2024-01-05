# Project Name

#Welcome to Test Task! This project utilizes an API_KEY from https://hunter.io/api-keys  to access external services. To set up your development environment, follow the instructions below.

pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

# up container
docker-compose up --build --force-recreate
