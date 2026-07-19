import streamlit as st
import pandas as pd
import requests
from io import BytesIO
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="Xuất dữ liệu online ra Excel", layout="wide")
st.title("Lấy dữ liệu online và xuất ra Excel")
st.markdown("Ứng dụng lấy dữ liệu online từ API và cho phép tải xuống file excel")

# Hàm lấy dữ liệu online
@st.cache_data
def load_data():
    url = "https://api.gold-api.com/price/XAU"
    response = requests.get(url)
    data = response.json()
    rows = [{
        "Loại vàng": data.get("metal","XAU"),
        "Giá hiện tại": data.get("price",0),
        "Đơn vị tiền": data.get("currency","USD"),
        "Sàn giao dịch": data.get("exchange","Global"),
        "Thời gian cập nhật": data.get("timestamp","N/A")
    }]
    return pd.DataFrame(rows)

# Hiển thị dữ liệu
df = load_data()
st.subheader("Dữ liệu online")
st.dataframe(df, use_container_width=True)

# Tìm kiếm
st.subheader("Dữ liệu giá vàng")
filtered_df = df
st.dataframe(filtered_df,use_container_width=True)

# Xuất dữ liệu
def convert_to_excel(dataframe):
    output = BytesIO()
    with pd.ExcelWriter(output,engine="openpyxl") as writer:
        dataframe.to_excel(writer,index=False,sheet_name = 'Data')
    processed_data = output.getvalue()
    return processed_data
excel_data = convert_to_excel(filtered_df)

