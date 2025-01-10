import sys
import streamlit as st
import altair as alt
from streamlit.web import cli as stcli

from data.google import load_scholarship_tracking

scholarship = load_scholarship_tracking()
scholarship = scholarship.groupby(['Date', 'Done'])['Amount(min)'].sum().reset_index()
scholarship['Amount(h)'] = scholarship['Amount(min)'].map(lambda amount: amount/60)

st.header('Scholarship')
scholarship_effort_timeline = alt.Chart(
    scholarship, title=alt.Title('Scholarship efforts over time')).mark_line().encode(
    alt.X('Date:T').title('Date'),
    alt.Y('Amount(h):Q').title('Hours'),
    alt.Color('Done').title('Type of Work')
)
scholarship_effort_distribution = alt.Chart(
    scholarship, title=alt.Title('Scholarship efforts distribution')).mark_arc(innerRadius=30).encode(
    alt.Theta('sum(Amount(h))').title('Hours'),
    alt.Color('Done').title('Type of Work')
)
st.altair_chart(scholarship_effort_timeline, use_container_width=True)
st.altair_chart(scholarship_effort_distribution, use_container_width=True)


if __name__ == '__main__':
    if not st.runtime.exists():
        sys.argv = ["streamlit", "run", "Scholarship.py"]
        sys.exit(stcli.main())
