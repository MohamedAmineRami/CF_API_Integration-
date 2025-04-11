import requests
import json

# --- Configuración ---
base_url = "https://api.cloudframework.io/erp/portal-users/2.0/cloudframework"
signin_url = f"{base_url}/web-oauth/signin"
check_url = f"{base_url}/check"

signin_payload = {
    "ClientId": "testclient",
    "username": "Fran",
    "userpassword": "qwerty1234",
    "key": "randonm_key",
    "_avoid_email": "1"
}

signin_headers = {
    "X-WEB-KEY": "CFAPITEST"
}

try:
    # --- 1. Sign in (POST request) ---
    print(f"Sending POST request to: {signin_url}")
    response_signin = requests.post(signin_url, headers=signin_headers, json=signin_payload)
    response_signin.raise_for_status()

    data_signin = response_signin.json()
    print("Sign-in Response:")
    print(json.dumps(data_signin, indent=4))

    web_token = data_signin.get("data", {}).get("web_token")

    if web_token:
        print(f"\nweb_token Obtenido con éxito : {web_token}")

        # --- 2. Check Portal User (GET request with the token) ---
        # Authorization header empty
        check_headers = {}
        print(f"\nSending GET request to: {check_url}")
        response_check = requests.get(check_url, headers=check_headers)
        response_check.raise_for_status()

        data_check = response_check.json()
        print("\nCheck User Response:")
        print(json.dumps(data_check, indent=4))

    else:
        print("\nError: web_token no encontrado en the sign-in response.")

except requests.exceptions.RequestException as e:
    print(f"\nAn error occurred during the request: {e}")
except json.JSONDecodeError:
    print("\nError: Could not decode JSON response.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")