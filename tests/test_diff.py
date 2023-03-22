import pytest
from gendiff.generate_diff import generate_diff


json1 = 'tests/fixtures/file1.json'
json2 = 'tests/fixtures/file2.json'
yml1 = 'tests/fixtures/file1.yml'
yml2 = 'tests/fixtures/file2.yml'
result_stylish = 'tests/fixtures/result_stylish'
result_plain = 'tests/fixtures/result_plain'
result_json = 'tests/fixtures/result_json'

formaters = ['stylish', 'plain', 'json']


@pytest.mark.parametrize('file1, file2, result, format_name',
                         [(json1, json2, result_stylish, formaters[0]),
                          (json1, json2, result_plain, formaters[1]),
                          (json1, json2, result_json, formaters[2]),
                          (yml1, yml2, result_stylish, formaters[0]),
                          (yml1, yml2, result_plain, formaters[1]),
                          (yml1, yml2, result_json, formaters[2])])
def test_gendiff(file1, file2, result, format_name):
    with open(result) as res:
        assert generate_diff(file1, file2, format_name) == res.read()
