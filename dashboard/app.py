import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Workforce Intelligence",
    layout="wide"
)

st.title(
    "🤖 AI Workforce Intelligence Platform"
)

st.subheader(
    "Employee Attrition Prediction & Retention Analytics"
)

df = pd.read_csv(
    "../data/retention_recommendations.csv"
)

####################################################

st.header(
    "Executive Overview"
)

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Employees",
    len(df)
)

c2.metric(
    "Critical Employees",
    len(
        df[
            df['CriticalityLevel']
            ==
            'Critical'
        ]
    )
)

c3.metric(
    "Medium Risk",
    len(
        df[
            df['CriticalityLevel']
            ==
            'Medium'
        ]
    )
)

c4.metric(
    "Expected Financial Loss",
    "$"+"{:,.0f}".format(
        df['FinancialLoss'].sum()
    )
)

####################################################

st.header(
    "Criticality Distribution"
)

fig = px.pie(
    df,
    names='CriticalityLevel',
    title='Workforce Criticality'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

####################################################

st.header(
    "Attrition Probability"
)

fig = px.histogram(
    df,
    x='AttritionProbability',
    nbins=20
)

st.plotly_chart(
    fig,
    use_container_width=True
)

####################################################

st.header(
    "Top Financial Risk Employees"
)

top = df.sort_values(
    'CriticalityScore',
    ascending=False
).head(10)
st.write(top.columns)
st.dataframe(
    top[
        [
            'AttritionProbability',
            'CriticalityLevel',
            'EmployeeValueScore',
            'FinancialLoss',
            'ActionPriority'
        ]
    ]
)

####################################################

st.header(
    "AI Retention Recommendations"
)

employee = st.selectbox(
    "Select Employee",
    df.index
)

st.write(
    "Attrition Probability:",
    round(
        df.loc[
            employee,
            'AttritionProbability'
        ],
        2
    )
)

st.write(
    "Criticality:",
    df.loc[
        employee,
        'CriticalityLevel'
    ]
)

st.write(
    "Priority:",
    df.loc[
        employee,
        'ActionPriority'
    ]
)

st.write(
    "Recommendations:"
)

st.write(
    df.loc[
        employee,
        'Recommendations'
    ]
)