#!/usr/bin/env bash

# bash script to setup database for the first time

python -c "import app; app.createDBTable()"
echo "> Database created"

pip install -r requirements.txt
echo "> Required packages installed" 
