Télécharger les dépendances:
pip install -r requirements.txt

Pour éxecuter les tests:
pytest

Pour lancer l'application:
gunicorn --worker-tmp-dir /dev/shm --config gunicorn_config.py app:app
