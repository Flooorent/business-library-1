from pyspark.sql import SparkSession
from business_library_1.transformations import add_1


def test_add_1():
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame([[2.8, 3.1], [0.0, 20.2]]).toDF("x", "y")
    actual_df = add_1(df, "x")

    expected_df = spark.createDataFrame(
        [
            [3.8, 3.1],
            [1.0, 20.2],
        ]
    ).toDF("x", "y")

    assert actual_df.collect() == expected_df.collect()
