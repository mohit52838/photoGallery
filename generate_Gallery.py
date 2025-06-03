import os
import zipfile

image_folder = "images"
output_file = "index.html"

html_header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>END SEM PPS</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>📸 My Screenshot Gallery</h1>

  <a href="download_all.zip" download class="download-all">⬇️ Download All Images</a>

  <div class="gallery">
"""

html_footer = """
  </div>

  <!-- Lightbox Container -->
  <div id="lightbox" class="lightbox">
    <span class="close">&times;</span>
    <img class="lightbox-content" id="lightbox-img">
  </div>

  <script src="script.js"></script>
</body>
</html>
"""

image_files = [f for f in os.listdir(image_folder)
               if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))]

image_tags = ""
for image in sorted(image_files):
    image_path = f"{image_folder}/{image}"
    image_tags += f'''
    <div class="image-container">
      <img src="{image_path}" alt="{image}" class="gallery-img">
      <a href="{image_path}" download class="download-btn">⬇ Download</a>
    </div>
    '''

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_header + image_tags + html_footer)

print(f"✅ Generated {output_file} with {len(image_files)} images.")

# Create ZIP of all images
with zipfile.ZipFile("download_all.zip", "w") as zipf:
    for file in image_files:
        file_path = os.path.join(image_folder, file)
        zipf.write(file_path, arcname=file)  # Add with no folder prefix

print("✅ Created download_all.zip with all images.")
