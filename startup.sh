#!/bin/bash

W_DIR=$(pwd)

# switch to python env and run API
. ./fyp/bin/activate
python app.py &

# run front-end
cd client
npm run serve &

# return
cd $W_DIR