#!/usr/bin/python

"""plotting graph with python3"""

import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd


def pygraph(booktoread):


    pd.read_excel(booktoread,sheet_name="Sheet1")
    menMeans = mdf["Minutes"]
    menMeans = tuple(menMeans.values)

    quarters = mdf["Quarter"]
    quarters = tuple(quarters.values)

    N = 4
    menMeans = (20, 35, 30, 35)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.30      # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width) #these are the blebottom values

    plt.ylabel('outage minutes')
    plt.title('outage Minutes per Quarter')
    plt.xticks(ind, quarters)
    plt.yticks(np.arange(0, 201,15))
    plt.legend((p1[0],), ('Minutes',))


    now=datetime.datetime.now()
    plt.savefig(now.strftime("%Y-%m-%d-outage.png"))
    plt.show()

