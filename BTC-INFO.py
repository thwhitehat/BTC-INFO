import argparse
import requests
import json
import sys
import shutil

# Function to print the BTC-INFO banner
def print_banner():
    banner = """
   _____ _     _______ _____ ____  _   _ _______ 
  / ____| |   |__   __|_   _/ __ \| \ | |__   __|
 | (___ | |_     | |    | ||  | | |  \| |  | |   
  \___ \| __|    | |    | ||  | | | . ` |  | |   
  ____) | |_     | |   _| ||__| | |\  |  | |   
 |_____/ \__|    |_|  |_____\____/|_| \_|  |_|   
                                                 
    """

    # Get the terminal width
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate the number of spaces to center the banner
    banner_width = len(banner.splitlines()[0])
    spaces = (terminal_width - banner_width) // 2

    # Print the centered banner
    print("\033[92m" + " " * spaces + banner + "\033[0m")

# Function to display help message
def display_help():
    help_message = """
BTC-INFO - BTC OSINT Tool

Usage:
    python btc_info.py -a <btc_address> [-o <output_file>] -v -H

Options:
    -a, --address=<btc_address>     Specify the BTC address to retrieve information.
    -o, --output=<output_file>      Specify the output file to save the results in JSON format. (optional)
    -v, --verbose                   Enable verbose mode to display detailed information.
    -H, --help                      Display help message.

Example:
    python btc_info.py -a 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa -o result.json -v
    """

    print(help_message)

# Function to retrieve BTC information using Blockstream API
def get_btc_info(address, output_file, verbose):
    # Code to retrieve BTC information using Blockstream API
    url = f"https://blockstream.info/api/address/{address}"
    response = requests.get(url)

    if response.status_code == 200:
        btc_info = response.json()

        # Save the result in the output file if provided
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(btc_info, f)

        if verbose:
            print(json.dumps(btc_info, indent=4))
        else:
            print("BTC information retrieved successfully.")
    else:
        print("Error occurred while retrieving BTC information.")

# Main function
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(prog='BTC-INFO', description='BTC OSINT Tool')
    parser.add_argument('-a', '--address', help='Specify the BTC address to retrieve information.', required=True)
    parser.add_argument('-o', '--output', help='Specify the output file to save the results in JSON format. (optional)')
    parser.add_argument('-v', '--verbose', help='Enable verbose mode to display detailed information.', action='store_true')
    parser.add_argument('-H', '--display_help', help='Display help message.', action='store_true')

    args = parser.parse_args()

    # Check if help option is specified
    if args.display_help:
        display_help()
        sys.exit(0)

    # Print the BTC-INFO banner
    print_banner()

    # Check if BTC address is provided
    if not args.address:
        print("Please provide a BTC address using the -a or --address option.")
        sys.exit(1)

    # Retrieve BTC information
    get_btc_info(args.address, args.output, args.verbose)

if __name__ == '__main__':
    main()
