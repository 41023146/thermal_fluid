import streamlit as st


st.markdown("# 熱流力實驗期末報告 ")
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("### 一、創新夾持裝置機械設計 ")
st.markdown("### 二、環境量測與控制裝置機械設計 ")
 
st.write(" ")
st.write(" ") 
st.markdown("##### 指導老師：周榮源 ")
st.markdown("##### 班級：四設四甲 ")
st.markdown("##### 組別：第六組")
st.markdown("##### 組員：")
st.markdown("##### 41023112 王啟騰 ")
st.markdown("##### 41023121 李承翰 ")
st.markdown("##### 41023134 林建維 ")
st.markdown("##### 41023146 洪偉陞 ")
st.markdown("##### 41023147 紀閔翔 ")
st.divider()
st.write("網頁網址：https://thermalfluid-2rxfjxddewzzec29qxtvka.streamlit.app/")
st.write("倉儲網址：https://github.com/41023146/thermal_fluid ")
st.divider()
st.markdown("##### 日期：中華民國　114年01月06日")
st.divider()

st.markdown("## 一、概論")
st.markdown("### 主題一、創新夾持裝置機械設計 ")
st.write("""
1.整理各式(家)真空產生器的特點  \n
2.整理各式(家)真空產生器的產品與功能介紹 \n
""")
st.image("images/ex7_01.png",width=800)
st.divider()
st.markdown("### 主題二、環境量測與控制裝置機械設計")
st.write("""
1.整理各式(家)散熱器元件或模組的特點 \n
2.整理各式(家)散熱器元件或模組的產品與功能介紹 \n
熱導材料的選擇 \n
    鋁合金：輕量化，熱導率適中。 \n
    純銅：高熱導率，但較重且昂貴。 \n
1.熱阻分析 \n
    使用熱傳公式估算熱阻： Rth=Rconduction+RconvectionR_{th} = R_{conduction} + R_{convection}Rth=Rconduction+Rconvection\n 
    計算每層材料及散熱鰭片的熱傳效率。\n 
2.鰭片設計 \n
    鰭片數量與間距：增加表面積提升散熱。\n
    鰭片厚度：根據流體動力學平衡重量與效能。
""")
st.image("images/ex7_02.png",width=800)
st.divider()
st.markdown("## 二、原理與設計方法")
st.markdown("### 主題一、創新夾持裝置機械設計 ")
st.write("1.整理真空產生器設計與要求規範")
st.image("images/ex7_03.png",caption="鑽頭尺寸：3mm鑽頭刃 長約25mm6mm鑽頭刃長約40mm9mm鑽頭刃長約 55mm 11.5mm(for快速接頭攻牙；深度需大於10mm)",width=800)
st.divider()

st.write("2.整理真空產生器設計方法 ")
st.image("images/ex7_04.png", width=800)
st.divider()
st.write("3.依據原理與工件大小之零組件設計圖 ")
st.image("images/ex7_05.png",width=800)
st.image("images/ex7_06.png",caption="實體圖" ,width=600)
st.divider()
st.markdown("### 主題二、環境量測與控制裝置機械設計" )
st.write("1.整理散熱器設計與要求規範 ")
st.image("images/ex7_07.png",width=800)
st.divider()
st.write("2.整理散熱器設計方法 ")
st.image("images/ex7_08.png",width=800)
st.divider()
st.write("3.依據原理與工件大小之零組件設計圖")
st.image("images/ex7_09.png",width=800)
st.divider()
st.markdown("## 三、	實驗量測與數據分析")
st.markdown("### 主題一、創新夾持裝置機械設計")
st.write("""
1.依照Excel檔進行設計參數計算 \n
2.詳細列出軟體分析之過程(CAD模型、條件、材料常數、計算方法、其他) 
""")
st.image("images/ex7_10.png",width=800)
st.image("images/ex7_40.png",width=800)
st.divider()
st.write("1.1匯入圖檔")
st.image("images/ex7_11.png",width=800)
st.divider()
st.write("1.2設定k-epsilon(2eqn)")
st.image("images/ex7_12.png",width=800)
st.divider()
st.write("1.3設定空氣")
st.image("images/ex7_13.png",width=800)
st.divider()
st.write("1.4設定速度")
st.image("images/ex7_14.png",width=800)
st.divider()
st.write("1.5設定初始化")
st.image("images/ex7_15.png",width=800)
st.image("images/ex7_16.png",width=800)
st.image("images/ex7_17.png",width=800)
st.divider()
st.markdown("### 主題二、環境量測與控制裝置機械設計")
st.write("""
1.依照Excel檔進行設計參數計算 \n
2.詳細列出軟體分析之過程(CAD模型、條件、材料常數、計算方法、其他) 
""")
st.image("images/ex7_18.png",width=800)
st.divider()
st.write("2.1 開啟ansys熱傳分析")
st.image("images/ex7_19.png",width=800)
st.divider()
st.write("2.2 導入模型")
st.image("images/ex7_20.png",width=800)

st.image("images/ex7_21.png",width=800)
st.divider()
st.write("2.3 設置網格")

