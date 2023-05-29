import os
import subprocess

scss_dir = './scss'
css_dir = './css'

for file in os.listdir(scss_dir):
    if file.endswith(".scss"):
        input_file = os.path.join(scss_dir, file)
        output_file = os.path.join(css_dir, file.replace('.scss', '.css'))

        subprocess.run(['sass', input_file, output_file])
        
        print(f'Compiled {input_file} to {output_file}')

