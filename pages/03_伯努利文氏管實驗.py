import streamlit as st

st.title("實驗三.伯努利文氏管實驗")

st.divider()

st.markdown("### 壹.實驗目的")
st.write("流體力學中，伯努利定理描述流體沿著一條穩定、非粘滯性，不可壓縮的流線移動，其壓力、速度及高度的變化形成一關係式，此一關係式對於流體力學中許多運動的特性做了合理的解釋，例如：棒球的運動軌跡，飛機機翼的升力等。藉由此實驗來檢驗伯努利方程式中能量守恆的概念，如此對於流體運動中速度與壓力的關係能有較深刻的認識。")
st.write("本標準型流量產生裝置，係依據AMCA210-16規範之標準所建立，此AMCA210-16規範為工業界所採用之標準風量量測單元，而本設備之核心架構就是以此一基礎上所建立之標準風量產生器。")
st.write("流體力學中，伯努利方程式描述流體沿著一條穩定、非粘滯性及不可壓縮的流線移動，其壓力、速度及高度的變化形成一關係式，此一關係式對於流體力學中許多運動的特性做了合理的解釋，例如：棒球的運動軌跡，飛機機翼的昇力等。而本裝置的目的為幫助致力於流體力學學習的學員，藉由文氏管的壓力與速度的量測，來檢驗伯努利方程式能量守恆與質量守恆的概念，如此對流體運動中速度與壓力的關係有較深刻的認識與了解。另外，本裝置所使用的標準風量產生裝置，係根據國際規範AMCA 210-16製造而得，其精確度的可在3 % 以內，其結構及流量計算原理與目前廣泛應用於工業界風扇及系統阻抗測試之AMCA風洞是一致的，而學員透過實際量測，可對風洞流量量測的原理與方法做深入的了解。")
st.write("因此，學習者若能活用部份流體及熱傳遞學裡的知識，並且按部就班學習、測試及體會，同時這個架構是IT產業界在研發及實際生產中正在使用的工業技術，將使學習者產學的認知關係更加密切，必能裨益不少。")
st.divider()

st.markdown("### 貳.	儀器與設備")
st.image("images/ex3_01.png")
st.image("images/ex3_02.png")
st.divider()
st.markdown("#### 一.乾溼球溫度計")
st.image("images/ex3_03.png")
st.image("images/ex3_04.png")
st.divider()
st.markdown("#### 二.控制箱與操作面板")
st.image("images/ex3_05.png")
st.image("images/ex3_06.png")
st.divider()
st.markdown("#### 三.文氏管測試件")
st.image("images/ex3_07.png")
st.image("images/ex3_08.png")
st.divider()
st.markdown("#### 四.準流量產生裝置")
st.image("images/ex3_09.png")
st.image("images/ex3_10.png")
st.divider()
st.markdown("#### 五.標準流量產生器用AMCA噴嘴")
st.image("images/ex3_11.png")
st.image("images/ex3_12.png")
st.divider()
st.markdown("#### 六.水柱壓力計")
st.image("images/ex3_13.png")
st.image("images/ex3_14.png")
st.divider()
st.markdown("#### [實驗儀器規格與尺寸]")
st.write("""
1.標準流量產生裝置，流量精度3%以內，得做為流體實驗室之流量基準。 \n
2.噴嘴法標準流量計，使用AMCA210 Fig.15構造，流量範2.31~85.9 CFM。\n
    2.1 共用腔體：φ150 mm \n
    2.2 共用量測裝置：乾球溫度Td、濕球溫度Tw、腔室溫度Tc、大氣壓力Pb、腔室靜壓Ps、噴嘴前後壓差P56。 \n
    2.3 數位儀表顯示數值 \n
    2.4 差壓P56量測儀錶，做差壓顯示。 \n
        A. 壓力轉換器精度±0.25%以內。 \n
        B. 壓力差範圍：0 ~ 127 mmAq。 \n
        C. 附壓差轉換器原廠報告。
""")
st.image("images/ex3_15.png")
st.write("""
3.精確流量產生器以4組可交換之噴嘴機構及吹氣鼓風機，於管路中形成氣流。 \n
    3.1 於文氏管中間距位置量測壓力，壓力孔位置10組以上。 \n
    3.2 附20水柱壓力計，有效水柱高480 mm。 \n
    3.3 選配LW-9402差壓量測模組，作模型任二壓力孔之差壓顯示。 \n
        a. 壓力轉換器精度±0.25%以內。 \n
        b. 壓力差範圍：0~127 mmAq。 \n
        c. 差壓力數字顯示器及RS-485通訊介面(未外接)。 \n
    3.4 調節變頻器調節流量。 \n
4.文氏管入口角度有四種，45∘、22.5∘、10∘及4.2∘。\n 
5.附操作檯：1.2 (L) X 0.7 (D) X 1.6 (H) m。 \n
6.使用電力：AC220V，單相，5A。
""")
st.divider()
st.markdown("### 參.實驗原理")
st.write("""
AMCA (Air Movement and Control Association) 風量計算原理\n
AMCA-210為美國空氣移動控制協會訂立之標準，符合美國國家標準。 本項標準風量產生裝置的所有外觀、尺寸及量測硬體，均依據美國空氣移控協會標準AMCA 210-16規範的結構設計製造，規範中規定了風洞腔體相關尺寸、量測點位置、整流網（settling means）配置原則等。
""")
st.image("images/ex3_16.png",caption="AMCA 210-16 規範示意圖")
st.write("其中，對於關鍵元件─噴嘴(Nozzle)的設計，也有其依據的準則，其尺寸、表面粗糙度都受到規範的限制。噴嘴為一特殊設計的漸縮管，具有較高且穩定的Cd值，在不同的雷諾數狀態下，可達0.95 ~ 0.99，表示流體通過時會有較小的摩擦損失，可有效用做流量計算。")
st.image("images/ex3_17.png",caption="MCA 210-16 規範噴嘴規格示意圖")
st.image("images/ex3_18.png",caption="不同規格噴嘴之流量係數與雷諾數的關係")
st.write("噴嘴流量計屬於差壓式流量計，進行流量量測時，首先需要得到噴嘴喉部的速 度。在流體水平流動而不考慮位能變化的情況下，符合伯努利方程式(Bernoulli’s equation)的公式可寫為：")
st.image("images/ex3_19.png")
st.write("""
ρair：空氣密度，與當時環境之溫度、濕度及大氣壓力有關。 \n
P1：噴嘴上游壓力；U1：噴嘴上游速度 \n
P2：噴嘴下游壓力；U2：噴嘴下游(喉部)速度 \n
由於噴嘴上游腔室可視為均壓型壓力腔室，其流體速度遠小於喉部速度，故 \n
""")
st.image("images/ex3_20.png")
st.write("根據符合質量守恆的連續方程式(Continuous equation)，通過噴嘴喉部的理論 流量為：")
st.image("images/ex3_21.png")
st.write("由於風洞設計係依AMCA 210-16之規範條件設計，則Cd值計算可參考規範 中之經驗公式，其為雷諾數的函數，如下：")
st.image("images/ex3_22.png")
st.write("藉由以上公式推導，可以了解此流量產生裝置的計算方法。")
st.divider()

