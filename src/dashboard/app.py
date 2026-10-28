import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# RETAILIQ — PREMIUM E-COMMERCE INTELLIGENCE DASHBOARD
# ============================================================

st.set_page_config(
    page_title="RetailIQ | E-Commerce Intelligence",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# DESIGN SYSTEM
# ----------------------------------------------------------

# Color palette
COLORS = {
    "bg": "#06090f",
    "surface": "#0c1219",
    "surface_2": "#111a26",
    "surface_3": "#16202e",
    "text": "#edf0f7",
    "text_secondary": "#8d99ae",
    "text_muted": "#5c6a7e",
    "border": "rgba(255,255,255,0.06)",
    "accent": "#6c7bff",
    "accent_soft": "rgba(108,123,255,0.12)",
    "teal": "#38bfa7",
    "teal_soft": "rgba(56,191,167,0.10)",
    "positive": "#34d399",
    "negative": "#f87171",
    "warning": "#fbbf24",
    "chart_sequence": [
        "#6c7bff", "#38bfa7", "#a78bfa", "#f59e42",
        "#f472b6", "#67e8f9", "#c084fc", "#fbbf24",
        "#34d399", "#f87171", "#818cf8", "#2dd4bf",
    ],
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

/* ---- RESET & BASE ---- */
:root {
    --bg: """ + COLORS["bg"] + """;
    --surface: """ + COLORS["surface"] + """;
    --surface-2: """ + COLORS["surface_2"] + """;
    --surface-3: """ + COLORS["surface_3"] + """;
    --text: """ + COLORS["text"] + """;
    --text-secondary: """ + COLORS["text_secondary"] + """;
    --text-muted: """ + COLORS["text_muted"] + """;
    --border: """ + COLORS["border"] + """;
    --accent: """ + COLORS["accent"] + """;
    --teal: """ + COLORS["teal"] + """;
    --radius: 14px;
    --radius-sm: 10px;
    --radius-lg: 20px;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1520px;
    padding: 1.8rem 2.4rem 3rem;
}

/* ---- SIDEBAR ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #090e17 0%, #060a10 100%);
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] .block-container {
    padding: 1.2rem 0.8rem 1.5rem;
}

[data-testid="stSidebar"] hr {
    margin: 0.8rem 0;
    border-color: var(--border);
}

[data-testid="stSidebar"] .stRadio > label {
    color: var(--text-muted);
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 2px;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    border-radius: var(--radius-sm);
    padding: 9px 12px;
    font-size: 13px;
    font-weight: 500;
    transition: background .15s ease;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.04);
}

/* ---- BRAND ---- */
.brand {
    padding: 4px 8px 14px;
}

.brand-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -1.2px;
    background: linear-gradient(135deg, #ffffff 0%, #9ba4ff 55%, #38bfa7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-sub {
    color: var(--text-muted);
    font-size: 11px;
    line-height: 1.5;
    margin-top: 4px;
}

.sidebar-stat {
    color: var(--text-secondary);
    font-size: 11px;
    line-height: 1.7;
}

.sidebar-stat strong {
    color: var(--text);
    font-weight: 600;
}

/* ---- PAGE HEADER ---- */
.page-header {
    margin-bottom: 24px;
}

.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(26px, 3vw, 34px);
    font-weight: 700;
    letter-spacing: -1.2px;
    margin: 0 0 6px;
    line-height: 1.1;
}

.page-subtitle {
    color: var(--text-muted);
    font-size: 13px;
    line-height: 1.5;
    max-width: 700px;
}

/* ---- KPI CARDS ---- */
.kpi-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 18px 20px;
    min-height: 100px;
    transition: border-color .15s ease;
}

.kpi-card:hover {
    border-color: rgba(108,123,255,0.18);
}

.kpi-label {
    color: var(--text-muted);
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 10px;
}

.kpi-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.8px;
    color: var(--text);
}

