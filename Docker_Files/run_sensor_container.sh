## TO Build docker image
docker build -t sensors-container:latest .

##TO Run docker image
sudo docker run --name sensors-container sensors-container
# sudo docker run --restart=always sensors-container data_generator.py
# docker logs sensors-containe