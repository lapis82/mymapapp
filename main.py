import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="Rome Catacombs Map", layout="wide")

# 제목 및 설명
st.title("🕯️ 로마의 주요 카타콤베 지도")
st.markdown("""
로마의 지하 묘지, 카타콤베(catacombs)는 초기 기독교 공동체의 역사와 예술을 간직한 중요한 유적지입니다.  
아래 지도에서 위치를 확인하고, 오른쪽의 드롭다운에서 상세 정보를 살펴보세요.
""")

# 카타콤베 데이터
catacomb_info = {
    "San Sebastiano": {
        "coords": [41.8466, 12.5113],
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/San_Sebastiano_fuori_le_mura_Facade.jpg/800px-San_Sebastiano_fuori_le_mura_Facade.jpg",
        "desc": "성 세바스티아노의 순교 장소로 여겨지며, 지하 묘지와 고대 바실리카가 함께 있는 초기 기독교 순례지입니다.",
        "url": "https://www.catacombe.org/en/"
    },
    "San Callisto": {
        "coords": [41.8555, 12.5106],
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/CatacombeSanCallisto01.jpg/800px-CatacombeSanCallisto01.jpg",
        "desc": "가장 크고 유명한 카타콤베로 교황들의 묘지인 'Crypt of the Popes'가 있습니다.",
        "url": "https://www.catacombe.roma.it/en/"
    },
    "Priscilla": {
        "coords": [41.9292, 12.5112],
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Catacombe_di_Priscilla_-_cubicolo_della_velatio.jpg/800px-Catacombe_di_Priscilla_-_cubicolo_della_velatio.jpg",
        "desc": "초기 기독교 벽화가 잘 보존된 '카타콤베의 여왕'으로 불립니다.",
        "url": "https://www.catacombepriscilla.com/"
    },
    "Domitilla": {
        "coords": [41.8483, 12.5042],
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Italy.Rome.Catacombs.jpg/800px-Italy.Rome.Catacombs.jpg",
        "desc": "가장 오랜 역사를 지닌 카타콤베 중 하나로, 지하 바실리카와 초기 무덤이 보존되어 있습니다.",
        "url": "https://www.catacombe.domitilla.it/"
    },
    "Sant'Agnese": {
        "coords": [41.9158, 12.5234],
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sant'Agnese_fuori_le_mura.jpg/800px-Sant'Agnese_fuori_le_mura.jpg",
        "desc": "순교자 성 아그네스를 기리는 이 카타콤베는 조용하고 아름답게 보존된 유적입니다.",
        "url": "https://www.santagnese.org/catacombe/"
    }
}

# 지도 생성
rome_coords = [41.8902, 12.4922]
map_rome = folium.Map(location=rome_coords, zoom_start=12, tiles="CartoDB positron")

# 마커 추가
for name, data in catacomb_info.items():
    folium.Marker(
        location=data["coords"],
        popup=name,
        tooltip=name,
        icon=folium.Icon(color='darkred', icon='info-sign')
    ).add_to(map_rome)

# 지도 표시
st_folium(map_rome, width=1000, height=600)

# 선택 박스
selection = st.selectbox("📍 카타콤베를 선택하세요", list(catacomb_info.keys()))

# 선택된 카타콤베 정보 표시
info = catacomb_info[selection]
st.subheader(f"🧾 {selection}")
st.image(info["img"], use_column_width=True)
st.markdown(info["desc"])
st.markdown(f"🔗 [공식 웹사이트 바로가기]({info['url']})", unsafe_allow_html=True)
