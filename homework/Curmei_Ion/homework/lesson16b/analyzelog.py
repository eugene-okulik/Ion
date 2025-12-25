import argparse
import os


def find_text_in_file(file_path, search_text):
    results = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_number, line in enumerate(f, start=1):
                words = line.strip().split()
                for i, word in enumerate(words):
                    if search_text in word:
                        start = max(0, i - 5)
                        end = min(len(words), i + 6)
                        snippet = " ".join(words[start:end])
                        results.append((line_number, snippet))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Search for text in log files from a folder"
    )
    parser.add_argument("folder", help="Full path to the folder containing log files")
    parser.add_argument(
        "--text", required=True, help="Text to search for in the log files"
    )

    args = parser.parse_args()
    folder = args.folder
    search_text = args.text

    if not os.path.isdir(folder):
        print(f"The specified folder does not exist: {folder}")
        return

    print(f"\n Searching for '{search_text}' in files from: {folder}\n")

    for file_name in os.listdir(folder):
        full_path = os.path.join(folder, file_name)
        if os.path.isfile(full_path):
            results = find_text_in_file(full_path, search_text)
            for line_number, snippet in results:
                print(f" {file_name} | line {line_number}:")
                print(f" ...{snippet}...\n")


if __name__ == "__main__":
    main()
