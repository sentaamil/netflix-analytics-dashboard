import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Load environment variables from .env file
load_dotenv()

# -------------------------------
# ✅ SQLAlchemy Engine from .env
# -------------------------------
def get_connection():
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT")
    db = os.getenv("MYSQL_DATABASE")

    connection_str = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(connection_str)
    return engine

# -------------------------------
# ✅ Fetch Data from MySQL
# -------------------------------
def fetch_data():
    engine = get_connection()
    df = pd.read_sql_query("SELECT * FROM netflix", engine)

    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month_name()
    df['listed_in_split'] = df['listed_in'].fillna('').apply(lambda x: [i.strip() for i in x.split(',')])
    return df

# -------------------------------
# ✅ Netflix Themed Streamlit Dashboard
# -------------------------------
st.set_page_config(layout="wide", page_title="Netflix Analytics Dashboard", initial_sidebar_state="expanded")

# Netflix-inspired CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Netflix+Sans:wght@300;400;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 50%, #000000 100%);
        color: white;
        font-family: 'Netflix Sans', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(90deg, #e50914 0%, #b20710 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(229, 9, 20, 0.3);
    }
    
    .netflix-title {
        font-size: 3rem;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin: 0;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #f0f0f0;
        margin-top: 0.5rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e50914;
        box-shadow: 0 4px 20px rgba(229, 9, 20, 0.2);
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .metric-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #e50914;
        margin: 0;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #cccccc;
        margin-top: 0.5rem;
    }
    
    .section-header {
        color: #e50914;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e50914;
    }
    
    .stSelectbox > div > div {
        background-color: #2d2d2d;
        color: white;
        border: 1px solid #e50914;
    }
    
    .stTextInput > div > div {
        background-color: #2d2d2d;
        color: white;
        border: 1px solid #e50914;
    }
    
    .stSidebar {
        background: linear-gradient(180deg, #1a1a1a 0%, #0d0d0d 100%);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #e50914 0%, #b20710 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #b20710 0%, #e50914 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(229, 9, 20, 0.4);
    }
    
    .chart-container {
        background: #1a1a1a;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
    <div class="main-header">
        <h1 class="netflix-title">🎬 NETFLIX ANALYTICS</h1>
        <p class="subtitle">Comprehensive Content Analytics Dashboard</p>
    </div>
""", unsafe_allow_html=True)

# Load data
try:
    df = fetch_data()
    st.success("✅ Successfully connected to MySQL database!")
except Exception as e:
    st.error(f"❌ Failed to load data from MySQL: {e}")
    st.stop()

# Sidebar Filters with Netflix styling
with st.sidebar:
    st.markdown('<div class="section-header">🔍 FILTER OPTIONS</div>', unsafe_allow_html=True)
    
    type_filter = st.selectbox("📱 Content Type", ["All"] + sorted(df["type"].dropna().unique().tolist()))
    country_filter = st.selectbox("🌍 Country", ["All"] + sorted(df["country"].dropna().unique().tolist()))
    year_filter = st.selectbox("📅 Release Year", ["All"] + sorted(df["release_year"].dropna().unique().astype(int).tolist(), reverse=True))
    search_title = st.text_input("🔎 Search Title")
    
    # Rating filter
    rating_filter = st.selectbox("⭐ Rating", ["All"] + sorted(df["rating"].dropna().unique().tolist()))
    
    st.markdown("---")
    st.markdown("### 📊 Dashboard Stats")
    st.info(f"Total Records: {len(df):,}")
    st.info(f"Date Range: {df['release_year'].min()} - {df['release_year'].max()}")

# Apply filters
filtered_df = df.copy()
if type_filter != "All":
    filtered_df = filtered_df[filtered_df["type"] == type_filter]
if country_filter != "All":
    filtered_df = filtered_df[filtered_df["country"] == country_filter]
if year_filter != "All":
    filtered_df = filtered_df[filtered_df["release_year"] == int(year_filter)]
if rating_filter != "All":
    filtered_df = filtered_df[filtered_df["rating"] == rating_filter]
if search_title:
    filtered_df = filtered_df[filtered_df["title"].str.contains(search_title, case=False, na=False)]

# Key Metrics with Netflix styling
st.markdown('<div class="section-header">📈 KEY METRICS</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{filtered_df.shape[0]:,}</div>
            <div class="metric-label">Total Titles</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    movies_count = filtered_df[filtered_df['type'] == 'Movie'].shape[0]
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{movies_count:,}</div>
            <div class="metric-label">Movies</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    tv_shows_count = filtered_df[filtered_df['type'] == 'TV Show'].shape[0]
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{tv_shows_count:,}</div>
            <div class="metric-label">TV Shows</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    countries_count = filtered_df['country'].nunique()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{countries_count:,}</div>
            <div class="metric-label">Countries</div>
        </div>
    """, unsafe_allow_html=True)

# Row 1: Content Type Distribution and Release Year Trends
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">🎭 Content Type Distribution</div>', unsafe_allow_html=True)
    
    # Plotly donut chart
    type_counts = filtered_df['type'].value_counts()
    fig_donut = go.Figure(data=[go.Pie(
        labels=type_counts.index,
        values=type_counts.values,
        hole=0.4,
        marker_colors=['#e50914', '#b20710']
    )])
    fig_donut.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        showlegend=True,
        height=400
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with col2:
    st.markdown('<div class="section-header">📅 Release Year Trends</div>', unsafe_allow_html=True)
    
    # Line chart for release years
    year_counts = filtered_df['release_year'].value_counts().sort_index()
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=year_counts.index,
        y=year_counts.values,
        mode='lines+markers',
        line=dict(color='#e50914', width=3),
        marker=dict(color='#e50914', size=6),
        fill='tonexty',
        fillcolor='rgba(229, 9, 20, 0.1)'
    ))
    fig_line.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333'),
        height=400
    )
    st.plotly_chart(fig_line, use_container_width=True)

