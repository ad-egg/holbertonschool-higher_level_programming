#!/bin/bash
# script that takes a URL then sends it a request and displays only the status code of the response
curl "$1" -sIw "%{http_code}" -o /dev/null
