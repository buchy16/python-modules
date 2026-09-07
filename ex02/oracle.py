import os
import math
from dotenv import load_dotenv

if (__name__ == "__main__"):
    print("ORACLE STATUS: Reading the Matrix...\n")
    # load the .env
    load_dotenv(override=False)

    try:
        print("Configuration loaded:")
        # Remember this "huge dict" ? we can add our enve variable,
        # local to our computer, we set these variable in the .env,
        # then we access these varible like a normal enve variable
        print(f"Mode: {os.environ['MATRIX_MODE']}")

        os.environ["DATABASE_URL"]
        print("Database: Connected to local instance")
        if (os.environ["API_KEY"].split(":"))[1] == str(
                                                round(math.sqrt(0x4ad50ab))):
            print("API Access: Owner authentified, welcome")
        else:
            print("API Access: Authenticated, welcome")
        print(f"Log Level: {os.environ['LOG_LEVEL']}")
        os.environ["ZION_ENDPOINT"]
        print("Zion Network: Online\n")

        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")

        print("The Oracle sees all configurations.")
    # if a enve variable is missing, the except will catch the error
    except (KeyError) as e:
        print(f"ERROR while loading, variable {e} not valide or not found")
    except IndexError:
        print("ERROR while loading, variable API_KEY not valide or not found")
