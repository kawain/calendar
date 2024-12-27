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
calendar.day_name = ["日", "月", "火", "水", "木", "金", "土"]


def create_calendar_html_with_holidays():
    with open("./style.css", "r", encoding="utf-8") as f:
        css = f.read()

    year = 2025
    html = "<html><head><style>"
    html += css
    html += (
        f"""</style></head><body><h1>{year} (令和7) 年</h1><div class="container">"""
    )

    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        div_id = ' class="break-after"' if month == 6 else ""
        html += f"<div{div_id}><h2>{month}月</h2>"  # divで囲む
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

    html += "</div></body></html>"

    return html


# HTMLファイルとして保存
with open("calendar_2025_with_holidays.html", "w", encoding="utf-8") as f:
    f.write(create_calendar_html_with_holidays())
