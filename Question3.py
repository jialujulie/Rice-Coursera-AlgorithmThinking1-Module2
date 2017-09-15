# compare targeted_order and fast_targeted_order
import Question1_randomattachorder
import urllib2
import random
import time
import math
import Project2_BFS
import matplotlib.pyplot as plt

running_times = []
running_times_fast = []
for n in range(10,1000,10):
    graph_UPA = Question1_randomattachorder.UPA(n,5)
    time0 = time.time()
    Question1_randomattachorder.targeted_order(graph_UPA)
    time1 = time.time()

    running_times.append(time1-time0)

    time0_fast = time.time()
    Question1_randomattachorder.fast_targeted_order(graph_UPA)
    time1_fast = time.time()

    running_times_fast.append(time1_fast-time0_fast)

# Plotting
plt.plot(list(range(10,1000,10)),running_times,'-r',label = 'targeted_order')
plt.plot(list(range(10,1000,10)),running_times_fast,'-b', label = 'fast_targeted_order')
plt.legend(loc = 'upper right')

plt.title('Efficiency Comparision of two algorithms for generating targeted order-desktop python')
plt.xlabel('Number of Nodes of graphs')
plt.ylabel('Running times')
#plt.scatter(indegree_distribution.keys(),normalize_dist)

plt.show()