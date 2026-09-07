import sys
import os
import site


if (__name__ == "__main__"):
    # test if the variable VIRTUAL_ENV is used, if it is, that mean that we are
    # on a enve
    if ("VIRTUAL_ENV" in os.environ):
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        # os.environ is a huge dict with infos about the enve, python and more
        print(f"Virtual Environment: {os.environ['VIRTUAL_ENV_PROMPT']}")

        # prefix is an attribut that contain the path of
        # where python is intalled
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment !")
        print("Safe to install package without \
affecting the global systeme.\n")
        print("Package installation path:")
        print(site.USER_SITE)

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment !")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate    # On Windows\n")

        print("Then run this programe again")
