# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
#from datetime import timedelta,datetime
#import plotly.graph_objects as go
from pjs_qlab.data.YahooPriceFetcher import YahooPriceFetcher as price_fetcher
from pjs_qlab.analytics.cQuantClass import cQuantClass as cQuant


# ── Data fetching ──────────────────────────────────────────────────────────────
#df=pd.DataFrame()
@st.cache_resource(ttl=timedelta(minutes=5),
                   max_entries=20,
                   show_spinner=True,
                   )

def get_closes(adjusted=True, freq='d'):
    return y_obj.get_close(adjusted=adjusted, freq=freq)

def get_cum_returns(freq='d'):
    return q_obj.get_cum_returns(freq=freq)

def get_pct_returns(freq='d'):
    return q_obj.get_pct_returns(freq=freq)

def get_log_returns(freq='d'):
    return q_obj.get_log_returns(freq=freq)

def get_rebase(freq='d'):
    return q_obj.get_rebase(freq=freq)

def get_largest_pct_drop(days=30):
    return q_obj.get_largest_pct_drop(days=days)

def get_largest_pct_rise(days=30):
    return q_obj.get_largest_pct_rise(days=days)

def get_hist_vlt_series(days=30):
    return q_obj.get_hist_vlt_series(days=days)

def get_summary(freq='ME'):
    return q_obj.get_summary(freq=freq)



def function_executor(func, parameters,tickers,title='title' ):
    st.subheader(title)
    output_df=func(parameters)
    output_df.index = output_df.index.date
    st.dataframe(

        output_df.style
        .format("{:.2%}", subset=tickers)
        .background_gradient(subset=tickers, cmap="RdYlGn")
        .highlight_max(subset=tickers, color="lightgreen")
        .highlight_min(subset=tickers, color="salmon"),

        hide_index=False,  # hide the index column
        column_order=tickers,  # reorder columns shown

    )
    return output_df


# ── Page config ────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Investment Ideas Quant Lab 2",
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
