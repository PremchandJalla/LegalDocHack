import os
import subprocess

def launch_app():
    subprocess.run(["python3", "app/main.py"])

if __name__ == "__main__":
    launch_app()
