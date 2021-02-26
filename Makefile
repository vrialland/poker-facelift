serve:
	FLASK_ENV=development python server.py

serve-prod:
	FLASK_ENV=production python server.py

test:
	pytest .

lint:
	flake8
