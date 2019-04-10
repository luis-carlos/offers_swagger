#!/bin/bash
echo Hello, World
for i in $(ls -t ~/Documents/OffersSwagger/VCS/productT*); do
	echo item: $i
	#cp $i ~/Documents/git-repos/offers_swagger/data/vcs
	break
done

#py hello-world.py
declare -a StringArray=("vcs" "joann")
for i in ${StringArray[@]}; do
	echo Folder: $i
done