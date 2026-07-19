import streamlit as st
import feedparser

@st.cache_data
def load_news():
    return feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
@st.cache_data
def load_news_gold():
    return feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
tab1, tab2 = st.tabs(["Đọc báo", "Giá vàng"])
with tab1:
    st.header("Tin tức mới nhất trên VnExpress")
    feed = load_news()
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
with tab2:
    st.header("Cập nhật giá vàng trên Vietnamnet")
    feed = load_news_gold()
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)