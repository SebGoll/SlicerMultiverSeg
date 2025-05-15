from pathlib import Path

if __name__ == '__main__':
    import sys
    import slicer

    print(sys.path)

    sys.path.append(Path(__file__).parent.joinpath("../..").resolve().as_posix())
    print(sys.path)

    slicer.util.quit()