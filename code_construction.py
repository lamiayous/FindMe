# import torchvision.transforms as transforms 
# import torchvision.datasets as Datasets
import torch
from torchvision.utils import save_image
import numpy as np

device = torch.device('cpu')
def test_image_reconstruction(net, testloader, encoder):
        for batch in testloader:
            img, _ = batch
            img = img.to(device)
            img_code = encoder(img)
            outputs = net(img)
            outputs = outputs.view(outputs.size(0), 3, 128, 128).cpu().data
            save_image(img, 'original_images.png')
            save_image(outputs, 'reconstructed_images.png')
            break
        return img_code

def unique_code(img_codes):
        codes_arr = torch.detach(img_codes).numpy()
        no_imgs = len(codes_arr)
        index = 0 

        while index < no_imgs:
            img_no = str(index)
            filename = ("TESTTTT" + img_no + ".txt")
            np.savetxt(filename, codes_arr[index])
            index += 1