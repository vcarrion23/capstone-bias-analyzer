import streamlit as st
import spacy
import re
import pandas as pd

# ---------------------------------------------------------
# 1. Page Configuration & Premium Enterprise Dashboard CSS
# ---------------------------------------------------------
st.set_page_config(page_title="Pedagogical Bias Analyzer", layout="wide") 

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    h1, h2, h3, h4, h5, h6, p, li, span, label { color: #FAFAFA !important; }
    .stTextArea textarea {
        background-color: #1A1C23 !important;
        color: #FFFFFF !important;
        border: 1px solid #333842 !important;
        border-radius: 8px;
        padding: 15px;
        font-size: 16px;
    }
    button[kind="primary"] {
        background-color: #1E6091 !important;
        border: 1px solid #184E77 !important;
        color: white !important;
        border-radius: 6px !important;
        transition: all 0.2s ease-in-out;
    }
    button[kind="primary"]:hover {
        background-color: #168AAD !important;
        border: 1px solid #1A759F !important;
    }
    button[kind="secondary"] {
        background-color: #2B2D31 !important;
        border: 1px solid #404249 !important;
        color: #D1D2D3 !important;
        border-radius: 6px !important;
    }
    button[kind="secondary"]:hover {
        background-color: #383A40 !important;
        border: 1px solid #4F545C !important;
        color: white !important;
    }
    div[data-testid="stExpander"] { background-color: #1A1C23 !important; border: 1px solid #333842 !important; border-radius: 8px; }
    div[data-testid="stInfo"] { background-color: #112338 !important; border: 1px solid #1C3B5E !important; border-radius: 8px; }
    div[data-testid="stSuccess"] { background-color: #12291D !important; border: 1px solid #1E4631 !important; border-radius: 8px; }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. ZERO-TRUST LOGIN PORTAL
# ---------------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("<br><br><br>", unsafe_allow_html=True)
        st.title("🔒 Enterprise HR Portal")
        st.info("This system processes highly confidential employee data. Please authenticate with Zero-Trust architecture to proceed.")
        pwd = st.text_input("Enter Master Password:", type="password")
        if st.button("Secure Login", use_container_width=True, type="primary"):
            if pwd == "admin123":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Unauthorized access. Incorrect password.")
    st.stop() 

# ---------------------------------------------------------
# 3. Load Models & Dictionaries (CLEAN VERSION)
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

bias_lexicon = {
    "Abrasive": ["always fails", "never", "incompetent", "unacceptable", "too aggressive", "bossy", "aggressive"],
    "Benevolent": ["sweet", "nurturing", "bubbly", "compassionate to a fault", "too nice"],
    "Racial/Cultural": ["articulate", "culture fit", "diverse candidate", "urban"], 
    "Gendered": ["emotional", "shrill", "hysterical", "man up", "gentleman"]
}

# ---------------------------------------------------------
# 4. Core Logic Functions
# ---------------------------------------------------------
def check_for_bias(sentence_text):
    sentence_lower = sentence_text.lower()
    for category, phrases in bias_lexicon.items():
        for phrase in phrases:
            pattern = r'\b' + re.escape(phrase.lower()) + r'\b'
            if re.search(pattern, sentence_lower):
                return {"type": category, "trigger_word": phrase}
    return None

def analyze_long_review(full_text):
    doc = nlp(full_text)
    total_sentences = 0
    observations = []
    
    for sentence in doc.sents:
        text_chunk = sentence.text.strip()
        if not text_chunk:
            continue
            
        total_sentences += 1
        detected_bias = check_for_bias(text_chunk)
        if detected_bias:
            observations.append({
                "category": detected_bias['type'],
                "trigger_word": detected_bias['trigger_word'],
                "sentence": text_chunk
            })
    return observations, total_sentences

def contains_objective_markers(text):
    doc = nlp(text)
    has_objective_entities = any(ent.label_ in ['CARDINAL', 'DATE', 'MONEY', 'PERCENT'] for ent in doc.ents)
    has_numbers = any(token.pos_ == 'NUM' for token in doc)
    return has_objective_entities or has_numbers

# ---------------------------------------------------------
# 5. Main Application UI
# ---------------------------------------------------------
with st.sidebar:
    st.write("Logged in as: **HR Admin**")
    if st.button("Logout", use_container_width=True, type="secondary"):
        st.session_state.authenticated = False
        st.rerun()

st.title("Pedagogical Bias Analyzer")
st.markdown("""
**Traditional automated HR tools often act as a 'black box,' silently correcting text without explaining why. This tool is designed differently.** It acts as a pedagogical co-editor to help managers identify implicit linguistic bias.

**How to use it:** Paste your performance review into the text area below. If subjective phrasing is detected, you will be prompted to reflect on your wording and provide concrete, objective business metrics.
""")

user_input = st.text_area("Review Text:", height=250)

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False
    st.session_state.observations = []
    st.session_state.total_sentences = 0

if st.button("Analyze Review", type="primary"):
    if user_input.strip():
        with st.spinner("Running deep sentence tokenization and scanning lexicon..."):
            obs, total = analyze_long_review(user_input)
            st.session_state.observations = obs
            st.session_state.total_sentences = total
            st.session_state.analysis_done = True
    else:
        st.info("Please enter some text to analyze.")

# ---------------------------------------------------------
# 6. Premium Analytics Dashboard & Pedagogy Flow
# ---------------------------------------------------------
if st.session_state.analysis_done:
    st.divider()
    obs = st.session_state.observations
    total_flags = len(obs)
    
    if st.session_state.total_sentences > 0:
        flag_percentage = (total_flags / st.session_state.total_sentences) * 100
        overall_score = max(0, 100 - flag_percentage)
    else:
        overall_score = 100.0

    dash_col1, dash_col2 = st.columns([1, 2])
    
    with dash_col1:
        st.markdown("### Objectivity Rating")
        st.metric(label="System Output", value=f"{overall_score:.1f}%")
        st.caption(f"Reviewed **{st.session_state.total_sentences}** sentences. Found **{total_flags}** observation(s).")
    
    with dash_col2:
        st.markdown("### Linguistic Breakdown")
        if total_flags > 0:
            category_counts = {}
            for o in obs:
                cat = o["category"]
                category_counts[cat] = category_counts.get(cat, 0) + 1
                
            for category, count in category_counts.items():
                percentage = (count / total_flags) * 100
                st.write(f"**{category}** ({count} instances) - *{percentage:.1f}%*")
                st.progress(int(percentage))
        else:
            st.success("No linguistic bias detected in this text.")

    st.write("<br>", unsafe_allow_html=True)

    if total_flags == 0:
        if st.button("Submit Official Review to HR", type="primary", use_container_width=True):
            st.balloons()
            st.toast("Official Review Submitted Successfully!", icon="✅")
            st.session_state.analysis_done = False
            st.rerun()
    else:
        st.info("ℹ️ **Action Required:** Please review the following specific observations and complete the Socratic reflection to unlock submission.")
        
        for o in obs:
            with st.expander(f"Observation: {o['category']} Language Detected"):
                st.markdown(f"**Flagged Phrase:** `{o['trigger_word']}`")
                st.write(f"> *\"{o['sentence']}\"*")
        
        st.markdown("---")
        st.markdown("### Socratic Reflection Gateway")
        st.write("To proceed with submission, you must justify the highlighted wording above.")
        
        justification = st.text_area("What specific, observable business behaviors led you to use these words?", height=120)
        
        if justification:
            if contains_objective_markers(justification):
                st.success("✅ Objective markers detected. Accountability metric met.")
                if st.button("Submit Official Review to HR", type="primary"):
                    st.balloons()
                    st.toast("Official Review Submitted Successfully!", icon="✅")
                    st.session_state.analysis_done = False
                    st.rerun()
            else:
                st.info("ℹ️ We noticed your justification did not include objective business metrics (e.g., specific numbers, dates, or measurable outcomes).")
                
                liability_check = st.checkbox("I acknowledge that my subjective reasoning will be placed in the official HR record.")
                
                if liability_check:
                    if st.button("Submit Official Review (With Subjective Marker)", type="primary"):
                        st.toast("Review Submitted with Subjective Marker", icon="⚠️")
                        st.session_state.analysis_done = False
                        st.rerun()
                else:
                    st.button("Submit Official Review", disabled=True)
