#!/usr/bin/bash
echo "write your custom message:"
read message
git add .
git commit -m" $message"
git push
