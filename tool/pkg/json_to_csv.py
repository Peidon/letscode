import pandas as pd
import json

if __name__ == '__main__':
    # Reading JSON data from a file
    with open("holidays.json", "r") as f:
        json_data = json.load(f)

    # Converting JSON data to a pandas DataFrame
    for k, v in json_data.items():
        df = pd.json_normalize(v)
        df.to_csv("{0}.csv".format(k), index=False)
