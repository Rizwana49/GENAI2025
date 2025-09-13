import os
import glob

# =======================================================================
# YOU NEED TO CHANGE THE FOLDER PATH BELOW TO YOUR SPECIFIC PATH
# Example: 'C:/Users/YourUsername/Desktop/Gen-AI/web_pages'
# Make sure to use forward slashes (/) or double backslashes (//)
# =======================================================================
folder_path = r'C:\Users\Windows\Downloads\ticket project\web_pages'

# Name of the output text file
output_file = 'combined_html_content.txt'

# Change the current working directory to the specified folder
try:
    os.chdir(folder_path)
    print(f"Working in directory: {os.getcwd()}")
except FileNotFoundError:
    print(f"Error: The folder path was not found. Please check the path and try again.")
    exit()

# Get a list of all HTML files in the specified directory
html_files = glob.glob('*.html')

# Open the output file in write mode ('w')
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Loop through each HTML file found
    for html_file in html_files:
        print(f'Reading content from: {html_file}')
        
        # Read the content of each HTML file
        with open(html_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            
            # Write a separator with the file name and then the file's content
            outfile.write(f'--- Start of file: {html_file} ---/n/n')
            outfile.write(content)
            outfile.write('/n/n')
            outfile.write(f'--- End of file: {html_file} ---/n/n')

print(f'Successfully combined all HTML files into: {output_file}')