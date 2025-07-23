import streamlit as st
import json
import os

# Configuration
DATA_PATH = "causal_ablation_results (2).json"
IMAGE_FOLDER = "graph_images (1)"
IMAGES_PER_PAGE = 5

# Load data
with open(DATA_PATH) as f:
    data = json.load(f)

st.title("📊 Causal Graph Comparison Viewer")

# Pagination
total_pages = (len(data) - 1) // IMAGES_PER_PAGE + 1
page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)

start_idx = (page - 1) * IMAGES_PER_PAGE
end_idx = start_idx + IMAGES_PER_PAGE
page_data = data[start_idx:end_idx]

# Display rows
for idx, entry in enumerate(page_data):
    col1, col2, col3 = st.columns([2, 4, 4])
    
    # Metadata column
    with col1:
        st.markdown(f"""
        ### 🔍 Entry {start_idx + idx + 1}
        - **Model:** `{entry.get("model")}`
        - **Level:** `{entry.get("level")}`
        - **Iteration:** `{entry.get("iteration")}`
        """)

    # Graph 1 image
    # with col2:
    #     img1_name = entry.get("graph1_file", "") or f"comparison_{start_idx + idx}_1.png"
    #     img1_path = os.path.join(IMAGE_FOLDER, img1_name)
    #     if os.path.exists(img1_path):
    #         st.image(img1_path, caption="Graph 1", use_column_width=True)
    #     else:
    #         st.warning("Graph 1 image not found")

    # # Graph 2 image
    # with col3:
    #     img2_name = entry.get("graph2_file", "") or f"comparison_{start_idx + idx}_2.png"
    #     img2_path = os.path.join(IMAGE_FOLDER, img2_name)
    #     if os.path.exists(img2_path):
    #         st.image(img2_path, caption="Graph 2", use_column_width=True)
    #     else:
    #         st.warning("Graph 2 image not found")
    with col2:
        # Use the full image path from the data entry for Graph 1
        subfolder = f"comparison_{start_idx + idx}_model_{entry['model']}"
        subfolder_path = subfolder.split("/")[0]
        img1_path = os.path.join(IMAGE_FOLDER, subfolder_path)
        files = os.listdir(img1_path)
        img1_file = next((f for f in files if f.endswith('_1.png')), None)
        if img1_file:
            full_img1_path = os.path.join(img1_path, img1_file)
            st.image(full_img1_path, caption="Graph 1", use_container_width=True)
        else:
            st.warning(f"Graph 1 not found: {img1_path}")

    with col3:
        # Use the full image path from the data entry for Graph 1
        subfolder = f"comparison_{start_idx + idx}_model_{entry['model']}"
        subfolder_path = subfolder.split("/")[0]
        img1_path = os.path.join(IMAGE_FOLDER, subfolder_path)
        files = os.listdir(img1_path)
        img1_file = next((f for f in files if f.endswith('_2.png')), None)
        if img1_file:
            full_img1_path = os.path.join(img1_path, img1_file)
            st.image(full_img1_path, caption="Graph 2", use_container_width=True)
        else:
            st.warning(f"Graph 2 not found: {img1_path}")