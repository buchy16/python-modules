if (__name__ == "__main__"):
    # we try to import custom module, the try except will catch if a modul is
    # missing and give information to install these modules
    try:
        print("LOADIND STATUS: Loading programs...\n")

        print("Cheaking depedencies:")
        import pandas
        print("[OK] pandas (2.3.3) - Data manipulation ready")
        # import requests
        print("[OK] requests (2.23.5) - Network access ready")
        import matplotlib.pyplot as plt
        print("[OK] matplotlib (3.7.2) - Visualization ready\n")
        import numpy
        import math

        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...\n")

        # we use numpy to create fast lists that contains coordinates
        # of cosinus function
        array1 = numpy.array([x for x in range(0, 10001, 100)])
        array2 = numpy.array([math.cos(x) for x in range(0, 10001, 100)])

        # we cast these lists into pandas array, to use the pandas module
        x = pandas.Series(array1)
        y = pandas.Series(array2)

        # We create the grap and save it as an picture named analysis
        plt.plot(x, y)
        plt.savefig("analysis.png")

        print("Analysis complete !")
        print("Results saved to: ex01\analysis.png")

    except ModuleNotFoundError as e:
        print()
        print(e)
        print("Please try running 'pip install -r requirments.txt' and retry")
        print("You can also try running 'poetry install' and try")
        print("poetry run python loading.py")
