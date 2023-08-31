from encoder_decoder import encoder
from encoder_decoder import decoder
from encoder_decoder import autoencoder
from code_construction import test_image_reconstruction
import torch
import torchvision.transforms as transforms 
import torchvision.datasets as Datasets
import matplotlib.pyplot as plt
import numpy as np
# class encoder_code:
def unique_code_files(img_codes):
    print(img_codes)
    codes_arr = torch.detach(img_codes).numpy()
    print
    print(codes_arr)
    no_imgs = len(codes_arr)
    index = 0 

    while index < no_imgs:
        img_no = str(index)
        filename = ("ImagenumberTest1.txt")
        np.savetxt(filename, codes_arr[index])
        index += 1

def encoder_code(trained_model):
    #data loader
        test_dataset_path = 'imgs/test/'
        transform = transforms.Compose([transforms.Resize((128, 128)), transforms.ToTensor()])
        test_dataset = Datasets.ImageFolder(root = test_dataset_path, transform = transform)
        test_loader = torch.utils.data.DataLoader(dataset = test_dataset, batch_size = 1, shuffle=True)
        #load the model 
        FILE =trained_model

        model = autoencoder(encoder(), decoder())
        model.load_state_dict(torch.load(FILE))
        model.eval()
        img_codes = test_image_reconstruction(net = model, testloader = test_loader)

        unique_code_files(img_codes)
        return img_codes