# scripts/create_test_user.py

from django.contrib.auth import get_user_model

def run():
    User = get_user_model()
    
    if not User.objects.filter(username='testuser').exists():
        User.objects.create_user(
            username='testuser',
            password='testuser123',
            is_staff=True,
            is_superuser=False,
            email='test@example.com'
        )
        print("✅ Test user created.")
    else:
        print("ℹ️ Test user already exists.")
