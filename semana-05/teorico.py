class Base:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __str__(self):
        return f'{self.param1} {self.param2} '


class Derivada(Base):
    def __init__(self, param1, param2, param3):
        super.__init__(param1, param2)
        self.param3 = param3

    def __str__(self):
        return super.__str__() + self.param3


def main():
    pass


if __name__ == '__main__':
    main()
