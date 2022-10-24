up:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py collectstatic --no-input --clear
	python manage.py runserver
