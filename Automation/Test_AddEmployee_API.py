import random
import string
import requests

BASE_URL = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees"
HEADERS = {"Authorization": "Basic VGVzdFVzZXI4NTQ6bjd7QTFsKTBOTSF1"}
FIRST_NAME = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
LAST_NAME = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
DEPENDANTS = rand_int = random.randint(0, 32)

# Create
new_employee = {"firstName": FIRST_NAME, "lastName": LAST_NAME, "dependants": DEPENDANTS}
resp = requests.post(BASE_URL, headers=HEADERS, json=new_employee)
employee_id = resp.json().get("id")

# Read
resp = requests.get(f"{BASE_URL}/{employee_id}", headers=HEADERS)
print(resp.json())
