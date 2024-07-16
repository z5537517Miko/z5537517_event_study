"""
yf_example3 module
This module downloads Qantas stock prices for a given year and saves them into a CSV file.
"""

import os
import toolkit_config as cfg
from yf_example2 import yf_prc_to_csv


def qan_prc_to_csv(year):
    """
    Downloads Qantas stock prices for the given year and saves them into a CSV file.

    Parameters:
        year (int): The year for which to download stock prices.
    """
    # Define the start and end period
    start_period = f"{year}-01-01"
    end_period = f"{year}-12-31"

    # Define the output file path
    output_file = os.path.join(cfg.DATADIR, f"qan_prc_{year}.csv")

    # Download the data for the given period and ticker 'QAN.AX'
    yf_prc_to_csv('QAN.AX', output_file, start=start_period, end=end_period)


if __name__ == "__main__":
    # Test the function with the year 2020
    qan_prc_to_csv(2020)