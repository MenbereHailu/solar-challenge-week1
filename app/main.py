import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


from .utils import load_data, summary_table


# Load data
df = load_data()

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")
st.title("☀️ Cross-Country Solar Potential Dashboard")

# Sidebar
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect(
    "Select Countries",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

metric = st.sidebar.selectbox("Select Metric", options=['GHI', 'DNI', 'DHI'])

filtered_df = df[df['Country'].isin(countries)]

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Country', y=metric, data=filtered_df, palette='Set2')
ax.set_ylabel(f"{metric} (W/m²)")
st.pyplot(fig)

# Summary Table
st.subheader("📊 Summary Statistics")
st.dataframe(summary_table(filtered_df))

# Top Regions Table
st.subheader(f"🏆 Top 5 Records by {metric}")
st.dataframe(filtered_df.sort_values(by=metric, ascending=False).head(5))

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
