# Django TODO Application

A simple TODO application built with Django that allows you to create, edit, delete, and manage your todos with due dates.

## Features

- ✅ Create, edit, and delete TODOs
- ✅ Assign due dates to TODOs
- ✅ Mark TODOs as completed/incomplete
- ✅ Clean, responsive web interface
- ✅ Django admin integration

## Testing Features Added

### Test Files Created
- `todos/tests.py` - Comprehensive test suite
- `todo_project/test_settings.py` - Test-specific Django settings
- `test.py` - Standalone test runner script

### Test Coverage
- **Model Tests**: Todo creation, string representation, ordering, field defaults
- **Form Tests**: Validation, required/optional fields, widget configuration
- **View Tests**: All CRUD operations, template rendering, redirects, success messages
- **URL Tests**: URL pattern resolution and responses
- **Integration Tests**: Complete user workflows from creation to deletion

### Test Statistics
- **5 Test Classes** with **25+ individual test methods**
- **100% Model Coverage** (creation, validation, representation)
- **Complete CRUD Operations** testing
- **Form Validation** for all scenarios
- **URL Resolution** and response testing
- **Integration Workflows** end-to-end

## Setup Instructions

### Prerequisites

Make sure you have Python installed on your system. We recommend using `uv` for package management.

### 1. Install uv (optional but recommended)

```bash
# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Set up the project

If using uv:
```bash
uv venv
uv pip install -r requirements.txt
```

If using pip directly:
```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (optional, for Django admin)

```bash
python manage.py createsuperuser
```

### 5. Run tests (optional but recommended)

```bash
python manage.py test
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access the application

- Main application: http://127.0.0.1:8000/
- Django admin (if you created a superuser): http://127.0.0.1:8000/admin/

## Usage

### Managing TODOs

1. **View all TODOs**: Visit the homepage to see all your todos
2. **Create a new TODO**: Click "Add New Todo" and fill in the form
3. **Edit a TODO**: Click "Edit" next to any todo to modify it
4. **Mark as complete/incomplete**: Click "Mark Complete" or "Mark Incomplete"
5. **Delete a TODO**: Click "Delete" and confirm the action

### TODO Fields

- **Title**: Required field for the todo title
- **Description**: Optional detailed description
- **Due Date**: Optional date and time when the todo should be completed
- **Completed**: Checkbox to mark the todo as done

## Project Structure

```
todo_project/
├── todo_project/          # Main Django project
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── todos/                # Todo application
│   ├── migrations/       # Database migrations
│   ├── templates/todos/  # HTML templates
│   ├── __init__.py
│   ├── admin.py          # Django admin configuration
│   ├── apps.py           # App configuration
│   ├── forms.py          # Django forms
│   ├── models.py         # Database models
│   ├── urls.py           # App URL configuration
│   └── views.py          # View functions
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Testing

The application includes comprehensive test coverage for models, views, forms, and URLs.

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests with verbose output
python manage.py test --verbosity=2

# Run tests for specific app
python manage.py test todos

# Run a specific test class
python manage.py test todos.tests.TodoModelTest

# Run a specific test method
python manage.py test todos.tests.TodoModelTest.test_todo_creation
```

### Test Coverage

The test suite includes:

- **Model Tests**: Todo creation, string representation, ordering, field defaults
- **Form Tests**: Validation, required/optional fields, widget configuration
- **View Tests**: All CRUD operations, template rendering, redirects, success messages
- **URL Tests**: URL pattern resolution and responses
- **Integration Tests**: Complete user workflows from creation to deletion

## Development

To contribute to this project:

1. Clone the repository
2. Set up a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Run tests: `python manage.py test`
6. Start development server: `python manage.py runserver`

## License

This project is open source and available under the MIT License.
