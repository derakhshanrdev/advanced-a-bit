class Jungle:
    def __init__(self, name=''):
        self.name = name

    def welcomeMessage(self):
        print(f'Hello {self.name}, welcome to Jungle class ')


def main():
    j = Jungle()
    j.welcomeMessage()
    k = Jungle('ali')
    k.welcomeMessage()


if __name__ == '__main__':
    main()
