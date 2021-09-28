import json

def write_json(root, img_num):
    '''
    split original json file for da
    param: img_num  # of original images used for generation. 
                    # of generated images is supposed to be 5*img_num since 5 captions were given per image
    '''
    with open(f'{root}/dataset_flickr30k.json', 'r') as fin:
        dataset = json.load(fin)
    images = dataset['images'][:img_num]

    dataset_da = {
        'dataset': 'flickr30k_da',
        'images': []
    }
    for img in images:
        for i,s in enumerate(img['sentences']):
            new_img = {
                'sentids': [img['sentids'][i]],
                'imgid': img['imgid'],
                'sentences': [s],
                'split': img['split'],
                'id': f"{img['imgid']}_{i}"
            }
            dataset_da['images'].append(new_img)

    with open(f'{root}/dataset_flickr30k_da.json', 'w') as fout:
        json.dump(dataset_da, fout)

if __name__ == '__main__':
    # root = '/data/private/mxy/code/T2I_CL/DM-GAN+CL/output/coco_DMGAN_2021_08_15_14_19_42/Model/netG_epoch_120/f30k'
    # out_path = '/data/private/mxy/data'
    root = '/data/share/image-caption'
    img_num = 22684
    write_json(root, img_num)