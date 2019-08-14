import subprocess

def convert(input, output):
    subprocess.run(['avconv', '-i', input, '-vcodec', 'copy', '-r', '252/100', '-y', output])
