#!/bin/bash

mkdir content
mkdir output

echo "output" >> .gitignore

if [ ! -d output/.git ]
then
    pushd output
    git init
    git remote add origin git@github.com:antroy/antroy.github.io.git
    git fetch
    git checkout -b pelican_master
    git branch --set-upstream-to=origin/pelican_master pelican_master
    popd
fi
