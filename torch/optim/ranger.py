import torch, math
from .optimizer import Optimizer, required
import itertools as it
from .lookahead import *
from .radam import *

def Ranger(params, alpha=0.5, k=6, *args, **kwargs):
     radam = RAdam(params, *args, **kwargs)
     return Lookahead(radam, alpha, k)
