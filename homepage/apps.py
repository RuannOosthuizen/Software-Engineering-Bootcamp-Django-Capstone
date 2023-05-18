from django.apps import AppConfig


class HomepageConfig(AppConfig):
    """
    Configuration class for the 'homepage' Django application.

    Attributes:
        default_auto_field (str): The default auto-generated field type for models.
        name (str): The name of the application.

    Example usage:
        >>> config = HomepageConfig()
        >>> config.default_auto_field
        'django.db.models.BigAutoField'
        >>> config.name
        'homepage'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'
