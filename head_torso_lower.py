import cv2

from glob import glob


import sys
import numpy as np
from tqdm import tqdm

if __name__ == '__main__':
	src_dir = sys.argv[1]
	dst_dir = sys.argv[2]
	import os.path as osp
	for s in tqdm(glob(osp.join(src_dir, '*.png'))):
		f, n = osp.split(s)
		c = cv2.imread(s)
		x = np.zeros_like(c)
		x += np.where(c==1, 1, 0).astype(np.uint8)
		x += np.where(c==2, 1, 0).astype(np.uint8)
		x += np.where(c==4, 1, 0).astype(np.uint8)
		x += np.where(c==11, 1, 0).astype(np.uint8)
		x += np.where(c==13, 1, 0).astype(np.uint8)
		x += np.where(c==3, 2, 0).astype(np.uint8)
		x += np.where(c==5, 2, 0).astype(np.uint8)
		x += np.where(c==6, 2, 0).astype(np.uint8)
		x += np.where(c==7, 2, 0).astype(np.uint8)
		x += np.where(c==14, 2, 0).astype(np.uint8)
		x += np.where(c==15, 2, 0).astype(np.uint8)
		x += np.where(c==8, 3, 0).astype(np.uint8)
		x += np.where(c==9, 3, 0).astype(np.uint8)
		x += np.where(c==10, 3, 0).astype(np.uint8)
		x += np.where(c==12, 3, 0).astype(np.uint8)
		x += np.where(c==16, 3, 0).astype(np.uint8)
		x += np.where(c==17, 3, 0).astype(np.uint8)
		x += np.where(c==18, 3, 0).astype(np.uint8)
		x += np.where(c==19, 3, 0).astype(np.uint8)
		x += np.where(c==0, 4, 0).astype(np.uint8)  # others
		d = osp.join(dst_dir, n)
		cv2.imwrite(d, x)
