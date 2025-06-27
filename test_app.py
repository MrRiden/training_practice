import pytest
from matcher import match_template

def test_matching_queries():
    fields1 = {
        "f_name1": "aaa@bbb.ru",
        "f_name2": "27.05.2025"
    }
    assert match_template(fields1) == "Test" 

    fields2 = {
        "login": "vasya",          
        "f_name1": "aaa@bbb.ru",
        "f_name2": "27.05.2025"
    }
    assert match_template(fields2) == "Test"

def test_non_matching_queries():

    fields = {
        "f_name1": "aaa@bbb.ru"
    }
    result = match_template(fields)
    assert isinstance(result, dict)
    assert result == {"f_name1": "email"}


    fields = {
        "login": "vasya",
        "f_name2": "27.05.2025"
    }
    result = match_template(fields)
    assert isinstance(result, dict)
    assert result == {
        "login": "text", 
        "f_name2": "date"
    }

    fields = {
        "f_name1": "vasya",
        "f_name2": "27.05.2025"
    }
    result = match_template(fields)
    assert isinstance(result, dict)
    assert result == {
        "f_name1": "text",
        "f_name2": "date"
    }


    fields = {
        "f_name1": "27.05.2025",
        "f_name2": "+7 903 123 45 78"
    }
    result = match_template(fields)
    assert isinstance(result, dict)
    assert result == {
        "f_name1": "date",
        "f_name2": "phone" 
    }