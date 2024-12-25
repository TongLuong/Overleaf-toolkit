import subprocess

subprocess.run(["wget https://mirror.clientvps.com/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz"], shell = True)
subprocess.run(["tar -xf install-tl-unx.tar.gz"], shell = True)
subprocess.run(["perl install-tl", "i"], shell = True)