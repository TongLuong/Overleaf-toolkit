import subprocess, os

subprocess.run(["chmod +x bin/init"], shell = True)
subprocess.run(["bin/init"], shell = True)

subprocess.run(["chmod +x bin/up"], shell = True)
subprocess.run(["bin/up"], shell = True)

subprocess.run(["chmod +x bin/start"], shell = True)
subprocess.run(["bin/start"], shell = True)

subprocess.run(["chmod +x bin/shell"], shell = True)
subprocess.run(["bin/shell"], shell = True)

subprocess.run(["wget https://mirror.clientvps.com/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz"], shell = True)
subprocess.run(["tar -xf install-tl-unx.tar.gz"], shell = True)
subprocess.run(["perl install-tl", "i"], shell = True)