# docker setup
cd docker
docker-compose up
# app setup
cd .. 
./manage.py migrate
./manage.py runserver
