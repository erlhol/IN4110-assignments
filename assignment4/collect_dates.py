"""
Task 2 (IN4110 only)

parsing dates from wikipedia
"""

from __future__ import annotations

import re

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_date_patterns() -> tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"(?P<year>\d{4})"
    # month should accept month names or month numbers
    expr_for_month = [rf"\b[{m[0].lower()+m[0]}]{m[1:3]}(?:{m[3:]})?\b" for m in month_names]
    month_names_pat = "|".join(expr_for_month)
    month = rf"(?P<month>({month_names_pat})|(\d{{1,2}}))"
    # day should be a number, which may or may not be zero-padded
    day = r"(?P<day>\d{1,2})"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit do nothing
    if s.isdigit():
        return s

    # Convert to number as string
    ind = -1
    for i in range(len(month_names)):
        if month_names[i].lower().startswith(s.lower()):
           ind = i
           break 

    num = str(ind + 1)
    return zero_pad(num)


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    if len(n) == 2:
        return n
    return "0"+n


def find_dates(text: str, output: str | None = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
        output (str, Optional) : The file to write the output to if wanted
    return:
        results (List): A list with all the dates found
    """
    year, month, day = get_date_patterns()

    # Date on format YYYY/MM/DD - ISO
    ISO = f"{year}-{month}-{day}"

    # Date on format DD/MM/YYYY
    DMY = rf"{day}\s{month}\s{year}"

    # Date on format MM/DD/YYYY
    MDY = rf"{month}\s{day},\s{year}"

    # Date on format YYYY/MM/DD
    YMD = rf"{year}\s{month}\s{day}"

    # list with all supported formats
    formats = [ISO,DMY,MDY,YMD]
    dates = []

    # find all dates in any format in text

    reformat_by_pattern(dates,text,ISO)
    reformat_by_pattern(dates,text,DMY)
    reformat_by_pattern(dates,text,MDY)
    reformat_by_pattern(dates,text,YMD)

    # Write to file if wanted
    if output:
        with open(output) as out_file:
            for date in dates:
                out_file.write(date+"\n")

    liste = sorted(dates)
    sorted_dates = [date for _, date in liste]
    return sorted_dates

def reformat_by_pattern(dates: list, text: str, pattern: str):
    """Reformat all dates with the found pattern
    arguments:
        dates (list):  list of dates
        text (str): the text where we retrieve dates
        pattern (str): the pattern we are searching for
    return:
        None
    """
    matches = re.finditer(rf"{pattern}",text)
    for match in matches:
        if match:
            day = zero_pad(match.group("day"))
            month = convert_month(match.group("month"))
            year = match.group("year")
            date_element = f"{year}/{month}/{day}"
            dates.append((match.start(),date_element))