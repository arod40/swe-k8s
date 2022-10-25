docker build -t k8s-tuto-server .
echo y | docker image prune
docker compose up