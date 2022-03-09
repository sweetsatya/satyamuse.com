#!/usr/bin/env python3
#
# Generate HTML markup for lyrics/.
#
# Use like this on macos:
# $ python3 script/generate_lyrics.py | pbcopy
#
import glob
import sys

if len(sys.argv) == 2:
    files = [ sys.argv[1] ]
else:
    files = glob.glob('lyrics/*.txt')

for file in files:
    with open(file) as f:
        stanzas=f.read().split('\n\n')

    for stanza in stanzas:
        if len(stanza.replace("\n", "")) == 0:
            continue
        print('<ul class="lyrics">')

        for line in stanza.split('\n'):
            print('<li>')
            print(line)
            print('</li>')

        print('</ul>')
        print()