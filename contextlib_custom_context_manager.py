from contextlib import contextmanager


@contextmanager
def poem_files(file, mode):
    print("Opening File")
    open_poem_file = open(file, mode)
    try:
        yield open_poem_file
    finally:
        print("Closing File")
        open_poem_file.close()


@contextmanager
def card_files(file, mode):
    print("Opening File")
    open_card_file = open(file, mode)
    try:
        yield open_card_file
    finally:
        print("Closing File")
        open_card_file.close()


with poem_files("poem.txt", "r") as poem:
    with card_files("card.txt", "w") as card:
        print(poem)
        print(card)
        card.write(poem.read())
