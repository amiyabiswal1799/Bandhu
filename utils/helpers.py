import uuid
from datetime import datetime
from config import get_config

config = get_config()


def generate_session_id():
    return str(uuid.uuid4())


def allowed_file(filename):
    if '.' not in filename:
        return False
    extension = filename.rsplit('.', 1)[1].lower()
    return extension in config.ALLOWED_EXTENSIONS


def format_timestamp(dt):
    if dt is None:
        return None
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def sanitize_filename(filename):
    import re
    filename = re.sub(r'[^\w\s.-]', '', filename)
    filename = re.sub(r'\s+', '_', filename)
    return filename


def validate_file_size(file_size):
    return file_size <= config.MAX_UPLOAD_SIZE
