from abc import ABCMeta, abstractmethod


class Jungle(metaclass=ABCMeta):
    def __init__(self, name='vida'):
        self.name = name

    def WelcomeMessage(self):
        print(f'Hello {self.name}, welcome to jungle :)')

   # @abstractmethod
   # def scarysound(self):
   #     pass