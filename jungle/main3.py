from jungle.JungleBook3 import Jungle, RateJungle


def main():
    j = Jungle('daniel')
    j.WelcomeMessage()

    r = RateJungle(3)
    r.PrintRating()
    r._StaffRating = 15
    print('StaffRating :', r.StaffRating)
    print('GuideRating : ', r._RateJungle__JungleGuideRating)


if __name__ == '__main__':
    main()
