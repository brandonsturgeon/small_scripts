import random
# {pronoun} {modal verb} {verb} {determiner} {noun}

class SentenceBuilder():
    def __init__(self):
        self.pronouns    = ['I', 'he', 'she', 'you', 'it', 'that', 'they', 'each', 'few', 'many', 'someone', 'everybody']
        self.modal_verbs = ['must', 'shall', 'will', 'should', 'would', 'can', 'could', 'may','might']
        self.verbs       = ['run', 'jump', 'break', 'ram', 'destroy', 'color']
        self.determiner  = ['the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'our', 'their', 'much', 'many', 'most', 'some', 'any', 'enough', 'one', 'all', 'both', 'half', 'either', 'neither', 'each', 'every', 'other', 'another', 'such', 'what', 'rather', 'quite']
        self.nouns       = ['dog', 'pup', 'kitter', 'kite', 'shoe', 'shoes', 'phone', 'keyboard', 'mouse']

        pronoun    = random.choice(self.pronouns)
        modal_verb = random.choice(self.modal_verbs)
        verb       = random.choice(self.verbs)
        determiner = random.choice(self.determiner)
        noun       = random.choice(self.nouns)
        print "{} {} {} {} {}".format(pronoun, modal_verb, verb, determiner, noun)

if __name__ == "__main__":
    SentenceBuilder()
