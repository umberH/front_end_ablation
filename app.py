import streamlit as st
import json
import os

# Configuration
DATA_PATH = "causal_ablation_results.json"
IMAGE_FOLDER = "graph_images"
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
    with col2:
        img1_name = entry.get("graph1_file", "") or f"comparison_{start_idx + idx}_1.png"
        img1_path = os.path.join(IMAGE_FOLDER, img1_name)
        if os.path.exists(img1_path):
            st.image(img1_path, caption="Graph 1", use_column_width=True)
        else:
            st.warning("Graph 1 image not found")

    # Graph 2 image
    with col3:
        img2_name = entry.get("graph2_file", "") or f"comparison_{start_idx + idx}_2.png"
        img2_path = os.path.join(IMAGE_FOLDER, img2_name)
        if os.path.exists(img2_path):
            st.image(img2_path, caption="Graph 2", use_column_width=True)
        else:
            st.warning("Graph 2 image not found")
