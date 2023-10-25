# Importing the necessary libraries
import os
import requests
import datetime
# returns the URL of the report for a given date, formated as YYYYMMDD
def get_url(date_str):
    # Return the URL of the report
    return f"https://www.ice.com/marketdata/publicdocs/mifid/commitment_of_traders/IFEU_FUT_{date_str}.csv"
# Defining a function that takes a URL as an argument and downloads the report as a CSV file
def download_report(url):
    # Send a GET request to the URL and get the response
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Get the file name from the URL
        file_name = url.split("/")[-1]
        # Create the download directory if it doesn't exist
        os.makedirs("/lakehouse/default/Files/eua_cot_reports/", exist_ok=True)
        # Save the response content as a file with the same name as the URL
        with open("/lakehouse/default/Files/eua_cot_reports/" + file_name, "wb") as f:
            f.write(response.content)
        # Print a message to indicate success
        print(f"Downloaded {file_name}")
    else:
        # Print a message to indicate failure
        print(f"Failed to download {url}")
report_date = datetime.datetime.now().strftime("%Y%m%d")
url = get_url(report_date)
download_report(url)
