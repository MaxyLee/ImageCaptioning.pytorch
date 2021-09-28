import os
import copy
import json

def write_json_fs(root, ratio):
    '''
    write json for fewshot
    '''
    with open(f'{root}/dataset_coco.json', 'r') as fin:
        dataset = json.load(fin)
    images = dataset['images']

    num_imgs = int(len(images) * ratio)

    dataset_da = {
        'dataset': f'coco_da_{ratio}',
        'images': [],
    }

    i = 0
    for img in images:
        if img['split'] == 'train' or img['split'] == 'restval':
            dataset_da['images'].append(img)
            i += 1
            if i == num_imgs:
                break

    with open(f'{root}/dataset_coco_fs.json', 'w') as fout:
        json.dump(dataset_da, fout)

def write_json_lostgan(root, img_root):
    '''
    write json for LostGAN which only generate about 70k images
    '''
    with open(f'/data/share/data/coco2017/annotations/dataset_coco_lostgan.json', 'r') as fin:
        dataset = json.load(fin)
    images = dataset['images']

    dataset_da = {
        'dataset': f'coco_da_lostgan',
        'images': [],
    }

    for img in images:
        img_name = f"{img_root}/{str(img['cocoid']).zfill(12)}.jpg"
        if os.path.isfile(img_name):
            new_img = copy.deepcopy(img)
            new_img['sentences'] = [img['sentences']]
            dataset_da['images'].append(new_img)

    print(f"wrote {len(dataset_da['images'])} images")

    with open(f'{root}/dataset_coco_lostgan_sub.json', 'w') as fout:
        json.dump(dataset_da, fout)

def write_json(root, ratio):
    '''
    write json for da
    param: ratio  # of synthetic data / # of real data
                  1:1 or 2:1 or 5:1 as usual
    '''
    with open(f'{root}/dataset_coco.json', 'r') as fin:
        dataset = json.load(fin)
    images = dataset['images']

    dataset_da = {
        'dataset': f'coco_da_{ratio}',
        'images': copy.deepcopy(images),
    }

    for i in range(1, ratio):
        for img in images:
            new_img = copy.deepcopy(img)
            new_img['cocoid'] = f"{img['cocoid']}_{i}"
            dataset_da['images'].append(new_img)

    with open(f'{root}/dataset_coco_da_{ratio}.json', 'w') as fout:
        json.dump(dataset_da, fout)

if __name__ == '__main__':
    root = '/data/share/image-caption'
    img_root = '/data/share/Seg-Backtranslation/data/gen_imgs_lostgan_train_sub'
    # ratio = 0.1
    # write_json_fs(root, ratio)
    write_json_lostgan(root, img_root)