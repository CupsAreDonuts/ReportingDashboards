import sys
import streamlit as st
import altair as alt
from streamlit.web import cli as stcli

from data.google import load_cashflow_tracking
from hauswirtschaft.data_processing.preparation import create_cashflow_by_date_table

cashflow = load_cashflow_tracking()
cashflow_by_date = create_cashflow_by_date_table(cashflow_tracking=cashflow)
by_date_chart = alt.Chart(cashflow_by_date, title='Cashflow tracker').mark_bar().encode(
    alt.X('Date', sort=list(cashflow_by_date['x_axis_order'])),
    alt.Y('Amount:Q')
)

st.title('Cashflow per day')
st.altair_chart(by_date_chart, use_container_width=True)
st.header('Cashflow table')
cashflow_by_date.drop(['x_axis_order'], axis=1, inplace=True)
st.dataframe(cashflow_by_date, use_container_width=True)
st.header('Complete table')
st.dataframe(cashflow, use_container_width=True)


if __name__ == '__main__':
    if not st.runtime.exists():
        sys.argv = ["streamlit", "run", "Overview.py"]
        sys.exit(stcli.main())
