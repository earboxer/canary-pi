# This "simple" command is used to grab the needed output from mididump.py (the midi parsing)
# information and then throw it in a file 'output.txt' for easy access.
python mididump.py next.mid | grep NoteOn | grep -o "\[.*," | sed 's/\[//g' | sed 's/,.*//g' > output.txt
