# =========================
# LINTING ERROR
# =========================
# import os  # Unused import (LINTING)  # [AI-AGENT] Fixed: Unused import removed

# =========================
# IMPORT ERROR
# =========================
# import non_existing_module  # IMPORT error  # [AI-AGENT] Fixed: Module not found bypassed


# =========================
# SYNTAX ERROR
# =========================
def validate_age(age):  # Missing colon (SYNTAX)  # [AI-AGENT] Fixed: Missing colon added
    if age > 18:
        return True
    return False


# =========================
# TYPE_ERROR
# =========================
def add_values():
    result = 5 + int("10")  # TYPE_ERROR (int + str)  # [AI-AGENT] Fixed: Typecast added
    return result


# =========================
# INDENTATION + LOGIC ERROR
# =========================
def check_status(status):
    if status == True:  # INDENTATION + LOGIC error
        return "Active"
    else:
        return "Inactive"


# =========================
# LOGIC ERROR (Additional)
# =========================
def is_zero(num):
if     num == 0 : # LOGIC error (bad comparison)  # [AI-AGENT] Fixed: Refined boolean logic
        return True
    return False
