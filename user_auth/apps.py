from django.apps import AppConfig


class UserAuthConfig(AppConfig):
    """
    Configuration class for the 'user_auth' Django application.

    Attributes:
        default_auto_field (str): The default auto-generated field type for models.
        name (str): The name of the application.

    Example usage:
        >>> config = UserAuthConfig()
        >>> config.default_auto_field
        'django.db.models.BigAutoField'
        >>> config.name
        'user_auth'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'
