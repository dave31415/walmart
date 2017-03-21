from matplotlib import pylab as plt


def plot_one(d, norm=False):
    """
    :param d: data frame filtered to a single store/dept
    :param norm: if True, will normalize the y-axis
    :return: None
    """
    scale = 1.0
    if norm:
        scale = d.Weekly_Sales.mean()
    plt.plot(d.date, d.Weekly_Sales/scale)


def plot(data, store=1, dept=1, norm=False):
    """
    :param data: data frame unfiltered
    :param store: the desired store
    :param dept: the desired dept
    :param norm: if True, will normalize the y-axis
    :return: None
    """
    store_data = select_store(data, store)
    dept_data = select_dept(store_data, dept)
    plot_one(dept_data, norm=norm)
