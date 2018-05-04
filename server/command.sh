# This "simple" command is used to grab the needed output from mididump.py (the midi parsing)
# information and then throw it in a file 'output.txt' for easy access (after it sorts it
# from highest to lowest)
python mididump.py next.mid | grep NoteOn | grep -o "\[.*," | sed 's/\[//g' | sed 's/,.*//g' | sort -r > output.txt
