import argparse 

def parser_img():
    parser = argparse.ArgumentParser()
    parser.add_argument("--upload", type=str, default=None)
    parser.add_argument("--query", type=str, default=None, nargs=2) #if querying, two arguments are required
    args = parser.parse_args() 
    upload = args.upload
    query = args.query
    return upload, query