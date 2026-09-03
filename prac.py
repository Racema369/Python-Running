
from datetime import date, timedelta
import csv

# Nepali BS month lengths:
# [Baisakh, Jestha, Ashadh, Shrawan, Bhadra, Ashwin,
#  Kartik, Mangsir, Poush, Magh, Falgun, Chaitra]

bs_month_lengths = {
    2075: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
    2076: [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
    2077: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
    2078: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
    2079: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
    2080: [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
    2081: [31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30],
}

# Starting and ending Gregorian dates
ad_start = date(2018, 7, 17)
ad_end   = date(2024, 7, 15)

# Corresponding starting BS date
bs_year = 2075
bs_month = 4
bs_day = 1

current_ad = ad_start

rows = []

while current_ad <= ad_end:

    rows.append([
        current_ad.strftime("%m/%d/%Y"),
        f"{bs_year:04d}.{bs_month:02d}.{bs_day:02d}"
    ])

    # Move one day forward in BS
    bs_day += 1

    if bs_day > bs_month_lengths[bs_year][bs_month - 1]:
        bs_day = 1
        bs_month += 1

        if bs_month > 12:
            bs_month = 1
            bs_year += 1

    # Move one day forward in AD
    current_ad += timedelta(days=1)


# Write CSV file
filename = "nepali_ad_2018-2024.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Gregorian Date", "Nepali Date"])
    writer.writerows(rows)

print(f"Created: {filename}")
print(f"Total data rows: {len(rows)}")
print(f"First row: {rows[0]}")
print(f"Last row: {rows[-1]}")
