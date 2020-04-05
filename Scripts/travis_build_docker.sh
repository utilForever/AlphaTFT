#!/usr/bin/env bash

set -e

if [ $# -eq 0 ]
  then
    docker build -t utilforever/alphatft .
else
    docker build -f $1 -t utilforever/alphatft:$2 .
fi
docker run utilforever/alphatft