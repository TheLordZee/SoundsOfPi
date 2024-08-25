from pypiano import Piano
from mingus.containers import Note
import mingus.core.intervals as intervals
from mingus.containers import NoteContainer
from mingus.containers import Bar
import mingus.core.chords as chords
from mingus.containers import Track
import mingus.core.notes as notes

from notes_list import notes_list

file = "pi.txt"

txt_file = open(file)

count = 0


t = Track()

count = 0

bar = Bar()

for key in notes_list.keys():
    bar.place_notes(notes_list.get(key), 4)
    count+=1
    if(count == 4):
        t.add_bar(bar)
        bar = Bar()
        count = 0

p = Piano()
p.play(t, recording_file="pi.wav", record_seconds=4)