# ⚽ **Image Classifier using VGG16 & Streamlit**  

This project is a **deep learning-based image classifier** that predicts whether an uploaded image contains a **soccer ball** or other objects. It is built using **Streamlit** for the web interface and **VGG16 (a pre-trained deep learning model)** for image classification.

---

## 🚀 **Demo**
👉 **Live App:** [https://machine-learning-gddffquxsgcekqf5mxzcir.streamlit.app/](#)  
👉 **GitHub Repository:** [shrihanshu/machine-learning](#)  

---

## 📝 **Project Overview**  

This project uses **VGG16**, a convolutional neural network (CNN) pre-trained on **ImageNet**, to classify uploaded images. The model takes an input image, processes it, and returns the **top 3 predictions** with confidence scores.  

🔹 **User Uploads an Image (JPG, PNG, JPEG)**  
🔹 **App Preprocesses the Image (Resizing, Normalization)**  
🔹 **VGG16 Model Predicts the Image Class**  
🔹 **Top 3 Predictions are Displayed**  

---

## 📂 **Project Structure**  
**/soccer-ball-classifier │── app.py # Main Streamlit app │── requirements.txt # Dependencies │── README.md # Documentation**

---

## 🛠️ **Tech Stack**
- **Python 3.x**  
- **Streamlit** (Web App Framework)  
- **TensorFlow / Keras** (Pre-trained VGG16 Model)  
- **NumPy** (Array Operations)  
- **OpenCV (cv2)** (Image Processing)  

---


---

## 🛠️ **Tech Stack**
- **Python 3.x**  
- **Streamlit** (Web App Framework)  
- **TensorFlow / Keras** (Pre-trained VGG16 Model)  
- **NumPy** (Array Operations)  
- **OpenCV (cv2)** (Image Processing)  

---

## 🛠️ **Tech Stack**
- **Python 3.x**  
- **Streamlit** (Web App Framework)  
- **TensorFlow / Keras** (Pre-trained VGG16 Model)  
- **NumPy** (Array Operations)  
- **OpenCV (cv2)** (Image Processing)  

---

## 🛠️ **Tech Stack**
- **Python 3.x**  
- **Streamlit** (Web App Framework)  
- **TensorFlow / Keras** (Pre-trained VGG16 Model)  
- **NumPy** (Array Operations)  
- **OpenCV (cv2)** (Image Processing)
## 🖥️ **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo

---

### ** 2️⃣ CREATE A VIRTUAL ENVIRONMENT** ###

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

---

### **3️⃣ Install Dependencies ** ###
pip install -r requirements.txt

### **4️⃣ Run the App Locally** ###
streamlit run app.py

### **Deployment on Streamlit Community Cloud**
1️⃣ Push your project to GitHub
2️⃣ Go to Streamlit Cloud and log in
3️⃣ Click "New App", select your repo, and choose app.py as the entry point
4️⃣ Click "Deploy" 🚀

⚠️ Note: Ensure your requirements.txt includes:

nginx
Copy
Edit
streamlit
numpy
opencv-python-headless
tensorflow

### **How It Works**
1️⃣ User uploads an image
2️⃣ Image is read using OpenCV (cv2)
3️⃣ Preprocessing:

Resize to 224x224 pixels
Convert to array format
Normalize using imagenet_utils.preprocess_input
4️⃣ VGG16 Model Predicts the Top 3 Labels
5️⃣ Results are displayed with confidence percentages
---

### ** 🛠️ Troubleshooting **
1️⃣ Getting libGL.so.1: cannot open shared object file Error?
Fix: Use opencv-python-headless instead of opencv-python in requirements.txt.

2️⃣ Streamlit App Not Deploying?
Ensure your GitHub repo is public
Check the Streamlit logs for errors
Verify that requirements.txt is correctly formatted

---


# **🔮 Future Improvements** #
✅ Add support for multiple image uploads
✅ Improve UI with better styling
✅ Deploy on AWS/GCP for scalability

