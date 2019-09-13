htl:
	unzip -o TrainVal_parsing_annotations.zip
	unzip TrainVal_parsing_annotations.zip
	unzip -o TrainVal_parsing_images.zip
	unzip TrainVal_parsing_images.zip
	python head_torso_lower.py train_segmentations train_htl_seg
	python head_torso_lower.py val_segmentations val_htl_seg
	python to_grayscale.py train_htl_seg
	python to_grayscale.py val_htl_seg
	python gen_odgt.py

zip:
	zip -u LIP.zip train.odgt val.odgt
	zip -r LIP.zip train_htl_seg val_htl_seg train_images val_images
