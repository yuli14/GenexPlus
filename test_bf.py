import random

import matplotlib.pyplot as ply
import numpy

from brute_force import best_match_ts
from data_operations import normalize_ts_with_min_max
from group_operations import generate_source


def generate_ts():
    random_number = []
    result = dict()
    for i in range(2):
        random_val = numpy.random.uniform(1000, 20000)
        for j in range(280):
            random_number.append(numpy.random.uniform(random_val, (random_val + 1000)))

        result["random_ts_ID_" + str(i)] = random_number
        random_number = []
    return result


def generate_query():
    result = []

    random_val = numpy.random.uniform(1000, 20000)

    for i in range(numpy.random.randint(20, 280)):
        result.append(numpy.random.uniform(random_val, (random_val + 1000)))

    return result


# test_ts = generate_ts()
# test_query = generate_query()
#
# match_result = best_match_ts(test_query, test_ts)
#
# plt.figure(figsize=(15, 15))
# plt.plot(match_result['value'], label='match result')
# plt.plot(test_query, label='test query')
# plt.show()

# Prepare test ts and query
features_to_append = [0, 1, 2, 3, 4]
res_list, time_series_dict, global_min, global_max = generate_source('2013e_001_2_channels_02backs.csv',
                                                                     features_to_append)

normalized_ts_dict = normalize_ts_with_min_max(time_series_dict, global_min, global_max)


def generate_query_v2(ts_dict, amount=5):
    query_results = []
    for i in range(amount):
        query_id, query_raw_ts = random.choice(list(ts_dict.items()))
        start = (i + 1) * 2
        query_sequence = query_raw_ts[start:numpy.random.randint(low=start + 5, high=len(query_raw_ts) // 2)]

        query_results.append(query_sequence)

    return query_results


query_set = generate_query_v2(normalized_ts_dict, 3)

amount = 0

for each in query_set:
    amount += 1
    ply.figure()
    ply.title("query " + str(amount))
    ply.plot(each)
    ply.show()

    match_set = best_match_ts(each, normalized_ts_dict)

    for i in range(len(match_set)):
        match_ts_dict = match_set[i]

        ply.figure(i)
        ply.title("match_ts " + str(i + 1))
        ply.plot(match_ts_dict['value'])
        ply.show()
