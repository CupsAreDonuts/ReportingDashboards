import gspread
import pandas as pd
from pathlib import Path

import streamlit as st

key_location = Path(__file__).parent.parent / 'keys/google_sheets.json'
authenticator = gspread.service_account(filename=key_location.resolve())


def load_scholarship_tracking():
    spreadsheet = authenticator.open('Improvement Tracker')
    worksheet = spreadsheet.worksheet('Scholarship')
    scholarship = pd.DataFrame(worksheet.get_all_records())
    scholarship['Date'] = scholarship['Date'].map(lambda date: pd.to_datetime(date, format='%d.%m.%Y'))
    return scholarship


def load_cashflow_tracking():
    spreadsheet = authenticator.open('Cashflow')
    worksheet = spreadsheet.worksheet('Tracker')
    cashflow_tracking = pd.DataFrame(worksheet.get_all_records())
    cashflow_tracking['Date'] = cashflow_tracking['Date'].map(lambda date: pd.to_datetime(date, format='%d.%m.%Y'))
    return cashflow_tracking
