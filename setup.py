import os
import platform
import subprocess
import sys
import signal
from dotenv import load_dotenv


load_dotenv()
system = platform.system()
requirements_file = "requirements.txt"


def create_venv():
    venv_dir = os.path.join(os.getcwd(), ".venv")
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment at {venv_dir}")
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    else:
        print(f"Virtual environment already exists at {venv_dir}")


def is_venv_activated():
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def activate_venv():
    if is_venv_activated():
        print("Virtual environment is already activated.")
        return

    venv_dir = os.path.join(os.getcwd(), ".venv")

    if system == "Windows":
        activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
        activation_cmd = f'"{activate_script}"'
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        activation_cmd = f"source '{activate_script}'"

    print(f"Activating virtual environment from {activate_script}")
    subprocess.run(activation_cmd, shell=True)


def install_requirements():
    if not os.path.exists(requirements_file):
        print(f"{requirements_file} not found. Skipping installation.")
        return

    print(f"Installing requirements from {requirements_file}")
    subprocess.run(
        [os.path.join(".venv", "bin", "pip"), "install", "-r", requirements_file],
        check=True,
    )


def run_main_app():
    print("Running main application with gunicorn...")

    gunicorn_cmd = [
        os.path.join(".venv", "bin", "gunicorn"),
        "-w",
        "4",
        "-b",
        f"{os.getenv('URI')}",
        "main:app",
    ]

    subprocess.run(gunicorn_cmd)


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    create_venv()
    activate_venv()
    install_requirements()
    run_main_app()
