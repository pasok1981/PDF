import json
import statistics

from itertools import groupby
from pickling import read_json

def get_stats(_filename):
    ranks = read_json(_filename)
    l = [val for val in ranks.values()]
    
    print("Mean is: {}".format(statistics.mean(l)))
    print("Median is: {}".format(statistics.median(l)))
    print("Media grouped is {}".format(statistics.median_grouped(l)))
    print("Std dev. is: {}".format(statistics.stdev(l)))
    print("Variance is: {}".format(statistics.variance(l)))

    ranks = list(dict.fromkeys(l))
    groups = [len(list(group)) for key, group in groupby(l)]
    zipped = list(zip(ranks, groups))

    sum_p, sum_f = sum(count for grade, count in zipped if grade>=5), sum(count for grade, count in zipped if grade<5)
 
    #First rank then sum for each one.
    print("Rank->Count: {}".format(zipped))
    print("Passed: {}".format(sum_p))
    print("Next Semester: {}".format(sum_f))
    print("Pass rate: {:.2f}".format((sum_p/sum(groups))*100.0))
    
if __name__ == "__main__":
    get_stats('./ranksSWE19.json')