# Row 2: Top Genres and Ratings Distribution
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">🎬 Top 10 Genres</div>', unsafe_allow_html=True)
    
    genre_counts = Counter([genre for sublist in filtered_df['listed_in_split'] for genre in sublist])
    top_genres = pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False).head(10)
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        x=top_genres['Count'],
        y=top_genres['Genre'],
        orientation='h',
        marker_color='#e50914',
        marker_line=dict(color='#b20710', width=1)
    ))
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333'),
        height=400
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.markdown('<div class="section-header">⭐ Content Ratings Distribution</div>', unsafe_allow_html=True)
    
    rating_counts = filtered_df['rating'].value_counts()
    fig_rating = go.Figure()
    fig_rating.add_trace(go.Bar(
        x=rating_counts.index,
        y=rating_counts.values,
        marker_color=['#e50914', '#b20710', '#8b0000', '#660000', '#4d0000'][:len(rating_counts)],
        marker_line=dict(color='white', width=1)
    ))
    fig_rating.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333'),
        height=400
    )
    st.plotly_chart(fig_rating, use_container_width=True)

# Row 3: Country Distribution and Duration Analysis
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">🌍 Top 10 Countries</div>', unsafe_allow_html=True)
    
    country_counts = filtered_df['country'].value_counts().head(10)
    fig_country = go.Figure()
    fig_country.add_trace(go.Bar(
        x=country_counts.values,
        y=country_counts.index,
        orientation='h',
        marker_color='#e50914',
        marker_line=dict(color='#b20710', width=1)
    ))
    fig_country.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333'),
        height=400
    )
    st.plotly_chart(fig_country, use_container_width=True)

with col2:
    st.markdown('<div class="section-header">⏱️ Content Added Over Time</div>', unsafe_allow_html=True)
    
    # Monthly additions
    monthly_additions = filtered_df.groupby(['year_added', 'month_added']).size().reset_index(name='count')
    monthly_additions = monthly_additions.dropna()
    
    if not monthly_additions.empty:
        fig_monthly = go.Figure()
        for year in sorted(monthly_additions['year_added'].unique()):
            year_data = monthly_additions[monthly_additions['year_added'] == year]
            fig_monthly.add_trace(go.Scatter(
                x=year_data['month_added'],
                y=year_data['count'],
                mode='lines+markers',
                name=str(int(year)),
                line=dict(width=2)
            ))
        fig_monthly.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis=dict(gridcolor='#333'),
            yaxis=dict(gridcolor='#333'),
            height=400,
            showlegend=True
        )
        st.plotly_chart(fig_monthly, use_container_width=True)
    else:
        st.info("No date information available for visualization")

# Row 4: Content Analysis
st.markdown('<div class="section-header">🔍 Content Analysis</div>', unsafe_allow_html=True)

# Good vs Bad Content Classification
def classify_content(description):
    if isinstance(description, str):
        text = description.lower()
        negative_keywords = ['kill', 'violence', 'murder', 'death', 'war', 'crime', 'blood']
        positive_keywords = ['love', 'family', 'friendship', 'comedy', 'romance', 'adventure', 'fun']
        
        negative_count = sum(1 for keyword in negative_keywords if keyword in text)
        positive_count = sum(1 for keyword in positive_keywords if keyword in text)
        
        if negative_count > positive_count:
            return "Intense"
        elif positive_count > negative_count:
            return "Family-Friendly"
        else:
            return "Neutral"
    return "Neutral"

filtered_df['content_category'] = filtered_df['description'].apply(classify_content)

col1, col2 = st.columns(2)

with col1:
    category_counts = filtered_df.groupby(['type', 'content_category']).size().reset_index(name='count')
    fig_category = px.bar(
        category_counts,
        x='type',
        y='count',
        color='content_category',
        color_discrete_map={'Family-Friendly': '#4CAF50', 'Neutral': '#FFC107', 'Intense': '#e50914'},
        title='Content Categories by Type'
    )
    fig_category.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400
    )
    st.plotly_chart(fig_category, use_container_width=True)

with col2:
    # Heatmap of ratings by type
    rating_type_crosstab = pd.crosstab(filtered_df['rating'], filtered_df['type'])
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=rating_type_crosstab.values,
        x=rating_type_crosstab.columns,
        y=rating_type_crosstab.index,
        colorscale='Reds',
        text=rating_type_crosstab.values,
        texttemplate="%{text}",
        textfont={"size": 12, "color": "white"}
    ))
    fig_heatmap.update_layout(
        title="Rating Distribution Heatmap",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

# Data Table
st.markdown('<div class="section-header">📋 Filtered Data Preview</div>', unsafe_allow_html=True)
st.dataframe(
    filtered_df[['title', 'type', 'country', 'release_year', 'rating', 'duration']].head(10),
    use_container_width=True
)

# SQL Query Section
st.markdown('<div class="section-header">💻 Custom SQL Query</div>', unsafe_allow_html=True)
query = st.text_area("Enter your SELECT query:", "SELECT * FROM netflix LIMIT 10", height=100)
if st.button("🚀 Execute Query"):
    try:
        engine = get_connection()
        result_df = pd.read_sql_query(query, engine)
        st.success(f"✅ Query executed successfully! Returned {len(result_df)} rows.")
        st.dataframe(result_df, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Query failed: {e}")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>🎬 Netflix Analytics Dashboard | Built with Streamlit, MySQL & Plotly</p>
        <p>📊 Real-time data visualization with interactive filters</p>
    </div>
""", unsafe_allow_html=True)