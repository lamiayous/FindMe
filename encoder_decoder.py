from torch import nn
import torch

device = torch.device('cpu')

class encoder(nn.Module):
  def __init__(self, out_channels=16, latent_dim=256):
    super().__init__()

    self.net = nn.Sequential(
        nn.Conv2d(3, 16, 3, padding=1), 
        nn.ReLU(),
        nn.Conv2d(16, 16, 3, padding=1), 
        nn.ReLU(),
        nn.Conv2d(16, 32, 3, padding=1,stride = 2),
        nn.ReLU(),
        nn.Conv2d(32, 32, 3, padding=1),
        nn.ReLU(),
        nn.Conv2d(32, 64, stride = 2, kernel_size = 3, padding=1),
        nn.ReLU(),
        nn.Conv2d(64, 64, 3, padding=1), 
        nn.ReLU(),
        nn.Conv2d(64, 128, 3, padding=1, stride =2), 
        nn.ReLU(),
        nn.Dropout(0.05),
        nn.Conv2d(128, 128, 3, padding=1), 
        nn.ReLU(),
        nn.Dropout(0.05),
        nn.Flatten(),
        nn.Linear(32*out_channels*8*8, latent_dim),
        nn.ReLU(),
    )

  def forward(self, x):
    x = x.view(-1, 3, 128, 128)
    output = self.net(x)
    return output
  

class decoder(nn.Module):
  def __init__(self, in_channels=3, out_channels=16, latent_dim=256):
    super().__init__()

    self.out_channels = out_channels

    self.linear = nn.Sequential(
        nn.Linear(latent_dim, 32*out_channels*8*8),
        nn.ReLU(),
    )

    self.conv = nn.Sequential(
        nn.ConvTranspose2d(8*out_channels, 8*out_channels, 3, padding=1), 
        nn.ReLU(),
        nn.Dropout(0.05),
        nn.ConvTranspose2d(8*out_channels, 4*out_channels, 3, padding=1, 
                           stride=2, output_padding=1), 
        nn.ReLU(),
        nn.Dropout(0.05),
        nn.ConvTranspose2d(4*out_channels, 4*out_channels, 3, padding=1), 
        nn.ReLU(),
        nn.ConvTranspose2d(4*out_channels, 2*out_channels, 3, padding=1, 
                           stride=2, output_padding=1),
        nn.ReLU(),
        nn.ConvTranspose2d(2*out_channels, 2*out_channels, 3, padding=1),
        nn.ReLU(),
        nn.ConvTranspose2d(2*out_channels, out_channels, 3, padding=1, 
                           stride=2, output_padding=1),
        nn.ReLU(),
        nn.ConvTranspose2d(out_channels, out_channels, 3, padding=1),
        nn.ReLU(),
        nn.ConvTranspose2d(out_channels, in_channels, 3, padding=1)
    )

  def forward(self, x):
    output = self.linear(x)
    output = output.view(-1, 128, 16, 16)
    output = self.conv(output)
    return output
  
#  defining autoencoder
class autoencoder(nn.Module):
  def __init__(self, encoder, decoder):
    super().__init__()
    self.encoder = encoder
    self.encoder.to(device)
    
    self.decoder = decoder
    self.decoder.to(device)

  def forward(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded