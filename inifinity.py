import os
import subprocess
import base64

def insecure_deserialization(data):
    """
    This function contains a critical security vulnerability.
    It performs unsafe deserialization of user input.
    """
    import pickle
    return pickle.loads(base64.b64decode(data))  # Critical: Insecure deserialization

def sql_injection_vulnerability(user_id):
    """
    This function contains a SQL injection vulnerability.
    """
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Critical: SQL Injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id  
    cursor.execute(query)
    return cursor.fetchall()

def command_injection(filename):
    """
    This function contains a command injection vulnerability.
    """
    # Critical: Command injection vulnerability
    os.system("rm " + filename)  
    
    # Another command injection using subprocess
    subprocess.call("grep 'pattern' " + filename, shell=True)

def hardcoded_credentials():
    """
    This function contains hardcoded credentials.
    """
    # Critical: Hardcoded credentials
    username = "admin"
    password = "super_secret_password123!"
    api_key = "AIzaSyDUJf84NrDQAb-65sfdj23SdJFka121"
    
    return connect_to_service(username, password, api_key)

def connect_to_service(user, pwd, key):
    # Placeholder function
    return True

def memory_leak():
    """
    Potential resource leak.
    """
    # Critical: Resource leak - file not closed
    f = open("important_data.txt", "r")
    data = f.read()
    # Missing f.close()
    return data

def null_pointer_dereference(data):
    """
    Function with potential null pointer dereference.
    """
    # Critical: Potential null pointer dereference
    if len(data) > 5:
        return data.process()
    # Missing else case, could return None and cause NPE later
    
if _name_ == "_main_":
    # Demonstrate potential path traversal vulnerability
    user_input = "../../../etc/passwd"
    with open(user_input, "r") as f:  # Critical: Path traversal
        content = f.read()
    
    # Call to insecure random
    import random  # Not cryptographically secure
    token = random.randint(1000, 9999)  # Critical: Weak random for security
    
    # Insecure exception handling
    try:
        result = sql_injection_vulnerability("1; DROP TABLE users;")
    except Exception:
        # Critical: Overly broad exception catch
        pass  # Silently catch all exceptions
