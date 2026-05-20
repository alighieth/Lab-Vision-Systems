import os
import shutil
from icrawler.builtin import BingImageCrawler

# Define your target directories and precise search terms
base_dir = "Lab-Vision-Systems/data/assignment2"

# Format: {"prefix": "highly specific search query"}
categories = {
    "person": "single person portrait",
    "robot": "single robot"
}

def scrape_images(keyword, save_dir, target_images):
    os.makedirs(save_dir, exist_ok=True)
    print(f"Starting download for '{keyword}' into {save_dir}...")
    
    crawler = BingImageCrawler(
        storage={'root_dir': save_dir},
        downloader_threads=4 
    )
    
    # Oversample to ensure we get enough valid links
    crawler.crawl(
        keyword=keyword, 
        max_num=400 
    )

def rename_and_trim_images(directory, prefix, target_count):
    # Grab all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Sort them so 000001.jpg is processed first
    files.sort()
    
    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(directory, filename)
        
        # If we have reached our target count, delete any excess files
        if index > target_count:
            os.remove(old_path)
            continue
            
        # Keep the original file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Create the new name
        new_filename = f"{prefix}{index}{file_extension}"
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)

if __name__ == "__main__":
    target_amount = 180
    
    for folder_prefix, search_keyword in categories.items():
        save_path = os.path.join(base_dir, folder_prefix)
        
        # 1. Download with oversampling
        scrape_images(
            keyword=search_keyword, 
            save_dir=save_path, 
            target_images=target_amount
        )
        
        # 2. Rename and trim down to exactly 180
        print(f"Renaming and trimming down to exactly {target_amount} files...")
        rename_and_trim_images(
            directory=save_path, 
            prefix=folder_prefix, 
            target_count=target_amount
        )
        
    print("Scraping, renaming, and trimming complete!")
