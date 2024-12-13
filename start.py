import subprocess

subprocess.run(["sudo apt install gnome-terminal"], shell = True)
subprocess.run(["sudo apt-get update"], shell = True)
subprocess.run(["sudo apt-get install ./docker-desktop-amd64.deb"], shell = True)

subprocess.run(["chmod -R 755 bin"], shell = True)

# subprocess.run(["chmod +x bin/init"], shell = True)
subprocess.run(["bin/init"], shell = True)

# subprocess.run(["chmod +x bin/up"], shell = True)
subprocess.run(["bin/up"], shell = True)

# subprocess.run(["chmod +x bin/start"], shell = True)
subprocess.run(["bin/start"], shell = True)

# subprocess.run(["chmod +x bin/shell"], shell = True)
subprocess.run(["bin/shell"], shell = True)

subprocess.run(["wget https://mirror.clientvps.com/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz"], shell = True)
subprocess.run(["tar -xf install-tl-unx.tar.gz"], shell = True)
subprocess.run(["perl install-tl", "i"], shell = True)