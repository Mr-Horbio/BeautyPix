import argparse
import sys
import pyfiglet
from screen_shot import browser
from merge import merge_files

# LOGO FOR CLI
f = pyfiglet.figlet_format("BeautyPIX")
print(f)
print("By Mr.Horbio")

# Set up the main parser
parser = argparse.ArgumentParser(description='Usages of BeautyPix', epilog="created by Mr.Horbio")

# Add subparsers for different commands
subparsers = parser.add_subparsers(dest='command')

# Subparser for the 'screenshot' command
screenshot_parser = subparsers.add_parser('screenshot', help='Take screenshots of subdomains')
screenshot_parser.add_argument('-p', dest='Path', required=True, help='File containing subdomains')
screenshot_parser.add_argument('-t', dest='timeout', type=float, default=0.5, help='Timeout in seconds for screenshots (default 0.5)')

# Subparser for the 'merge' command
merge_parser = subparsers.add_parser('merge', help='Merge two files and remove duplicates')
merge_parser.add_argument('-f', '--files', nargs=2, required=True, help='Input files to merge')
merge_parser.add_argument('-o', '--output', required=True, help='Output file for merged content')

# Version argument
parser.add_argument('-V', action='version', help='Print version', version=" %(prog)s 1.0 ")

# Parse arguments
args = parser.parse_args()

# Execute commands based on the subcommand used
if args.command == 'screenshot':
    file_path = args.Path
    time_out = args.timeout
    browser(file_path, time_out)
elif args.command == 'merge':
    file1, file2 = args.files
    output_file = args.output
    merge_files(file1, file2, output_file)
else:
    parser.print_help(sys.stderr)
    sys.exit()
