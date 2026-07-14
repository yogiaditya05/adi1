import requests
import json
import os

def main():
    # 1. Generate Webhook
    url_generate = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Aditya ",
        "regNo": "0827RL23",
        "email": "adityayogi23@acropolis.in"
    }
    headers = {"Content-Type": "application/json"}
    
    print("Generating Webhook...")
    response = requests.post(url_generate, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    
    webhook_url = data["webhook"]
    access_token = data["accessToken"]
    
    print(f"Webhook URL: {webhook_url}")
    print(f"Access Token: {access_token[:10]}...")
    
    # 2. Prepare the SQL Solution
    sql_query = """SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
    d.DEPARTMENT_NAME
FROM 
    PAYMENTS p
JOIN 
    EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN 
    DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE 
    DAY(p.PAYMENT_TIME) != 1
ORDER BY 
    p.AMOUNT DESC
LIMIT 1;"""

    # 3. Submit the solution
    print("Submitting the SQL query...")
    submit_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    submit_payload = {
        "finalQuery": sql_query
    }
    
    submit_response = requests.post(webhook_url, headers=submit_headers, json=submit_payload)
    
    result = {
        "generate_status": response.status_code,
        "submit_status": submit_response.status_code,
        "submit_response": submit_response.text,
        "sql_query": sql_query
    }
    
    print(f"Submit Status: {submit_response.status_code}")
    print(f"Submit Response: {submit_response.text}")
    
    # Save the result to a json file to display on the Netlify site
    os.makedirs("netlify-site", exist_ok=True)
    with open("netlify-site/result.json", "w") as f:
        json.dump(result, f, indent=4)
    
if __name__ == "__main__":
    main()

