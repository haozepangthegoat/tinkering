"""
A script to run LaTeX code.
by haozepangthegoat

Examples
--------
$ python3 <this script name> <main tex file>
"""
import os
import subprocess
import sys

# Parameters
ENGINE = 'xelatex'
SIMPLE_COMPILE = False


# IO
def indicate(indicator_text):
    """Print indicator text"""

    # ANSI escape codes for colors and formatting
    blue = '\033[94m'
    bold = '\033[1m'
    end = '\033[0m'

    # Constructing the string with the desired formatting
    formatted_text = blue + '=>' + end + ' ' + bold + indicator_text + end
    print(formatted_text)

def clean_aux():
    """Clean files after computation"""
    # folder name
    temp_folder = '.tmp'
    extension_to_clear = ['.aux', '.log', '.nav', '.toc', '.out', '.snm']
    # clean files
    for file in os.listdir(os.getcwd()):
        if any(file.endswith(ext) for ext in extension_to_clear):
            if file.startswith('.'):
                continue
            os.remove(file)


class Compile:
    """Compile LaTeX"""

    def __init__(self):
        self.compile()
        subprocess.run(["open", f"{self.pdf_file}"])
        clean_aux()

    @property
    def tex_file(self) -> str:
        """File name of .tex file"""
        file_name = sys.argv[1]
        if file_name.endswith('.tex'):
            return file_name
        raise TypeError('This is not a .tex file')

    @property
    def pdf_file(self) -> str:
        return self.tex_file.replace('.tex', '.pdf')

    def compile(self):
        """Compile LaTeX via command line"""
        indicate(f"Compiling {self.tex_file}")

        subprocess.run([ENGINE, f"{self.tex_file}"])
        if SIMPLE_COMPILE is False:
            subprocess.run([ENGINE, f"{self.tex_file}"])

        indicate(f"Compilation success!")


if __name__ == '__main__':
    Compile()
