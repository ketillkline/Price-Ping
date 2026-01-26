import re
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


class StrongPasswordValidator:
    def __init__(self):
        self.min_length = 8
        self.max_length = 128
    def validate(self, password: str, user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError(_(self.get_help_text("At least 1 uppercase letter")))
        if not re.search(r"[a-z]", password):
            raise ValidationError(_(self.get_help_text("At least 1 lowercase letter")))
        if not re.search(r"\d", password):
            raise ValidationError(_(self.get_help_text("At least 1 number")))
        if not re.search(r"[!@#$%^&*(),.<>/;:`~]+", password):
            raise ValidationError(_(self.get_help_text("At least 1 special character")))
        if len(password) < self.min_length:
            raise ValidationError(_(self.get_help_text(f"Only {len(password)} characters long. Must be at least {self.min_length}")))
        if len(password) > self.max_length:
            raise ValidationError(_(self.get_help_text(f"Too long. Must be no more than {self.max_length} characters long.")))


    def get_help_text(self, error: str):
        return _(f"Your password does not meet the specified criteria. What's missing: {error}")
