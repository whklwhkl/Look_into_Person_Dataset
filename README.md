# Using LIP as Body Part Segmentation Dataset

## setting up
This repo contains code for dataset preparition, which converts the fine-grained LIP dataset into a coarse one to serve the purpose of part-based ReID.
0. `git clone` and `cd` into the folder

1. download the images and annotations to the folder
	>https://drive.google.com/open?id=0BzvH3bSnp3E9cVl3b3pKdmFlclE 

	>https://drive.google.com/open?id=15tifhBogDs_oBUKaUf362vzZTlIdzktv
2. run the following commands in the terminal
	```bash
	make
	```
3. (optional) packing things up by `make zip`, and a `LIP.zip` file would show up

## usage
Each line of those `.odgt` is formatted with **json**. The keys are:
`fpath_img`, `fpath_segm`, `height`, `width`
File paths are relative paths to the `.odgt` files.

## annotations

For each pixel in the `.png` annotations

- `1`: head
- `2`:torso
- `3`:lower body
- `4`:background