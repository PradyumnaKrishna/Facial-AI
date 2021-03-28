docker build -t ipradyumna/facial-ai:amd64-$(date '+%Y-%m-%d') .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push ipradyumna/facial-ai:amd64-$(date '+%Y-%m-%d')