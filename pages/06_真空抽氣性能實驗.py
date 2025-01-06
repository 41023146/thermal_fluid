import streamlit as st


st.title("實驗六. 真空抽氣性能實驗")

st.divider()

st.markdown("### 壹.實驗目的")
st.write("本實驗旨在深入研究真空系統的運行特性，通過真空幫浦的性能測試，了解真空腔體內的壓力變化過程以及各種影響因素。本實驗的核心任務包括評估真空幫浦的抽氣速率、終極壓力以及系統的氣導效能，並探討壓力變化曲線與抽氣效率之間的關係。")
st.write("在實驗過程中，首先組裝真空系統，並進行密封性檢測，確保真空腔體及管路系統無洩漏問題。通過逐步降低系統內壓力，記錄壓力下降過程中的數據，並繪製壓力下降曲線（Pump Down Curve）。此外，實驗會調整角閥和洩氣閥的開度，研究系統在不同條件下的抽氣和洩氣性能，並利用這些數據計算等效氣導（Conductance）。這些測試不僅幫助理解系統內壓力變化的動態過程，也有助於評估不同條件下的最佳操作參數。")
st.write("實驗的另一重點是分析真空幫浦的性能指標，包括抽氣速率的穩定性和達到終極壓力所需的時間。這些數據可以用來比較不同類型真空幫浦的性能優劣，從而為選擇適合特定應用的幫浦提供參考。")
st.write("實驗結果具有廣泛的應用價值，例如在半導體製造、光電產業和科學研究中的真空技術設計與優化。特別是，這些數據可用於提高真空乾燥、薄膜沉積和氣相製程等操作的效率與精確性。同時，透過本實驗，參與者能更加系統性地掌握真空技術的基本原理，理解壓力、體積與流速之間的數學關係，並運用於實際工程設計中。")
st.write("總體來說，此實驗不僅是一次性能測試，更是一個學習和理解真空技術在高科技應用中關鍵作用的過程，對於真空系統的優化與創新設計具有重要意義")
st.divider()

st.markdown("### 貳.	儀器與設備")
st.image("images/ex6_01.png")
st.image("images/ex6_02.png")
st.image("images/ex6_03.png")
st.divider()

