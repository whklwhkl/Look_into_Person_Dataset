from PIL import Image


import sys
from tqdm import tqdm
from glob import glob
import os.path as osp

for fp in tqdm(glob(osp.join(sys.argv[1], '*.png'))):
	im = Image.open(fp)
	im = im.convert('L')
	im.save(fp)
