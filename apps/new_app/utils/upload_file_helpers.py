from pathlib import Path
import os

from django.core.exceptions import ValidationError

# ALLOWED_EXTENSIONS = ['.pdf','.csv','.doc','.xlsx','.py']
MAX_FILE_SIZE = 1024 * 1024 * 2


def is_valid_size(file):
    if file.size > MAX_FILE_SIZE:
        raise ValidationError("File size is too big")







