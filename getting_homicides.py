import numpy as np 
import pandas as pd

with open("vancrime.csv") as f:
    data = pd.read_csv(f)

data = data[data["TYPE"] == "Homicide"]

data.to_csv("vanhomi.csv")