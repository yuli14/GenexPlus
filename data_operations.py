def get_data(id, start, end, time_series_dict):
    """

    :param id:
    :param start:
    :param end:
    :param timeSeries: raw time series data

    :return list: return a sub-sequence indexed by id, start point and end point in data
    """
    # TODO should we make timeSeries a dic as well as a list (for distributed computing)

    if id not in time_series_dict.keys():
        raise Exception("data_operations: get_data: subsequnce of ID " + id + " not found in TimeSeries!")
    else:
        return time_series_dict[id][start:end]