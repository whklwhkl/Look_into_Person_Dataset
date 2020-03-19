from tqdm import tqdm
from PIL import Image
import json
import os.path as osp

for s in ['train', 'val']:
	f = open(s+'.odgt', 'w')
	for t in tqdm(open(s+'_id.txt').readlines(), desc=s):
		i = t.strip()
		imp = osp.join(s+'_images', i+'.jpg')
		im = Image.open(imp)
		sgp = osp.join(s+'_full_seg', i+'.png')
		w, h = im.size
		d = {'fpath_img':imp, 'fpath_segm':sgp, 'height':h, 'width':w}
		print(json.dumps(d), file=f)
	f.close()
