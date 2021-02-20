images:
	cd images && mv $(SRC)/*.png . && find * -name "*.png" | sed 's/.png//g' | xargs -I % convert %.png %.webp
	cd images && rm *.png

all: images
	python gen.py > images.js
