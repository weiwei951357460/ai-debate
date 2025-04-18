import streamlit as st

st.set_page_config(page_title="AI 候選人之戰", page_icon="🗳️", layout="centered")

st.title("🗳️ AI 候選人之戰")
st.write("選擇一位候選人聽聽他們的政見：")

characters = {
    "Vera（理性派）": "我們應該以制度為本，透過數據驅動政策決策。",
    "Blaze（氣氛派）": "人民才是國家的根！我們不能讓冷冰冰的 AI 決定未來！",
    "Atlas（中立派）": "若 AI 能被適當監督，也許可參與公共決策的技術面。",
    "阿智（搞笑候選人）": "我主張每天三點點名 AI，不準請假還自罰卡神幣！"
}

choice = st.radio("請選擇候選人", list(characters.keys()))

if choice:
    st.image(f"{choice.split('（')[0].lower()}.png", width=200)
    st.success(characters[choice])
