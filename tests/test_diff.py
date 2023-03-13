import pytest
from gendiff.generate_diff import generate_diff
from gendiff.data import prepare_data


json1 = 'tests/fixtures/file1.json'
json2 = 'tests/fixtures/file2.json'
result_json = 'tests/fixtures/result_json.json'


@pytest.mark.parametrize(
                        'file1, file2, result', 
                        [(json1, json2, result_json)]
)
def test_gendiff(file1, file2, result):
    with open(result) as res:
        assert generate_diff(file1, file2) == res.read()
