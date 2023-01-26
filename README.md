# docker setup
cd docker
docker-compose up
# app setup 
./manage.py migrate
./manage.py runserver
