import json
import pandas as pd

from pyspark.sql import SparkSession
from pyspark.sql import Row

path = "../data/raw_file/11112022_taxi.json"

spark = SparkSession.builder.getOrCreate()

with open(path, 'r') as file:
    load_taxi_file = json.loads(file.read())

df = spark.read.json(path)

df.printSchema()
while False:
    df = pd.DataFrame(load_taxi_file)

    amount = df.amount.apply(pd.Series)
    transaction = df.transaction_info.apply(pd.Series)


while False:
    values = []
    for data in load_taxi_file:
        values.append(pd.DataFrame([data['amount']]))

    amount = pd.concat(values)

    values = []
    for data in load_taxi_file:
        values.append(pd.DataFrame([data['transaction_info']]))

    transaction_info = pd.concat(values)

    print(amount)
    print(transaction_info)
