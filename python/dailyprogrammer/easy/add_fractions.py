# https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/
# Brandon Sturgeon

class Fraction():
    def __init__(self, fraction_input):
        split = [int(x) for x in fraction_input.rsplit("/")]
        self.numer = split[0]
        self.denom = split[1]

    def print_fraction(self):
        print "{} / {}".format(self.numer, self.denom)

    def simplify(self):
        is_simplified = False
        while not is_simplified:
            if self.numer % 2 != 0 or self.denom % 2 != 0:
                is_simplified = True
                break
            else:
                self.numer /= 2
                self.denom /= 2


def get_input():
    fraction_input = raw_input("Please enter the first fraction: ")
    fraction_one = Fraction(fraction_input)

    fraction_input = raw_input("Please enter the second fraction: ")
    fraction_two = Fraction(fraction_input)

    return fraction_one, fraction_two

def handle_input(the_input):
    fraction_one, fraction_two = the_input

    if fraction_one.denom == fraction_two.denom:
        add_similar(fraction_one, fraction_two)
    else:
        add_different(fraction_one, fraction_two)


def get_common_denom(fraction_one, fraction_two):
    common_denom = fraction_one.denom * fraction_two.denom
    return common_denom

# Make the fractions similar and then pass it to add_similar
def add_different(fraction_one, fraction_two):
    # Make denoms equal
    # Reduce
    common_denom = get_common_denom(fraction_one, fraction_two)
    fraction_one.denom = common_denom
    fraction_two.denom = common_denom

    # fraction_one.print_fraction()
    # fraction_two.print_fraction()

    # Now that they're similar we can add similar
    add_similar(fraction_one, fraction_two)

def add_similar(fraction_one, fraction_two):
    top_sum = sum((fraction_one.numer, fraction_two.numer))
    new_frac = Fraction("{}/{}".format(top_sum, fraction_one.denom))

    # Simplify

    # 1. Check if we can simplify
    if new_frac.denom % new_frac.numer == 0:
        # All done
        return new_frac.print_fraction()
    else:
        # Not all done
        new_frac.simplify()
        return new_frac.print_fraction()


if __name__ == "__main__":
    handle_input(get_input())
