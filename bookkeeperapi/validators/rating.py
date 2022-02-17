from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_rating(value):
    if value > 5:
        raise ValidationError(
            _('%(value)s is greater than 5'),
            params={'value': value},
        )
