#! /bin/bash

# for item in wordlist

# echo item into
# gpg --passphrase-fd <item> /mnt/flag/.trash/flag.txt.gpg

for p in $(cat /root/Desktop/sorted.txt)
do
  echo "${p}"
	gpg --output /root/flag --batch --passphrase "${p}" --decrypt /mnt/flag/.trash/flag.txt.gpg

	if [ -a /root/flag ]
	then
		echo "found ${p}"
		exit
	fi
done

#
# for line in $(cat /root/Desktop/gibson_wordlist_l33t.txt);
#   do
#     echo $line | gpg --output=/root/Desktop/winning.txt --batch --passphrase 0 --decrypt /mnt/flag/.trash/flag.txt.gpg
#
#     if [-a /root/Desktop/winning.txt]
#     then
#       echo 'winning'
#       exit
#     fi
#
#   done
# /mnt/flag/.trash/flag.txt.gpg
