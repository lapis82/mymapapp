import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Rome Catacombs Map", layout="wide")

st.title("🕯️ 로마의 카타콤베 안내 지도")
st.markdown("""
로마에는 초기 기독교 공동체가 사용했던 지하 묘지인 카타콤베(catacombs)가 여러 곳에 흩어져 있습니다.  
아래 지도는 그 중 대표적인 유적들을 보여줍니다.
""")

# 지도 중심 좌표
rome_coords = [41.8902, 12.4922]
map_rome = folium.Map(location=rome_coords, zoom_start=12, tiles="CartoDB positron")

# 카타콤베 정보 (이름, 좌표, 설명)
catacombs = [
    ("산 세바스티아노(San Sebastiano)", [41.8466, 12.5113], "성 세바스티아노의 이름을 딴 초기 기독교 묘지"),
    ("산 칼리스토(San Callisto)", [41.8555, 12.5106], "교황들의 묘지가 있는 가장 크고 중요한 카타콤베"),
    ("프리스킬라(Priscilla)", [41.9292, 12.5112], "초기 벽화로 유명하며 '카타콤베의 여왕'이라 불림"),
    ("도미틸라(Domitilla)", [41.8483, 12.5042], "광대한 터널과 지하 바실리카를 포함"),
    ("산타 아그네스(Sant'Agnese)", [41.9158, 12.5234], "성녀 아그네스를 기리는 카타콤베"),
]

# 마커 추가
for name, coords, desc in catacombs:
    folium.Marker(
        location=coords,
        popup=f"<b>{name}</b><br>{desc}",
        tooltip=name,
        icon=folium.Icon(color='darkred', icon='info-sign')
    ).add_to(map_rome)

# Streamlit에 지도 표시
st_data = st_folium(map_rome, width=1000, height=600)
