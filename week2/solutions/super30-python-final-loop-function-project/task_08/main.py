def password_strength(password):
    """Return whether a password is strong and list missing requirements."""
    has_upper = has_lower = has_number = has_special = False
    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_number = True
        else:
            has_special = True
    missing = []
    if not has_upper: missing.append("uppercase letter")
    if not has_lower: missing.append("lowercase letter")
    if not has_number: missing.append("number")
    if not has_special: missing.append("special character")
    if len(password) < 8: missing.append("at least 8 characters")
    return {"strong": not missing, "missing": missing}


print(password_strength("Python@123"))
print(password_strength("hello"))
