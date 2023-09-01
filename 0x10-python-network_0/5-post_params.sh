#!/bin/bash
# bash script to send POST using curl
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
