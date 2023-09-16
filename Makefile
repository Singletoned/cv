.PHONY: build
build:
	python scripts/pug-to-html.py
	wkhtmltopdf cv.html cv.pdf
