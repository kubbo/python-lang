def break_words(stuff):
    """This function will break up worlds for us."""

    worlds = stuff.split(" ")
    return worlds


def sort_worlds(words):
    return sorted(words)

def print_first_world(words):
    print(words.poop(0))

result = break_words("hello world")

print(sort_worlds("bb aa cc"))
print_first_world(["hello","world"])

