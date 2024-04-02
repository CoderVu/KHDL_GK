import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv(r"D:\DUT\DH_HK6\KHDL\DEALINEGK\Crawl\data.csv")

# Chuyển các giá trị "-" thành NaN
df.replace("-", pd.NA, inplace=True)

# Xóa dấu phẩy trong cột "Official Points"
df['Official Points'] = df['Official Points'].str.replace(',', '')

# Xóa dấu phẩy trong cột "Dropping"
df['Dropping'] = df['Dropping'].str.replace(',', '')

# Chuyển định dạng của cột "Official Points" và "Dropping" thành số nguyên
df['Official Points'] = df['Official Points'].apply(lambda x: int(x) if pd.notnull(x) else x)
df['Dropping'] = df['Dropping'].apply(lambda x: int(x) if pd.notnull(x) else x)

# Bảng ánh xạ từ viết tắt đến tên đầy đủ của quốc gia
country_mapping = {
    'srb': 'Serbia',
    'esp': 'Spain',
    'ita': 'Italy',
    'rus': 'Russia',
    'ger': 'Germany',
    'den': 'Denmark',
    'nor': 'Norway',
    'pol': 'Poland',
    'aus': 'Australia',
    'gre': 'Greece',
    'bul': 'Bulgaria',
    'usa': 'United States',
    'fra': 'France',
    'chi': 'Chile',
    'ned': 'Netherlands',
    'cze': 'Czech Republic',
    'arg': 'Argentina',
    'fin': 'Finland',
    'chn': 'China',
    'cro': 'Croatia',
    'can': 'Canada',
    'hun': 'Hungary',
    'por': 'Portugal',
    'jpn': 'Japan',
    'bra': 'Brazil',
    'sui': 'Switzerland',
    'col': 'Colombia'
}

# Chuyển đổi viết tắt đất nước thành tên đầy đủ
df['Country'] = df['Country'].map(country_mapping)

# Hiển thị dữ liệu sau khi xử lý
print(df)

# Lưu DataFrame đã được xử lý vào một tệp CSV mới
df.to_csv("Processed_data.csv", index=False)