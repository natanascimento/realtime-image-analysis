.PHONY: help setup start install uninstall reinstall download
.DEFAULT: help

help:
	@echo "make start"
	@echo "          Run python project"
	@echo "----------"
	@echo "make install"
	@echo "          Install face analysis packages"
	@echo "----------"
	@echo "make uninstall"
	@echo "          Uninstall face analysis packages"
	@echo "----------"
	@echo "make reinstall"
	@echo "          Reinstall face analysis packages"
	@echo "----------"

setup:
	echo "Downloading yolov3-608"
	curl -o ./app/models/yolov3/yolov3-608/yolov3.weights https://pjreddie.com/media/files/yolov3.weights
	echo "Downloading yolov3-tiny"
	curl -o ./app/models/yolov3/yolov3-tiny/yolov3.weights https://pjreddie.com/media/files/yolov3-tiny.weights

start:
	poetry run start

install: 
	pip install poetry && poetry install

uninstall: 
	poetry cache clear pypi --all && rm -f poetry.lock

reinstall: uninstall install

realtime-analysis-with-yolo/app/models/yolov3/yolov3-608/yolov3.weights
realtime-analysis-with-yolo/app/models/yolov3/yolov3-tiny/yolov3.weights