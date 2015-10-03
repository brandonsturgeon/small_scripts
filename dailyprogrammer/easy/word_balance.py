# https://www.reddit.com/r/dailyprogrammer/comments/3c9a9h/20150706_challenge_222_easy_balancing_words/
# Brandon Sturgeon

from string import ascii_uppercase

# Easy alphabet
# We add a - to the front so we don't have to worry about +1'ing later
ALPH = ascii_uppercase
ALPH = "-"+ALPH



# Quick #
def balance_quick(GIVEN):
    for k, letter in enumerate(GIVEN):
        before_value = sum([ALPH.find(the_letter)*(len(GIVEN[:k])-_) for _, the_letter in enumerate(GIVEN[:k])])
        after_value = sum([ALPH.find(the_letter)*(_+1) for _, the_letter in enumerate(GIVEN[k+1:])])

        if before_value == after_value:
            return "{} {} {} - {}".format(GIVEN[:k], letter, GIVEN[k+1:], after_value)

# Long #
def balance_long(GIVEN):

    # Letter is balance point
    for k, letter in enumerate(GIVEN):

        # Calculate value of all letters before balance point
        before_values = []
        for before_k, before_letter in enumerate(GIVEN[:k]):
            # Distance before is harder because the first thing in
            # the list of before_letters is actually the furthest
            letter_weight = ALPH.find(before_letter)
            distance = len(GIVEN[:k]) - before_k
            before_values.append(letter_weight * distance)
        before_sum = sum(before_values)

        # Calculate value of all letters after balance point
        after_values = []
        for after_k, after_letter in enumerate(GIVEN[k+1:]):
            # Don't need to do anything special with distance, it's just the key+1
            letter_weight = ALPH.find(after_letter)
            distance = after_k+1
            after_values.append(letter_weight * distance)
        after_sum = sum(after_values)


        # Final check
        if before_sum == after_sum:
            return "{} {} {} - {}".format(GIVEN[:k], letter, GIVEN[k+1:], after_sum)

the_word = "WRONGHEADED"
print "Quick way"
print balance_quick(the_word)

print ""

print "Long way"
print balance_long(the_word)