st.markdown("### 軟體計算流量範例")
st.write("本裝置附有AMCA 210軟體，手動輸入參數值後，自動計算出該狀態下的標準 流量。")
st.image("images/ex3_23.png")
st.write("""
需要手動輸入的參數值如下(紅色虛線框所示)： \n
1. 環境乾球溫度Td \n
2. 環境濕球溫度 Tw \n
3. 腔室溫度 T5 (T5=T8) \n
4. 大氣壓力Pb \n
5. 噴嘴上下游差壓 P56 \n
6. 腔室靜壓 P5 (P5=P8+P56) \n
7.標準流量產生裝置腔室內徑D5 (=150mm) \n
8. 使用噴嘴直徑D6 \n
輸入完成後，自動計算出以CFM及CMM單位表示的流量(藍色虛線框所示)。
""")
st.divider()

st.markdown("### 手動計算流量範例")
st.image("images/ex3_24.png")
st.write("""
輸入參數如下： \n
 Td=23.2°C  \n
 Tw=18.6°C  \n
 T5=T8=22.4°C  \n
 Pb=741.0mmHg \n
 P56=115.5mmAq(噴嘴差壓) \n
 P5腔室壓力=272.5mmAq(P5=P56+P8) \n
 腔式寬度D=150mm \n
 噴嘴尺寸Dn=24.02mm \n
試算當時流量為多少？ \n
計算步驟：
""")
st.markdown("#### 1.先求出Atmospheric Air Density")
st.image("images/ex3_25.png")
st.divider()
st.markdown("#### 2.計算Chamber Air Density")
st.image("images/ex3_26.png")
st.divider()
st.markdown("#### 3.計算Air Viscosity")
st.image("images/ex3_27.png")
st.divider()
st.markdown("#### 4.Alpha Ratio")
st.image("images/ex3_28.png")
st.divider()
st.markdown("#### 5.Expansion Factor")
st.image("images/ex3_29.png")
st.divider()
st.markdown("#### 6.Reynolds Number & Discharge Coefficient")
st.image("images/ex3_30.png")
st.image("images/ex3_31.png")
st.divider()
st.markdown("#### 7.最後Flow Rate for Chamber Nozzles")
st.image("images/ex3_32.png")
st.divider()

st.markdown("### 肆.實驗步驟")
st.markdown("##### 測試件安裝與量測")
st.image("images/ex3_33.png")
st.image("images/ex3_34.png")
st.image("images/ex3_35.png")
st.image("images/ex3_36.png")
st.divider()
st.markdown("##### 標準流量產生裝置操作")
st.image("images/ex3_37.png")
st.image("images/ex3_38.png")
st.divider()
st.markdown("##### 多管水柱壓力計充填與排放充填液體操作步驟")
st.image("images/ex3_39.png")
st.image("images/ex3_40.png")
st.image("images/ex3_41.png")
st.image("images/ex3_42.png")
st.markdown("### 伍.	實驗結果")

st.image("images/ex3_44.png",caption="操作面板對應之參數")
st.image("images/ex3_45.png",caption="計算流量之範例")
st.image("images/ex3_46.png",caption="F=0之操作面板")
st.image("images/ex3_47.png",caption="F=0軟體計算流量 (註:當P56輸入0之後軟體就會當機，因此沒有結果)")
st.image("images/ex3_48.png",caption="F=20.16之操作面板")
st.image("images/ex3_49.png",caption="F=20.16軟體計算流量")
st.image("images/ex3_50.png",caption="F=30.24之操作面板")
st.image("images/ex3_51.png",caption="F=30.24軟體計算流量")
st.image("images/ex3_52.png",caption="F=40.26之操作面板")
st.image("images/ex3_53.png",caption="F=40.26軟體計算流量")


st.image("images/ex3_43.png")







