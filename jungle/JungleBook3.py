class Jungle:
    def __init__(self, name='nima'):
        self.name = name

    def WelcomeMessage(self):
        print(f'Hello {self.name} welcome to jungle')


class RateJungle:
    def __init__(self, FeedBack):
        self._RateJungle__JungleGuideRating = None
        self.FeedBack = FeedBack

        self._StaffRating = 50

        self.__JungleGuideRating = 100

        self.UpdateStaffRating()
        self.UpdateGuideRating()

    def PrintRating(self):
        print(
            f'FeedBack : {self.FeedBack}\t"StaffRating" : {self._StaffRating}\tGuideRating : '
            f'{self.__JungleGuideRating}')

    def UpdateStaffRating(self):
        if self.FeedBack < 5:
            self._StaffRating += 5
        else:
            self._StaffRating -= 5

    def UpdateGuideRating(self):
        if self.FeedBack < 5:
            self._StaffRating += 10
        else:
            self.__JungleGuideRating -= 10

    @property
    def StaffRating(self):
        return self._StaffRating
