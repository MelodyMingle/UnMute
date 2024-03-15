from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import MinimumLengthValidator

class SilentMinimumLengthValidator(MinimumLengthValidator):
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                "This password is too short. It must contain at least %(min_length)d characters.",
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ""