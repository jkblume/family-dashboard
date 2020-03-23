build:
	@echo "No additional build steps available"
test:
	pipenv run python manage.py test --settings project.settings
run:
	pipenv run python manage.py migrate --noinput
	pipenv run python manage.py collectstatic --noinput
	pipenv run gunicorn project.wsgi --workers 5 -b 0.0.0.0:8000 -t 600 --access-logfile - --error-logfile -
run_dev:
	pipenv run python manage.py runserver_test 0.0.0.0:8000

run_worker:
	pipenv run python manage.py migrate --noinput
	pipenv run python manage.py runworker