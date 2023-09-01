#!/bin/bash
# bash script to get allowed options using cURL
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
