# https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/
# Brandon Sturgeon

def garland(given):
    for i in xrange(len(given)/2):
        print given[:i]
        print given[-i:]
        if given[:i] == given[-i:]:
            print i

print garland("alfalfa")