.kpi-note {
    color: var(--text-muted);
    font-size: 10px;
    margin-top: 6px;
    line-height: 1.4;
}

/* ---- SECTION ---- */
.section-label {
    color: var(--accent);
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 6px;
}

.section-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 19px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 16px;
}

/* ---- INSIGHT CARD ---- */
.insight-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 18px 20px;
    height: 100%;
}

.insight-label {
    color: var(--text-muted);
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.insight-body {
    color: var(--text-secondary);
    font-size: 12.5px;
    line-height: 1.6;
}

.insight-body strong {
    color: var(--text);
}

/* ---- METRIC OVERRIDE ---- */
div[data-testid="stMetric"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 14px 16px;
}

div[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

div[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

/* ---- TABLE ---- */
div[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
}

/* ---- INPUTS ---- */
.stSelectbox, .stMultiSelect, .stDateInput {
    font-size: 12px;
}

.stButton > button {
    border-radius: var(--radius-sm);
    border: 1px solid var(--border);
    font-weight: 500;
}

/* ---- MISC ---- */
hr {
    border-color: var(--border) !important;
    margin: 1rem 0;
}

footer { visibility: hidden; }

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.08);
    border-radius: 3px;
}

/* Remove top padding from main */
.main .block-container {
    padding-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():
    feature_df = pd.read_csv("outputs/features/retailiq_features.csv")
    rfm = pd.read_csv("outputs/customer_analysis/customer_rfm.csv")
    cluster_df = pd.read_csv("outputs/customer_analysis/customer_clusters.csv")
    cluster_summary = pd.read_csv("outputs/customer_analysis/cluster_summary.csv")
    products = pd.read_csv("outputs/product_analysis/product_performance.csv")
    categories = pd.read_csv("outputs/product_analysis/category_performance.csv")
    brands = pd.read_csv("outputs/product_analysis/brand_performance.csv")
    states = pd.read_csv("outputs/geography_analysis/state_performance.csv")
    cities = pd.read_csv("outputs/geography_analysis/city_performance.csv")
    return_reasons = pd.read_csv("outputs/operations_analysis/return_reasons.csv")
    return_status = pd.read_csv("outputs/operations_analysis/return_status.csv")
    payment_methods = pd.read_csv("outputs/operations_analysis/payment_methods.csv")
    payment_status = pd.read_csv("outputs/operations_analysis/payment_status.csv")
    rating_summary = pd.read_csv("outputs/operations_analysis/rating_summary.csv")
    sentiment_summary = pd.read_csv("outputs/operations_analysis/sentiment_summary.csv")
    category_reviews = pd.read_csv("outputs/operations_analysis/category_reviews.csv")
    category_returns = pd.read_csv("outputs/operations_analysis/category_returns.csv")
    verified_reviews = pd.read_csv("outputs/operations_analysis/verified_reviews.csv")

    return {
        "df": feature_df,
        "rfm": rfm,
        "clusters": cluster_df,
        "cluster_summary": cluster_summary,
        "products": products,
        "categories": categories,
        "brands": brands,
        "states": states,
        "cities": cities,
        "return_reasons": return_reasons,
        "return_status": return_status,
        "payment_methods": payment_methods,
        "payment_status": payment_status,
        "rating_summary": rating_summary,
        "sentiment_summary": sentiment_summary,
        "category_reviews": category_reviews,
        "category_returns": category_returns,
        "verified_reviews": verified_reviews,
    }


data = load_data()

df = data["df"]
rfm = data["rfm"]
clusters = data["clusters"]
cluster_summary = data["cluster_summary"]
products = data["products"]
categories = data["categories"]
brands = data["brands"]
states = data["states"]
cities = data["cities"]
return_reasons = data["return_reasons"]
return_status_df = data["return_status"]
payment_methods = data["payment_methods"]
payment_status_df = data["payment_status"]
rating_summary = data["rating_summary"]
sentiment_summary = data["sentiment_summary"]
category_reviews = data["category_reviews"]
category_returns = data["category_returns"]
verified_reviews = data["verified_reviews"]

df["date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["month"] = df["date"].dt.to_period("M").astype(str)


# ============================================================
# HELPERS
# ============================================================

def money(x):
    """Format currency in Indian notation."""
    x = float(x)
    if abs(x) >= 1e7:
        return f"Rs. {x / 1e7:.2f} Cr"
    if abs(x) >= 1e5:
        return f"Rs. {x / 1e5:.1f} L"
    return f"Rs. {x:,.0f}"


def kpi_card(label, value, note=""):
    """Render a KPI card."""
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-note">{note}</div>
    </div>
    """


def style_chart(fig, height=390):
    """Apply consistent chart styling."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=11, color="#8d99ae"),
        title_font=dict(family="Space Grotesk, sans-serif", size=16, color="#edf0f7"),
        margin=dict(l=16, r=16, t=52, b=28),
        height=height,
        hoverlabel=dict(
            bgcolor="#111a26",
            font_color="#edf0f7",
            font_size=12,
            bordercolor="rgba(255,255,255,0.08)",
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=10, color="#8d99ae"),
        ),
        colorway=COLORS["chart_sequence"],
    )
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=10),
    )
    fig.update_yaxes(
        gridcolor="rgba(255,255,255,0.04)",
        zeroline=False,
        tickfont=dict(size=10),
    )
    return fig


