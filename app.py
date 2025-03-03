import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.applications import VGG16, imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

# Load the pre-trained model
model = VGG16(weights="imagenet")

# Streamlit app title
st.title("Soccer Ball Classifier with VGG16")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Resize and preprocess the image
    resized = cv2.resize(image, (224, 224))
    image_array = img_to_array(resized)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = imagenet_utils.preprocess_input(image_array)
    
    # Make prediction
    preds = model.predict(image_array)
    decoded_preds = imagenet_utils.decode_predictions(preds, top=3)[0]
    
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Display predictions
    st.subheader("Predictions:")
    for (i, (imagenet_id, label, prob)) in enumerate(decoded_preds):
        st.write(f"{i+1}. {label}: {prob*100:.2f}%")