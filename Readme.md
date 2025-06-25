#  **Image Classifier using VGG16 & Streamlit**  

This project is a **deep learning-based image classifier** that predicts whether an uploaded image contains a **soccer ball** or other objects. It is built using **Streamlit** for the web interface and **VGG16 (a pre-trained deep learning model)** for image classification.

---

##  **Demo**
 **Live App:** [https://machine-learning-gddffquxsgcekqf5mxzcir.streamlit.app/](#)  
 **GitHub Repository:** [shrihanshu/machine-learning](#)  

---

##  **Project Overview**  

This project uses **VGG16**, a convolutional neural network (CNN) pre-trained on **ImageNet**, to classify uploaded images. The model takes an input image, processes it, and returns the **top 3 predictions** with confidence scores.  

 **User Uploads an Image (JPG, PNG, JPEG)**  
 **App Preprocesses the Image (Resizing, Normalization)**  
 **VGG16 Model Predicts the Image Class**  
 **Top 3 Predictions are Displayed**  

---

##  **Project Structure**  
**/soccer-ball-classifier │── app.py # Main Streamlit app │── requirements.txt # Dependencies │── README.md # Documentation**




 



##  **Tech Stack**
- **Python 3.x**  
- **Streamlit** (Web App Framework)  
- **TensorFlow / Keras** (Pre-trained VGG16 Model)  
- **NumPy** (Array Operations)  
- **OpenCV (cv2)** (Image Processing)
##  **Installation & Setup**  

 ### ** Clone the Repository**

 ### ** CREATE A VIRTUAL ENVIRONMENT**    

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

---

### ** Install Dependencies ** ###
pip install -r requirements.txt

### ** Run the App Locally** ###
streamlit run app.py

### **Deployment on Streamlit Community Cloud**
 Push your project to GitHub
 Go to Streamlit Cloud and log in
 Click "New App", select your repo, and choose app.py as the entry point
 Click "Deploy" 🚀

### **How It Works**
1 User uploads an image
---
2 Image is read using OpenCV (cv2)
---
3 Preprocessing:

Resize to 224x224 pixels
---
Convert to array format
---
Normalize using imagenet_utils.preprocess_input
---
4 VGG16 Model Predicts the Top 3 Labels
---
5 Results are displayed with confidence percentages
---

### **  Troubleshooting **
1 Getting libGL.so.1: cannot open shared object file Error?
Fix: Use opencv-python-headless instead of opencv-python in requirements.txt.

2 Streamlit App Not Deploying?
Ensure your GitHub repo is public
Check the Streamlit logs for errors
Verify that requirements.txt is correctly formatted

---


### ** Future Improvements** ###
 Add support for multiple image uploads
---
 Improve UI with better styling
---
 Deploy on AWS/GCP for scalability

