import os


def process_files():
    folder_A = r'S:\LearnPython\inputs'
    codes_file_B = r'S:\LearnPython\outputs\B.txt'
    output_file_C = r'S:\LearnPython\outputs\C.txt'

    with open(codes_file_B, 'r', encoding='utf-8') as f:
        codes = [line.strip() for line in f if line.strip()]

    txt_files = [os.path.join(folder_A, x) for x in os.listdir(folder_A) if x.endswith('.txt')]

    os.makedirs(os.path.dirname(output_file_C), exist_ok=True)

    with open(output_file_C, 'w', encoding='utf-8') as out_f:
        for code in codes:
            found_line = None
            for file_path in txt_files:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if code in line:
                            found_line = line.strip()
                            break
                if found_line:
                    break

            out_f.write(f"Looking for '{code}'\n")
            if found_line:
                out_f.write(f"Output: {found_line}\n\n")
            else:
                out_f.write("Output: Not found in the log files\n\n")
    print(f"Processing complete. Check results in {output_file_C}")


def main():
    process_files()


if __name__ == "__main__":
    main()
