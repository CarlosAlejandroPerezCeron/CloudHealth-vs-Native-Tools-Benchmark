import pandas as pd
import matplotlib.pyplot as plt
from utils import get_env, log

def compare_results(ch, aws, azure):
    log("Comparing detection and latency...")

    summary = pd.concat([ch, aws, azure], ignore_index=True)
    summary["date"] = pd.to_datetime(summary.get("Date", pd.Timestamp.today()))

    coverage = summary.groupby("source")["Service"].nunique().reset_index()
    coverage.columns = ["Tool", "ServiceCount"]
    coverage.to_csv(f"{get_env('OUTPUT_DIR')}/coverage_summary.csv", index=False)

    plt.bar(coverage["Tool"], coverage["ServiceCount"])
    plt.title("Service Coverage Comparison")
    plt.ylabel("Unique Services Detected")
    plt.tight_layout()
    plt.savefig(f"{get_env('OUTPUT_DIR')}/coverage_summary.png")

    log("Coverage and detection metrics exported.")
    return coverage
