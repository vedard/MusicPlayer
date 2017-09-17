run:
	python3 application.py --debug

clean:
	find . -type f -name "*.py[co]" -delete 
	find . -type f -name "*.ui~" -delete 
	find . -type d -name "__pycache__" -delete

test:
	python3 -m unittest discover test "*_test.py"

init:
	pip3 install -r requirements.txt

help:
	@echo ""
	@echo "init"
	@echo "    Download requirements"
	@echo "test"
	@echo "    Run all test"
	@echo "run"
	@echo "    Run the program"
	@echo "clean"
	@echo "    Remove python artifacts."

.PHONY: init test clean run help
