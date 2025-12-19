import solara

@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 台北GIS儀表板
        歡迎來到台北GIS儀表板！這個應用程式展示了台北市的地理資訊系統（GIS）功能，讓您可以探索城市的各種地理數據和地圖視覺化。
        """
        solara.Markdown(markdown)

    # ✅ 修正 1：確認網址是乾淨的 Raw 連結
    # 你的圖片檔名是 taipei.jpg
    image_url = "https://raw.githubusercontent.com/Jie-Yan094/1105Solara-webmap-app/main/taipei.jpg"
    
    solara.Markdown("## 台北行政圖")
    
    with solara.Row(gap="16px", style={"flex-wrap": "wrap", "justify-content": "center"}):
        
        with solara.Div(style={
            "flex": "1 1 48%",
            "min-width": "300px",
            "max-height": "400px",
            "overflow": "hidden",
            "border-radius": "8px",
            "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.1)",
        }):
            # ✅ 修正 2：直接使用 image_url，不要再用 f-string 加字了
            solara.Image(
                image_url, 
                width="100%"
            )