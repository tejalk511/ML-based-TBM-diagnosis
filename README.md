# 🧠 ML-Driven Clinical Decision Support for Tuberculosis Meningitis Diagnosis

## Introduction

Diagnosing Tuberculous Meningitis (TBM) and Pyogenic Meningitis (PM) is challenging, especially in resource-limited areas lacking advanced diagnostic tools. This project addresses this challenge by offering a cost-effective diagnostic tool powered by Machine learning and an intuitive web interface to facilitate early and accurate diagnosis of TBM and PM in rural settings.

## Overview of the system 

The diagram represents a Clinical Decision Support System (CDSS), where user input and clinical data are processed by a Diagnostic Model to determine the condition's normality. If abnormal, the Intensity Analyzer evaluates severity, and the system outputs intensity metrics and a graphical representation for user interaction.

![image](https://github.com/user-attachments/assets/f2c6a509-1659-46b1-b247-fbd6b80b97d7)

## Machine Learning model deployed - 
- The ensemble learning model trains three base models (Random Forest, Gradient Boosting, and SVM (linear)) on the same training set, producing individual predictions.
- The outputs (Prediction 1, 2, and 3) are combined to generate the Final Prediction, improving accuracy and robustness through result aggregation.

![image](https://github.com/user-attachments/assets/fe68e99a-fc0c-4107-88ab-3105b7eb629d)



## 🛠️ Technical Details

- **Programming Language**: Python 3.x
- Libraries:
  - **NumPy**: For efficient numerical data manipulation.
  - **Matplotlib**: For creating visualizations.
- Machine Learning:
  - **Random Forest**: For robust classification.
  - **Gradient Boosting**: Enhances model accuracy through iterative improvements.
  - **Support Vector Machine (SVM)** - Linear: For effective data separation.

![image](https://github.com/user-attachments/assets/483c352e-5a24-4fa9-b813-9629e5db5e99)

📊 **Clinical Decision Support System (CDSS)**
- **Interactive Web Interface**: Easy-to-use Gradio interface designed for minimal training.
- **Machine Learning Model**: Provides reliable diagnoses based on CSF data.
- **Graphical and Textual Output**: Clear visual and textual explanations of diagnostic results.
- 📝 **Input**:
7 CSF Laboratory Features: Essential data points for accurate meningitis diagnosis.


- 📈 **Output**:
Graphical Representation: Visual severity representation using Matplotlib.
Textual Summary: Clear indications of severity levels (e.g., Mild, Severe, Highly Severe).



## 📝 Conclusion
The Meningitis Diagnostic Aid combines advanced machine learning techniques with a userfriendly interface to offer a practical diagnostic solution, overcoming challenges in under-resourced medical environments.
