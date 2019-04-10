#!/bin/bash
SOURCE="~/Documents/OffersSwagger/"
DESTINATION='~/Documents/git-repos/offers_swagger/data/'
PATTERN='/productT*'

echo Hello, World
#for i in $(ls -t ~/Documents/OffersSwagger/VCS/productT*); do
#	echo item: $i
	#cp $i ~/Documents/git-repos/offers_swagger/data/vcs
#	break
#done

#py hello-world.py
# declare -a StringArray=("vcs" "joann")
# for i in ${StringArray[@]}; do
# 	#echo Source: $SOURCE$i$PATTERN
# 	for j in $(`ls -t {$SOURCE$i$PATTERN}`); do
# 		echo item: $item
# 		break
# 	done
# done

search_dir="~/Documents/OffersSwagger/vcs"

for i in $(ls -t "$search_dir"/*); do
	echo $i
	break
done