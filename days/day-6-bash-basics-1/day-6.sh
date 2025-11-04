#!/bin/bash

#Echo user if root

ROOT_UID=0   # Root has $UID 0.

if [ "$UID" -eq "$ROOT_UID" ]  # Will the real "root" please stand up?
then
  echo "You are root."
else
  echo "You are just an ordinary user (but mom loves you just the same)."
fi

echo "You are in $PWD"

count=0
extension=$1
echo "*$extension"
find . -mindepth 1 -type f -name "*$extension" -printf x | wc -c

exit 0
