import pytest
import pandas as pd
@pytest.fixture(scope="session")
def data():
    df = pd.read_csv("content/RSE_Juelich/day3/reproducible-research-project/data/clean/clean.csv")
    return df