run_server:
	python manage.py runserver

shell:
	python manage.py shell

create_superuser:
	python manage.py createsuperuser

run_migrate:
	python manage.py migrate

run_makemigrations:
	python manage.py makemigrations

pre_commit_run:
	pre-commit run --files

install:
	pip install -r requirements.txt

run_celery_worker:
	celery -A noosh_backend worker --loglevel=info

run_celery_beat:
	celery -A noosh_backend beat --loglevel=info

.PHONY: run_server create_superuser
.PHONY: run_migrate run_makemigrations
.PHONY: install pre_commit_run
.PHONY: shell
.PHONY: run_celery_worker run_celery_beat
