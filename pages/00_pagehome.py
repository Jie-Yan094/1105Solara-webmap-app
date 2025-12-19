import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 台北GIS儀表板
        歡迎來到台北GIS儀表板！這個應用程式展示了台北市的地理資訊系統（GIS）功能，讓您可以探索城市的各種地理數據和地圖視覺化。
        """
        solara.Markdown(markdown)

    repo_url = "https://raw.githubusercontent.com/Jie-Yan094/final_Penghu_coralreef/main/penghuDTM.csv"
    solara.Markdown("## 台北行政圖")
    
    # 使用 solara.Row 建立並排佈局，並設定間距和響應式換行
    # 這裡的樣式用於控制圖片的並排和響應式行為
    with solara.Row(gap="16px", style={"flex-wrap": "wrap", "justify-content": "center"}):
        
        with solara.Div(style={
            "flex": "1 1 48%",                      # 佈局：平均佔據 48% 寬度
            "min-width": "300px",                   # 佈局：最小寬度
            "max-height": "400px",                  # 容器最大高度
            "overflow": "hidden",                   # 確保圖片不超出容器
            "border-radius": "8px",                 # 視覺：圓角
            "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.1)", # 視覺：陰影
        }):
            # solara.Image 負責載入圖片，只設定寬度為 100%，高度自動按比例縮放
            solara.Image(
                image=f"{repo_url}pic_01.jpg",
                width="100%",
                # 移除 height 和 alt 參數以提高相容性
            )