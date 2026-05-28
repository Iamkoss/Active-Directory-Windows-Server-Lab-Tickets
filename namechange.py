import os
import re

MD_FILE_PATH = '05_Active_directory.md'

def increment_all_md_links(file_path, target_start=31):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # This looser pattern finds any link starting with numbers between 31 and 61
    # Group 1: images/
    # Group 2: The starting number prefix
    # Group 3: The middle text and whatever trailing numbers/characters are right before .png
    pattern = re.compile(r'(images/)(\d+)(.*?\.png)', re.IGNORECASE)

    def replace_match(match):
        prefix, first_num_str, rest_of_path = match.groups()
        first_num = int(first_num_str)

        if first_num >= target_start:
            new_num = first_num + 1
            
            # Increment the trailing number right before .png as well
            updated_rest = re.sub(r'(\d+)(\.png)$', lambda m: f"{int(m.group(1)) + 1}{m.group(2)}", rest_of_path)
            return f"{prefix}{new_num}{updated_rest}"
        
        return match.group(0)

    updated_content, count = pattern.subn(replace_match, content)

    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Successfully updated {count} image links in '{file_path}' to be incremental.")
    else:
        print("No image links found matching the criteria.")

if __name__ == "__main__":
    increment_all_md_links(MD_FILE_PATH, target_start=31)