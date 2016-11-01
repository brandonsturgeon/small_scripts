# {pronoun} {modal verb} {verb} {determiner} {noun}

class SentenceBuilder():
    def __init__(self):
        self.pronouns    = []
        self.modal_verbs = ['must', 'shall', 'will', 'should', 'would', 'can', 'could', 'may','might']
        self.verbs       = []
        self.determiner  = []
        self.nouns       = []

if __name__ == "__main__":
    SentenceBuilder()
