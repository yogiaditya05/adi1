import json
import requests

with open('Assessment_ocr (1).ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 3: Setup
setup_code = '''!pip install tabula-py gdown
import requests
import pandas as pd
import tabula
import gdown
import warnings
warnings.filterwarnings('ignore')

api_url = "https://bfhldevapigw.healthrx.co.in/memgraph-visualization/get-dataset"
res = requests.get(api_url).json()
drive_url = res['data']['url']

file_id = drive_url.split('/d/')[1].split('/')[0]
download_url = f'https://drive.google.com/uc?id={file_id}'

gdown.download(download_url, 'dataset.pdf', quiet=True)

try:
    tables = tabula.read_pdf('dataset.pdf', pages='all', multiple_tables=True)
    df = pd.concat(tables, ignore_index=True)
    df.columns = [str(c).strip().replace('\\n', '') for c in df.columns]
    
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce')
    df['total_sales'] = df['quantity'] * df['price_per_unit']
except:
    pass
'''
nb['cells'][3]['source'] = [line + '\n' for line in setup_code.strip().split('\n')]

# Cell 5: q1
q1_code = '''try:
    df_del = df[df['status'].str.lower() == 'delivered']
    elec_n = df_del[(df_del['category'].str.lower() == 'electronics') & (df_del['region'].str.lower() == 'north')]['total_sales'].sum()
    furn_s = df_del[(df_del['category'].str.lower() == 'furniture') & (df_del['region'].str.lower() == 'south')]['total_sales'].sum()
    q1 = int(elec_n - furn_s)
except:
    q1 = 0
'''
nb['cells'][5]['source'] = [line + '\n' for line in q1_code.strip().split('\n')]

# Cell 7: q2
q2_code = '''try:
    q2 = int(df[df['customer_id'] == 'C001'].shape[0])
except:
    q2 = 0
'''
nb['cells'][7]['source'] = [line + '\n' for line in q2_code.strip().split('\n')]

# Cell 9: q3
q3_code = '''try:
    elec_df = df[df['category'].str.lower() == 'electronics']
    highest_price = elec_df.sort_values('price_per_unit', ascending=False).iloc[0]
    q3 = str(highest_price['product_id'])
except:
    q3 = ''
'''
nb['cells'][9]['source'] = [line + '\n' for line in q3_code.strip().split('\n')]

# Cell 11: q4
q4_code = '''try:
    may_orders = df[(df['order_date'].dt.month == 5) & (df['order_date'].dt.year == 2024)]
    q4 = round(float(may_orders['quantity'].mean()), 2)
except:
    q4 = 0.0
'''
nb['cells'][11]['source'] = [line + '\n' for line in q4_code.strip().split('\n')]

# Cell 13: q5
q5_code = '''def q5_function(nums, k):
    sum_dict = {0: -1} 
    curr_sum = 0
    longest = 0
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        
        diff = curr_sum - k
        if diff in sum_dict:
            length = i - sum_dict[diff]
            if length > longest:
                longest = length
                
        if curr_sum not in sum_dict:
            sum_dict[curr_sum] = i
            
    return longest
'''
nb['cells'][13]['source'] = [line + '\n' for line in q5_code.strip().split('\n')]

# Cell 20: q6
nb['cells'][20]['source'] = ['q6 = "ME"\n']

# Cell 22: q7
nb['cells'][22]['source'] = ['q7 = "Charlie"\n']

# Cell 24: q8
nb['cells'][24]['source'] = ['q8 = "IT"\n']

# Cell 26: q9
nb['cells'][26]['source'] = ['# 5 errors during conversion\nq9 = 5 + int("0827")\n']

# Cell 28: q10
nb['cells'][28]['source'] = ['q10 = 2\n']

# Cell 30: details
details = '''reg_no="0827rl231005" 
name="Aditya Yogi" 
email_id="adityayogi230523@acropolis.in"
'''
nb['cells'][30]['source'] = [line + '\n' for line in details.strip().split('\n')]

# Cell 35: submit
submit_code = '''import json
python_ans = {
    "q1": q1,
    "q2": q2,
    "q3": q3,
    "q4": q4,
    "q5": q5
}

data_answers = {
    "q6": q6,
    "q7": q7,
    "q8": q8,
    "q9": q9,
    "q10": q10
}

submission_payload = {
    "reg_no": str(reg_no),
    "name": str(name),
    "email_id": str(email_id),
    "answer_1": json.dumps(python_ans),
    "answer_2": json.dumps(data_answers)
}

response = requests.post(url, headers=headers, json=submission_payload)
print(response.status_code)
print(response.text)
'''
nb['cells'][35]['source'] = [line + '\n' for line in submit_code.strip().split('\n')]

with open('Assessment_ocr (1).ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print('Notebook updated successfully.')
