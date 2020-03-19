full:
	cp -r train_segmentations train_full_seg
	cp -r val_segmentations val_full_seg
	python to_grayscale.py train_full_seg
	python to_grayscale.py val_full_seg
	ls val_full_seg/|cut -d. -f1 > val_id.txt
	ls train_full_seg/|cut -d. -f1 > train_id.txt
	python gen_odgt.py

zip:
	zip -u LIP.zip train.odgt val.odgt
	zip -r LIP.zip train_full_seg val_full_seg train_images val_images
