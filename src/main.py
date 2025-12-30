from fetch_cloudhealth import fetch_cloudhealth_data
from fetch_aws_cad import fetch_aws_cad
from fetch_azure_cost import fetch_azure_data
from compare_results import compare_results
from utils import log

def main():
    log("=== CloudHealth vs Native Tools Benchmark ===")
    ch = fetch_cloudhealth_data()
    aws = fetch_aws_cad()
    azure = fetch_azure_data()
    compare_results(ch, aws, azure)
    log("Benchmark complete.")

if __name__ == "__main__":
    main()
