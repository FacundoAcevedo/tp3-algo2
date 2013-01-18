#!/bin/bash

#variables
MAIN=src/main.py
#Ubico la version de python
which python &> /dev/null && PY=$(which python)
which python2 &> /dev/null && PY=$(which python2)
which python2.7 &> /dev/null && PY=$(which python2.7)

#Lo corro con nice para que valla mas rapido

nice -20 $PY $MAIN

