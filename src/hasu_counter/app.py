import streamlit as st

st.set_page_config(page_title="LLO カウンタ", page_icon="💬")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("リンクラ LLO カウンタ")

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