from enum import Enum
from typing import Optional, Any
from pydantic import BaseModel, Field
from src.census.constants import CensusYears, Counties


class SearchParams(BaseModel):
    search: str = "Search"
    pageSize: int = None
    page_offset: int = None
    census_year: CensusYears = Field(..., example="1901")
    surname: Any = Field(example=None)
    firstname: Any = None
    barony: Any = None
    parish: str = None
    ward: str = None
    townland: str = None
    houseNumber: str = None
    familyId: str = None
    ded: str = None
    age: str = None
    sex: str = None
    relationToHead: str = None
    religion: str = None
    education: str = None
    occupation: str = None
    marriageStatus: str = None
    yearsMarried: str = None
    birthplace: str = None
    nativeCountry: str = None
    language: str = None
    deafdumb: str = None
    causeOfDeath: str = None
    yearOfDeath: str = None
    familiesNumber: str = None
    malesNumber: str = None
    familiesNumber: str = None
    maleServNumber: str = None
    femaleServNumber: str = None
    estChurchNumber: str = None
    romanCatNumber: str = None
    presbNumber: str = None
    protNumber: str = None
    marriageYears: str = None
    childrenBorn: str = None
    childrenLiving: str = None

    def dict(self, *args, **kwargs) -> 'dict[str, Any]':
        """
            Override the default dict method to exclude None values in the response
        """
        dict = super().dict(*args, **kwargs)
        dict = {k: v for k, v in dict.items() if v != 'string'}
        if dict['census_year']:
            dict['census_year'] = dict['census_year'].value
        return dict

