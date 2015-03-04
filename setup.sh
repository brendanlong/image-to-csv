#!/bin/bash
virtualenv -p python3 .
source bin/activate
pip install pillow
echo "You probably want to 'source bin/activate' now"
