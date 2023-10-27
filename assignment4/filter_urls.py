"""
Task 1.2, 1.3

Filtering URLs from HTML
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str | None = None,
) -> set[str]:
    """
    Find all the url links in a html text using regex

    Arguments:
        html (str): html string to parse
        base_url (str): the base url to the wikipedia.org pages
        output (Optional[str]): file to write to if wanted
    Returns:
        urls (Set[str]) : set with all the urls found in html text
    """
    # create and compile regular expression(s)
    a_pat = re.compile(r'<a[^>]+>', flags=re.IGNORECASE)
    href_pat = re.compile(r'href="([^"]+)"', flags=re.IGNORECASE)
    stripped_pat = re.compile(r'(.*?)(#|$)', flags=re.IGNORECASE)
    protocol_pat = re.compile(r'.*(?=\/\/)', flags=re.IGNORECASE)
    url_set = set()

    # 1. find all the anchor tags, then
    urls = a_pat.findall(html)

    for url in urls:
        # 2. find the urls href attributes
        match = href_pat.search(url)
        if match:
            # find the url, without #
            my_url_match = stripped_pat.search(match.group(1))

            if my_url_match:
                my_url = my_url_match.group(1)
                # if the match is an empty string, it means that there is no url
                if my_url == '':
                    continue

                # if the match conatins two // in a row, it means that it is a
                # protocol relative url. 
                elif len(my_url) >= 2 and (my_url[0] == '/' and my_url[1] == '/'):
                    protocol_match = protocol_pat.findall(base_url)
                    if protocol_match:
                        url_set.add(protocol_match[0]+my_url)
                
                # if it is only one /, it means that is a relative url
                elif my_url[0] == '/':
                    url_set.add(base_url+my_url)
                # else it is a "normal" url
                else:
                    url_set.add(my_url)

    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        with open(output,"w") as out_file:
            for url in url_set:
                out_file.write(url+"\n")

    return url_set

def find_all_articles(html: str, language: str, output: str | None = None) -> set[str]:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
        - output (str, optional): the file to write the output to if wanted
    returns:
        - (Set[str]) : a set with urls to all the articles found
    """
    urls = find_urls(html=html,output=output)
    pattern = re.compile(rf'\b{language}wikipedia.org\/wiki\b(?!.*:)')
    articles = {url for url in urls if pattern.search(url)}

    # Write to file if wanted
    if output:
        with open(output,"w") as out_file:
            for url in articles:
                out_file.write(url+"\n")
    return articles

def find_articles(html: str, output: str | None = None) -> set[str]:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
        - output (str, optional): the file to write the output to if wanted
    returns:
        - (Set[str]) : a set with urls to all the articles found
    """
    return find_all_articles(html,"",output)


def find_english_articles(html: str, output: str | None = None) -> set[str]:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
        - output (str, optional): the file to write the output to if wanted
    returns:
        - (Set[str]) : a set with urls to all the articles found
    """
    return find_all_articles(html,"en.",output)


## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attribute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
    return src_set
