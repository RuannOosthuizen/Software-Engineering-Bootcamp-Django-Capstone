from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    Configuration class for the 'polls' Django application.

    Attributes:
        default_auto_field (str): The default auto-generated field type for models.
        name (str): The name of the application.

    Example usage:
        >>> config = PollsConfig()
        >>> config.default_auto_field
        'django.db.models.BigAutoField'
        >>> config.name
        'polls'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
