# 'make' runs the 'make build' goal by default
.DEFAULT_GOAL=build

build: index.html lyrics.html
	@echo "salem satya, your website is ready"

# we build the index.html file with template.html, lyrics.html and main.css as inputs
index.html: lyrics.html inputs/template.html inputs/main.css
	@echo "generating index.html from templates.."
	@bash scripts/generate_html.sh > index.html

# Generate lyrics.html as output if any of the files in lyrics/ directory changed
lyrics.html: inputs/lyrics/lambodara.txt
	@echo "generating $@ from lyrics/.."
	python3 scripts/generate_lyrics.py > lyrics.html