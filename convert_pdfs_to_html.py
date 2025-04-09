import os
import subprocess

def convert_pdfs(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(input_folder):
        if file.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder, file)
            print(f"\nConverting {file}...")
            command = ['pdf2htmlEX', '--dest-dir', output_folder, input_path]

            try:
                subprocess.run(command, check=True)
                print(f"Converted: {file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {file}: {e}")

script_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_dir, "pdfs_input")
output_folder = os.path.join(script_dir, "html_output")

convert_pdfs(input_folder, output_folder)