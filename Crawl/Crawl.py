import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

def get_atp_rankings(url, delay=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    sleep(delay)  # Sleep for a while to avoid being blocked

    soup = BeautifulSoup(response.content, "html.parser")

    container_div = soup.find("div", class_="atp_rankings-all")
    if container_div:
        rankings = []
        rows = container_div.find_all("tr")

        # Loop through each row
        for row in rows[1:]:  # Skip the first row as it contains headers
            # Extract player information from the row
            cells = row.find_all("td")
            
            # Check if there are enough cells
            if len(cells) >= 8:
                rank = cells[0].text.strip()#lấy ra vị trí của cầu thủ     
                player_name = cells[1].find("a").text.strip()
                age = cells[2].text.strip()
                points = cells[3].text.strip()
                plus_minus = cells[4].text.strip()
                tournaments_played = cells[5].text.strip()
                dropping = cells[6].text.strip()
                next_best = cells[7].text.strip()
                
                # Extract the flag information
                flag_img = cells[1].find("img", class_="flag")
                if flag_img:
                    country_name = flag_img.get("src").split("/")[-1].split(".")[0]
                else:
                    country_name = "Unknown"

                # Append data to rankings list
                rankings.append({
                    "Rank": rank,
                    "Player Name": player_name,
                    "Age": age,
                    "Official Points": points,
                    "+/-": plus_minus,
                    "Tournaments Played": tournaments_played,
                    "Dropping": dropping,
                    "Next Best": next_best,
                    "Country": country_name
                })

        return rankings
    else:
        print("Không tìm thấy container chứa dữ liệu.")
        print(f"Lỗi: Không thể truy xuất dữ liệu. Mã trạng thái: {response.status_code}")

# URL of ATP rankings page
url = "https://www.atptour.com/en/rankings/singles?RankRange=0-5000&Region=all&DateWeek=Current+Week&fbclid=IwAR1yBrFbMNi5BOxv370aP89SSgjF1gbCQbz8Azhb0mCSdb6uKtAM3tXTkMg"

# Get ATP rankings data
delay = 1  # Seconds
rankings = get_atp_rankings(url, delay)

# Save data to CSV file
if rankings:
    with open(r"D:\DUT\DH_HK6\KHDL\DEALINEGK\atp_rankingdatnuocc.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = rankings[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for ranking in rankings:
            writer.writerow(ranking)
    print("Dữ liệu đã được lưu vào file atp_rankings.csv")
else:
    print("Không tìm thấy dữ liệu.")
