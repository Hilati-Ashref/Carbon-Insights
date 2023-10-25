# EUA Commitment of Traders (COT) Report Downloader

This Python script allows you to download the Commitment of Traders (COT) report for European Union Allowances (EUAs) from the ICE Exchange. The script is designed to run on a scheduled basis and fetch the latest report in CSV format.

## Features

- Automatically fetches the most recent EUA COT report.
- Organizes downloaded reports in a specified directory.
- Provides status messages for successful and failed downloads.

## Getting Started

Follow these instructions to set up and use the script.

### Prerequisites

Before you begin, ensure you have Python and the required libraries installed:

- Python 3.x
- [Requests](https://pypi.org/project/requests/)
- [datetime](https://docs.python.org/3/library/datetime.html)

You can install the necessary libraries using pip:

```bash
pip install requests
