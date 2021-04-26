##Put docker processes on stop
docker ps | awk '{print $1}' | tail -n+2 | xargs docker stop

##Remove docker processes
docker ps -a | awk '{print $1}' | tail -n+2 | xargs docker rm

##Remove docker image
docker images | grep \<none\> | awk '{print $3}' | xargs docker rmi
docker images | grep sensors-container | awk '{print $3}' | xargs docker rmi

##Sanity check
docker ps -a
docker images