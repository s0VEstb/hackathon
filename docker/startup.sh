echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser if not exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='1').exists():
    User.objects.create_superuser(username='1', email='1@gmail.com', password='1')
EOF

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
gunicorn hackathon.wsgi:application --bind 0.0.0.0:8000
