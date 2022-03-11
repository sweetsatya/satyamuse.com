#!/usr/bin/env bash
#
# Generate HTML from templates.
#

set -euo pipefail

# insert $1 into $2 where marker $3 is
insert() {
    line=$(grep -n $3 $2 | cut -d ":" -f 1)
    { head -n $(($line-1)) $2; cat $1; tail -n +$(($line+1)) $2; }
}

# insert main.css template.html '{{style}}' > /tmp/index0.html
insert lyrics.html template.html '{{lyrics}}' > index.html
