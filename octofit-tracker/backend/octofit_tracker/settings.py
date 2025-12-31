DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
        }
    }
}

# Allow Codespace URL and localhost
import os
codespace_name = os.environ.get('CODESPACE_NAME')
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if codespace_name:
    ALLOWED_HOSTS.append(f'{codespace_name}-8000.app.github.dev')
INSTALLED_APPS = [
    # ...existing apps...
    'rest_framework',
    'djongo',
    'corsheaders',
    'octofit_tracker',
]