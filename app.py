import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header("Cuadro de mandos de vehículos")

# Cargar datos
vehicles = pd.read_csv("vehicles_us.csv")

show_hist = st.checkbox('Mostrar histograma del odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_hist:
    st.write('Histograma del odómetro')
    fig_odometer = px.histogram(vehicles, x="odometer", nbins=30)
    st.plotly_chart(fig_odometer, use_container_width=True, key="chart_odometer_checkbox")

if show_scatter:
    st.write('Gráfico de dispersión: precio vs odómetro')
    fig_scatter = px.scatter(vehicles, x='odometer', y='price', color='type')
    st.plotly_chart(fig_scatter, use_container_width=True, key="chart_scatter_checkbox")

# Gráfico 1
fig_price = px.histogram(vehicles, x='price', nbins=30, title='Distribución de precios')
st.plotly_chart(fig_price, key="chart_price")

# Gráfico 2
fig_type = px.histogram(vehicles, x='type', title='Cantidad de vehículos por tipo')
st.plotly_chart(fig_type, key="chart_type")

# Gráfico 3
fig_fuel = px.histogram(vehicles, x='fuel', title='Cantidad de vehículos por tipo de combustible')
st.plotly_chart(fig_fuel, key="chart_fuel")

