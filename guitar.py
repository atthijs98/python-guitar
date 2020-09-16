import winsound
import time

# A semitone (half-step) is the twelfth root of two
# https://en.wikipedia.org/wiki/Semitone
# https://en.wikipedia.org/wiki/Twelfth_root_of_two
SEMITONE_STEP = 2 ** (1/12)

# Standard tuning for a guitar - EADGBE
LOW_E_FREQ = 82.4    # Baseline - low 'E' is 82.4Hz
# In standard tuning, we use the fifth fret to tune the next string
# except for the next-to-highest string where we use the fourth fret.
STRING_STEPS = [5, 5, 5, 4, 5]

# Number of frets can vary but we will just presume it's 24 frets
N_FRETS = 24

# This will be a list of the frequencies of all six strings,
# a list of six lists, where each list is that string's frequencies at each fret
fret_freqs = []
# Start with the low string as our reference point
# We just short-hand the math of multipliying by SEMITONE_STEP over and over
fret_freqs.append([LOW_E_FREQ * (SEMITONE_STEP ** n) for n in range(N_FRETS)])
# Now go through the upper strings and base of each lower-string's fret, just like
# when we are tuning a guitar
for tuning_fret in STRING_STEPS:
    # Pick off the nth fret of the previous string and use it as our base frequency
    base_freq = fret_freqs[-1][tuning_fret]
    fret_freqs.append([base_freq * (SEMITONE_STEP ** n) for n in range(N_FRETS)])

for stringFreqs in fret_freqs:
    # We don't need 14 decimal places of precision, thank you very much.
    print(["{:.1f}".format(f) for f in stringFreqs])


base_notes = {"E": 82.4, "A": 110.0, "D": 146.8, "G": 196.0, "B": 246.9, "e": 329.6}
semitone_step = 2 ** (1/12)

def beep(note, tempo):
    string, fret = note[:len(note)//2], note[len(note)//2:]
    string_to_play = int(base_notes.get(string))
    print(string_to_play * (semitone_step ** int(fret)))
    winsound.Beep(int(string_to_play * (semitone_step ** int(fret))), tempo)

beep("A3", 500)
beep("D0", 500)
beep("D2", 500)
beep("D3", 500)
beep("G0", 500)
beep("G2", 500)
beep("B0", 500)
beep("B1", 500)



