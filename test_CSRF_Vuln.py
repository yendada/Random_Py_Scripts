#Security Testing Functions

def check_security_vulnerability(input_data):
    # Simulate a security test for a specific vulnerability
    if "CSRF" in input_data:
        return "CSRF Vulnerability found"
    else:
        return "No vulnerability detected"

input_data = "This is a CSRF vulnerable script."
result = check_security_vulnerability(input_data)

print(result.upper())

