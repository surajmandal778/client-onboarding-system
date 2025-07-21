# 🧾 Client Onboarding System

A simple and user-friendly Django web application to manage client onboarding, including adding, editing, listing, and exporting client data to PDF.

---

## 📦 Features

- ✅ Add new clients with details like name, email, phone, company, services, and status
- ✅ View client list in dashboard
- ✅ Edit existing client information
- ✅ Export client report as PDF
- ✅ Login authentication for access control

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/surajmandal778/client-onboarding-system.git
cd client-onboarding-system

2. Create and activate a virtual environment
bash

python -m venv env
env\Scripts\activate  # Windows
# or
source env/bin/activate  # macOS/Linux


3. Install dependencies
bash
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the project root with the following:

ini

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your_django_secret_key
DEBUG=True


🛠️ Database Setup
You can either:

Run the included schema.sql in MySQL:

bash

mysql -u root -p < schema.sql
Or let Django handle it:

bash

python manage.py makemigrations
python manage.py migrate

🔑 Superuser Creation (Optional for Admin Access)
bash

python manage.py createsuperuser
▶️ Running the App
bash

python manage.py runserver
Visit: http://127.0.0.1:8000

🧪 Test Login Credentials (Optional)
Username: admin

Password: admin123

📄 Bonus: Client Report
Visit the /report route to view a list of all clients. You can also export the list as a PDF.

📁 Folder Structure
bash

client_onboarding/
├── core/                  # Main app
│   ├── templates/         # HTML templates
│   ├── static/            # CSS files
│   ├── views.py           # Django views
│   ├── models.py          # Data models
│   └── urls.py            # App URLs
├── client_onboarding/
│   └── settings.py        # Project settings
├── requirements.txt       # Python dependencies
├── schema.sql             # MySQL DB schema (optional)
├── .env                   # Environment variables (NOT committed)
└── manage.py              # Django entry point

📬 Contact
For issues or queries, feel free to reach out at:
📧 surajmandal778@example.com

✅ Submit this GitHub repo link to your mentor/manager after verifying that all files are pushed.

Let me know if you want a simplified version or if you'd like me to include GIFs/screenshots in it.








