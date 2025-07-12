import folium

# Create a base map centered on Rome
rome_coords = [41.8902, 12.4922]
map_rome = folium.Map(location=rome_coords, zoom_start=12, tiles="CartoDB positron")

# List of catacombs: (Name, [Latitude, Longitude], Description)
catacombs = [
    (
        "Catacombs of San Sebastiano",
        [41.8466, 12.5113],
        "One of the earliest and most accessible Christian burial sites, named after Saint Sebastian."
    ),
    (
        "Catacombs of San Callisto",
        [41.8555, 12.5106],
        "The largest and most important catacomb in Rome, containing the Crypt of the Popes."
    ),
    (
        "Catacombs of Priscilla",
        [41.9292, 12.5112],
        "Known as the 'Queen of the Catacombs' for its historical significance and frescoes."
    ),
    (
        "Catacombs of Domitilla",
        [41.8483, 12.5042],
        "One of the oldest catacombs, with a subterranean basilica and extensive tunnels."
    ),
    (
        "Catacombs of Sant'Agnese",
        [41.9158, 12.5234],
        "Dedicated to Saint Agnes, located near the basilica built in her honor."
    )
]

# Add each catacomb to the map
for name, coords, description in catacombs:
    folium.Marker(
        location=coords,
        popup=f"<b>{name}</b><br>{description}",
        tooltip=name,
        icon=folium.Icon(color='darkred', icon='info-sign')
    ).add_to(map_rome)

# Save map to HTML
map_rome.save("rome_catacombs_map.html")
