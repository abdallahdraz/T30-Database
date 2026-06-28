import streamlit as st
import requests
import json
import urllib.request

# =========================================================================
# ⚙️ إعدادات الصفحة والذكاء الاصطناعي
# =========================================================================
st.set_page_config(page_title="تحدي الثلاثين", page_icon="⚽", layout="centered")

LLAMA_API_KEY = "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" 
LLAMA_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# =========================================================================
# ☁️ محرك جلب البيانات السحابي (مع كاش لتسريع اللعبة على الموبايل)
# =========================================================================
@st.cache_data(ttl=3600)
def load_cloud_data():
    wiki_db, api_db = {}, {}
    try:
        wiki_db = requests.get("https://drive.google.com/uc?export=download&id=10tGI8KT1ueQMIjsRjX6wIB5-0BtcHngq", timeout=15).json()
        api_db = requests.get("https://raw.githubusercontent.com/abdallahdraz/T30-Database/main/Tahadi_ULTIMATE_DB.json", timeout=15).json()
    except:
        pass
    return wiki_db, api_db

wiki_db, api_db = load_cloud_data()

# =========================================================================
# 🖥️ غرفة الفار (VAR) المربوطة بـ Llama
# =========================================================================
def trigger_var(prompt, answer):
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "أنت حكم كروي صارم. أجب بـ 'إجابة صحيحة' أو 'إجابة خاطئة' مع السبب باختصار. استثنِ إسرائيل."},
            {"role": "user", "content": f"السؤال: {prompt}\nإجابة اللاعب: {answer}"}
        ]
    }
    try:
        req = urllib.request.Request(LLAMA_API_URL, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {LLAMA_API_KEY}'})
        response = urllib.request.urlopen(req, json.dumps(payload).encode('utf-8')).read().decode('utf-8')
        return json.loads(response)['choices'][0]['message']['content']
    except Exception as e:
        return f"خطأ في الاتصال بالحكم: {e}"

# =========================================================================
# 🕹️ إدارة حالة اللعبة (Session State)
# =========================================================================
if 'stage' not in st.session_state:
    st.session_state.stage = 'setup'
    st.session_state.p1 = {'name': '', 'score': 0, 'strikes': 0}
    st.session_state.p2 = {'name': '', 'score': 0, 'strikes': 0}
    st.session_state.round = 1
    st.session_state.q_idx = 1
    st.session_state.active = 'p1'

# =========================================================================
# 📱 واجهة المستخدم للموبايل (Mobile UI)
# =========================================================================
if st.session_state.stage == 'setup':
    st.title("⚽ تحدي الثلاثين - إعداد المواجهة")
    st.markdown("---")
    p1_name = st.text_input("اسم اللاعب الأول:", "عبدالله دراز")
    p2_name = st.text_input("اسم اللاعب الثاني:", "الخصم")
    
    if st.button("إطلاق صافرة البداية 🚀", use_container_width=True, type="primary"):
        st.session_state.p1['name'] = p1_name
        st.session_state.p2['name'] = p2_name
        st.session_state.stage = 'game'
        st.rerun()

elif st.session_state.stage == 'game':
    st.subheader(f"الفقرة {st.session_state.round} - السؤال [{st.session_state.q_idx}]")
    
    # لوحة النتائج
    col1, col2 = st.columns(2)
    with col1:
        st.error(f"🔴 {st.session_state.p1['name']}\n\nالنقاط: {st.session_state.p1['score']} | سترايك: {st.session_state.p1['strikes']}")
    with col2:
        st.info(f"🔵 {st.session_state.p2['name']}\n\nالنقاط: {st.session_state.p2['score']} | سترايك: {st.session_state.p2['strikes']}")
    
    st.markdown("---")
    
    prompt_text = "اذكر لاعبين لعبوا لقطبي إسبانيا (ريال مدريد وبرشلونة) عبر التاريخ."
    st.markdown(f"**السؤال:** {prompt_text}")
    
    active_player_name = st.session_state[st.session_state.active]['name']
    st.success(f"🎙️ دور الإجابة الآن: **{active_player_name}**")
    
    ans = st.text_input("إجابة اللاعب (اكتبها هنا للتحقق منها عبر الفار):")
    
    c1, c2 = st.columns(2)
    if c1.button("✅ إجابة صحيحة", use_container_width=True):
        st.session_state.active = 'p2' if st.session_state.active == 'p1' else 'p1'
        st.rerun()
        
    if c2.button("❌ سترايك (خاطئة)", use_container_width=True):
        p = st.session_state.active
        st.session_state[p]['strikes'] += 1
        if st.session_state[p]['strikes'] >= 3:
            opp = 'p2' if p == 'p1' else 'p1'
            st.session_state[opp]['score'] += 1
            st.session_state.p1['strikes'] = 0
            st.session_state.p2['strikes'] = 0
            st.session_state.q_idx += 1
            st.warning(f"🚨 3 سترايكس! النقطة تذهب لـ {st.session_state[opp]['name']}")
        st.rerun()

    if st.button("🖥️ استدعاء الـ VAR", use_container_width=True):
        if ans:
            with st.spinner('جاري مراجعة اللقطة مع حكم الذكاء الاصطناعي...'):
                decision = trigger_var(prompt_text, ans)
            st.warning(f"**قرار غرفة الفار:**\n\n{decision}")
        else:
            st.error("الرجاء كتابة الإجابة في الصندوق أولاً!")

    st.markdown("---")
    if st.button("السؤال التالي ⏭️", use_container_width=True, type="secondary"):
        st.session_state.p1['strikes'] = 0
        st.session_state.p2['strikes'] = 0
        st.session_state.q_idx += 1
        if st.session_state.q_idx > 3: # شرط الانتقال للفقرة اللي بعدها
            st.session_state.round += 1
            st.session_state.q_idx = 1
        st.rerun()
