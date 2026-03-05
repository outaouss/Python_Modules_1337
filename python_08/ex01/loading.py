def check_dependency(package_name: str) -> str:
    """
    Attempts to dynamically import a package to verify its presence.

    Logic:
    Uses the __import__ function to check if the library is installed.
    If successful, it retrieves the version and returns an [OK] status.
    If an ImportError occurs, it catches the exception and returns [KO].
    """

    package_message = {
        "pandas": " Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": " Visualization ready"
    }
    try:
        # Dynamic import allows checking presence
        # without crashing the main script
        module = __import__(package_name)

        # Returns formatted string with version metadata
        return (f"[OK] {package_name} ({module.__version__})"
                f" - {package_message[package_name]}")
    except ImportError:
        # Gracefully handle missing modules by returning status
        # instead of raising error
        return f"[KO] {package_name} not found"


def analyze_data() -> object | None:
    """
    Generates synthetic Matrix signal data using NumPy and Pandas.

    Logic:
    Creates a time series using arange and a random signal using randn.
    The dictionary is then converted into a Pandas DataFrame for
    structured analysis.
    """

    print("Analyzing Matrix data...")
    try:
        print("Processing 1000 data points...")
        import pandas
        import numpy

        # arange creates sequential x-axis data; randn creates
        # noisy y-axis data
        data = {
            "time": numpy.arange(1000),
            "signal": numpy.random.randn(1000)
        }

        # Convert raw dictionary into a structured tabular format
        d = pandas.DataFrame(data)

        return d
    except Exception as e:
        print(e)


def create_visualization(data: object) -> None:
    """
    Produces a graphical representation of the analyzed data.

    Logic:
    Utilizes matplotlib.pyplot to draw coordinates, add labels/titles,
    and export the final canvas to a PNG file.
    """
    try:
        import matplotlib.pyplot as plt

        print("Generating visualization...\n")

        # Map DataFrame columns to a line plot
        plt.plot(data["time"], data["signal"])

        # Add descriptive metadata to the chart axes and title
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Time")
        plt.ylabel("Signal")

        # Finalize by exporting the plot as a static image file
        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"Error during visualization: {e}")


if __name__ == "__main__":
    # Program Entry Point: Orchestrating the Matrix programs
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    dependencies = ["pandas", "requests", "matplotlib"]

    # Safety flag to prevent execution if the environment is incomplete
    flag = True

    for dependency in dependencies:
        val = check_dependency(dependency)
        # Scan for failure markers in the dependency check results
        if '[KO]' in val:
            flag = False
        print(val)

    # Only run the core logic if all required packages are present
    if flag:
        print()
        analyzed_data = analyze_data()

        # Pass the processed DataFrame into the visualization function
        create_visualization(analyzed_data)
    else:
        # Prevents runtime crashes from missing libraries
        print("\nNothing To Analyse !")
