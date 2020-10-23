#!/bin/sh

# push更新到仓库
MESSAGE=`date`
echo $MESSAGE

git add .
git commit -m "$MESSAGE"
git push origin master
