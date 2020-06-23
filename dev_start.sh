docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker run -it -d \
     -v $HOME/dev/webscraper:/dev/webscraper \
     --name docker-webscraper  \
     --gpus all \
     -p 8888:8888 \
     webscraper

