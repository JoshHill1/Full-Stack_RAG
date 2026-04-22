from parsers import parse_file
import os

test_dir = "test_files"

for filename in os.listdir(test_dir):
    file_path = os.path.join(test_dir, filename)
    # Border for the "FILE: filename"
    print(f"\n{'='*60}")
    print(f"FILE: {filename}")
    print(f"{'='*60}")
    try:
        text = parse_file(file_path)
        # Shows the first 500 characters for verification. 
        preview = text[:500] if len(text) > 500 else text
        print(preview)
        print(f"\n[Total length: {len(text)} characters]")
    except Exception as e:
        print(f"ERROR: {e}")
