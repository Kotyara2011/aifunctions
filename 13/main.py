# Import the argparse module
import argparse

# Import the editor.py file as a module
import editor

# Define a function to parse command-line arguments and return a namespace object
def parse_args():
    # Create an argument parser object
    parser = argparse.ArgumentParser(description="A program for generating ad creatives using AI")
    # Add arguments for the data source name, user id, password, ad account id, product id, and brand id
    parser.add_argument("-d", "--dsn", type=str, required=True, help="The data source name for connecting to the database")
    parser.add_argument("-u", "--uid", type=str, required=True, help="The user id for connecting to the database")
    parser.add_argument("-p", "--pwd", type=str, required=True, help="The password for connecting to the database")
    parser.add_argument("-a", "--account_id", type=int, required=True, help="The ad account id for extracting target audience and platform information")
    parser.add_argument("-r", "--product_id", type=int, required=True, help="The product id for extracting product features")
    parser.add_argument("-b", "--brand_id", type=int, required=True, help="The brand id for extracting branding guidelines")
    # Parse the arguments and return a namespace object
    args = parser.parse_args()
    return args

# Define a function to run the whole program using the namespace object and the functions from the editor.py file
def run_program(args):
    # Create a dictionary to store the data from the namespace object
    data = {
        "dsn": args.dsn,
        "uid": args.uid,
        "pwd": args.pwd,
        "account_id": args.account_id,
        "product_id": args.product_id,
        "brand_id": args.brand_id
    }
    # Create a window for editing and refining the ad creative using the data and the create_window function from the editor.py file
    editor.create_window(data)

# Call the parse_args function and store the returned namespace object in a variable
args = parse_args()
# Call the run_program function with the namespace object as an argument
run_program(args)

