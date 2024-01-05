# Project Name

#Welcome to Test Task! This project utilizes an API_KEY from https://hunter.io/api-keys  to access external services. To set up your development environment, follow the instructions below.

pip install python-dotenv  
from dotenv import load_dotenv  

load_dotenv()  

# up container  
docker-compose up --build --force-recreate  

# endpoints
http://127.0.0.1:8000/api/results/  
http://127.0.0.1:8000/api/results/{id_email}  
http://127.0.0.1:8000/api/results/{id_email}/delete  
http://127.0.0.1:8000/api/all-results/  
