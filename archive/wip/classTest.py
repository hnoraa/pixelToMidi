class Track():
    def __init__(self, name, program, index):
        self.name = name
        self.program = program
        self.index = index

    def __repr__(self):
        return f"{self.name} - {self.program} - {self.index}"


def test(value) -> str:
    return value

if __name__ == '__main__':
    t = Track("test track", 44, 0)

    print(t)
    print(repr(t))

    print(test(123.4))

    print(test.__annotations__)