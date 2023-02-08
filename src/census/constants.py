from enum import Enum

BASE_URL = "http://www.census.nationalarchives.ie"
SEARCH_URL = f"{BASE_URL}/search/results.jsp"

min_page_size = 10

max_page_size = 100

relation_to_head = [
    "Head of Family", "Wife", "Son", "Daughter", "Father", "Mother", "Sister", 
    "Brother", "Uncle", "Aunt", "Nephew", "Niece", "Cousin", "Grandfather", "Grandmother", 
    "Grandson", "Granddaughter", "Son-in-law", "Daughter-in-law", "Lodger", "Boarder", 
    "Servant", "Visitor", "Other"
]

religion = [
    "Roman Catholic", "Church of Ireland", "Church of England", "Church of Scotland", 
    "Presbyterian", "Methodist", "Independent", "Baptist", "Society of Friends/Quaker", 
    "Jew", "Plymouth Brethren", "Information refused", "Other",
]

literacy = [
    "Cannot read or write", "Can read only", "Can read and write", "Other",
]

marital_status = ["Married", "Single", "Widow", "Widower", "Other",]

country_of_origin = [
    "America", "Australia", "Austria", "Belgium", "Bulgaria", "Canada", "China", "Croatia", 
    "Denmark", "England", "France", "Germany", "Greece", "Hungary", "India", "Italy", 
    "Luxembourg", "Netherlands", "Norway", "Portugal", "Romania", "Russia", "Scotland", 
    "Serbia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", 
    "United States", "Wales",
]

language_proficieny = ["Irish", "English",  "Irish and English", "Other",]

specified_illnesses = ["Deaf", "Dumb", "Deaf and Dumb", "Blind", "Idiot", "Imbecile", "Lunatic", "Other",]

sex = ["Male", "Female"]

census_years = ["1821", "1831", "1841", "1851", "1901", "1911"]

class CensusYears(str, Enum):
    Y1821 = "1821"
    Y1831 = "1831"
    Y1841 = "1841"
    Y1851 = "1851"
    Y1901 = "1901"
    Y1911 = "1911"

class Counties(str):
    ANTRIM = "Antrim"
    ARMAGH = "Armagh"
    CARLOW = "Carlow"
    CAVAN = "Cavan"
    CLARE = "Clare"
    CORK = "Cork"
    DONEGAL = "Donegal"
    DOWN = "Down"
    DUBLIN = "Dublin"
    FERMANAGH = "Fermanagh"
    GALWAY = "Galway"
    KERRY = "Kerry"
    KILDARE = "Kildare"
    KILKENNY = "Kilkenny"
    KINGS = "King's Co."
    KINGS1821 = "King's"
    LAOIS = "Laois"
    LEITRIM = "Leitrim"
    LIMERICK = "Limerick"
    LONDONDERRY = "Londonderry"
    LONGFORD = "Longford"
    LOUTH = "Louth"
    MAYO = "Mayo"
    MEATH = "Meath"
    MONAGHAN = "Monaghan"
    OFFALY = "Offaly"
    QUEENS = "Queen's Co."
    QUEENS1851 = "Queen's"
    ROSCOMMON = "Roscommon"
    SLIGO = "Sligo"
    TIPPERARY = "Tipperary"
    TYRONE = "Tyrone"
    WATERFORD = "Waterford"
    WESTMEATH = "Westmeath"
    WEXFORD = "Wexford"
    WICKLOW = "Wicklow"


class CensusYearCounties():
    Y1911 = [
        Counties.ANTRIM,
        Counties.ARMAGH,
        Counties.CARLOW,
        Counties.CAVAN,
        Counties.CLARE,
        Counties.CORK,
        Counties.DONEGAL, 
        Counties.DOWN,
        Counties.DUBLIN,
        Counties.FERMANAGH,
        Counties.GALWAY,
        Counties.KERRY,
        Counties.KILDARE, 
        Counties.KILKENNY,
        Counties.KINGS,
        Counties.LEITRIM, 
        Counties.LIMERICK,
        Counties.LONDONDERRY,
        Counties.LONGFORD,
        Counties.LOUTH,
        Counties.MAYO,
        Counties.MEATH, 
        Counties.MONAGHAN,
        Counties.QUEENS,
        Counties.ROSCOMMON,
        Counties.SLIGO,
        Counties.TIPPERARY,
        Counties.TYRONE,
        Counties.WATERFORD,
        Counties.WESTMEATH,
        Counties.WEXFORD,
        Counties.WICKLOW, 
    ]

    Y1901 = Y1911

    Y1851 = [
        Counties.ANTRIM,
        Counties.ARMAGH,
        Counties.CAVAN,
        Counties.CLARE,
        Counties.DONEGAL, 
        Counties.DOWN,
        Counties.DUBLIN,
        Counties.FERMANAGH,
        Counties.KERRY,
        Counties.KILDARE, 
        Counties.LEITRIM, 
        Counties.LIMERICK,
        Counties.LONDONDERRY,
        Counties.LONGFORD,
        Counties.MAYO,
        Counties.MEATH, 
        Counties.MONAGHAN,
        Counties.QUEENS1851,
        Counties.ROSCOMMON,
        Counties.SLIGO,
        Counties.TIPPERARY,
        Counties.TYRONE,
        Counties.WATERFORD,
        Counties.WEXFORD,
        Counties.WICKLOW,   
    ]

    Y1841 = [
        Counties.ANTRIM,
        Counties.CARLOW,
        Counties.CAVAN,
        Counties.CORK,
        Counties.DUBLIN,
        Counties.FERMANAGH,
        Counties.LIMERICK,
        Counties.LONGFORD,
        Counties.MAYO,
        Counties.MONAGHAN,
        Counties.QUEENS1851,
        Counties.TYRONE,
        Counties.WESTMEATH,
        Counties.WICKLOW, 
    ]

    Y1831 = [
        Counties.ANTRIM,
        Counties.LONDONDERRY
    ]

    Y1821 = [
        Counties.ANTRIM,
        Counties.CARLOW,
        Counties.CAVAN,
        Counties.DUBLIN,
        Counties.FERMANAGH,
        Counties.GALWAY,
        Counties.KILKENNY,
        Counties.KINGS1821,
        Counties.LIMERICK,
        Counties.MAYO,
        Counties.MEATH,
    ]

        # Counties.ANTRIM,
        # Counties.ARMAGH,
        # Counties.CARLOW,
        # Counties.CAVAN,
        # Counties.CLARE,
        # Counties.CORK,
        # Counties.DONEGAL, 
        # Counties.DOWN,
        # Counties.DUBLIN,
        # Counties.FERMANAGH,
        # Counties.GALWAY,
        # Counties.KERRY,
        # Counties.KILDARE, 
        # Counties.KILKENNY,
        # Counties.KINGS,
        # Counties.KINGS1821,
        # Counties.LAOIS,
        # Counties.LEITRIM, 
        # Counties.LIMERICK,
        # Counties.LONDONDERRY,
        # Counties.LONGFORD,
        # Counties.LOUTH,
        # Counties.MAYO,
        # Counties.MEATH, 
        # Counties.MONAGHAN,
        # Counties.OFFALY,
        # Counties.QUEENS,
        # Counties.ROSCOMMON,
        # Counties.SLIGO,
        # Counties.TIPPERARY,
        # Counties.TYRONE,
        # Counties.WATERFORD,
        # Counties.WESTMEATH,
        # Counties.WEXFORD,
        # Counties.WICKLOW, 