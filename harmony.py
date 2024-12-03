from enum import IntEnum

# assumptions: octave equivalency & 12-tone equal temperament
Note = IntEnum('Note', 'C Csh_Db D Dsh_Eb E F Fsh_Gb G Gsh_Ab A Ash_Bb B', start=0)
Interval = IntEnum('Interval', 'Unison Min2nd Maj2nd Min3rd Maj3rd Per4th Dim5th Per5th Min6th Maj6th Min7th Maj7th Octave', start=0)

# notes can be transposed by an interval, giving another note
def transpose(note, interval) -> Note:
    return Note((note + interval) % Interval.Octave)

# we also define transposing in a loop, for convenience
def transpose_loop(note, interval, repeat):
    for i in range(repeat):
        note = transpose(note, interval)
    return note

# F is a perfect fifth below C, so it can be used to generate the C major scale
C_major = sorted([transpose_loop(Note.F, Interval.Per5th, index) for index in range(7)])
print(C_major)

def note_diff(n1, n2):
    return Interval((n1 - n2) % Interval.Octave)

major_scale = [note_diff(note, Note.C) for note in C_major]

G_major = [transpose(Note.G, i) for i in major_scale]

triads_in_C_major = []

# For every note in the scale...
for index in range(len(C_major)):
    # Build a triad by skipping every other note
    chord = [C_major[(index + triad_index) % len(C_major)] for triad_index in range(0, 5, 2)]
    triads_in_C_major.append(chord)


def invert(interval)-> Interval:
    return Interval(Interval.Octave - interval)

# We define a chord as being composed of a root note, and a quality
print(triads_in_C_major)
chords_in_C_major = {} 
for triad in triads_in_C_major:
    root = triad[0]
    qual = [note_diff(note, root) for note in triad]
    print(f"{root.name}: {qual[0].name} {qual[1].name} {qual[2].name}")
    chords_in_C_major[root] = qual

# Let's print these chords in the order the notes were originally derived

for root in [transpose_loop(Note.F, Interval.Per5th, index) for index in range(7)]:
    qual = chords_in_C_major[root]
    print(f"{root.name}: {qual[0].name} {qual[1].name} {qual[2].name}")
