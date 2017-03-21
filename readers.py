"""
Walmart public sales data from Kaggle
https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data
Aggregated by Store/Dept/Week

Utilities for reading the data and building useful data structures
"""

import pandas as pd


data_dir = "/Users/davej/data"


def read_purchases():
    """
    Read the purchase data
    :return: panda dataframe of purchase data
    """
    file = "%s/train.csv" % data_dir
    data = pd.read_csv(file)
    data['date'] = pd.to_datetime(data.Date)
    return data


def select_store(data, store):
    """
    Selects a store
    :param data: the entire data frame
    :param store: the desired store number [1 - 45]
    :return: the filtered data frame
    """
    assert 1 <= store <= 45
    d = data[data.Store == store]
    print("%s depts at store:%s" % (d.size, store))
    return d


def select_dept(data, dept):
    """
    Selects a depratment after store has been selected
    :param data: the data frame, filtered to be a single store
    :param dept: the desired department
    :return: the filtered data frame of a single store and department
    """
    d = data[data.Dept == dept]
    store = list(set(d.Store))
    assert len(store) == 1
    store = store[0]
    print("%s dates at store: %s,  dept: %s" % (d.size, store, dept))
    return d

def make_