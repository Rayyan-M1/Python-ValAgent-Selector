import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="VALORANT Agent Roulette", page_icon="🎯")

# Custom CSS to match Valorant colors
st.markdown("""
    <style>
    .main { background-color: #0f1923; }
    .stText, .stMarkdown, h1 { color: #ece8e1 !important; font-family: 'Arial'; }
    .agent-box { 
        font-size: 50px !important; 
        font-weight: bold; 
        color: #ff4655; 
        text-align: center;
        padding: 20px;
        border: 2px solid #ff4655;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🎯 AGENT SELECTION")
    
    agents = [
        "Astra", "Breach", "Brimstone", "Chamber", "Clove", "Cypher", 
        "Deadlock", "Fade", "Gekko", "Harbor", "Iso", "Jett", "KAY/O", 
        "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", 
        "Skye", "Sova", "Tejo", "Veto", "Viper", "Vyse", "Waylay", "Yoru"
    ]

    # Create an empty container for the animation
    placeholder = st.empty()
    
    # Button to trigger the roll
    if st.button('CLICK TO ROLL'):
        # Roulette Animation
        current_delay = 0.05
        for i in range(25):
            selected = random.choice(agents)
            placeholder.markdown(f'<div class="agent-box">{selected.upper()}</div>', unsafe_allow_html=True)
            
            # Gradually slow down
            if i > 15:
                current_delay += 0.05
            time.sleep(current_delay)

        # Final Choice
        final_agent = random.choice(agents)
        placeholder.markdown(f'<div class="agent-box" style="background-color: #ff4655; color: white;">{final_agent.upper()}</div>', unsafe_allow_html=True)
        st.balloons() # Fun web-only effect!
    else:
        placeholder.markdown('<div class="agent-box">READY?</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
