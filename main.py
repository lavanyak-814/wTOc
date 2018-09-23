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

WESTERN = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
CARNATIC = ['S', 'R', 'G', 'M', 'P', 'D', 'N']




def main():
    root, seq = convert.get_sequence()
    print(root, seq, "-----\n")
    notes = get_notes(seq)
    scale = build_scale(root)
    print("NOTES: ", notes)
    print("SCALE: ", scale)
    print("CARNATIC: ", convert(notes, scale))
    print("\ndone")


if __name__ == "__main__":
    main()
