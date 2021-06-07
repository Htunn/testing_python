install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
		python -m pytest -v --cov=testing tests/*.py
		
lint:
		pylint --disable=R,C ./testing/hello.py 

all: install lint test
