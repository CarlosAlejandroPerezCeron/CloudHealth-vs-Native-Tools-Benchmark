from azure.identity import ClientSecretCredential
from azure.mgmt.costmanagement import CostManagementClient
import pandas as pd
from utils import get_env, log

def fetch_azure_data(days=7):
    creds = ClientSecretCredential(
        tenant_id=get_env("AZURE_TENANT_ID"),
        client_id=get_env("AZURE_CLIENT_ID"),
        client_secret=get_env("AZURE_CLIENT_SECRET")
    )

    client = CostManagementClient(credential=creds)
    scope = f"/subscriptions/{get_env('AZURE_SUBSCRIPTION_ID')}"
    report = client.query.usage(
        scope=scope,
        parameters={"type": "Usage", "timeframe": "MonthToDate"}
    )

    df = pd.DataFrame(report.rows, columns=["Date", "Service", "Cost"])
    df["source"] = "Azure_Cost"
    log(f"Fetched {len(df)} Azure cost entries.")
    return df
