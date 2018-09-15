import pyexcel
from collections import OrderedDict
# 1. Prepare data

data = [
    {
        "name": "Huy",
        "city": "Hanoi",
        "age": 29,
    },
    {
        "name": "Quan",
        "city": "Hanoi",
        "age": 19,
    },
    {
        "name": "Duc",
        "city": "Hanoi",
        "age": 18,
    },
]

# 2. Save
data = [OrderedDict(item) for item in data]
pyexcel.save_as(records=data, dest_file_name="sample.xlsx")