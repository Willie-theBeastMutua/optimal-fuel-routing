import pandas as pd
from pathlib import Path

FUEL_DF = None

def load_fuel_prices():
    global FUEL_DF
    if FUEL_DF is None:
        path = Path(__file__).resolve().parents[2] / "fuel-prices-for-be-assessment.csv"
        FUEL_DF = pd.read_csv(path)
    return FUEL_DF
