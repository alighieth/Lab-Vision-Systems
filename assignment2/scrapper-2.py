import os
import requests

def download_images(image_urls, save_dir="./Lab-Vision-Systems/data/assignment2-robot"):
    # 1. Create the target directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Created directory: {save_dir}")
    
    # 2. Iterate through URLs and download
    for i, url in enumerate(image_urls):
        try:
            print(f"Downloading {i+1}/{len(image_urls)}: {url}")
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            
            # Define file path (using index to ensure unique names)
            filename = os.path.join(save_dir, f"robot_image_{i+1}.jpg")
            
            # Save the image content
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# --- Usage ---
# Replace this list with your actual provided links
robot_links = [
    "https://thumbs.dreamstime.com/b/woman-robot-cyborg-android-machine-human-also-part-living-female-surreal-weird-technology-57343661.jpg",
    "https://foreignpolicy.com/wp-content/uploads/2025/01/humanoid-robot-GettyImages-2158291771.jpg",
    "https://www.economist.com/cdn-cgi/image/width=1424,quality=80,format=auto/content-assets/images/20251115_TWSTP505.jpg",
    "https://cdn1-m.alittihad.ae/store/archive/image/2024/4/21/f8befdb1-ed90-4907-aae2-bd8fead6f5f7.png",
    "https://mmo.aiircdn.com/265/605c40646792b.jpg",
    "https://www.reuters.com/resizer/v2/https%3A%2F%2Farchive-images.prod.global.a201836.reutersmedia.net%2F2017%2F11%2F01%2FLYNXMPEDA02A9.JPG?auth=55ebee8c86fe746a296c5560ffab26982545472da2dc987a720f1ed5c0374962&width=1080&quality=80"
]

download_images(robot_links)
print("Download process complete.")
