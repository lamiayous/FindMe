import argparse 

def parser_img():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default=None)
    args = parser.parse_args() 
    img_file =args.image
    return img_file