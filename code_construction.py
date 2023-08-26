import torch
from torchvision.utils import save_image

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