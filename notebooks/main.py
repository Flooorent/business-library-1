# Databricks notebook source

from pyspark.sql import functions as F

from business_library_1.transformations import add_1
from shared_library_1.feature_engineering import sum_cols


data = spark.createDataFrame([[2.8, 3.1], [0.0, 20.2]]).toDF("x", "y")
data = sum_cols(data, "x", "y")
data = add_1(data, "sum_x_y")

data.show()
