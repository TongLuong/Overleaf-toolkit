import subprocess

subprocess.run(["bin/init"], shell = False)
subprocess.run(["bin/up"], shell = False)
subprocess.run(["bin/start"], shell = False)
subprocess.run(["bin/shell"], shell = False)
subprocess.run(["wget https://mirror.clientvps.com/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz"], shell = False)
subprocess.run(["tar -xf install-tl-unx.tar.gz"], shell = False)
subprocess.run(["perl install-tl", "i"], shell = False)