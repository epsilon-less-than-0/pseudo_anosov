from traintrack import *
from sage.combinat.permutation import Permutations
import copy

from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from is_traintrack_in_list import *



G = Graph({0:[0,3],1:[1,6],2:[2,5],3:[0,3,4],4:[3,5,6],5:[4,2,6],6:[1,4,5]}) 
order = {0:[(0,3),(0,0)],1:[(1,6),(1,1)],2:[(2,2),(2,5)],3:[(3,3),(0,3),(3,4)],4:[(3,4),(4,5),(4,6)],5:[(4,5),(2,5),(5,6)],6:[(4,6),(5,6),(1,6)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3])],"unmarked":[(3,[4,5,6])]}
singularity_type = {"marked":[1,1,1,1],"unmarked":[3],"boundary":[1]}
c = cusp(3,((3,4),(0,3)))
cusps_list = [c]
side_swapping = [(0,0),(3,3),(1,1),(2,2)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)


G_copy = Graph({0:[0,3],1:[1,6],2:[2,5],3:[0,3,4],4:[3,5,6],5:[4,2,6],6:[1,4,5]}) 
order_copy = {0:[(0,3),(0,0)],1:[(1,6),(1,1)],2:[(2,2),(2,5)],3:[(3,3),(0,3),(3,4)],4:[(3,4),(4,5),(4,6)],5:[(4,5),(2,5),(5,6)],6:[(4,6),(5,6),(1,6)]}
infpoly_copy = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3])],"unmarked":[(3,[4,5,6])]}
singularity_type_copy = {"marked":[1,1,1,1],"unmarked":[3],"boundary":[1]}
c_copy = cusp(3,((3,4),(0,3)))
cusps_copy = [c_copy]
side_swapping_copy = [(0,0),(3,3),(1,1),(2,2)]



T_copy = StandardTrainTrack(G_copy,cusps_copy, order_copy,singularity_type_copy ,infpoly_copy,side_swapping_copy)