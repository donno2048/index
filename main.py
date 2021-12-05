from re import sub
from sys import argv
from tqdm import tqdm
from shutil import rmtree
from os import mkdir, system
from urllib.request import urlopen
from subprocess import getstatusoutput
from http.server import test, SimpleHTTPRequestHandler
with open("index.html", "w+") as index:
    index.write("<!DOCTYPE html><html><body>")
    for i in tqdm(urlopen("https://raw.githubusercontent.com/donno2048/PyDonno/master/requirements.txt").read().decode("utf8").splitlines()):
        if i.startswith("#"):
            continue
        folder = sub(r"[-_.]+", "-", i).lower()
        rmtree(folder, ignore_errors=True)
        mkdir(folder)
        version, url = filter(lambda string: string.startswith("Home-page:") or string.startswith("Version:"), getstatusoutput("pip3 show " + i)[1].splitlines())
        url, version = url.replace("Home-page:", "").strip(), version.replace("Version:", "").strip()
        if i == "restricted-functions": url = "https://github.com/donno2048/restricted-functions" # special case, has its own website
        open(folder + "/index.html", "w+").write("<!DOCTYPE html><html><body><a href=\"git+%s#egg=%s-%s\">%s-%s</a><br/></body></html>" % (url, i, version, i, version))
        index.write("<a href=\"%s/\">%s</a><br/>" % (folder, i))
    rmtree("pydonno", ignore_errors=True)
    mkdir("pydonno")
    version, = filter(lambda string: string.startswith("Version:"), getstatusoutput("pip3 show pydonno")[1].splitlines())
    version = version.replace("Version:", "").strip()
    open("pydonno" + "/index.html", "w+").write("<!DOCTYPE html><html><body><a href=\"git+https://github.com/donno2048/pydonno#egg=pydonno-%s\">pydonno-%s</a><br/></body></html>" % (version, version))
    index.write("<a href=\"/pydonno/\">pydonno</a>")
    #mkdir("spamcmd") # virus
    index.write("</body></html>")
if "run" in argv: test(SimpleHTTPRequestHandler)
