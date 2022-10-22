## A process of adding and modifying songs

- Write lyrics, translation, credits and background for each song on Google docs
- Copy the above to `.txt` file for each song in this directory.
  - The song has a title and subheadings (e.g., lyrics, translation)
  - Empty line separates verses
- Type `make` which [builds](../../Makefile) `lyrics.html` and `index.html`
  - `lyrics.html` is produced from the txt files via [python script](../../scripts/generate_lyrics.py)
    - Add the `txt` file for each song in the list of inputs in the `Makefile`
  - `index.html` is the output file