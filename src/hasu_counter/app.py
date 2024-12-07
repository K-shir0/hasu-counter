import streamlit as st

# Google Tag Manager コード
gtm_script = f"""
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-WFPTBT5X');</script>
<!-- End Google Tag Manager -->
"""

st.markdown(gtm_script, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("LLO カウンタ")

st.write("全部押すと自動でリセットされます")

# セッション状態の初期化
if 'selection' not in st.session_state:
    st.session_state.selection = []

# リセット関数の定義
def reset_selection():
    st.session_state.selection = []

# 選択変更時の処理
def on_selection_change():
    if len(st.session_state.selection) == 9:  # 全部選択された場合
        st.session_state.selection = []

options = ["吟子", "花帆", "梢", "小鈴", "さやか", "綴理", "姫芽", "瑠璃乃", "慈"]
selection = st.pills(
    "選択", 
    options, 
    selection_mode="multi", 
    key="selection",
    on_change=on_selection_change
)

# リセットボタンを下に配置
st.button("リセット", on_click=reset_selection)