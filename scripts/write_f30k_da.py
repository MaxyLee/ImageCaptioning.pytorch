import json

def write_json(root, img_num):
    '''
    split original json file for da
    param: img_num  # of original images used for generation. 
                    # of generated images is supposed to be 5*img_num since 5 captions were given per image
    '''
    with open(f'{root}/dataset_flickr30k.json', 'r') as fin:
        dataset = json.load(fin)
    images = dataset['images']

    dataset_da = {
        'dataset': 'flickr30k_da',
        'images': images[:img_num]
    }

    with open(f'{root}/dataset_flickr30k_da.json', 'w') as fout:
        json.dump(dataset_da, fout)

if __name__ == '__main__':
    # root = '/data/private/mxy/code/T2I_CL/DM-GAN+CL/output/coco_DMGAN_2021_08_15_14_19_42/Model/netG_epoch_120/f30k'
    # out_path = '/data/private/mxy/data'
    root = '/data/share/image-caption'
    img_num = 22685
    write_json(root, img_num)