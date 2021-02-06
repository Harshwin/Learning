from os import environ

from pyspark.sql import SparkSession


def initialize_Spark():

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("simple etl job") \
        .getOrCreate()

    return spark

def loadDFWithoutSchema(spark):

    df = spark.read.format("csv").option("header", "true").load(environ["HOME"] + "E:\projects\Learning\spark\SparkScalaCourse\data\realestate.csv")

    return df

def clean_drop_data(df):

    df_dropped = df.drop("dateCrawled","nrOfPictures","lastSeen")
    df_filtered = df_dropped.where(col("seller") != "gewerblich")
    df_dropped_seller = df_filtered.drop("seller")
    df_filtered2 = df_dropped_seller.where(col("offerType") != "Gesuch")
    df_final = df_filtered2.drop("offerType")

    return df_final


data = loadDFWithoutSchema(initialize_Spark)
