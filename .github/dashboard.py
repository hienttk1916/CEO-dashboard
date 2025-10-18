import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


st.set_page_config(
    page_title="CEO Executive Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 CEO EXECUTIVE DASHBOARD")
st.markdown("---")


@st.cache_data
def get_data():
    return {
        'total_students': 160,
        'total_revenue': 45200000,
        'active_programs': 3,
        'completion_rate': 78.3,
        
        'revenue_trend': pd.DataFrame({
            'month': ['2025-01', '2025-02', '2025-03', '2025-04', '2025-05', '2025-06', '2025-07'],
            'revenue': [8000000, 12000000, 9500000, 11000000, 13000000, 10500000, 12500000]
        }),
        
        'top_programs': pd.DataFrame({
            'program': ['Cloud Computing', 'Web Development', 'AI Fundamentals', 'Cybersecurity', 'Data Science'],
            'revenue': [25000000, 20000000, 15000000, 12000000, 10000000]
        }),
        
        'geography': pd.DataFrame({
            'city': ['Hà Nội', 'Hồ Chí Minh', 'Hải Phòng', 'Đà Nẵng', 'Cần Thơ'],
            'students': [45, 38, 25, 22, 30]
        }),
        
        'teacher_performance': 72
    }

data = get_data()


st.subheader("📊 KPI Tổng quan")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Tổng Học Sinh",
        value=f"{data['total_students']}",
        delta="+12%"
    )

with col2:
    st.metric(
        label="Tổng Doanh Thu",
        value=f"{data['total_revenue']:,.0f} VND",
        delta="+18%"
    )

with col3:
    st.metric(
        label="Chương Trình Active",
        value=f"{data['active_programs']}",
        delta="+1"
    )

with col4:
    st.metric(
        label="Tỷ Lệ Hoàn Thành",
        value=f"{data['completion_rate']}%",
        delta="+5.2%"
    )

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Xu Hướng Doanh Thu")
    
    fig_line = px.line(
        data['revenue_trend'],
        x='month',
        y='revenue',
        labels={'revenue': 'Doanh thu (VND)', 'month': 'Tháng'},
        height=400
    )
    fig_line.update_traces(line=dict(color='#1f77b4', width=3))
    fig_line.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis_tickformat=',.0f'
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("🎯 Top Chương Trình")
    
    fig_bar = px.bar(
        data['top_programs'],
        x='revenue',
        y='program',
        orientation='h',
        labels={'revenue': 'Doanh thu (VND)', 'program': 'Chương trình'},
        height=400,
        color='revenue',
        color_continuous_scale='Blues'
    )
    fig_bar.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_tickformat=',.0f',
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    st.subheader("🗺️ Phân Bố Địa Lý")
    
    fig_geo = px.bar(
        data['geography'],
        x='city',
        y='students',
        labels={'students': 'Số học sinh', 'city': 'Thành phố'},
        height=400,
        color='students',
        color_continuous_scale='Viridis'
    )
    fig_geo.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    st.plotly_chart(fig_geo, use_container_width=True)

with col2:
    st.subheader("👨‍🏫 Hiệu Suất Giáo Viên")
    
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data['teacher_performance'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Utilization Rate (%)"},
        delta = {'reference': 65},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 75], 'color': "gray"},
                {'range': [75, 100], 'color': "darkgray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig_gauge.update_layout(height=400)
    st.plotly_chart(fig_gauge, use_container_width=True)


with st.sidebar:
    st.header("🎛️ Bộ Lọc")
    
    start_date = st.date_input(
        "Từ ngày",
        datetime(2025, 1, 1)
    )
    
    end_date = st.date_input(
        "Đến ngày",
        datetime(2025, 7, 31)
    )
    
    cities = st.multiselect(
        "Thành phố",
        ['Hà Nội', 'Hồ Chí Minh', 'Hải Phòng', 'Đà Nẵng', 'Cần Thơ'],
        default=['Hà Nội', 'Hồ Chí Minh', 'Hải Phòng', 'Đà Nẵng', 'Cần Thơ']
    )
    
    st.markdown("---")
    st.info()


st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "📊 CEO Executive Dashboard • Cập nhật: " + datetime.now().strftime("%Y-%m-%d %H:%M") +
    "</div>",
    unsafe_allow_html=True
)
