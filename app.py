# ==============================================================
# 🏥 Healthcare Cyber Risk Intelligence Dashboard
# Homeland Security Style – Streamlined + Insight Enhanced
# Author: Nathaniel Mueller
# ==============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import os
import streamlit.components.v1 as components

# --------------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------------
st.set_page_config(
    page_title="Healthcare Cyber Risk Intelligence Dashboard",
    layout="wide",
    page_icon="🏥",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------------------
# HEADER HERO BANNER
# --------------------------------------------------------------
banner_html = """
<style>
@media (max-width: 1000px) {
    .hero-banner { padding: 35px 20px 30px 20px !important; }
    .hero-banner h1 { font-size: 1.8rem !important; }
    .hero-banner p { font-size: 0.95rem !important; max-width: 100% !important; }
    .hero-watermark { display: none !important; }
}
</style>

<div class="hero-banner" style="
    background: linear-gradient(90deg, #0B3D91 0%, #1A73A8 100%);
    color: white;
    padding: 55px 30px 50px 30px;
    border-radius: 8px;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
    font-family: 'Helvetica Neue', sans-serif;
">
    <div class="hero-watermark" style='
        position: absolute;
        right: 40px;
        top: 20px;
        bottom: 0;
        width: 200px;
        background: url("https://cdn-icons-png.flaticon.com/512/3176/3176366.png") no-repeat right center;
        background-size: 180px;
        opacity: 0.08;
    '></div>

    <h1 style="margin-bottom: 10px; font-size: 2.3rem; font-weight: 700;">
        Healthcare Cyber Risk Intelligence Dashboard
    </h1>
    <p style="font-size: 1.05rem; color: #EAF2FA; max-width: 950px; line-height: 1.5;">
        A data-driven analysis of healthcare data breaches reported to the U.S. Department of Health & Human Services (HHS).
        This dashboard merges clinical and cybersecurity perspectives to visualize evolving threats,
        regional vulnerabilities, and organizational exposure across the U.S. healthcare system.
    </p>
</div>
"""
components.html(banner_html, height=280, scrolling=False)

# --------------------------------------------------------------
# GLOBAL STYLES
# --------------------------------------------------------------
px.defaults.template = "simple_white"
px.defaults.color_continuous_scale = ["#E4E8F0", "#0B3D91"]

st.markdown("""
<style>
.section-title {
    color: #0B3D91;
    font-weight: 700;
    border-left: 5px solid #1A73A8;
    padding-left: 10px;
    margin-top: 30px;
    font-size: 1.2rem;
}
.metric-positive { color: #006400; font-weight: 600; }
.metric-negative { color: #B22222; font-weight: 600; }
.metric-neutral { color: #444; }

/* Tabs */
div[data-testid="stTabs"] div[role="tablist"] {
    background-color: #E4E8F0;
    border-radius: 8px;
    padding: 6px;
    justify-content: center;
}
div[role="tab"] {
    background-color: #F9FAFB;
    color: #0B3D91;
    border-radius: 6px;
    padding: 8px 16px;
    margin: 0 4px;
    font-weight: 600;
}
div[role="tab"][aria-selected="true"] {
    background-color: #0B3D91;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------------
# HELPER: Render Full Chart with Rounded Shadow
# --------------------------------------------------------------
def plot_card(fig, height=460):
    html_code = f"""
    <div style="
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        padding: 10px 10px 0 10px;
        margin-bottom: 32px;
        overflow: hidden;
        transition: box-shadow .2s ease-in-out, transform .2s ease-in-out;
    " onmouseover="this.style.boxShadow='0 4px 14px rgba(0,0,0,0.15)';this.style.transform='translateY(-2px)';"
      onmouseout="this.style.boxShadow='0 2px 8px rgba(0,0,0,0.08)';this.style.transform='none';">
        {fig.to_html(include_plotlyjs='cdn', config={'displayModeBar': True}, full_html=False)}
    </div>
    """
    components.html(html_code, height=height + 40, scrolling=False)

# --------------------------------------------------------------
# LOAD DATA
# --------------------------------------------------------------
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "data_clean", "hhs_breaches_clean.csv")
    return pd.read_csv(file_path)

df = load_data()

# --------------------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------------------
with st.sidebar:
    st.markdown("<div style='color:#0B3D91; font-weight:700; font-size:1.1rem;'>Filter Options</div>", unsafe_allow_html=True)
    st.markdown("<hr style='margin:5px 0;'>", unsafe_allow_html=True)

    years = sorted(df["year"].dropna().unique())
    selected_year = st.selectbox("Year", ["All"] + [str(int(y)) for y in years])

    breach_types = sorted(df["type_of_breach"].dropna().unique())
    selected_type = st.selectbox("Breach Type", ["All"] + breach_types)

    states = sorted(df["state"].dropna().unique())
    selected_state = st.selectbox("State", ["All"] + states)

# --------------------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------------------
filtered_df = df.copy()
if selected_year != "All":
    filtered_df = filtered_df[filtered_df["year"] == int(selected_year)]
if selected_type != "All":
    filtered_df = filtered_df[filtered_df["type_of_breach"] == selected_type]
if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

# --------------------------------------------------------------
# KPI METRICS
# --------------------------------------------------------------
total_breaches = len(filtered_df)
total_affected = int(filtered_df["individuals_affected"].sum())
avg_affected = int(filtered_df["individuals_affected"].mean())

col1, col2, col3 = st.columns(3)
col1.metric("Total Breaches", f"{total_breaches:,}")
col2.metric("Individuals Affected", f"{total_affected:,}")
col3.metric("Average per Breach", f"{avg_affected:,}")

# --------------------------------------------------------------
# YEAR-OVER-YEAR CHANGE
# --------------------------------------------------------------
yearly_filtered = (
    filtered_df.groupby("year").size().reset_index(name="Total Breaches").sort_values("year")
)

change_text = ""
trend_icon = ""
trend_color = ""
if len(yearly_filtered) >= 2:
    change = yearly_filtered["Total Breaches"].iloc[-1] - yearly_filtered["Total Breaches"].iloc[-2]
    last_year = int(yearly_filtered["year"].iloc[-2])
    recent_year = int(yearly_filtered["year"].iloc[-1])
    if change > 0:
        trend_icon, trend_color = "▲", "#B22222"
        change_text = f"<span style='color:{trend_color}; font-weight:600;'>{trend_icon} {abs(change):,} more breaches ({recent_year} vs {last_year})</span>"
    elif change < 0:
        trend_icon, trend_color = "▼", "#006400"
        change_text = f"<span style='color:{trend_color}; font-weight:600;'>{trend_icon} {abs(change):,} fewer breaches ({recent_year} vs {last_year})</span>"
    else:
        change_text = f"<span style='color:#444;'>No change in total breaches ({recent_year} vs {last_year})</span>"

st.markdown(change_text, unsafe_allow_html=True)

# --------------------------------------------------------------
# ENHANCED SUMMARY INSIGHT CARD (Top breach type logic added)
# --------------------------------------------------------------
if len(filtered_df) > 0:
    severity = (
        "High Severity" if avg_affected > 500000 else
        "Moderate Severity" if avg_affected > 100000 else
        "Low Severity"
    )
    color_sev = (
        "#B22222" if severity == "High Severity" else
        "#D68910" if severity == "Moderate Severity" else
        "#1E8449"
    )

    # Find top breach type dynamically
    if "type_of_breach" in filtered_df.columns and not filtered_df["type_of_breach"].empty:
        top_type = (
            filtered_df["type_of_breach"]
            .value_counts()
            .idxmax()
            if not filtered_df["type_of_breach"].dropna().empty
            else "N/A"
        )
    else:
        top_type = "N/A"

    insight = f"""
    <div style='
        background:#F2F5FA;
        padding:22px 24px;
        border-radius:12px;
        margin-top:25px;
        color:#1B1F23;
        font-size:0.98rem;
        border-left:6px solid #0B3D91;
        box-shadow:0 2px 8px rgba(0,0,0,0.08);
        line-height:1.55;
    '>
        <div style='font-weight:700; color:#0B3D91; font-size:1.05rem; margin-bottom:6px;'>
            Key Insight
        </div>
        Over the selected timeframe, <b>{total_breaches:,}</b> healthcare data breaches 
        impacted approximately <b>{total_affected:,}</b> individuals across the U.S.
        (<span style='color:{trend_color}; font-weight:600;'>{trend_icon} {abs(change) if len(yearly_filtered)>=2 else 0:,} year-over-year change</span>).
        <br><br>
        The current average exposure per breach is <b>{avg_affected:,}</b> individuals,
        indicating a <span style='color:{color_sev}; font-weight:600;'>{severity}</span> risk level.
        <br><br>
        <i>Dominant breach category:</i> <b>{top_type}</b>.
    </div>
    """
    st.markdown(insight, unsafe_allow_html=True)

# --------------------------------------------------------------
# TAB SECTIONS
# --------------------------------------------------------------
st.markdown("<hr style='margin:25px 0;'>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Trends", "Geographic View", "Entities"])

# ---------------- TAB 1 ----------------
with tab1:
    st.markdown("<div class='section-title'>Breach Trends Over Time</div>", unsafe_allow_html=True)
    yearly_trend = filtered_df.groupby("year").size().reset_index(name="Total Breaches")
    fig_year = px.line(yearly_trend, x="year", y="Total Breaches", markers=True, color_discrete_sequence=["#0B3D91"])
    fig_year.update_layout(xaxis_title="Year", yaxis_title="Number of Breaches",
                           font=dict(size=13, color="#1B1F23"), plot_bgcolor="white",
                           margin=dict(l=30,r=30,t=10,b=30))
    plot_card(fig_year)

    st.markdown("<div class='section-title'>Breach Types Distribution</div>", unsafe_allow_html=True)
    breach_counts = filtered_df["type_of_breach"].value_counts().reset_index()
    breach_counts.columns = ["Type of Breach", "Total Breaches"]
    fig_breach = px.bar(breach_counts, x="Total Breaches", y="Type of Breach",
                        orientation="h", color="Total Breaches",
                        color_continuous_scale=["#E4E8F0", "#0B3D91"])
    fig_breach.update_layout(plot_bgcolor="white", margin=dict(l=30,r=30,t=10,b=30))
    plot_card(fig_breach)

# ---------------- TAB 2 ----------------
with tab2:
    st.markdown("<div class='section-title'>Geographic Distribution</div>", unsafe_allow_html=True)
    state_counts = filtered_df["state"].value_counts().reset_index()
    state_counts.columns = ["State", "Total Breaches"]
    fig_map = px.choropleth(state_counts, locations="State", locationmode="USA-states",
                            color="Total Breaches", scope="usa",
                            color_continuous_scale=["#E4E8F0", "#0B3D91"])
    fig_map.update_layout(margin=dict(l=0,r=0,t=0,b=0))
    plot_card(fig_map, height=500)

# ---------------- TAB 3 ----------------
with tab3:
    st.markdown("<div class='section-title'>Top Impacted Healthcare Entities</div>", unsafe_allow_html=True)
    top_entities = filtered_df["name_of_covered_entity"].value_counts().head(10).reset_index()
    top_entities.columns = ["Healthcare Entity", "Total Breaches"]
    fig_entities = px.bar(top_entities, x="Healthcare Entity", y="Total Breaches",
                          color="Total Breaches",
                          color_continuous_scale=["#E4E8F0", "#0B3D91"])
    fig_entities.update_layout(plot_bgcolor="white", margin=dict(l=30,r=30,t=10,b=30))
    plot_card(fig_entities)

# --------------------------------------------------------------
# EXPORT & FOOTER
# --------------------------------------------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data (CSV)", csv, "filtered_breach_data.csv", "text/csv")

st.markdown(
    f"""
    <hr style='border: 1px solid #0B3D91; margin-top: 40px; margin-bottom: 15px;'>
    <div style='text-align:center;color:#4B4B4B;font-size:0.9rem;'>
        © {datetime.datetime.now().year} Healthcare Cyber Risk Intelligence Dashboard · 
        Created by <b>Nathaniel Mueller</b><br>
        Tools: Python · Pandas · Plotly · Streamlit · GitHub · VS Code<br>
        Focus: Healthcare Data Security · Cyber Risk Analytics · Public Transparency
    </div>
    """,
    unsafe_allow_html=True
)
