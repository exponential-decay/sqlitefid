"""User facing entry point for pathlesstaken for anyone running the
code from the repository and not pypi.
"""

from src.sqlitefid import sqlitefid


def main():
    """Primary entry point for this script."""
    sqlitefid.main()


if __name__ == "__main__":
    main()
