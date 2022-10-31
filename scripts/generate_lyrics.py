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
    files = [f for f in glob.glob('inputs/lyrics/*.md') if not f.endswith('README.md')]

def parseTitle(lines):
    """Parse the title and any subheadings from lines of text.
    """

    assert lines[0][0] == '#', f'Title should be "# Title"'
    title = lines[0][1:].lstrip()
    print(f'Got title "{title}"', file=sys.stderr)
    result = []
    titleId = title.lower().replace(' ', '_')
    result.append(f'<div id="{titleId}" class="page">')
    result.append(f'<h2>{title}</h2>')

    for line in lines[1:]:
        if line[0:2] == "##":
            subHeading = line[2:].lstrip()
            print(f'Adding sub-header "{subHeading}"', file=sys.stderr)
            result.append(f'<h3>{subHeading}</h3>')
    return '\n'.join(result)


def parseFile(file):
    """Parse given file of lyrics and return HTML output as str.
    """
    result = []
    # We assume that the first line of the file is the song's title
    result.append(parseTitle(stanzas[0].split('\n')))

    # The remaining stanzas are assumed to be lyrics / subheadings
    for stanza in stanzas[1:]:
        # If a stanza is just whitespace, skip it
        if len(stanza.replace("\n", "")) == 0:
            continue
        lines = stanza.split('\n')

        # If a line begins with '##' it's assumed to be a subtitle
        if lines[0][0:2] == "##":
            print(f'Processing first line "{lines[0]}"', file=sys.stderr)
            assert len(lines) == 1, f'Line with "##" should be in its own stanza; please put newlines around "{lines[0]}"'
            subHeading = lines[0][2:].lstrip()
            print(f'Adding sub-header "{subHeading}"', file=sys.stderr)
            result.append(f'<h3>{subHeading}</h3>')
            continue

        result.append('<ul class="lyrics">')
        for line in lines:
            result.append('<li>')
            result.append(line)
            result.append('</li>')

        result.append('</ul>')
        result.append('')
    result.append('<p><a href="#music">(back)</a></p>')
    result.append('</div>')
    return '\n'.join(result)


if __name__ == '__main__':
    for file in sorted(files, reverse=True):
        with open(file) as f:
            stanzas=f.read().split('\n\n')

        print(parseFile(file))