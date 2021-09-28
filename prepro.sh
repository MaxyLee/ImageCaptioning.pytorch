set -ex

DATA_ROOT=/data/share/image-caption
MODEL=/data/private/mxy/data/image-caption

# original
JSON=$DATA_ROOT/dataset_flickr30k.json
OUT_DIR=$DATA_ROOT/f30ktalk
IMG_ROOT=/data/share/UNITER/origin_imgs/flickr30k/flickr30k-images

# da
# JSON_DA=$DATA_ROOT/dataset_coco.json
JSON_DA=$DATA_ROOT/dataset_coco_lostgan_sub.json
# JSON_DA=/data/share/data/coco2017/annotations/dataset_coco_lostgan.json # sub
OUT_DIR_DA=$DATA_ROOT/cocotalk_da_lostgan_sub
# IMG_ROOT_DA=/data/private/mxy/code/T2I_CL/DM-GAN+CL/output/coco_DMGAN_2021_08_15_14_19_42/Model/netG_epoch_120/f30k
# IMG_ROOT_DA=/data/share/Seg-Backtranslation/data/gen_imgs/train2017_2
# IMG_ROOT_DA=/data/share/Seg-Backtranslation/data/gen_imgs_lostgan_train
IMG_ROOT_DA=/data/share/Seg-Backtranslation/data/gen_imgs_lostgan_train_sub
LBL_JSON_DA=$DATA_ROOT/cocotalk_da_lostgan_sub.json
LBL_H5_DA=$DATA_ROOT/cocotalk_da_lostgan_sub

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