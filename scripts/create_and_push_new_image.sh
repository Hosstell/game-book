
USERNAME=${USERNAME}

VERSION=$(cat version.txt)
docker manifest inspect $USERNAME/game-book:$VERSION > /dev/null
if [ $? -eq 0 ]; then
  echo "--- ${VERSION} version already exists. Update version in version.txt in project root"
  exit 1
fi

set -e

docker build -t game-book .

echo "--- Deploying latest version of game-book image"
docker image tag game-book $USERNAME/game-book:latest
docker image push $USERNAME/game-book:latest

echo "--- Deploying ${VERSION} version of game-book image"
docker image tag game-book $USERNAME/game-book:${VERSION}
docker image push $USERNAME/game-book:${VERSION}

echo "--- New image is built (${VERSION}v.)"