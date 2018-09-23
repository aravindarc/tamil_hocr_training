#!/bin/sh

COUNT=266

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

a=0
while [ -f "../ImageStorage/RawImages/$a.jpg" ]
do
    rm -rf "../ImageStorage/ResultantStorage/$a"
    mkdir "../ImageStorage/ResultantStorage/$a"
    b=$(./DataAcquisition "../ImageStorage/RawImages/$a.jpg" "../ImageStorage/ResultantStorage/$a/")
    if [ $b -eq $COUNT ]
    then
        echo "${GREEN}Extracted character images from ${NC}$a.jpg"
    else
        echo "${RED}Error extracting from ${NC}$a.jpg"
    fi
    a=`expr $a + 1`
done
