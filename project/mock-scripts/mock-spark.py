import h5py
import sys
from pyspark.sql import *
from pyspark import SparkContext, SQLContext
import os
import numpy as np

if __name__ == "__main__":
    """
    Usage: doit [partitions]
    """
    sc = SparkContext()
    sqlContext = SQLContext(sc)
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2

    #################################################
    # read a dataset and return it as a Python list #

    def f(x):
        print(x)
        with h5py.File(x) as f:
            a = list(f['/analysis/songs'])
            b = list(f['/metadata/songs'])[0][9]
            c = list(f['/musicbrainz/songs'])[0][1]
            # result = a + b + c
            return list([np.asscalar(b), np.asscalar(c)])

    ################################################

    file_paths = sc.textFile("datasets.csv")

    rdd = file_paths.flatMap(f)

    # # # convert to dataframe
    counts = sqlContext.createDataFrame(rdd.map(lambda wc: Row(singer=wc)))

    # view the content of the dataframe
    counts.show()

    # rdd.map(lambda x: (x, )).toDF()

    # for x in rdd.collect():
    #     print("flag")
    #     print(x)

    # print(rdd.histogram(10))
    sc.stop()
