#lav

'''
TO DO
-get_notes
-build_key
    -major to minor converter?
-convert

FUTURE
-add interactive piano that will add notes
'''

import convert
import ui





def main():
    root, seq = convert.get_sequence()
    print(root, seq, "-----\n")
    notes = convert.get_notes(seq)
    scale = convert.build_scale(root)
    print("NOTES: ", notes)
    print("SCALE: ", scale)
    print("CARNATIC: ", convert.convert(notes, scale))
    ui.piano_set_up()
    print("\ndone")


if __name__ == "__main__":
    main()
