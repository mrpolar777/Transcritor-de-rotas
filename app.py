import streamlit as st
import requests
from fpdf import FPDF
import xml.etree.ElementTree as ET

# Configurações da API do OpenRoute Service
API_KEY = '5b3ce3597851110001cf62480bd5baa8181e4537ae3992295a474af9'
BASE_URL = 'https://api.openrouteservice.org/geocode/reverse'

# Função para extrair coordenadas do arquivo KML
def extract_coordinates_from_kml(kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()
    coordinates = []
    
    for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
        coords = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates').text
        coords = coords.strip().split(',')
        lon, lat = float(coords[0]), float(coords[1])
        coordinates.append((lat, lon))
    
    return coordinates

# Função para obter o nome da rua a partir das coordenadas
def get_street_name(lat, lon):
    params = {
        'api_key': API_KEY,
        'point.lon': lon,
        'point.lat': lat,
        'size': 1
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx
        data = response.json()
        if data.get('features'):
            return data['features'][0]['properties'].get('name')
    except requests.exceptions.RequestException:
        return None
    except KeyError:
        return None
    return None

# Função para gerar o PDF com os nomes das ruas
def generate_pdf(street_names, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for name in street_names:
        pdf.cell(200, 10, txt=name, ln=True)
    
    pdf.output(filename)

# Interface da aplicação Streamlit
st.title("Transcrição de Rotas com Nomes de Ruas")

uploaded_file = st.file_uploader("Faça o upload do arquivo KML", type="kml")

if uploaded_file is not None:
    coordinates = extract_coordinates_from_kml(uploaded_file)
    street_names = []
    
    # Barra de progresso para processamento
    progress_bar = st.progress(0)
    total_coords = len(coordinates)
    
    for i, (lat, lon) in enumerate(coordinates):
        street_name = get_street_name(lat, lon)
        if street_name:
            street_names.append(street_name)
        
        # Atualiza a barra de progresso
        progress_bar.progress((i + 1) / total_coords)
    
    if street_names:
        # Gera o PDF com os nomes das ruas
        pdf_filename = "nomes_das_ruas.pdf"
        generate_pdf(street_names, pdf_filename)
        
        # Disponibiliza o PDF para download
        with open(pdf_filename, "rb") as f:
            st.download_button("Baixar PDF", f, file_name=pdf_filename)
    else:
        st.write("Nenhum nome de rua encontrado.")