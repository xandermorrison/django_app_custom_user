# django_app_custom_user
Custom User model app for Django that replaces the default username primary key and replaces it with a unique email address

Django, by default, sets up its authentication system for users to sign in with unique usernames and passwords.

This app allows you to override that default and replace the unqiue identifier for users of your site to be _email_.

The new User model is already imported and configured in the admin.py file for use in the Django admin site. To use the new User in your views, just import it.
