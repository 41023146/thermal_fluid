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
1.依照Excel檔進行設計參數計算 
2.詳細列出軟體分析之過程(CAD模型、條件、材料常數、計算方法、其他) 
""")
st.image("images/ex7_10.png",width=800)
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
1.依照Excel檔進行設計參數計算 
2.詳細列出軟體分析之過程(CAD模型、條件、材料常數、計算方法、其他) 
""")
st.image("images/ex7_18.png",width=800)
st.write("2.1 開啟ansys熱傳分析")
st.image("images/ex7_19.png",width=800)
st.write("2.2 導入模型")
st.image("images/ex7_20.png",width=800)

st.image("images/ex7_21.png",width=800)
st.write("2.3 設置網格")

st.image("images/ex7_22.png",width=800)
st.write("2.4 設置邊界條件")
st.image("images/ex7_23.png",width=800)
st.image("images/ex7_24.png",width=800)
st.image("images/ex7_25.png",width=800)
st.image("images/ex7_26.png",width=800)
st.image("images/ex7_27.png",width=800)