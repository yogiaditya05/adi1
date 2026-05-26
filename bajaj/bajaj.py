import json
import requests

# Candidate Details
candidate_info = {
    "name": "Aditya Yogi",
    "regNo": "0827rl231005",
    "email": "your_email@example.com"
}

# API Endpoints
generate_webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

try:
    # Step 1: Generate webhook and token
    response = requests.post(
        generate_webhook_url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(candidate_info)
    )

    response.raise_for_status()

    api_data = response.json()

    webhook_url = api_data.get("webhook")
    access_token = api_data.get("accessToken")

    print("Webhook Generated Successfully")
    print(f"Webhook URL: {webhook_url}")

    # --------------------------------------------------------
    # Replace this SQL query with your actual solution
    # --------------------------------------------------------

    final_sql_query = """
    SELECT 
        p.AMOUNT AS SALARY,
        CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
        TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
        d.DEPARTMENT_NAME
    FROM PAYMENTS p
    JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
    WHERE DAY(p.PAYMENT_TIME) <> 1
    ORDER BY p.AMOUNT DESC
    LIMIT 1;
    """


    submission_payload = {
        "finalQuery": final_sql_query.strip()
    }

    # Step 2: Submit SQL Query
    submission_response = requests.post(
        webhook_url,
        headers={
            "Authorization": access_token,
            "Content-Type": "application/json"
        },
        data=json.dumps(submission_payload)
    )

    submission_response.raise_for_status()

    print("SQL Query Submitted Successfully")
    print(submission_response.text)

except requests.exceptions.RequestException as error:
    print("An error occurred while processing the request.")
    print(error)

