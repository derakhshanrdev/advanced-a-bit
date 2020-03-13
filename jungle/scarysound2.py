from jungle.JungleBook2 import Jungle


class Animal(Jungle):
    def scarysound(self):
        print('Animals are running away due the scary sound :(')


class Bird(Jungle):
    def scarysound(self):
        print('birds are flying away due the scary sound :(')


class Insect(Jungle):
    def scarysound(self):
        print('Insect do not care about the scary sound !')
