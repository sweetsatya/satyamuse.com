#
# Generate lyrics.html from inputs/lyrics/*.md.
#

# fail if any command fails
set -euo pipefail

LYRICS=$(python3 scripts/generate_lyrics.py)
echo "${LYRICS}" > lyrics.html