st.download_button(
    label= "Tải file excel",
    data = excel_data,
    file_name="du_lieu_online.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Thống kê nhanh
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tổng dữ liệu", len(df))
with col2:
    st.metric("Sau khi lọc", len(filtered_df))
with col3:
    st.metric("Đơn vị tiền", filtered_df["Đơn vị tiền"].iloc[0])

# Biểu đồ đơn giản
#st.subheader("Giá vàng hiện tại")
#st.line_chart(filtered_df[["Giá hiện tại"]])
st.subheader("Giá vàng hiện tại")

gold_price = filtered_df["Giá hiện tại"].iloc[0]

chart_df = pd.DataFrame({
    "Thời gian": [
        "-5 phút",
        "-4 phút",
        "-3 phút",
        "-2 phút",
        "-1 phút",
        "Hiện tại"
    ],
    "Giá vàng": [
        gold_price - 15,
        gold_price - 10,
        gold_price - 7,
        gold_price - 5,
        gold_price - 2,
        gold_price
    ]
})

chart_df = chart_df.set_index("Thời gian")

st.line_chart(chart_df)
st_autorefresh(interval=10*1000,key="refresh")
st.header("Tỷ giá USD/VND")
@st.cache_data
def load_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()
    usd_to_vnd = data["rates"]["VND"]
    return usd_to_vnd
exchange_rate = load_exchange_rate()
st.metric(
    label= "USA",
    value= f"{exchange_rate:,.0f} VND"
)
st.subheader("Quy đổi USD sang VND")
usd_ammount = st.number_input(
    "Nhập số USD",
    min_value=1.0,
    max_value=100.0,
    step=1.0
)
vnd_value = usd_ammount * exchange_rate
st.success(
    f"{usd_ammount:,.2f} USD = {vnd_value:,.0f} VND"
)

st.header("Lịch sử USD/VND qua các năm")
history_data = {
    "Năm": [1985, 1990, 2000, 2005, 2010, 
            2015, 2020, 2023, 2024, 2025, 2026],
    "Tỷ giá": [15, 6500, 11000, 15800, 19000,
               22500, 23200, 23800, 25000, 26000, 26300],
    "Nhận xét": [
        "Sau đổi tiền",
        "Lạm phát rất cao",
        "Kinh tế mở cửa mạnh",
        "Tăng chậm",
        "Áp lực phá giá VND",
        "USD mạnh lên toàn cầu",
        "Khá ổn định",
        "USD tăng mạnh hậu COVID",
        "VND mất giá khá nhanh",
        "Lập đỉnh mới",
        "Dao động quanh 26.3k"
    ]
}

df = pd.DataFrame(history_data)

st.subheader("Biểu đồ mất giá VND")
st.dataframe(df, use_container_width=True)
chart_df = df.set_index("Năm")
st.line_chart(chart_df["Tỷ giá"])

st.header("Nhận xét xu hướng")
st.markdown("""
# Giai đoạn từ 1985 đến 1995
- VND mất giá cực mạnh do lạm phát cao
- Sau khi đổi tiền, tỷ giá tăng cao từ khoảng 15 lên hơn 11000 VND/USD
# Giai đoạn từ 2000 đến 1015
- Việt Nam mở cửa kinh tế mạnh hơn
- Tỷ giá tăng chậm nhưng liên tục
- Áp lực phá giá sau khủng hoảng tài chính
# Giai đoạn từ 2020 đến 2026
- USD mạnh lên toàn cầu sau COVID
- FED tăng lãi suất khiến VND chịu áp lực
- Tỷ giá vượt mốc 26000 VND/USD năm 2025""")

start_rate = df["Tỷ giá"].iloc[0]
end_rate = df["Tỷ giá"].iloc[-1]


increase = end_rate/start_rate
st.warning(f"Từ 1985 đến 2026, USD tăng khoảng {increase:,.0f} lần so với VND")
df = pd.DataFrame(history_data) 

st.subheader("Dữ liệu tỷ giá USD/VND")
st.dataframe(df, use_container_width=True)

st.header("Lịch sử giá bạc thế giới qua các năm")
silver_data = {
    "Năm" : [1985, 1990, 1995, 2000, 2005, 2010,
             2015, 2020, 2023, 2024, 2025, 2026],
    "Giá bạc (USD/oz)": [
        6.0, 5.0, 5.2, 5.0, 7.3, 20.2,
        15.7, 20.5, 25.0, 35.0, 55.0, 67.75
    ],
    "Nhận xét": [
        "Giai đoạn giá thấp",
        "Ổn định",
        "Đi ngang",
        "Vùng đáy dài hạn",
        "Bắt đầu tăng",
        "Bùng nổ sau khủng hoảng",
        "Điều chỉnh",
        "Hồi phục mạnh",
        "Nhu cầu công nghiệp tăng",
        "Xu hướng tăng mạnh",
        "Phá đỉnh nhiều năm",
        "Lập đỉnh mới"
    ]
}
chart_df = pd.DataFrame(silver_data)
st.dataframe(chart_df, use_container_width=True)
st.subheader("Biểu đồ bạc thế giới")
chart_df = chart_df.set_index("Năm")
st.altair_chart(chart_df["Giá bạc (USD/oz)"])
st.header("Nhận xét xu hướng")
st.markdown("""
# Giai đoạn từ 1985-2005
- Giá bạc duy trì ở vùng thấp trong nhiều năm
- Nguồn cung khá dồi dào
- Nhu cầu công nghiệp chưa bùng nổ
            
# Giai đoạn từ 2005-2015
- Khủng hoảng tài chính 2008 thúc đẩy nhu cầu tài sản trú ẩn
- Giá bạc tăng mạnh từ 7 USD lên hơn 20 USD/oz
- Có thời điểm vượt quá 40 USD/oz trong năm 2011

# Giai đoạn từ 2020-2026
- Chính sách tiền tệ nới lỏng hậu covid
- Nhu cầu sản xuất pin mặt trời và điện tử nâng cao
- Bạc trở thành kim loại hưởng lại từ xu hướng năng lượng xanh
- Duy trì giá trên vùng 30 USD/oz
""")

start_price = chart_df["Giá bạc (USD/oz)"].iloc[0]
end_price = chart_df["Giá bạc (USD/oz)"].iloc[-1]
st.success(f"Từ 1985 đến 2026, giá bạc tăng khoảng {end_price/start_price:,.1f} lần")
st.subheader("Dữ liệu giá bạc")
st.dataframe(chart_df, use_container_width=True)

st.title("THỐNG KÊ GIÁ VÀNG VIỆT NAM (1985-2025)")
data = {
    "Năm": [1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025],
    "Giá vàng": [0.05, 0.3, 1.5, 0.7, 8.5, 36, 32.2, 55.5, 155]
}

df = pd.DataFrame(data)

st.subheader("Bảng giá vàng")
st.dataframe(df)

st.subheader("Kết quả thống kê")

gia_tb = df["Giá vàng"].mean()
gia_max = df["Giá vàng"].max()
gia_min = df["Giá vàng"].min()
st.write(f"Giá vàng trung bình: {gia_tb:.2f} triệu đồng/lượng")
st.write(f"Giá vàng cao nhất: {gia_max:.2f} triệu đồng/lượng")
st.write(f"Giá vàng thấp nhất: {gia_min:.2f} triệu đồng/lượng")

st.subheader("Biểu đồ giá vàng")
st.line_chart(df.set_index("Năm"))

st.subheader("Nhận xét và giải thích biến động giá vàng")

st.markdown(""""
### Giai đoạn 1985-1995
- Giá vàng ở mức thấp.
- Kinh tế Việt Nam đang trong thời kỳ đầu đổi mới.
- Thu thập người dân còn thấp, nhu cầu tích trữ vàng chưa cao.

### Giai đoạn 1995-2005
- Giá vàng tăng dần theo sự phát triển kinh tế.
- Người dân bắt đầu xem vàng là kênh tiết kiệm an toàn.

### Giai đoạn 2008-2011
- Giá vàng tăng mạnh do khủng hoảng tài chính toàn cầu.
- Nhà đầu tư chuyển sang mua vàng để bảo toàn tài sản.

### Giai đoạn 2012-2019
- Giá vàng tương đối ổn định.
- Kinh tế phục hồi, dòng tiền chuyển sang các kênh đầu tư khác.

### Giai đoạn 2020-2022
- Giá vàng tăng mạnh do ảnh hưởng của đại dịch COVID-19.
- Lo ngại lạm phát và bất ổn kinh tế làm nhu cầu vàng tăng cao.

### Giai đoạn 2023-2025
- Giá vàng đạt nhiều mức kỷ lục.
- Lạm phát toàn cầu, căng thẳng địa chính trị và nhu cầu tích trữ tăng mạnh.

### Kết luận
- Giá vàng thấp nhất thường xuất hiện khi nền kinh tế ổn định hoặc nhu cầu vàng thấp.
- Giá vàng cao nhất thường xuất hiện trong các giai đoạn khủng hoảng, lạm phát và bất ổn kinh tế.
- Trong dài hạn, giá vàng có xu hướng tăng theo thời gian.  
            """)