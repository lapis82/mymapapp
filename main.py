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
    (
        "San Sebastiano",
        [41.8466, 12.5113],
        """
        📍 **Via Appia Antica, 남쪽 로마 외곽**  
        이 카타콤베는 성 세바스티아노의 순교 장소로 여겨지며, 초기 기독교 순례지였습니다.  
        지하 묘지 외에도 고대 바실리카와 기념비적 무덤이 함께 있습니다.
        """
    ),
    (
        "San Callisto",
        [41.8555, 12.5106],
        """
        📍 **Via Appia Antica, San Sebastiano 북쪽 인근**  
        가장 크고 중요한 카타콤베로, 약 20km의 터널에 50만 명이 매장되었으며,  
        그 중 16명의 교황이 '교황의 크립트'에 안치되어 있습니다.
        """
    ),
    (
        "Priscilla",
        [41.9292, 12.5112],
        """
        📍 **Via Salaria, 북쪽 외곽**  
        '카타콤베의 여왕'이라 불리며, 2~4세기 벽화가 잘 보존되어 있습니다.  
        특히 성모 마리아와 아기 예수를 묘사한 가장 초기의 기독교 미술이 발견된 곳입니다.
        """
    ),
    (
        "Domitilla",
        [41.8483, 12.5042],
        """
        📍 **Via delle Sette Chiese**  
        약 15km에 달하는 긴 터널을 자랑하며, 초대 교회 시기의 미술과 묘비가 잘 남아 있습니다.  
        지하 바실리카와 2세기 기독교 성도들의 무덤도 포함되어 있습니다.
        """
    ),
    (
        "Sant'Agnese",
        [41.9158, 12.5234],
        """
        📍 **Via Nomentana**  
        어린 순교자 성 아그네스를 기념하는 카타콤베로, 근처에 있는 아름다운 산타 아그네세 푸오리 레 무라 교회와 함께 방문할 수 있습니다.  
        벽화와 초기 무덤들이 조용히 보존되어 있습니다.
        """
    )
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
