import re
from datetime import datetime

def is_date(value):
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            continue
    return False

def is_phone(value):
    return bool(re.fullmatch(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value))

def is_email(value):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value))

def detect_type(value):
    if is_date(value):
        return "date"
    if is_phone(value):
        return "phone"
    if is_email(value):
        return "email"
    return "text"
