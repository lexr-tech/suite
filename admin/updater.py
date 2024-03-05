import requests
from packaging import version as version_parser
import os
import subprocess
import sys

installed_version = "v1.0.0"

def print_boxed_message(messages, padding=2):
    max_length = max(len(message) for message in messages) + (padding * 2)
    horizontal_border = "+" + "-" * (max_length + 2) + "+"

    print(horizontal_border)
    for message in messages:
        # Calculate total padding needed for the message to be centered
        total_padding = max_length - len(message)
        # Calculate padding for the left side; right side padding will be the remainder
        left_padding = total_padding // 2 + padding
        right_padding = total_padding - left_padding + padding + 2  # Adjust for the border

        formatted_message = "|" + " " * left_padding + message + " " * right_padding + "|"

        # Adjust if the total length is off due to rounding
        if len(formatted_message) > max_length + 4:
            formatted_message = formatted_message[:max_length + 3] + "|"
        elif len(formatted_message) < max_length + 4:
            formatted_message += " " * (max_length + 4 - len(formatted_message)) + "|"

        print(formatted_message)
    print(horizontal_border)

def get_latest_version_from_github(repo_url):
    parts = repo_url.split("/")
    owner, repo = parts[-2], parts[-1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(api_url)
    response.raise_for_status()
    latest_version_tag = response.json()["tag_name"]
    return latest_version_tag

def main():
    try:
        latest_version = get_latest_version_from_github("https://github.com/lexr-tech/suite")

        messages = [
            "Welcome! This is LEXR's updater script for the LEXR Productivity Suite.",
            f"Latest version: {latest_version}",
            f"Installed version: {installed_version}"
        ]        
        print_boxed_message(messages)

        if version_parser.parse(latest_version) > version_parser.parse(installed_version):
            user_input = input("Update available. Would you like to proceed? (Y/n): ".format(installed_version, latest_version)).strip().lower()
            if user_input != 'y' and user_input != '':
                input("Exiting the script. If you have questions, please contact the LEXR Tech team.")
            else:
                script_path = r"C:\Users\%USERNAME%\LEXR Tech\Admin\installer.py"
                command = f'start cmd.exe /k python "{script_path}"'
                subprocess.run(command, shell=True)
        elif version_parser.parse(latest_version) == version_parser.parse(installed_version):
            input("Installed version is up-to-date. Exiting.")
        else:
            input("Installed version is newer than latest version. This shouldn't have happened.")
    except requests.HTTPError as e:
        input(f"Failed to fetch the latest version from GitHub: {e}")

if __name__ == "__main__":
    main()