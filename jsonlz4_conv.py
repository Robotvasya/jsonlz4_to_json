#!/usr/bin/env python3
import pathlib
import os
import argparse
import lz4.block


def is_valid_input_file(filename: str, file_format: bytes) -> bool:
    """
    Check file path and satisfying to binary format.

    :param filename: Path to file
    :param file_format: File header bytes
    :return:  True if format satisfied
    """
    if pathlib.Path(filename).is_file():
        try:
            with open(filename, 'rb') as inf:
                file_header = inf.read(6)
            return file_header == file_format
        except OSError as e:
            print(f"Error: Exception raised {e}")
            return False
    else:
        return False


def make_temp_binfile(filename: pathlib.Path) -> pathlib.Path:
    """
    Makes temp binary file. Returns file path of temp file.
    That new file you should decompress by decompress function

    :param filename: pathlib.Path - original Firefox jsonlz4 file
    :return: Path to temp binary file


    """
    temp_file = pathlib.Path('output.temp.dat')
    try:
        with open(filename, 'rb') as inFile:
            inFile.seek(12)
            with open(temp_file, 'wb') as outFile:
                for chunk in iter(lambda: inFile.read(1024), b''):
                    outFile.write(chunk)
        return temp_file
    except OSError as e:
        print(f"Error: Exception raised {e}")
        exit(1)



def decompress_temp_binfile(temp_file: pathlib.Path, output_file: pathlib.Path) -> pathlib.Path:
    """
    Decompress function for binary temp file, created by make_temp_binfile()

    :param temp_file:  pathlib.Path, - binary file
    :param output_file:  pathlib.Path, - output file

    :return: path to JSON file
    """
    try:
        with open(temp_file, mode='rb') as fp:
            input_data = fp.read()
            output_data = lz4.block.decompress(input_data, uncompressed_size=1024 * 1024)
        with open(output_file, "w") as ouf:
            ouf.write(output_data.decode("utf-8"))
        return output_file
    except lz4.block.LZ4BlockError as e:
        print(f"Decompression error: Exception raised {e}")
        exit(1)
    except OSError as e:
        print(f"Error: Exception raised {e}")
        exit(1)


def main():
    file_format: bytes = b"mozLz4"

    cli_usage_description = '''
    jsonlz4_conv.py input_file [-o OUTPUT_FILE] 
or help:  
    jsonlz4_conv.py --help
    '''

    parser = argparse.ArgumentParser(usage=cli_usage_description,
                                     description="Converts Firefox bookmark backup file from .jsonlz4 format to JSON format"
                                     )

    parser.add_argument('input_file',
                        help="Path to jsonlz4 file",
                        )
    parser.add_argument('-o',
                        dest='output_file',
                        help="Path to output JSON file. If argument is omitted, script uses the name of input_file",
                        required=False
                        )
    args = parser.parse_args()

    if not is_valid_input_file(args.input_file, file_format):
        print(f"Error: \"{args.input_file}\" - is wrong path to file, or not jsonlz4 format.")
        exit(1)

    input_file = pathlib.Path(args.input_file)
    output_file = pathlib.Path(args.output_file) if args.output_file else pathlib.Path(input_file.stem + ".json")

    tmp_file = make_temp_binfile(input_file)
    result_path = decompress_temp_binfile(tmp_file, output_file)
    os.remove(tmp_file)
    print(f"Your result file is {result_path}")
    exit(0)


if __name__ == '__main__':
    main()
