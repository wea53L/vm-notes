# $ scriptname -u URL -f wordlist.txt
# script will send URL + wordlist[index], evaulate response
# anything 200 = output to console
# ? can restrict to only directories ?

# v2: optional output file
# optional control what responses written out somehow
# can optionally get files? how to handle extensions?


def enum_wordlist(list):
    raw_list = open(list, 'rb')
    raw_words = raw_list.readlines()
    print(raw_words[0:10])
    return raw_words

def main():
    # handle arguments?
    # for PoC, skip making this a fully fledged script, just a hack that works
    target_url = "http://192.168.56.101/"
    wordlist_file = "/Users/warrenkopp/githubs/vm-notes/siph0n_subdomain_list.txt"

    # print attacking <url> with <listname.ext>
    print("Attacking : " + target_url)
    print("With file: " + wordlist_file)

    # read wordlist
    words = enum_wordlist(wordlist_file)

    # Attack!

    # results
    # #### of #### words results:
    # http://thing/result1
    # http://thing/result2 etc

if __name__ == '__main__':
    main()
