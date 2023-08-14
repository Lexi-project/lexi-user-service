compile:
	pip-compile requirements/requirements.in --output-file=requirements/requirements.txt
	pip-compile requirements/requirements-dev.in --output-file=requirements/requirements-dev.txt

install: compile
	pip install -r requirements/requirements.txt
	pip install -r requirements/requirements-dev.txt
	rm requirements/requirements.txt
	rm requirements/requirements-dev.txt

build: install
	python manage.py makemigrations
	python manage.py migrate --no-input
	python manage.py collectstatic --no-input

migrate:
	docker-compose run --rm app python manage.py migrate
