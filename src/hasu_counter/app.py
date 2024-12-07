import streamlit as st

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("LLO カウンタ")

# セッション状態の初期化
if 'selection' not in st.session_state:
    st.session_state.selection = []

# リセット関数の定義
def reset_selection():
    st.session_state.selection = []

options = ["吟子", "花帆", "梢", "小鈴", "さやか", "綴理", "姫芽", "瑠璃乃", "慈"]
selection = st.pills("選択", options, selection_mode="multi", key="selection")

# リセットボタンを下に配置
st.button("リセット", on_click=reset_selection)