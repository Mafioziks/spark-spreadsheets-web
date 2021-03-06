#!/bin/bash

W_DIR=$(pwd)

# switch to python env and run API
if [[ "env" == "$1" ]]; then
  . ./fyp/bin/activate
fi
python app.py &

# run front-end
cd client
npm run serve &

# return
cd $W_DIR