import pandas as pd


def create_cashflow_by_date_table(cashflow_tracking: pd.DataFrame):
    cashflow_tracking.loc[cashflow_tracking['Type'] == 'Expense', 'Amount'] = -cashflow_tracking['Amount']
    cashflow_by_date = cashflow_tracking.groupby('Date')['Amount'].sum().reset_index()
    cashflow_by_date.index.name = 'x_axis_order'
    cashflow_by_date['Date'] = cashflow_by_date['Date'].map(lambda date: f'{date.day}.{date.month}.{date.year}')
    cashflow_by_date.reset_index(inplace=True)
    return cashflow_by_date
