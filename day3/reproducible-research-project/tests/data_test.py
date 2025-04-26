import pytest
def test_clean_data(data):
    assert data.isna().sum().sum() == 0, "Data contains missing values"
    
def test_number_of_row(data):
    assert len(data) == 909, "Data does not have the expected number of rows"