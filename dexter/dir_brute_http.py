# built for python3.
# exercise to build a simple brute-forcer of my own
# input should be a url/ip address
# and wordlist file
# output will be the positive matches,
# and a calculation of hits.
# XXX matches from XXXX lines in file.

import requests

def main():
    # process & check url
    url = get_url_from_user()
    print(url + ' success')
    # process & check wordlist
    wordlist = get_wordlist_from_user()
    count = 0
    for word in wordlist:
        count += 1

    print(wordlist[1003].strip())
    # Attack!

    # output


def get_url_from_user():
    url = input('What is the base url(http://name.domain/ or http://ipaddress/)? ')
    # validate URL actually works

    return url


def get_wordlist_from_user():
    wordlist = []
    location = input('enter location of wordlist(/path/to/file.txt) ')
    # read file into list/dictionary
    raw_input = open(location, 'rb')
    wordlist = raw_input.readlines()
    raw_input.close()

    return wordlist

if __name__ == '__main__':
    main()
