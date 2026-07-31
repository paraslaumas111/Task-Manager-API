import pandas as pd

data = {
    "Customer": ["asd'","asd'"],
    "Income": [50000, 70000, 60000],
    "Loan": [20000, 40000, 30000]
}
print(pd.DataFrame(data))
