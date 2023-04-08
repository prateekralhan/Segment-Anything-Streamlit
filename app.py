import cv2
import sys
import json
import torch
import warnings
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="SAM - Streamlit",
    page_icon="🚀",
    layout= "wide",
    )

@st.cache_data()
def lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_data()
def mask_generate():
    sam_checkpoint = "model/sam_vit_l_0b3195.pth"
    model_type = "vit_l"
    device = "cuda"

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    mask_generator = SamAutomaticMaskGenerator(sam)
    return mask_generator


def show_anns(anns, ax):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    polygons = []
    color = []
    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
        ax.imshow(np.dstack((img, m*0.35)))

st.title("✨ Segment Anything 🏜")
st.info(' Let me help generate segments for any of your images. 😉')
col1, col2 = st.columns(2)
with col1:
    anim = lottie_local(r"./assets/animation.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            height = 700,
            width = 0,
            quality="high",
            key=None)

with col2:
    image_path = st.file_uploader("Upload Image 🚀", type=["png","jpg","bmp","jpeg"])
    if image_path is not None:
        with st.spinner("Working.. 💫"):
            image = cv2.imdecode(np.fromstring(image_path.read(), np.uint8), 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            mask_generator = mask_generate()
            masks = mask_generator.generate(image)

            col3, col4 = st.columns(2)
            with col3:
                st.image(image)
                st.success("Original Image")
            with col4:
                fig, ax = plt.subplots(figsize=(20,20))
                ax.imshow(image)
                show_anns(masks, ax)
                ax.axis('off')
                st.pyplot(fig)
                st.success("Output Image")
    else:
        st.warning('⚠ Please upload your Image! 😯')

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Segment Anything WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a> with the help of [segment-anything](https://github.com/facebookresearch/segment-anything/tree/main) built by [Meta Research](https://github.com/facebookresearch) ✨</center><hr>", unsafe_allow_html=True)
