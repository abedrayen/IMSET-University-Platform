# IMSET University Platform 🎓

A comprehensive Django-based university management platform for IMSET (Institut Méditerranéen des Sciences, de l'Économie et des Technologies) that handles student administration, course management, and automated diploma generation.

## 🌟 Features

### User Management
- **Multi-role authentication system** (Students, Teachers, Administrators)
- **Two-factor authentication (2FA)** for enhanced security
- **Custom user profiles** with personal information (CIN, date of birth, specialty, location)
- **Django REST Framework integration** for API access

### Course Management
- **Course creation and management** by teachers
- **Student enrollment system**
- **Teacher-course assignment**

### Diploma Generation
- **Automated diploma generation** for BTP and BTS degrees
- **PDF generation** using WeasyPrint
- **Professional diploma templates** with institutional branding
- **Multi-language support** (Arabic/French)
- **A4 landscape format** optimized for printing

## 🛠️ Technology Stack

- **Backend**: Django 4.2+
- **API**: Django REST Framework
- **Database**: SQLite (development)
- **PDF Generation**: WeasyPrint
- **Authentication**: Django's built-in auth system with custom extensions
- **Frontend**: Django Templates
- **Styling**: CSS with custom diploma layouts

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd IMSET
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 📁 Project Structure

```
IMSET/
├── accounts/           # User management and authentication
│   ├── models.py      # Custom User model with roles and 2FA
│   ├── views.py       # Authentication views
│   └── serializers.py # API serializers
├── courses/           # Course management system
│   ├── models.py      # Course model
│   └── views.py       # Course management views
├── diplomas/          # Diploma generation and templates
│   ├── models.py      # Diploma model
│   ├── templates/     # HTML templates for BTP/BTS diplomas
│   └── views.py       # Diploma generation logic
├── university_platform/  # Main Django project settings
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```

## 🔧 Configuration

### Environment Settings
The project uses Django's default development settings. For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Set up proper secret key management

### Database
- **Development**: SQLite (included)
- **Production**: Configure PostgreSQL or MySQL in `settings.py`

## 📝 API Endpoints

The platform provides REST API endpoints for:
- User authentication and management
- Course operations
- Diploma generation

Access the API documentation when the server is running.

## 🎨 Diploma Templates

The system supports multiple diploma types:
- **BTP** (Brevet de Technicien Professionnel)
- **BTS** (Brevet de Technicien Supérieur)

Templates are customizable and include:
- Institutional branding
- Student information
- Graduation dates
- Official formatting in Arabic and French

## 👥 User Roles

- **Students**: Access courses, view diplomas
- **Teachers**: Manage courses, view enrolled students
- **Administrators**: Full system access, user management, diploma generation

## 🔐 Security Features

- Two-factor authentication with time-limited codes
- Role-based access control
- CSRF protection
- Secure password validation
- Session management
- Unique CIN number validation

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run tests for specific apps:
```bash
python manage.py test accounts
python manage.py test courses
python manage.py test diplomas
```

## 📄 Dependencies

Key packages used:
- `Django>=4.2,<5.0` - Web framework
- `djangorestframework>=3.14.0` - API framework
- `weasyprint>=56.0` - PDF generation
- `pillow>=9.4.0` - Image processing
- `Babel` - Internationalization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support and questions, please contact the IMSET IT department or create an issue in this repository.

## 🏛️ About IMSET

Institut Méditerranéen des Sciences, de l'Économie et des Technologies (IMSET) is a leading educational institution focused on providing quality education in technology and business fields.

---

**Note**: This platform is designed specifically for IMSET's academic requirements and diploma standards.