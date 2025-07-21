import calendar
from datetime import date

# 国民の祝日・休日
# https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html
# 国民の祝日CSVから
holidays = [
    "2025/1/1",
    "2025/1/13",
    "2025/2/11",
    "2025/2/23",
    "2025/2/24",
    "2025/3/20",
    "2025/4/29",
    "2025/5/3",
    "2025/5/4",
    "2025/5/5",
    "2025/5/6",
    "2025/7/21",
    "2025/8/11",
    "2025/9/15",
    "2025/9/23",
    "2025/10/13",
    "2025/11/3",
    "2025/11/23",
    "2025/11/24",
    "2026/1/1",
    "2026/1/12",
    "2026/2/11",
    "2026/2/23",
    "2026/3/20",
    "2026/4/29",
    "2026/5/3",
    "2026/5/4",
    "2026/5/5",
    "2026/5/6",
    "2026/7/20",
    "2026/8/11",
    "2026/9/21",
    "2026/9/22",
    "2026/9/23",
    "2026/10/12",
    "2026/11/3",
    "2026/11/23",
]

# 日本語の曜日設定
calendar.setfirstweekday(calendar.SUNDAY)
WEEKDAY_NAMES_JP = ["日", "月", "火", "水", "木", "金", "土"]


def create_calendar_html_with_holidays():
    with open("./style.css", "r", encoding="utf-8") as f:
        css = f.read()

    start_date_str = "2025-07-01"
    end_date_str = "2026-12-31"

    start_dt = date.fromisoformat(start_date_str)
    end_dt = date.fromisoformat(end_date_str)

    # 祝日を検索しやすいようにsetに変換
    holidays_set = set(holidays)

    html_parts = []
    html_parts.append("<html><head><style>")
    html_parts.append(css)
    html_parts.append(f'</style></head><body><div class="container">')

    current_year = start_dt.year
    current_month = start_dt.month
    month_count = 0

    while date(current_year, current_month, 1) <= end_dt:
        cal = calendar.monthcalendar(current_year, current_month)

        is_last_month = current_year == end_dt.year and current_month == end_dt.month
        div_class = (
            ' class="break-after"'
            if (month_count + 1) % 6 == 0 and not is_last_month
            else ""
        )

        month_html = [f"<div{div_class}><h2>{current_year}年{current_month}月</h2>"]
        month_html.append("<table>")
        month_html.append(
            "<tr>" + "".join(f"<th>{d}</th>" for d in WEEKDAY_NAMES_JP) + "</tr>"
        )

        for week in cal:
            month_html.append("<tr>")
            for i, day in enumerate(week):
                if day == 0:
                    month_html.append("<td></td>")
                else:
                    classes = []
                    # 日曜日は0, 土曜日は6
                    if i == 0 or i == 6:
                        classes.append("weekend")

                    date_str = f"{current_year}/{current_month}/{day}"
                    if date_str in holidays_set:
                        classes.append("holiday")

                    class_attr = f" class=\"{' '.join(classes)}\"" if classes else ""
                    month_html.append(f"<td{class_attr}>{day}</td>")
            month_html.append("</tr>")
        month_html.append("</table></div>")
        html_parts.append("".join(month_html))

        # 次の月へ
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
        month_count += 1

    html_parts.append("</div></body></html>")
    return "".join(html_parts)


# HTMLファイルとして保存
with open("calendar_2025_2026_with_holidays.html", "w", encoding="utf-8") as f:
    f.write(create_calendar_html_with_holidays())
