build: index.html lyrics.html
	@echo "salem satya, your website is ready"

index.html: template.html lyrics.html
	@echo "generating index.html from templates.."
	@bash scripts/generate_html.sh > index.html

# Generate lyrics.html as output if any of the files in lyrics/ directory changed
lyrics.html: lyrics/lambodara.txt
	@echo "generating $@ from lyrics/.."
	python3 scripts/generate_lyrics.py > lyrics.html