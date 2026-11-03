import os
import cv2
import numpy as np

os.environ['MPLCONFIGDIR'] = r'C:\Users\LENOVO\.gemini\antigravity\brain\b768dafa-3595-483f-97f3-a6502a8b1ef6\scratch'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

repo_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(repo_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

frame_path = os.path.join(repo_dir, 'captured_frame.jpg')
img_bgr = cv2.imread(frame_path)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 1. Captured frame
fig, ax = plt.subplots(figsize=(6.5, 5))
ax.imshow(img_rgb)
ax.set_title('Captured Frame', fontsize=12)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_1_captured_frame.png'), bbox_inches='tight', dpi=150)
plt.close()

# 2. Display video
fig, ax = plt.subplots(figsize=(6.5, 4.8))
ax.imshow(img_rgb)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_2_display_video.png'), bbox_inches='tight', dpi=150)
plt.close()

# 3. Resized video (100, 150)
resized_frame = cv2.resize(img_bgr, (100, 150))
resized_rgb = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(figsize=(3.5, 5))
ax.imshow(resized_rgb)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_3_resized_video.png'), bbox_inches='tight', dpi=150)
plt.close()

# 4. Rotated video (90 deg clockwise)
rotated_frame = cv2.rotate(img_bgr, cv2.ROTATE_90_CLOCKWISE)
rotated_rgb = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(figsize=(4, 5))
ax.imshow(rotated_rgb)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_4_rotated_video.png'), bbox_inches='tight', dpi=150)
plt.close()

print('Outputs generated in assets folder.')
