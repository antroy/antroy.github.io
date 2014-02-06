#!/bin/bash

if [ ! -d content ]
then
    mkdir content
fi

if [ ! -d output ]
then
    mkdir output
fi

grep "^output$" .gitignore

if [ $? != 0 ]
then
    echo "output" >> .gitignore
fi

if [ ! -d output/.git ]
then
    pushd output
    git init
    git remote add origin git@github.com:antroy/antroy.github.io.git
    git fetch
    git checkout -b master
    git branch --set-upstream-to=origin/master master
    popd
fi