def page_header(title, subtitle):
    """Render page header."""
    st.markdown(f"""
    <div class="page-header">
        <h1 class="page-title">{title}</h1>
        <p class="page-subtitle">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def section_heading(label, heading):
    """Render section sub-heading."""
    st.markdown(f"""
    <div class="section-label">{label}</div>
    <div class="section-heading">{heading}</div>
    """, unsafe_allow_html=True)


def insight_card(label, body):
    """Render an insight card."""
    return f"""
    <div class="insight-card">
        <div class="insight-label">{label}</div>
        <div class="insight-body">{body}</div>
    </div>
    """


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-title">RetailIQ</div>
        <div class="brand-sub">Indian E-Commerce Intelligence Platform</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Executive Overview",
            "Sales Analytics",
            "Customer Intelligence",
            "Product Intelligence",
            "India Analytics",
            "Returns & Payments",
            "Reviews & Customer Experience",
        ],
        label_visibility="visible",
    )

    st.divider()

    st.markdown("""
    <div class="sidebar-stat">
        <strong>100,000</strong> orders<br>
        <strong>25,000</strong> customers<br>
        <strong>254,331</strong> order items<br>
        <strong>550</strong> products
    </div>
    """, unsafe_allow_html=True)

    st.caption("Simulated Indian e-commerce dataset")

    st.divider()
    st.caption("RetailIQ v1.0")


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    page_header(
        "Executive Overview",
        "Marketplace performance, revenue trends, and key business signals at a glance."
    )

    # --- KPIs (all dynamically computed) ---
    total_revenue = df["revenue"].sum()
    total_profit = df["item_profit"].sum()
    total_orders = df["order_id"].nunique()
    total_customers = df["customer_id"].nunique()
    avg_order_value = df.groupby("order_id")["final_amount"].first().mean()

    # Dynamic return count from the return_reasons output
    total_returns = int(return_reasons["return_count"].sum())
    return_rate = total_returns / total_orders * 100

    overall_margin = total_profit / total_revenue * 100

    cols = st.columns(5)
    kpi_data = [
        ("Total Revenue", money(total_revenue), "Gross item revenue"),
        ("Net Profit", money(total_profit), f"{overall_margin:.1f}% overall margin"),
        ("Orders", f"{total_orders:,}", "Unique transactions"),
        ("Customers", f"{total_customers:,}", "Unique buyers"),
        ("Return Rate", f"{return_rate:.2f}%", f"{total_returns:,} total returns"),
    ]
    for col, (label, value, note) in zip(cols, kpi_data):
        col.markdown(kpi_card(label, value, note), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Revenue Trend ---
    monthly = df.groupby("month", as_index=False)["revenue"].sum()
    fig = px.area(
        monthly, x="month", y="revenue",
        title="Revenue Trend",
        labels={"month": "", "revenue": "Revenue"},
    )
    fig.update_traces(
        line=dict(width=2, color=COLORS["accent"]),
        fillcolor="rgba(108,123,255,0.08)",
    )
    st.plotly_chart(style_chart(fig, 370), use_container_width=True)

    # --- Category + Order Status ---
    c1, c2 = st.columns(2)

    with c1:
        topcat = categories.sort_values("total_revenue", ascending=False).head(10)
        fig = px.bar(
            topcat.sort_values("total_revenue"),
            x="total_revenue", y="category", orientation="h",
            title="Top Categories by Revenue",
            labels={"total_revenue": "Revenue", "category": ""},
        )
        fig.update_traces(marker_color=COLORS["accent"])
        st.plotly_chart(style_chart(fig, 400), use_container_width=True)

    with c2:
        status = df.drop_duplicates("order_id")["order_status"].value_counts().reset_index()
        status.columns = ["status", "orders"]
        fig = px.pie(
            status, names="status", values="orders",
            hole=0.65, title="Order Status Distribution",
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=10,
        )
        st.plotly_chart(style_chart(fig, 400), use_container_width=True)

    # --- Business Insights ---
    section_heading("INSIGHTS", "Business Pulse")

    best_state = states.iloc[0]["delivery_state"]
    best_cat = categories.sort_values("total_revenue", ascending=False).iloc[0]["category"]
    loss_count = int((products["total_profit"] < 0).sum())

    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown(insight_card(
            "MARKET LEADER",
            f"<strong>{best_state}</strong> leads all states by revenue in the current analysis period."
        ), unsafe_allow_html=True)
    with i2:
        st.markdown(insight_card(
            "CATEGORY LEADER",
            f"<strong>{best_cat}</strong> generates the highest category revenue across the marketplace."
        ), unsafe_allow_html=True)
    with i3:
        st.markdown(insight_card(
            "PROFIT WATCH",
            f"<strong>{loss_count}</strong> products are currently loss-making and may need pricing or discount review."
        ), unsafe_allow_html=True)


# ============================================================
# SALES ANALYTICS
# ============================================================

elif page == "Sales Analytics":

    page_header(
        "Sales Analytics",
        "Revenue and profitability trends across time, categories, and products."
    )

    # --- Filters ---
    c1, c2 = st.columns([1, 1])
    with c1:
        date_min = df["date"].min().date()
        date_max = df["date"].max().date()
        date_range = st.date_input("Analysis Period", [date_min, date_max])
    with c2:
        all_cats = sorted(df["category"].dropna().unique())
        selected_cats = st.multiselect("Categories", all_cats, default=all_cats)

    if len(date_range) == 2:
        filtered = df[
            (df["date"].dt.date >= date_range[0])
            & (df["date"].dt.date <= date_range[1])
        ]
    else:
        filtered = df.copy()
    filtered = filtered[filtered["category"].isin(selected_cats)]

    # --- KPIs ---
    a, b, c, d = st.columns(4)
    a.metric("Revenue", money(filtered["revenue"].sum()))
    b.metric("Profit", money(filtered["item_profit"].sum()))
    c.metric("Orders", f"{filtered['order_id'].nunique():,}")
    d.metric("Units Sold", f"{filtered['quantity'].sum():,.0f}")

    # --- Revenue Trend ---
    filtered_copy = filtered.copy()
    filtered_copy["month"] = filtered_copy["date"].dt.to_period("M").astype(str)
    monthly_rev = filtered_copy.groupby("month", as_index=False)["revenue"].sum()
    fig = px.line(
        monthly_rev, x="month", y="revenue",
        markers=True, title="Revenue Trend",
        labels={"month": "", "revenue": "Revenue"},
    )
    fig.update_traces(line=dict(color=COLORS["accent"], width=2))
    st.plotly_chart(style_chart(fig, 400), use_container_width=True)

    # --- Category Breakdown ---
    c1, c2 = st.columns(2)
    with c1:
        cat_rev = (
            filtered.groupby("category", as_index=False)["revenue"]
            .sum()
            .sort_values("revenue", ascending=False)
        )
        fig = px.bar(
            cat_rev.head(12), x="revenue", y="category", orientation="h",
            title="Revenue by Category",
            labels={"revenue": "Revenue", "category": ""},
        )
        fig.update_traces(marker_color=COLORS["accent"])
        st.plotly_chart(style_chart(fig, 430), use_container_width=True)

    with c2:
        cat_prof = (
            filtered.groupby("category", as_index=False)["item_profit"]
            .sum()
            .sort_values("item_profit")
        )
        fig = px.bar(
            cat_prof, x="item_profit", y="category", orientation="h",
            title="Profit by Category",
            labels={"item_profit": "Profit", "category": ""},
        )
        fig.update_traces(marker_color=COLORS["teal"])
        st.plotly_chart(style_chart(fig, 430), use_container_width=True)


# ============================================================
# CUSTOMER INTELLIGENCE
# ============================================================

elif page == "Customer Intelligence":

    page_header(
        "Customer Intelligence",
        "Customer value, RFM segmentation, and K-Means clustering analysis."
    )

    # --- KPIs (dynamic) ---
    largest_segment = rfm["RFM_segment"].value_counts().idxmax()
    largest_segment_count = rfm["RFM_segment"].value_counts().max()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Purchasing Customers", f"{len(rfm):,}")
    c2.metric("Avg Frequency", f"{rfm['frequency'].mean():.2f}")
    c3.metric("Avg Monetary", money(rfm["monetary"].mean()))
    c4.metric("Largest Segment", f"{largest_segment}")

    # --- RFM Segments ---
    seg = rfm["RFM_segment"].value_counts().reset_index()
    seg.columns = ["segment", "customers"]
    fig = px.bar(
        seg.sort_values("customers"),
        x="customers", y="segment", orientation="h",
        title="RFM Customer Segments",
        labels={"customers": "Customer Count", "segment": ""},
    )
    fig.update_traces(marker_color=COLORS["accent"])
    st.plotly_chart(style_chart(fig, 420), use_container_width=True)

    # --- Clusters + Top Customers ---
    c1, c2 = st.columns(2)

    with c1:
        cluster_display = clusters.groupby("cluster").agg(
            customers=("customer_id", "count"),
            avg_recency=("recency", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_monetary=("monetary", "mean"),
        ).reset_index()
        cluster_display["avg_monetary"] = cluster_display["avg_monetary"].round(0)

        fig = px.scatter(
            cluster_display,
            x="avg_frequency", y="avg_monetary",
            size="customers", color="cluster",
            title="K-Means Customer Clusters (K=2)",
            labels={
                "avg_frequency": "Avg Frequency",
                "avg_monetary": "Avg Monetary Value",
                "cluster": "Cluster",
            },
            hover_data=["avg_recency", "customers"],
        )
        st.plotly_chart(style_chart(fig, 420), use_container_width=True)

    with c2:
        top_cust = rfm.sort_values("monetary", ascending=False).head(10).copy()
        top_cust["monetary_display"] = top_cust["monetary"].map(money)
        section_heading("TOP CUSTOMERS", "By Monetary Value")
        st.dataframe(
            top_cust[["customer_id", "frequency", "monetary_display", "RFM_score", "RFM_segment"]]
            .rename(columns={"monetary_display": "monetary"}),
            hide_index=True,
            use_container_width=True,
        )

    # --- Segment Strategy (all 6 segments) ---
    section_heading("STRATEGY", "Segment Recommendations")
    strategy = pd.DataFrame({
        "Segment": [
            "Champions",
            "Loyal Customers",
            "New Customers",
            "At Risk",
            "High Value At Risk",
            "Regular Customers",
        ],
        "Count": [
            int(rfm[rfm["RFM_segment"] == s].shape[0])
            for s in [
                "Champions", "Loyal Customers", "New Customers",
                "At Risk", "High Value At Risk", "Regular Customers",
            ]
        ],
        "Recommended Action": [
            "Reward with exclusive offers and premium experiences",
            "Cross-sell complementary products and loyalty benefits",
            "Onboarding sequences and second-purchase incentives",
            "Win-back campaigns with personalized re-engagement",
            "Priority outreach with high-value retention offers",
            "Personalized promotions to increase engagement",
        ],
    })
    st.dataframe(strategy, hide_index=True, use_container_width=True)


# ============================================================
# PRODUCT INTELLIGENCE
# ============================================================

elif page == "Product Intelligence":

    page_header(
        "Product Intelligence",
        "Product performance, category analysis, and profitability assessment."
    )

    # --- KPIs ---
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Products", f"{products['product_id'].nunique():,}")
    c2.metric("Categories", f"{categories['category'].nunique():,}")
    c3.metric("Loss-Making Products", f"{(products['total_profit'] < 0).sum():,}")
    c4.metric("Total Revenue", money(products["total_revenue"].sum()))

    # --- Top Products ---
    top_prod = products.sort_values("total_revenue", ascending=False).head(10)
    fig = px.bar(
        top_prod.sort_values("total_revenue"),
        x="total_revenue", y="product_name", orientation="h",
        title="Top 10 Products by Revenue",
        labels={"total_revenue": "Revenue", "product_name": ""},
        hover_data=["category", "total_profit"],
    )
    fig.update_traces(marker_color=COLORS["accent"])
    st.plotly_chart(style_chart(fig, 460), use_container_width=True)

    # --- Category Revenue vs Profit + Loss-Making ---
    c1, c2 = st.columns(2)

    with c1:
        fig = px.scatter(
            categories,
            x="total_revenue", y="total_profit",
            size="total_revenue", hover_name="category",
            title="Category Revenue vs Profit",
            labels={"total_revenue": "Revenue", "total_profit": "Profit"},
        )
        st.plotly_chart(style_chart(fig, 430), use_container_width=True)

    with c2:
        loss = products[products["total_profit"] < 0].sort_values("total_profit").head(12)
        fig = px.bar(
            loss, x="total_profit", y="product_name", orientation="h",
            title="Loss-Making Products",
            labels={"total_profit": "Profit (Loss)", "product_name": ""},
        )
        fig.update_traces(marker_color=COLORS["negative"])
        st.plotly_chart(style_chart(fig, 430), use_container_width=True)

    # --- Category Table ---
    section_heading("CATEGORIES", "Full Performance Table")
    display_cats = categories.sort_values("total_revenue", ascending=False).copy()
    display_cats["profit_margin"] = display_cats["profit_margin"].round(2)
    st.dataframe(display_cats, hide_index=True, use_container_width=True)


# ============================================================
# INDIA ANALYTICS
# ============================================================

elif page == "India Analytics":

    page_header(
        "India Analytics",
        "Geographic performance across Indian states and cities."
    )

    # --- Top States ---
    top_states = states.sort_values("revenue", ascending=False).head(15)
    fig = px.bar(
        top_states.sort_values("revenue"),
        x="revenue", y="delivery_state", orientation="h",
        title="Top 15 States by Revenue",
        labels={"revenue": "Revenue", "delivery_state": ""},
        hover_data=["profit", "profit_margin"],
    )
    fig.update_traces(marker_color=COLORS["accent"])
    st.plotly_chart(style_chart(fig, 480), use_container_width=True)

    # --- State Revenue vs Profit + Margins ---
    c1, c2 = st.columns(2)

    with c1:
        fig = px.scatter(
            states,
            x="revenue", y="profit",
            size="revenue", hover_name="delivery_state",
            title="State Revenue vs Profit",
            labels={"revenue": "Revenue", "profit": "Profit"},
        )
        st.plotly_chart(style_chart(fig, 420), use_container_width=True)

    with c2:
        top_margin = states.sort_values("profit_margin", ascending=False).head(12)
        fig = px.bar(
            top_margin.sort_values("profit_margin"),
            x="profit_margin", y="delivery_state", orientation="h",
            title="Highest Profit Margins by State",
            labels={"profit_margin": "Profit Margin (%)", "delivery_state": ""},
        )
        fig.update_traces(marker_color=COLORS["teal"])
        st.plotly_chart(style_chart(fig, 420), use_container_width=True)

    # --- Top Cities ---
    section_heading("CITIES", "Top 15 Cities by Revenue")
    top_cities = cities.sort_values("revenue", ascending=False).head(15)
    fig = px.bar(
        top_cities.sort_values("revenue"),
        x="revenue", y="delivery_city", orientation="h",
        title="Top 15 Cities by Revenue",
        labels={"revenue": "Revenue", "delivery_city": ""},
        hover_data=["delivery_state", "profit"],
    )
    fig.update_traces(marker_color=COLORS["accent"])
    st.plotly_chart(style_chart(fig, 480), use_container_width=True)

    # --- State Table ---
    section_heading("DATA", "State Performance Table")
    st.dataframe(states, hide_index=True, use_container_width=True)


# ============================================================
# RETURNS & PAYMENTS
# ============================================================

elif page == "Returns & Payments":

    page_header(
        "Returns & Payments",
        "Return patterns, payment behavior, and operational performance."
    )

    # --- KPIs (dynamic) ---
    total_returns = int(return_reasons["return_count"].sum())
    total_orders = df["order_id"].nunique()
    return_rate = total_returns / total_orders * 100

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Returns", f"{total_returns:,}")
    c2.metric("Return Rate", f"{return_rate:.2f}%")
    c3.metric("Payment Methods", f"{payment_methods['payment_method'].nunique():,}")
    c4.metric("Total Orders", f"{total_orders:,}")

    # --- Return Reasons + Payment Mix ---
    left, right = st.columns(2)

    with left:
        rr = return_reasons.sort_values("return_count", ascending=True)
        fig = px.bar(
            rr, x="return_count", y="return_reason", orientation="h",
            title="Return Reasons",
            labels={"return_count": "Returns", "return_reason": ""},
        )
        fig.update_traces(marker_color=COLORS["negative"])
        st.plotly_chart(style_chart(fig, 420), use_container_width=True)

    with right:
        fig = px.pie(
            payment_methods,
            names="payment_method", values="transactions",
            hole=0.62, title="Payment Method Distribution",
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=9,
        )
        st.plotly_chart(style_chart(fig, 420), use_container_width=True)

    # --- Category Returns ---
    section_heading("RETURNS", "Returns by Category")
    top_cat_returns = category_returns.sort_values("total_returns", ascending=False).head(10)
    fig = px.bar(
        top_cat_returns.sort_values("total_returns"),
        x="total_returns", y="category", orientation="h",
        title="Top 10 Categories by Return Volume",
        labels={"total_returns": "Returns", "category": ""},
        hover_data=["total_refund"],
    )
    fig.update_traces(marker_color=COLORS["warning"])
    st.plotly_chart(style_chart(fig, 400), use_container_width=True)

    # --- Payment Table ---
    section_heading("PAYMENTS", "Payment Method Performance")
    st.dataframe(
        payment_methods.sort_values("transactions", ascending=False),
        hide_index=True,
        use_container_width=True,
    )


# ============================================================
# REVIEWS & CUSTOMER EXPERIENCE
# ============================================================

elif page == "Reviews & Customer Experience":

    page_header(
        "Reviews & Customer Experience",
        "Customer ratings, sentiment distribution, and review quality metrics."
    )

    # --- KPIs (dynamic) ---
    total_reviews = int(rating_summary["review_count"].sum())
    avg_rating = (
        (rating_summary["rating"] * rating_summary["review_count"]).sum()
        / total_reviews
    )
    positive_count = int(
        sentiment_summary.loc[
            sentiment_summary["sentiment"] == "Positive", "review_count"
        ].iloc[0]
    )
    negative_count = int(
        sentiment_summary.loc[
            sentiment_summary["sentiment"] == "Negative", "review_count"
        ].iloc[0]
    )
    neutral_count = int(
        sentiment_summary.loc[
            sentiment_summary["sentiment"] == "Neutral", "review_count"
        ].iloc[0]
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Reviews", f"{total_reviews:,}")
    c2.metric("Average Rating", f"{avg_rating:.2f} / 5")
    c3.metric("Positive Reviews", f"{positive_count:,}")
    c4.metric("Negative Reviews", f"{negative_count:,}")

    # --- Rating Distribution + Sentiment ---
    left, right = st.columns(2)

    with left:
        fig = px.bar(
            rating_summary, x="rating", y="review_count",
            title="Rating Distribution",
            labels={"rating": "Rating", "review_count": "Reviews"},
        )
        fig.update_traces(marker_color=COLORS["accent"])
        fig.update_xaxes(dtick=1)
        st.plotly_chart(style_chart(fig, 400), use_container_width=True)

    with right:
        fig = px.pie(
            sentiment_summary,
            names="sentiment", values="review_count",
            hole=0.62, title="Sentiment Distribution",
            color="sentiment",
            color_discrete_map={
                "Positive": COLORS["positive"],
                "Neutral": COLORS["warning"],
                "Negative": COLORS["negative"],
            },
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=10,
        )
        st.plotly_chart(style_chart(fig, 400), use_container_width=True)

    # --- Category Reviews ---
    section_heading("CATEGORIES", "Review Performance by Category")
    top_cat_reviews = category_reviews.sort_values("average_rating", ascending=False).head(12)
    fig = px.bar(
        top_cat_reviews.sort_values("average_rating"),
        x="average_rating", y="category", orientation="h",
        title="Top Categories by Average Rating",
        labels={"average_rating": "Average Rating", "category": ""},
        hover_data=["review_count"],
    )
    fig.update_traces(marker_color=COLORS["teal"])
    st.plotly_chart(style_chart(fig, 430), use_container_width=True)

    # --- Experience Snapshot ---
    section_heading("EXPERIENCE", "Customer Experience Snapshot")
    positive_pct = positive_count / total_reviews * 100
    negative_pct = negative_count / total_reviews * 100
    verified_count = int(
        verified_reviews.loc[
            verified_reviews["verified_purchase"] == True, "review_count"
        ].iloc[0]
    )
    verified_pct = verified_count / total_reviews * 100

    a, b, c = st.columns(3)
    with a:
        st.markdown(insight_card(
            "POSITIVE EXPERIENCE",
            f"<strong>{positive_pct:.1f}%</strong> of reviewed experiences are classified as positive sentiment."
        ), unsafe_allow_html=True)
    with b:
        st.markdown(insight_card(
            "NEGATIVE SIGNAL",
            f"<strong>{negative_pct:.1f}%</strong> of reviewed experiences are classified as negative sentiment."
        ), unsafe_allow_html=True)
    with c:
        st.markdown(insight_card(
            "VERIFIED PURCHASES",
            f"<strong>{verified_pct:.1f}%</strong> of all reviews ({verified_count:,}) come from verified purchases."
        ), unsafe_allow_html=True)
