class Jungle:
    def __init__(self, name='hasan'):
        self.name = name

    def welcomeMessage(self):
        print(f'hello {self.name}, welcome to Jungle class :)')


class RateJungle(Jungle):
    def __init__(self, name, feedback):
        self.FeedBack = feedback
        super().__init__(name)

    def printRating(self):
        print(f'Thanks {self.name} for your feedback :)')
