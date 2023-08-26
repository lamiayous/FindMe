from ultralytics import YOLO

model = YOLO('best.pt')  # load a custom model

results = model('landscape.jpg', save=True) 

# for batch in train_data_loader:
#     inputs, targets = batch
#     for img in inputs:
#         image  = img.cpu().numpy()
#         # transpose image to fit plt input
#         image = image.T
#         # normalise image
#         data_min = np.min(image, axis=(1,2), keepdims=True)
#         data_max = np.max(image, axis=(1,2), keepdims=True)
#         scaled_data = (image - data_min) / (data_max - data_min)
#         # show image
#         plt.imshow(scaled_data)
#         plt.show()