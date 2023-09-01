#!/bin/bash
# bash script to get header body length using cURL
curl -sI "$1" | grep Content-Length | cut -d ":" -f2 | tr -d " "
