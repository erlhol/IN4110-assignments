"""
Task 4

collecting olympic statistics from wikipedia
"""

from __future__ import annotations

from pathlib import Path
import requesting_urls
from bs4 import BeautifulSoup
import re
from itertools import groupby
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Countries to submit statistics for
scandinavian_countries = ["Norway", "Sweden", "Denmark"]

# Summer sports to submit statistics for
summer_sports = ["Sailing", "Athletics", "Handball", "Football", "Cycling", "Archery"]


def report_scandi_stats(url: str, sports_list: list[str], work_dir: str | Path) -> None:
    """
    Given the url, extract and display following statistics for the Scandinavian countries:

      -  Total number of gold medals for for summer and winter Olympics
      -  Total number of gold, silver and bronze medals in the selected summer sports from sport_list
      -  The best country in number of gold medals in each of the selected summer sports from sport_list

    Display the first two as bar charts, and the last as an md. table and save in a separate directory.

    Parameters:
        url (str) : url to the 'All-time Olympic Games medal table' wiki page
        sports_list (list[str]) : list of summer Olympic games sports to display statistics for
        work_dir (str | Path) : (absolute) path to your current working directory

    Returns:
        None
    """

    # Make a call to get_scandi_stats
    # Plot the summer/winter gold medal stats
    # Iterate through each sport and make a call to get_sport_stats
    # Plot the sport specific stats
    # Make a call to find_best_country_in_sport for each sport
    # Create and save the md table of best in each sport stats

    work_dir = Path(work_dir)
    country_dict = get_scandi_stats(url)

    stats_dir = work_dir / "olympic_games_results"
    stats_dir.mkdir(exist_ok=True)
    plot_scandi_stats(country_dict,stats_dir)

    best_in_sport = []
    # Valid values for medal ["Gold" | "Silver" |"Bronze"]
    medal = ...

    for sport in sports_list:
        results: dict[str, dict[str, int]] = {}
        for country in country_dict:
            results[country] = get_sport_stats(country_dict[country]["url"],sport)
        
        # Plot here based on results.
        plot_sport_specific_stats(results,sport,stats_dir)
        # Write best_country by sport to file
        best_country = find_best_country_in_sport(results)
        best_in_sport.append(best_country)

    best_countries = best_sports_to_md(sports_list,best_in_sport)
    out_file = open(stats_dir / 'best_of_sport_by_Gold.md',"w")
    out_file.write(best_countries)
    out_file.close() 


def get_scandi_stats(
    url: str,
) -> dict[str, dict[str, str | dict[str, int]]]:
    """Given the url, extract the urls for the Scandinavian countries,
       as well as number of gold medals acquired in summer and winter Olympic games
       from 'List of NOCs with medals' table.

    Parameters:
      url (str): url to the 'All-time Olympic Games medal table' wiki page

    Returns:
      country_dict: dictionary of the form:
        {
            "country": {
                "url": "https://...",
                "medals": {
                    "Summer": 0,
                    "Winter": 0,
                },
            },
        }

        with the tree keys "Norway", "Denmark", "Sweden".
    """

    html = requesting_urls.get_html(url)
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find('span', id='List_of_NOCs_with_medals_(sortable_&_unranked)').find_next('table')
    base_url = "https://en.wikipedia.org"

    rows = table.find_all('a',string=scandinavian_countries)

    country_dict: dict[str, dict[str, str | dict[str, int]]] = {}

    for row in rows:
        country = row.string
        country_url = row.get('href')
        row = row.find_parent('tr')
        cols = row.find_all('td')
        info_dict = {'url': base_url+country_url, 'medals': {'Summer': int(cols[2].string), 'Winter': int(cols[7].string)} }
        country_dict[country] = info_dict

    return country_dict


def get_sport_stats(country_url: str, sport: str) -> dict[str, int]:
    """Given the url to country specific performance page, get the number of gold, silver, and bronze medals
      the given country has acquired in the requested sport in summer Olympic games.

    Parameters:
        - country_url (str) : url to the country specific Olympic performance wiki page
        - sport (str) : name of the summer Olympic sport in interest. Should be used to filter rows in the table.

    Returns:
        - medals (dict[str, int]) : dictionary of number of medal acquired in the given sport by the country
                          Format:
                          {"Gold" : x, "Silver" : y, "Bronze" : z}
    """
    html = requesting_urls.get_html(country_url)
    soup = BeautifulSoup(html,'html.parser')
    pattern = re.compile(r'medals_by_summer_sport', re.IGNORECASE)
    table = soup.find('span', id=pattern).find_next('table')

    medals = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0,
    }

    rows = table.find_all('a',string=sport)

    for row in rows:
        row = row.find_parent('tr')
        cols = row.find_all('td')
        medals["Gold"] = int(cols[0].string)
        medals["Silver"] = int(cols[1].string)
        medals["Bronze"] = int(cols[2].string)
    return medals


