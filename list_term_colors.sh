#!/bin/zsh


# if's are just there to format them nicely
for i in {0..255} ; do
    if [ $i -lt 10 ]
	then
	val="\x1b[38;5;${i}mcolour${i}   "
	printf $val
    elif [ $i -lt 100 ]
    then
	val="\x1b[38;5;${i}mcolour${i}  "
	printf $val
    else
	val="\x1b[38;5;${i}mcolour${i} "
	printf $val
    fi
done
