python mididump.py next.mid | grep NoteOn | grep -o "\[.*," | sed 's/\[//g' | sed 's/,.*//g'