st.image("images/ex7_22.png",width=800)
st.divider()
st.write("2.4 設置邊界條件")
st.image("images/ex7_23.png",width=800)
st.image("images/ex7_24.png",width=800)
st.image("images/ex7_25.png",width=800)
st.image("images/ex7_26.png",width=800)
st.image("images/ex7_27.png",width=800)
st.write("""
2.5 求解 \n
2.6 查看結果
""")
st.image("images/ex7_28.png",width=800)
st.divider()
st.markdown("### 主題三、bladeless wind turbine結構設計(僅Fluent模擬) ")
st.write("1.詳細列出軟體分析之過程(CAD模型、條件、材料常數、計算方法、其他) ")
st.image("images/ex7_30.png",width=800)
st.image("images/ex7_31.png",width=800)
st.image("images/ex7_29.png",width=800)
st.divider()
st.markdown("## 四、結果與討論")
st.markdown("### 主題一、創新夾持裝置機械設計")
st.write("""
 1.依照Excel檔建立真空產生器與周邊3D設計圖(零件、組合、爆炸) \n
 2.依照Excel檔建立真空產生器計算書(公式法) \n
 3.繪圖並討論數值模擬結果及計算書結果與數值模擬(CAE法)之誤差? \n
 4.繪圖並討論實驗測試結果及可能誤差大小與原因? 
""")
st.image("images/ex7_32.png",width=800)
st.image("images/ex7_33.png",width=800)
st.write("在電腦模擬之下，數據稍微跟想像的不太一樣，有可能是加工導致的誤差，所以在實驗前以及加工前都要把這些變數都考慮進去。")
st.write("實際測試結果(固體測試、不規則物體測試、大荷重測試、袋體測試) ")
st.image("images/ex7_34.png",width=800)
st.image("images/ex7_35.png",width=800)
st.write("我們這組工件吸力不管吸袋體或大荷重的東西都非常牢固，設計的不錯。 ")
st.image("images/ex7_41.png",width=800)

st.divider()
st.markdown("### 主題二、環境量測與控制裝置機械設計 ")
st.write("""
 1.依照Excel檔建立散熱器與周邊3D設計圖(零件、組合、爆炸) \n
 2.依照Excel檔建立散熱器計算書(公式法) \n
 3.繪圖並討論數值模擬結果及計算書結果與數值模擬(CAE法)之誤差? \n
 4.繪圖並討論實驗測試結果及可能誤差大小與原因? 
""")
st.image("images/ex7_37.png",width=800)
st.write("""
電腦模擬數據因假設理想條件，無法反映實際測量中受環境影響（如濕氣變化或散熱片狀態）的誤差。\n
因此，模擬與實測數據存在差異，提醒我們設計與實驗時需考量現實環境的變數，以更準確解釋結果。
""")
st.image("images/ex7_38.png",width=800)
st.write("測量結果證明裝置成功實現其預期功能，因為當底部的熱量傳遞到頂部時，溫度有所下降，展現了良好的散熱效果。")
st.image("images/ex7_39.png",width=800)
st.divider()
st.markdown("## 五、結論")
st.markdown("### 主題一、創新夾持裝置機械設計")
st.write("""
在本次課程中，本報告深入學習了真空原理的應用，並在老師的指導下進行了創新夾持裝置的設計。本報告通過實際操作，根據所學的知識進行了尺寸設計，並運用了程式模擬進行對比。\n
在進行實驗後，本報告發現實際測量結果與模擬數據之間有些微的誤差，但誤差範圍並不大。儘管如此，這一小部分的差異仍然讓本報告深刻反思並討論了可能的原因。本報告意識到，這些微小誤差可能源自於設計過程中的一些細節，例如模擬假設或某些現實條件的未完全考慮。\n
這次經歷讓本報告更加認識到設計過程中的細節對結果的影響。即使是微小的誤差，也能幫助本報告在未來的設計中更加謹慎，並注意到在模擬和實際操作之間的差異。通過這次反思，本報告對設計與模擬的關聯有了更深的理解，並學會如何在未來的工作中進一步減少這類誤差。\n
""")

st.markdown("### 主題二、環境量測與控制裝置機械設計")
st.write("""
這次散熱實驗讓本報告對散熱系統的運作機制有了更深入的了解。本報告通過測量散熱裝置頂部和底部的溫度，發現兩者之間確實存在一定的溫差，但這個溫差相對較小，顯示出散熱效果的均勻性較好。更令人滿意的是，實驗中的現實數據與本報告事先模擬之結果非常接近，這不僅證明了模擬數據的準確性，也讓本報告對散熱系統之設計更有信心。從實驗結果來看，散熱裝置能夠有效地分散熱量，避免了局部過熱，保證了設備的穩定運行。儘管如此，本報告也認識到仍有進一步優化的空間，比如增加散熱面積或選用更高效的材料來提升散熱效率。\n
總體而言，這次實驗不僅加深對散熱過程的理解，也看到理論與現實的契合，並啟發了在未來設計散熱系統時，如何進一步提高其性能。
""")
st.divider()
st.image("images/ex7_36.png",width=800)
st.divider()

st.image("images/ex7_42.png",width=800)
st.image("images/ex7_43.png",width=800)