st.markdown("### 參.	實驗原理")
st.write("""
(一) 真空幫浦抽氣原理 \n
真空幫浦之功能是將一特定空間之氣體抽除，使氣體密度降低，達到某一壓力狀態。但 是，氣體在真空系統中之流動特性隨壓力之不同而有很大差異，如表 1 所示。因此，對不同 壓力範圍必須依相對應之抽氣原理來設計不同型態幫浦。同時，針對特定抽氣要求，需組合 搭配不同性能與型態之真空幫浦來使用，才能達到有效又經濟之真空抽氣目的。圖 1 所示為 一真空系統基本架構，主要包括真空腔體、真空幫浦 ( 粗抽幫浦及高真空幫浦 )、真空計、抽 氣管路系統及壓力調節功能 ( 製程氣體供氣、清洗、壓力控制 ) 等。 真空幫浦之抽氣速率 (Pumping Speed) 係指幫浦進氣口處之容積流率大小，其單位為 L/s, m3 /hr 等型式。在穩定抽氣狀態時，可由氣流通量 (Throughput) Q 及壓力 P 來決定，亦即 S = Q/P。單位時間內通過一導通面積單元之氣體質量稱為質量流率 (Mass Flow Rate)，事實上與 氣流通量具有相同物理意義，但在真空技術中常以壓力及體積之乘積 PV 值，間接表示氣體 總質量 G。真空幫浦之抽氣量即進氣口處之氣流通量，其單位是 Torr•L/s。如果進氣口壓力為 定值，則氣流通量可寫成 Q = P × S。真空幫浦之抽氣量不同於抽氣速率，Q 之大小較具實際
""")
st.image("images/ex6_04.png")
st.write("""
物理意義：氣體密度高時，壓力大，若密度與溫度為定值，則 Q 與 S 成正比；但是，在高真空狀態下，氣體密度很稀薄，此時 Q 之大小較能表示真空幫浦真正性能，抽氣速率本身並不 足以完整顯示真空抽氣系統之工作效能。 \n
另一個常見的真空系統名詞為氣導 (Conductance, C)，氣導之特性包含： \n
(1) 其單位與抽氣速率相同； \n
(2) 氣導大小決定於管路幾何形狀及氣壓； \n
(3) 真空度高時，氣導與壓力無關。在中低真空度時，與壓力有密切關聯； \n
(4) 由於真空系統中有許多孔、閥、管⋯等元件，會造成氣導降低，因此真空幫浦實際有效抽 氣速率 (Seff) 可由下式求得
""")
st.image("images/ex6_05.png")
st.write("氣導大小可由 Q = C(P1-P2) 關係式求得，在相同壓差下，氣流通量與氣導成正比。所以， 參考表 1 中氣導的計算式可知，選擇真空管路之原則是長度 (L) 要短，直徑 (D) 要大。")
st.image("images/ex6_06.png",caption="真空氣流分類")
st.divider()
st.markdown("### 肆.	實驗項目")
st.write("""
1.	真空系統組裝：\n
    (1)以擦拭紙沾酒精將所有O-ring及封合面清潔乾淨，並檢察有無損傷。\n
    (2)依照示意圖與實體圖將所有KF25接頭包括O-ring鎖緊(要對準不可太用力，避免將O-ring壓傷)，完成真空系統組裝。\n
2.	簡易測漏方法：\n
    (1)開啟真空幫浦，並注意真空計之讀值，若壓力一直無法下降，則立刻關閉真空幫浦電源。\n
    (2)檢查各個接頭有無確實鎖好，必要時拆開接頭重新鎖緊。\n
    (3)當真空幫浦能順暢運作後，觀察真空計之讀值能一直往下降，表示抽真空功能正常。\n
    (4)關閉真空幫浦電源準備進行後續實驗。\n
3.	真空壓力量測：\n
    (1)將真空幫浦進氣口位置之NW25 Angle valve開度調整為1/4。注意Vent valve是否確實關緊。\n
    (2)準備好可以計時之計時器，啟動真空幫浦，每5秒紀錄真空計之壓力讀數與時間，總計錄時間為10分鐘。\n
    (3)重複(2)之動作，直到讀數不再變化(約20分鐘後達到穩態後)為止。記錄下最後壓力讀數，此為終極壓力。\n
    (4)將真空幫浦關閉，接著打開Vent valve讓腔體內外壓力達到平衡為止。此時真空計讀數應為1atm(760Torr)左右。\n
    (5)調整NW25 Angle valve開度調整為其他開度，並重複上述步驟進行實驗。注意Vent valve是否確實關緊。\n
    (6)完成後關閉真空幫浦，接著打開Vent valve讓腔體內外壓力達到平衡為止。\n
4.	Venting實驗：\n
    (1)將真空幫浦進氣口位置之NW25 Angle valve開度調整為全開。注意Vent valve是否確實關緊。\n
    (2)啟動真空幫浦，將腔體壓力抽至終極壓力(應與上一實驗一致)。\n
    (3)將NW25 Angle valve關閉，接著關掉真空幫浦。將Vent valve開度調整為1/4，每5秒紀錄真空計之壓力讀數與時間，直到讀數不再變化(達到穩態後)為止。\n
    (4)將Vent valve關閉，接著將NW25 Angle valve全開，之後將真空幫浦打開，將腔體壓力抽至終極壓力(應與上一實驗一致)。\n
    (5)重複(3)-(4)動作，完成其他調整Vent valve開度調整。\n
    (6)完成後關閉真空幫浦，接著打開Vent valve讓腔體內外壓力達到平衡為止。
""")
st.markdown("### 伍.	實驗結果")
st.image("images/ex6_07.png")
st.image("images/ex6_08.png")
# 在這裡添加實驗一的具體內容，如圖表、數據等
