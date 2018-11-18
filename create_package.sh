#!/bin/sh

FILE_NAME="skill_magic_giulio.zip"

rm $FILE_NAME
cp ./src/magic_giulio.py ./magic_giulio_venv/lib/python3.7/site-packages/
cd ./magic_giulio_venv/lib/python3.7/site-packages/ && zip -r ../../../../$FILE_NAME . && cd -