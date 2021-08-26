set -ex

DATA_ROOT=/data/share/image-caption
MODEL=/data/private/mxy/data/image-caption

# original
JSON=$DATA_ROOT/dataset_flickr30k.json
OUT_DIR=$DATA_ROOT/f30ktalk
IMG_ROOT=/data/share/UNITER/origin_imgs/flickr30k/flickr30k-images

# da
JSON_DA=$DATA_ROOT/dataset_flickr30k_da.json
OUT_DIR_DA=$DATA_ROOT/f30ktalk_da
IMG_ROOT_DA=/data/private/mxy/code/T2I_CL/DM-GAN+CL/output/coco_DMGAN_2021_08_15_14_19_42/Model/netG_epoch_120/f30k
LBL_JSON_DA=$DATA_ROOT/f30ktalk_da.json
LBL_H5_DA=$DATA_ROOT/f30ktalk_da

# pre labels for da
python scripts/prepro_labels_da.py \
    --input_json $JSON_DA \
    --output_json $LBL_JSON_DA \
    --output_h5 $LBL_H5_DA

# pre ngram for da
# python scripts/prepro_ngrams.py \
#     --input_json $JSON_DA \
#     --dict_json $LBL_JSON_DA \
#     --output_pkl $DATA_ROOT/f30k_da-train \
#     --split train


# pre feats for da
# python scripts/prepro_feats_da.py \
#     --input_json $JSON_DA \
#     --output_dir $OUT_DIR_DA \
#     --images_root $IMG_ROOT_DA \
#     --model_root $MODEL

# pre feats
# python scripts/prepro_feats.py \
#     --input_json $JSON \
#     --output_dir $OUT_DIR \
#     --images_root $IMG_ROOT \
#     --model_root $MODEL