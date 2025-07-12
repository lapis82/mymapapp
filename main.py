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
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/San_Sebastiano_fuori_le_mura_Facade.jpg/320px-San_Sebastiano_fuori_le_mura_Facade.jpg" width="100%">
        <p>
        📍 <b>Via Appia Antica</b><br>
        성 세바스티아노의 순교 장소로 여겨지며, 지하 묘지와 고대 바실리카가 함께 있는 초기 기독교 순례지입니다.
        <br>
        🔗 <a href="https://www.catacombe.org/en/" target="_blank">공식 웹사이트</a>
        </p>
        """
    ),
    (
        "San Callisto",
        [41.8555, 12.5106],
        """
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/CatacombeSanCallisto01.jpg/320px-CatacombeSanCallisto01.jpg" width="100%">
        <p>
        📍 <b>Via Appia Antica</b><br>
        가장 크고 유명한 카타콤베로 교황들의 묘지인 'Crypt of the Popes'가 있습니다.
        <br>
        🔗 <a href="https://www.catacombe.roma.it/en/" target="_blank">공식 웹사이트</a>
        </p>
        """
    ),
    (
        "Priscilla",
        [41.9292, 12.5112],
        """
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Catacombe_di_Priscilla_-_cubicolo_della_velatio.jpg/320px-Catacombe_di_Priscilla_-_cubicolo_della_velatio.jpg" width="100%">
        <p>
        📍 <b>Via Salaria</b><br>
        초기 기독교 벽화가 잘 보존된 '카타콤베의 여왕'으로 불립니다.
        <br>
        🔗 <a href="https://www.catacombepriscilla.com/" target="_blank">공식 웹사이트</a>
        </p>
        """
    ),
    (
        "Domitilla",
        [41.8483, 12.5042],
        """
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Italy.Rome.Catacombs.jpg/320px-Italy.Rome.Catacombs.jpg" width="100%">
        <p>
        📍 <b>Via delle Sette Chiese</b><br>
        가장 오랜 역사와 함께 지하 바실리카가 보존된 복합 유적입니다.
        <br>
        🔗 <a href="https://www.catacombe.domitilla.it/" target="_blank">공식 웹사이트</a>
        </p>
        """
    ),
    (
        "Sant'Agnese",
        [41.9158, 12.5234],
        """
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sant'Agnese_fuori_le_mura.jpg/320px-Sant'Agnese_fuori_le_mura.jpg" width="100%">
        <p>
        📍 <b>Via Nomentana</b><br>
        어린 순교자 성녀 아그네스를 기리는 곳으로, 지하묘지와 바실리카가 함께 있습니다.
        <br>
        🔗 <a href="https://www.santagnese.org/catacombe/" target="_blank">공식 웹사이트</a>
        </p>
        """
    )
]

# 마커 추가
for name, coords, desc in catacombs:
    html = f"""
    <div style="width: 300px; max-height: 260px; overflow-y: auto; font-size: 14px;">
        <strong>{name}</strong><br>
        {desc}
    </div>
    """
    popup = folium.Popup(html, max_width=350)
    
    folium.Marker(
        location=coords,
        popup=popup,
        tooltip=name,
        icon=folium.Icon(color='darkred', icon='info-sign')
    ).add_to(map_rome)



# 마커 추가
for name, coords, desc in catacombs:
    html = f"""
    <div style="width: 300px; max-height: 200px; overflow-y: auto; font-size: 14px;">
        <strong>{name}</strong><br>
        {desc}
    </div>
    """
    popup = folium.Popup(html, max_width=350)
    
    folium.Marker(
        location=coords,
        popup=popup,
        tooltip=name,
        icon=folium.Icon(color='darkred', icon='info-sign')
    ).add_to(map_rome)




# Streamlit에 지도 표시
st_data = st_folium(map_rome, width=1000, height=600)
