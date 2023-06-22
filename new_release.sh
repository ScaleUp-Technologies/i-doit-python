#!/bin/bash

if [ "$1" == "" ] ; then
    echo "Please sepcify a new version number" 1>&2
    exit 1
fi

VERSION=$1
GIT_STATUS=$(git status -s |grep -v new_release.sh)

if [ -n "${GIT_STATUS}" ] ; then
    echo "Please checkin all files" 1>&2
    exit 1
fi

sed -i -e "s/version = .*/version = \"${VERSION}\"/" pyproject.toml
git commit -m 'New Version $VERSION' pyproject.toml
git tag v${VERSION}
echo git push origin v${VERSION}
echo git push origin main

