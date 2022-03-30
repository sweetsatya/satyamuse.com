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
    # todo: we want a certain order for the lyrics..
    files = glob.glob('inputs/lyrics/*.txt')

for file in sorted(files, reverse=True):
    with open(file) as f:
        stanzas=f.read().split('\n\n')


    # We assume that the first line of the file is the song's title
    title = stanzas[0]
    titleAnchor = title.lower().replace(' ', '_')
    print(f'<div id="{titleAnchor}" class="page">')
    print(f'<a href="#{titleAnchor}"><h3>{title}</h3></a>')
    for stanza in stanzas[1:]:
        if len(stanza.replace("\n", "")) == 0:
            continue
        print('<ul class="lyrics">')

        for line in stanza.split('\n'):
            print('<li>')
            print(line)
            print('</li>')

        print('</ul>')
        print()
    print('<p><a href="#music">(back)</a></p>')
    print('</div>')