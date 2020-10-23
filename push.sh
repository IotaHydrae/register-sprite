#!/bin/bash

# push更新到仓库
MESSAGE=`date`
echo $MESSAGE

echo "Adding files to git"
git add .
echo "Adding message"
git commit -m "$MESSAGE"

echo "\033[32m PUSHING...\033[0m"
git push origin master
