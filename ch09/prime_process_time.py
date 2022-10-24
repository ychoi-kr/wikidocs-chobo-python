import sys
import os
import importlib
from glob import glob
from time import process_time


N = 2 ** 12
#N = 2 ** 13

sys.path.append('../ch04')
os.chdir('../ch04')

for pth in glob('prime*'):
    name = os.path.splitext(pth)[0]
    print(f'\nRunning {pth} ...')
    mod = importlib.import_module(name)
    
    start = process_time()
    mod.prime(N)
    end = process_time()
    print('elapsed:', end - start)

