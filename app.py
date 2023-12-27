import streamlit as st
import folium
from streamlit_folium import folium_static
st.set_page_config(layout="wide")
# Sample data
districts = ["District A", "District B", "District C"]
corredors = ["Corridor 1", "Corridor 2", "Corridor 3"]
cooperativas = ["Coop 1", "Coop 2", "Coop 3"]
rotas = ["Rota 1", "Rota 2", "Rota 3"]

# Function to filter data based on selected filters
def filter_data(selected_district, selected_corredor, selected_cooperativa, selected_rota):
    # Add your logic to filter data based on selected filters
    # For now, let's just return the selected filters
    return selected_district, selected_corredor, selected_cooperativa, selected_rota

# Sample map centered around a location
map_center = [-23.5505, -46.6333]

# Function to display routes on the map
def display_routes(selected_district, selected_corredor, selected_cooperativa, selected_rota):
    # Use the selected filters to get the filtered data
    filtered_data = filter_data(selected_district, selected_corredor, selected_cooperativa, selected_rota)

    # Clear existing routes on the map
    mymap = folium.Map(location=map_center, zoom_start=12)

    # Add logic to display routes and bus stops on the map based on filtered_data
    # For now, let's just add a sample route
    route_points = [(-23.55, -46.63), (-23.56, -46.64), (-23.57, -46.65)]
    folium.PolyLine(route_points, color="blue", weight=2.5, opacity=1).add_to(mymap)

    # Display the map with updated routes using folium_static
    folium_static(mymap, width=1200, height=800)  # Adjust width and height as needed

# Streamlit app layout
st.title("Rede Estrutural Metropolitano")
st.sidebar.header("Filters")

# Add filter widgets to the sidebar
selected_district = st.sidebar.selectbox("Select Area", districts)
selected_corredor = st.sidebar.selectbox("Select Corredor", corredors)
selected_cooperativa = st.sidebar.selectbox("Select Cooperativa", cooperativas)
selected_rota = st.sidebar.selectbox("Select Rota", rotas)
selected_cooperativa = st.sidebar.selectbox("Select Tipo de Rota", cooperativas)


# Display routes on the map based on selected filters
display_routes(selected_district, selected_corredor, selected_cooperativa, selected_rota)
