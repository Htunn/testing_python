def test_nested_dictionaries(): 
    result = {'first': 12, 'second': 13,'others': {'success': True, 'msg': 'A success message!'}}
    expected = {'first': 12, 'second': 13,'others': {'success': True, 'msg': 'A sucess message!'}}
    assert result == expected
