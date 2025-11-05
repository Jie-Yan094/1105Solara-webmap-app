import solara
import leafmap.maplibregl as leafmap

def create_map():

    m = leafmap.Map(
        center=[121.55555, 25.08722],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("CartoDB.DarkMatter")
    m.add_geojson("https://bdon.github.io/taipei_mrt/", layer_name="w")

    return m

@solara.component
def Page():
    m = create_map()
    return m.to_solara()