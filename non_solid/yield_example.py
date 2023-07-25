

def yield_example():
    call_made()
    yield 1
    call_made()
    yield 2
    call_made()
    yield 5
    call_made()


def call_made():
    print('call')


if __name__ == '__main__':
    result = yield_example()
    for number in result:
        print(number)