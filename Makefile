# 'make' runs the 'make build' goal by default
.DEFAULT_GOAL=build

build: index.html
	@echo "salem satya, your website is ready as index.html"

# we build the index.html file with template.html, lyrics.html, main.css and main.js as inputs
#
# We would want to have a pre-commit hook or similar to check that there's no diff between the text file and generated outputs
# when doing 'git commit' due to modified inputs
index.html: lyrics.html inputs/template.html inputs/main.css inputs/main.js
	@echo "generating index.html from templates.."
	@bash scripts/generate_html.sh > index.html

# Generate lyrics.html as output if any of the files in lyrics/ directory changed
# Ideal would be to not need to list all the files as inputs into lyrics.html
lyrics.html: inputs/lyrics/lambodara.txt inputs/lyrics/lila.txt inputs/lyrics/edge_of_chaos.txt inputs/lyrics/panta_rhei.txt inputs/lyrics/phoenix.txt inputs/lyrics/belye_krylya.txt
	@echo "generating $@ from lyrics/.."
	python3 scripts/generate_lyrics.py > lyrics.html