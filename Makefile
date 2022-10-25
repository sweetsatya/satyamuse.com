# 'make' runs the 'make build' goal by default
.DEFAULT_GOAL=build

build: index.html
	@echo "salem satya, your website is ready as index.html"

# we build the index.html file with template.html, lyrics.html, main.css and main.js as inputs
index.html: lyrics.html inputs/template.html inputs/main.css inputs/main.js
	@echo "generating index.html from templates.."
	@bash scripts/generate_html.sh > index.html

# Generate lyrics.html as output if any of the files in lyrics/ directory changed
# Ideal would be to not need to list all the files as inputs into lyrics.html
lyrics.html: inputs/lyrics/lambodara.txt inputs/lyrics/lila.txt inputs/lyrics/edge_of_chaos.txt inputs/lyrics/panta_rhei.txt
	@echo "generating $@ from lyrics/.."
	python3 scripts/generate_lyrics.py > lyrics.html