from django.contrib import admin
from django.apps import apps

# Get the app config for the 'scrapper' app
app_config = apps.get_app_config('scrapper')

# Get all models from the 'scrapper' app
models = app_config.get_models()

# Register all models with the admin site
for model in models:
    # Check if the model is already registered
    if not admin.site.is_registered(model):
        admin.site.register(model)