def find_best_country_in_sport(
    results: dict[str, dict[str, int]], medal: str = "Gold"
) -> str:
    """Given a dictionary with medal stats in a given sport for the Scandinavian countries, return the country
        that has received the most of the given `medal`.

    Parameters:
        - results (dict) : a dictionary of country specific medal results in a given sport. The format is:
                        {"Norway" : {"Gold" : 1, "Silver" : 2, "Bronze" : 3},
                         "Sweden" : {"Gold" : 1, ....},
                         "Denmark" : ...
                        }
        - medal (str) : medal type to compare for. Valid parameters: ["Gold" | "Silver" |"Bronze"]. Should be used as a key
                          to the medal dictionary.
    Returns:
        - best (str) : name of the country(ies) leading in number of gold medals in the given sport
                       If one country leads only, return its name, like for instance 'Norway'
                       If two countries lead return their names separated with '/' like 'Norway/Sweden'
                       If all or none of the countries lead, return string 'None'
    """
    valid_medals = {"Gold", "Silver", "Bronze"}
    if medal not in valid_medals:
        raise ValueError(
            f"{medal} is invalid parameter for ranking, must be in {valid_medals}"
        )

    # Get the requested medals and determine the best
    best = sorted([(v[medal], k) for k, v in results.items()],reverse=True)

    # group into countries with the same number of medals
    grouped_best = [list(items) for _,items in groupby(best, key=lambda x: x[0])]

    # If just one group: meaning that they are equal in rank:
    if len(grouped_best) == 1:
        return "None"
    
    # else: there are different groups
    str_to_return = ""
    for country_and_medal in grouped_best[0]:
        if str_to_return != "":
            str_to_return += "/" + country_and_medal[1]
        else:
            str_to_return += country_and_medal[1]

    return str_to_return

def best_sports_to_md(sports_list, best_countries):
    df = pd.DataFrame({
        "Sport": sports_list,
        "Best country":best_countries
    })
    text = "Best Scandinavian country in Summer Olympic sports, based on most number of Gold medals\n"
    return text+df.to_markdown(index=False)


# Define your own plotting functions and optional helper functions
def plot_sport_specific_stats(
    results: dict[str, dict[str, int]], 
    sport: str,
    output_parent: str | Path | None = None 
) -> None:
    """Plot the number of gold, silver and bronze medals for the scandinavian countries.

    Parameters:
      results (dict[str, dict[str, int]]) : a nested dictionary of country names and the corresponding number of summer and winter
                            gold medals from 'List of NOCs with medals' table.
                            Format:
                            {"country_name": {"Gold" : x, "Silver" : y, "Bronze": z}}
      output_parent (str | Path) : parent file path to save the plot in
    Returns:
      None
    """
    
    countries_list = list(results.keys())
    medals = list(results[countries_list[0]].keys()) # the types of medals
    num_countries = len(countries_list)
    num_medals = len(medals)

    bar_width = 0.2
    index = np.arange(num_countries)

    colors = {'Gold': 'gold', 'Silver': 'silver', 'Bronze': 'brown'}

    for i in range(num_medals):
        medal_counts = [results[country][medals[i]] for country in countries_list]
        bars = plt.bar(index + i * bar_width, medal_counts, bar_width,
                label=medals[i],color=colors[medals[i]])
        plt.bar_label(bars)

    plt.xlabel('Countries')
    plt.ylabel('Number of Medals in '+sport)
    plt.xticks(index, countries_list)

    plt.title(f"Number of medals in {sport} for scandinavian countries in summer Olympic Games")
    # save the figure to a file
    filename = Path(output_parent) / Path(f"{sport}_medal_ranking.png")
    plt.savefig(filename)
    plt.clf()
    

def plot_scandi_stats(
    country_dict: dict[str, dict[str, str | dict[str, int]]],
    output_parent: str | Path | None = None,
) -> None:
    """Plot the number of gold medals in summer and winter games for each of the scandi countries as bars.

    Parameters:
      results (dict[str, dict[str, int]]) : a nested dictionary of country names and the corresponding number of summer and winter
                            gold medals from 'List of NOCs with medals' table.
                            Format:
                            {"country_name": {"Summer" : x, "Winter" : y}}
      output_parent (str | Path) : parent file path to save the plot in
    Returns:
      None
    """
    countries_list = list(country_dict.keys())
    branches = list(country_dict[countries_list[0]]['medals'].keys()) # summer or winter olympics
    num_countries = len(countries_list)
    num_branches = len(branches)

    bar_width = 0.2
    index = np.arange(num_countries)

    colors = {'Summer': 'red', 'Winter': 'blue'}

    for i in range(num_branches):
        medal_counts = [country_dict[country]['medals'][branches[i]] for country in countries_list]
        bars = plt.bar(index + i * bar_width, medal_counts, bar_width,
                label=branches[i],color=colors[branches[i]])
        plt.bar_label(bars)

    plt.xlabel('Countries')
    plt.ylabel('Number of Medals')
    plt.xticks(index, countries_list)

    plt.title("Number of gold medals for scandinavian countries in Olympic Games")
    # save the figure to a file
    filename = Path(output_parent) / Path("total_medal_ranking.png")
    plt.savefig(filename)
    plt.clf()


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
    work_dir = Path(__file__).parent
    report_scandi_stats(url, summer_sports, work_dir)
