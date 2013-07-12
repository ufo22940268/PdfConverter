all:
	#python main.py
	python server.py

.PHONY: test
test:
	python file_parser.py

.PHONY: unit-test
unit-test:
	python unit_test.py


#.DEFAULT_GOAL := unit-test
.DEFAULT_GOAL := all
