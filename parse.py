import argparse 

def parser_img():
    parser = argparse.ArgumentParser()
    upload_img = parser.add_argument("--upload", type=str, default=None)
    query_img = parser.add_argument("--query", type=str, default=None, nargs=2)
    args = parser.parse_args() 
    if upload_img != None:
        upload = args.upload
    if query_img != None:
        query = args.query
    return upload, query