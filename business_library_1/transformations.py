from pyspark.sql import functions as F


def add_1(df, col1):
    return df.withColumn(col1, F.col(col1) + 1)
