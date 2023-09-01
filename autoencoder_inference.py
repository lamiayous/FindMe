from encoder_decoder import encoder
from encoder_decoder import decoder
from encoder_decoder import autoencoder
from code_construction import image_code_extraction
import torch
import torchvision.transforms as transforms 
import torchvision.datasets as Datasets

def encoder_code(trained_model):
    test_dataset_path = 'imgs/test/'
    transform = transforms.Compose([transforms.Resize((128, 128)), transforms.ToTensor()]) #setting transforms
    test_dataset = Datasets.ImageFolder(root = test_dataset_path, transform = transform) #applying transforms to dataset
    test_loader = torch.utils.data.DataLoader(dataset = test_dataset, batch_size = 1, shuffle=True)

    FILE =trained_model #load the model

    model = autoencoder(encoder(), decoder()) #calling autoencoder
    model.load_state_dict(torch.load(FILE)) #loading pretrained model
    model.eval() #this is to turn off all dropout layers
    img_codes = image_code_extraction(net = model, testloader = test_loader) #extracting image codes

    return img_codes