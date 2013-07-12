all:
	#python main.py
	python server.py

.PHONY: test
test:
	python file_parser.py


.DEFAULT_GOAL := all
