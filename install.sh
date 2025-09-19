#!/bin/bash

sudo dnf update
sudo dnf install python3-3.13.7-1

python3 -m pip install virtualenv
python3 -m virtualenv virtual
source virtual/vin/actvate

sudo dnf install PyQt5==5.15.11
sudo dnf install PyQt5_sip==12.16.1

python app.py


