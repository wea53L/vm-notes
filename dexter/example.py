# https://codingsec.net/2016/05/brute-forcing-directories-file-locations/
# which is a copy/paste from Black Hat Python

import threading
import queue
import urllib.request
import urllib.parse
import urllib.error

threads = 50
target_url = "http://192.168.56.101"
wordlist_file = "/Users/warrenkopp/githubs/vm-notes/siph0n_subdomain_list.txt"
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101   Firefox/19.0"

def build_wordlist(wordlist_file):

    # read in the word list
    fd = open(wordlist_file,"rb")
    raw_words = fd.readlines()
    fd.close()

    # found_resume = False
    words = queue.Queue()

    for word in raw_words:
        word = word.rstrip()
        # if resume is not None:
        #     if found_resume:
        #         words.put(word)
        #     else:
        #         if word == resume:
        #             found_resume = True
        #             print("Resuming wordlist from: %s" % resume)
        #         else:
        #             words.put(word)
        words.put(word)
    return words

def dir_bruter(word_queue,extensions):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        # check to see if there is a file extension; if not,
        # it's a directory path we're bruting
        dot = '.'
        if dot.encode() not in attempt:
            print(attempt_list)
            attempt_list.append("/%s/" % attempt)
        else:
            print(attempt_list)
            attempt_list.append("/%s" % attempt)

        # if we want to bruteforce extensions
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt,extension))

        # iterate over our list of attempts
        for brute in attempt_list:
            url = "%s%s" % (target_url,urllib.parse.quote(brute))
            try:
                headers = {}
                headers["User-Agent"] = user_agent
                r = urllib.request.Request(url,headers=headers)
                response = urllib.request.urlopen(r)

                if len(response.read()):
                    print("[%d] =&gt; %s" % (response.code,url))

            except urllib.error.URLError as e:
                if hasattr(e, 'code') and e.code != 404:
                    print("!!! %d =&gt; %s" % (e.code,url))
                pass



word_queue = build_wordlist(wordlist_file)
extensions = ''  # [".php",".bak",".orig",".inc"]

dirb = dir_bruter(word_queue, extensions)

# for i in range(threads):
#     t = threading.Thread(target=dir_bruter, args=(word_queue,extensions))
#     t.start()
