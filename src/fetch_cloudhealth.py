import requests
import pandas as pd
from utils import get_env, log

def fetch_cloudhealth_data(days=7):
    api_key = get_env("CH_API_KEY")
    org_id = get_env("CH_ORG_ID")
    url = f"https://chapi.cloudhealthtech.com/v1/anomalies?org_id={org_id}&timeframe=last_{days}_days"

    headers = {"Authorization": f"Bearer {api_key}"}
    resp = requests.get(url, headers=headers)
    data = resp.json().get("anomalies", [])

    df = pd.DataFrame(data)
    df["source"] = "CloudHealth"
    log(f"Fetched {len(df)} CloudHealth anomalies.")
    return df
