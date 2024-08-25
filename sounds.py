from pypiano import Piano
from mingus.containers import Note
import mingus.core.intervals as intervals
from mingus.containers import NoteContainer
from mingus.containers import Bar
import mingus.core.chords as chords
from mingus.containers import Track
import mingus.core.notes as notes
import mingus.extra.lilypond as LilyPond
from notes_list import notes_list

source = "pi.txt"

file = open(source)
t = Track()

overflow = ""
while True:
    line = overflow + file.readline()

    if (not line) or len(overflow) == len(line):
        break

    i = 0

    while i < len(line) - 3:
        num_notes = int(line[i])
        i+=1
        time = int(line[i:i+2]) if int(line[i:i+2]) > 0 else 100
        i+=2
        if num_notes == 0:
            n=Note('D-7', dynamics={"channel":0})
            if not t.add_notes(n, time):
                curr_bar = t.bars[len(t.bars)-1]
                beat =  curr_bar.length / (curr_bar.length - curr_bar.current_beat)
                t.add_notes(n, beat)

        elif i + (2 * num_notes) > len(line)-1:
            i-=3
            break
        else:
            curr_notes = []
            while num_notes > 0:
                curr_notes.append(notes_list.get(line[i:i+2]))
                num_notes-=1
                i+=2
            if(not t.add_notes(curr_notes, time)):
                curr_bar = t.bars[len(t.bars)-1]
                beat =  curr_bar.length / (curr_bar.length - curr_bar.current_beat) 
                t.add_notes(curr_notes, beat)
                if(not t.add_notes(curr_notes, beat)):
                    t.add_notes(curr_notes, beat+.0000000000000002)
                    
    overflow = line[i:len(line)-1]

b = Bar()


n=Note('D-7', dynamics={"channel":0})
b.place_notes(n, 4)

t.add_bar(b)
# print(t)

pond = LilyPond.from_Track(t)
f = open("piSounds.txt", 'w')
f.write(pond)
# print(pond)
LilyPond.to_pdf(pond, 'sheet')

# i = 1
# for bar in t.bars:
#     pond = LilyPond.from_Bar(bar)
#     LilyPond.to_png(pond, f'Bar{i}')
#     LilyPond.to_pdf(pond, f'Bar{i}')
#     i+=1

p = Piano()
# p.play(t, recording_file="pi.wav")