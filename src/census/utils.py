"""Services for the census search"""
import re
import math
import asyncio
import lxml
import pandas as pd
from bs4 import BeautifulSoup
from urllib import parse
from aiohttp import ClientSession
from fastapi import HTTPException
from fastapi import status as http_status
from src.census.constants import SEARCH_URL
from src.census.constants import min_page_size, max_page_size
from src.census.schemas import SearchParams



# http://www.census.nationalarchives.ie/search/results.jsp?census_year=1911&surname=&exact=&firstname=&county19011911=&county1821=&county1831=&county1841=&county1851=&townland=&ded=&age=&sex=&relationToHead=&religion=&education=&occupation=&marriageStatus=&marriageYears=&childrenBorn=&childrenLiving=&birthplace=&nativeCountry=&language=&deafdumb=&houseNumber=&familiesNumber=&malesNumber=&femalesNumber=&maleServNumber=&femaleServNumber=&estChurchNumber=&romanCatNumber=&presbNumberDiv=&protNumber=&parish=&barony=&yearsMarried=&causeOfDeath=&yearOfDeath=&familyId=&ageInMonths=&search=Search&sort=&pageSize=100
# http://www.census.nationalarchives.ie/search/results.jsp?
# searchMoreVisible=true
# sort tends to be the field with word Sort after. except sex and age which are just that
# RelevanceSurnameForenameTownland or StreetDEDCountyAgeSex
# &sort=
# &pager.offset=100
# &pageSize=100
# &census_year=1911
# &surname=
# &firstname=
# &county19011911=
# &county1821=
# &county1831=
# &county1841=
# &county1851=
# &barony=
# &parish=
# &ward=
# &townland=
# &houseNumber=
# &familyId=
# &ded=
# &age=
# &sex=
# &search=Search
# &ageInMonths=
# &relationToHead=
# &religion=
# &education=
# &occupation=
# &marriageStatus=
# &yearsMarried=
# &birthplace=
# &nativeCountry=
# &language=
# &deafdumb=
# &causeOfDeath=
# &yearOfDeath=
# &familiesNumber=
# &malesNumber=
# &femalesNumber=
# &maleServNumber=
# &femaleServNumber=
# &estChurchNumber=
# &romanCatNumber=
# &presbNumber=
# &protNumber=
# &marriageYears=
# &childrenBorn=
# &childrenLiving=

async def get_results(search_params: SearchParams):
    """Get the search results"""
    search_params.pageSize = max_page_size
    total_results, num_pages = await get_results_count(search_params)
    print ('total_results', total_results)
    print ('num_pages', num_pages)
    if total_results == 0:
        return []
    if total_results > 1000:
        raise HTTPException(
            status_code=http_status.HTTP_400_BAD_REQUEST,
            detail=f"{total_results} results. Too many results. Max is 1000. Please narrow your search."
        )
    jobs = []
    for i in range(1, num_pages+1):
        search_params.page_offset = (i-1) * max_page_size
        url = make_url(search_params)
        jobs.append(get_html(url))

    pages = await asyncio.gather(*jobs)
    dataframes = []
    for html in pages:
        df = get_df_from_html(html)
        dataframes.append(df)

    all_results_df = pd\
        .concat(dataframes, axis=0, ignore_index=True)\
        .rename(columns=snake_case, inplace=True)\
        .fillna('', inplace=True)
    return all_results_df.to_dict(orient='records')


async def get_results_count(search_params: SearchParams):
    """Get the number of results and the number of pages"""
    url = make_url(search_params, pageSize=10)
    html = await get_html(url)
    pg_start, pg_end, total_results = find_results_info(html)
    num_pages = math.ceil(total_results / max_page_size)
    return total_results, num_pages


def get_df_from_html(html):
    """get a dataframe from the census search results page"""
    df_list = pd.read_html(str(html.find_all('table')))
    df = df_list[0]
    return df


def make_url(search_params, pageSize=None):
    """make a url for the census search page"""
    params = search_params.copy()
    if pageSize:
        params.pageSize = pageSize
    param_str = parse.urlencode(params.dict(exclude_none=True))
    if params.page_offset:
        param_str += f"&pager.offset={params.page_offset}"
    url = f"{SEARCH_URL}?{param_str}"
    print (url)
    return url


def find_results_info(bs4html):
    """
    use regex to get the number of results from string like 
    'Displaying results 1 - 10 of 24'
    """
    results_str = bs4html.find_all(class_="short")[0].text
    regex = re.compile(r"Displaying results (\d+) - (\d+) of (\d+)")
    match = regex.search(results_str)
    if match:
        return int(match.group(1)), int(match.group(2)), int(match.group(3))
    else:
        return 0, 0, 0


def snake_case(s):
    """convert a string to snake_case"""
    return '_'.join(
        re.sub('([A-Z][a-z]+)', r' \1',
        re.sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).replace('/', ' ').split()).lower()



async def get_html(url: str) -> BeautifulSoup:
    """get the html from a url"""
    async with ClientSession() as session:
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
        async with session.get(url, headers=headers) as response:
            text = await response.text()

            if response.status == 200:
                html = BeautifulSoup(markup=text, features="lxml")
                return html

    raise HTTPException(status_code=http_status.HTTP_501_NOT_IMPLEMENTED,
                        detail=f"Scraper didn't succeed in getting data:\n"
                               f"\turl: {url}\n"
                               f"\tstatus code: {response.status}\n"
                               f"\tresponse text: {text}")
