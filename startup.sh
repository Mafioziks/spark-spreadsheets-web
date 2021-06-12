#!/bin/bash

W_DIR=$(pwd)

docker container start 68d93d810679
docker container start 37ffdcc21f02

vue ui & # TODO: run vue project server itself

# switch to python env and run API
if [[ "env" == "$1" ]]; then
  . ./fyp/bin/activate
fi
python app.py &

# run front-end
cd client || exit 1
npm run serve &

# return
cd "$W_DIR" || exit 1