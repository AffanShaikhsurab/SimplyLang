import argparse
import interpreter


def run(filename):
    ast, error = interpreter.run(filename)
    if error is not None:
        try:
            print(error.print())
        except:
            print(error)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run a Simply language file.")
    parser.add_argument("filename", help="The .simply file to run")

    # Parse arguments
    args = parser.parse_args()
    filename = args.filename

    # Check file extension
    if not filename.endswith(".simply"):
        print("Invalid file format, should be in .simply format")
        return

    # Run the interpreter
    run(filename)


if __name__ == "__main__":
    main()
