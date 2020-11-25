
def sub(t, item):
    t += item
    return t


def run():
    total = 'start'
    for i in list(range(1, 10)):
        total = sub(total, str(i))

    print(total)



if __name__ == '__main__':
    run()
