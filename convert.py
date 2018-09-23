#CONVERT

def get_sequence():
    print("Please enter key (in major): ")
    root = input().upper()
    print("Please enter a sequence notes: ")
    sequence = input().split()
    return (root, sequence)

def get_notes(seq: list) -> list:
    result = []
    for x in seq:
        if x.upper() in WESTERN:
            result.append(x.upper())
    return result

def build_scale(root: str) -> list:
    start = 0
    for x in range(0, len(WESTERN)):
        if WESTERN[x] == root:
            start = x
            break
    return [WESTERN[x%12], WESTERN[(x+2)%12], WESTERN[(x+4)%12],
            WESTERN[(x+5)%12], WESTERN[(x+7)%12], WESTERN[(x+9)%12],
            WESTERN[(x+11)%12]]

def convert(notes: list, scale: list) -> list:
    result = []
    try:
        for i in notes:
            result.append(CARNATIC[scale.index(i)])
        return result
    except (ValueError):
        print("Note", i, "not in scale")
