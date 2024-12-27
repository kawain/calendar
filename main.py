import calendar

# 令和7年（2025年）の国民の祝日・休日
holidays = [
    "1月1日",
    "1月13日",
    "2月11日",
    "2月23日",
    "2月24日",
    "3月20日",
    "4月29日",
    "5月3日",
    "5月4日",
    "5月5日",
    "5月6日",
    "7月21日",
    "8月11日",
    "9月15日",
    "9月23日",
    "10月13日",
    "11月3日",
    "11月23日",
    "11月24日",
]

# 日本語の曜日設定
calendar.setfirstweekday(calendar.SUNDAY)
calendar.month_name = [
    None,
    "1月",
    "2月",
    "3月",
    "4月",
    "5月",
    "6月",
    "7月",
    "8月",
    "9月",
    "10月",
    "11月",
    "12月",
]
calendar.day_name = ["日", "月", "火", "水", "木", "金", "土"]


def create_calendar_html_with_holidays():
    year = 2025
    html = "<html><head><style>"
    html += """
body {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

h2 {
  text-align: center;
}

table {
  border-collapse: collapse;
  margin: 10px;
}

th,
td {
  border: 1px solid black;
  padding: 5px;
  text-align: center;
}

th {
  background-color: #eee;
}

td {
  height: 50px;
  vertical-align: top;
}

.weekend,
.holiday {
  background-color: #ccc;
  font-weight: bold;
}

    """
    html += "</style></head><body>"

    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        html += f"<div><h2>(R7) {year}年{month}月</h2>"  # divで囲む
        html += "<table>"
        html += "<tr>" + "".join(f"<th>{d}</th>" for d in calendar.day_name) + "</tr>"

        for week in cal:
            html += "<tr>"
            for i, day in enumerate(week):
                if day == 0:
                    html += "<td></td>"
                else:
                    classes = []
                    if i == 0 or i == 6:  # 土日
                        classes.append("weekend")
                    if f"{month}月{day}日" in holidays:  # 祝日
                        classes.append("holiday")
                    class_attr = f" class=\"{' '.join(classes)}\"" if classes else ""
                    html += f"<td{class_attr}>{day}</td>"
            html += "</tr>"
        html += "</table></div>"  # 閉じdivタグ

    html += "</body></html>"
    return html


# HTMLファイルとして保存
with open("calendar_2025_with_holidays.html", "w", encoding="utf-8") as f:
    f.write(create_calendar_html_with_holidays())
