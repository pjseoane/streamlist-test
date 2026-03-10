# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

st.set_page_config(
    page_title="Investment Ideas Quant Lab",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Investment Ideas Quant Lab")
st.caption("Powered by yfinance · Data from Yahoo Finance")

with st.sidebar:
    st.header("⚙️ Settings/New Layout")

    with st.expander("Tickers", icon=":material/playlist_add_check:",expanded=True):
        pass
    with st.expander('Datasets', icon=":material/dataset:", expanded=False):
        pass

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗃️ Datasets","📊 Price Charts", "⚖️ Comparison", "📋 Fundamentals", "🔥 Correlation"])

with tab1: pass

with tab2: pass
with tab3: pass
with tab4: pass
with tab5: pass




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
