import os
import gdown # type: ignore

# Function to download a file if it doesn't exist
def download_file_from_drive(file_id, output_path):
    if not os.path.exists(output_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_path, quiet=False)
    else:
        print(f"{output_path} already exists.")

# Download all large files from Drive
download_file_from_drive("1TQufrjDz2-30ySMwRJ3HcBeuE2BMLEoW", "Files/similarity_tags_genres.pkl")
download_file_from_drive("1RJ5icDjlKfQllORZTp9U6geo5yRo5OJd", "Files/similarity_tags_keywords.pkl")
download_file_from_drive("10utgLRK6AOXx9zwJ4MbDBdjdgbjMe-Uq", "Files/similarity_tags_tags.pkl")
download_file_from_drive("15P-hjV4bonM-CDLQxYojdvIsYlNp6Qei", "Files/similarity_tags_tcast.pkl")
download_file_from_drive("18hLf_4awuOM1GTQma1EuPfotu6XVd7Dk", "Files/similarity_tags_tprduction_comp.pkl")
