import hashlib
from homework.config import STUDENT_NAME
from homework.mail import send_email


def calculate_hashes(text: str) -> tuple[str, str]:
    text_bytes = text.encode("utf-8")
    md5_hash = hashlib.md5(text_bytes).hexdigest()
    sha256_hash = hashlib.sha256(text_bytes).hexdigest()
    return (md5_hash, sha256_hash)

def print_value(value: any) -> str:
    print(value, type(value))
    return f"{value} {type(value)}" 


if __name__ == "__main__":
    result = None
    values = (1, 1.0, True, "hse", ["hse"], ("hse",), {"hse"}, {"hse": "mag"})

    result = STUDENT_NAME + "\n"
    for value in values:
        result += (print_value(value) + "\n")
    result += STUDENT_NAME

    md5_hash, sha256_hash = calculate_hashes(result)
    send_email(md5_hash, sha256_hash)