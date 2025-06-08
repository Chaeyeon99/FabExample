def transform_email(email):
    if "@" in email:
        user, domain = email.split("@")
        return f"{user[:2]}***@{domain}"
    return email
