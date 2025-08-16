#!/usr/bin/env python3
import os
import time
import requests
import tarfile
from argparse import ArgumentParser

# Repository settings
REPO_OWNER = "AhmedXV-V12"
REPO_NAME = "xv3_packages"
BRANCH = "main"
BASE_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/raw/{BRANCH}/"

def download_package(package_name):
    """Download package from GitHub"""
    try:
        package_url = f"{BASE_URL}{package_name}.tar.gz"
        print(f"Downloading {package_name}...")
        print(f"searching : {package_url} ...")
        print(f"install now {package_name}.tar.gz ...")
        print("Processing xv3 now xv3.packages ...")
        time.sleep(3)
        print(" xv3 now install package ...")
        print(f"10%")
        time.sleep(1)
        print(f"20%")
        time.sleep(1)
        print(f"30%")
        time.sleep(1)
        print(f"40%")
        time.sleep(1)
        print(f"50%")
        time.sleep(1)
        print(f"60%")
        time.sleep(1)
        print(f"70%")
        time.sleep(1)
        print(f"80%")
        time.sleep(1)
        print(f"90%")
        time.sleep(4)
        print(f"100%")
        time.sleep(15)
        print("the installation is complete.")

        response = requests.get(package_url, stream=True)
        if response.status_code != 200:
            print(f"Error: Package not found (HTTP {response.status_code})")
            return False

        temp_file = f"{package_name}.tar.gz"
        with open(temp_file, "wb") as f:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                progress = int(downloaded / total_size * 100)
                print(f"\rProgress: {progress}%", end='', flush=True)
            print()

        os.makedirs("packages", exist_ok=True)
        with tarfile.open(temp_file, "r:gz") as tar:
            tar.extractall(f"packages/{package_name}")
        
        os.remove(temp_file)
        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def install(package_name):
    """Main installation function"""
    if os.path.exists(f"packages/{package_name}"):
        print(f"Package {package_name} already installed!")
        return

    if download_package(package_name):
        print(f"Successfully installed {package_name}!")
    else:
        print(f"Failed to install {package_name}")

if __name__ == "__main__":
    parser = ArgumentParser(description="XV3 Package Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("package_name")
    
    args = parser.parse_args()
    
    if args.command == "install":
        install(args.package_name)
    else:
        parser.print_help()