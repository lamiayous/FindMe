from encoder_decoder import encoder
from encoder_decoder import decoder
from encoder_decoder import autoencoder

from code_construction import test_image_reconstruction
from code_construction import unique_code
import torch
import torchvision.transforms as transforms 
import torchvision.datasets as Datasets

#data loader
test_dataset_path = './autoencoder/imgs/fake_test'
transform = transforms.Compose([transforms.Resize((128, 128)), transforms.ToTensor()])
test_dataset = Datasets.ImageFolder(root = test_dataset_path, transform = transform)
test_loader = torch.utils.data.DataLoader(dataset = test_dataset, batch_size = 4, shuffle=True)

#load the model 
FILE = "last.pth"

model = autoencoder(encoder(), decoder())
model.load_state_dict(torch.load(FILE))
model.eval()
img_codes = test_image_reconstruction(net = model, testloader = test_loader, encoder = encoder())
unique_code(img_codes)