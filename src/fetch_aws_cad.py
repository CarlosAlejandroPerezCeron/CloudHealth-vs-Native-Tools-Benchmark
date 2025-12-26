import boto3
import pandas as pd
from utils import get_env, log

def fetch_aws_cad():
    client = boto3.client("ce", region_name=get_env("AWS_REGION"))
    resp = client.list_anomaly_subscriptions()

    records = []
    for sub in resp["AnomalySubscriptions"]:
        records.append({
            "monitor_name": sub["SubscriptionName"],
            "last_updated": sub["LastUpdatedDate"],
            "source": "AWS_CAD"
        })

    df = pd.DataFrame(records)
    log(f"Fetched {len(df)} AWS CAD monitors.")
    return df
