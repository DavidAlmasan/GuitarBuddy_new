def chordToIndex(chord):
    """Takes <chord> variable and returns an integer"""
    chordDict = {"A": 0,
                 "Am": 1,

                 "B": 2,
                 "Bm": 3,

                 "C": 4,
                 "Cm": 5,

                 "D": 6,
                 "Dm": 7,

                 "E": 8,
                 "Em": 9,

                 "F": 10,
                 "Fm": 11,

                 "G": 11,
                 "Gm": 12,}

    return chordDict(chord)
