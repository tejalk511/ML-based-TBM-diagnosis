# 🧠 Meningitis Diagnostic Aid using Machine Learning

## Introduction

Meningitis is a severe condition that demands prompt diagnosis. However, specialized diagnostic tools and expertise are often unavailable in resource-limited or rural settings. This project addresses this challenge by offering a cost-effective diagnostic tool powered by machine learning and an intuitive web interface.


## ❓ Problem Statement

- **Access Limitations**: Specialized diagnostic tests are often out of reach in resource-constrained settings.

- **Critical Early Detection**: Timely diagnosis is essential for effective treatment but is often delayed.

- **Resource Deficiency**: Limited availability of advanced diagnostic tools impacts patient care.

## 💡 Solution Overview

- **Data Input**: Enter CSF profile features through the web interface.
- **Model Analysis**: Machine learning models process the data to generate diagnostic outputs.

- **Results Presentation**: Results are displayed with graphical and textual summaries, highlighting the severity of the condition.

📊 **Clinical Decision Support System (CDSS)**

- 🌐 **Interactive Web Interface**: Easy-to-use Gradio interface designed for minimal training.
- 🧬 **Machine Learning Model**: Provides reliable diagnoses based on CSF data.
- 📊 **Graphical and Textual Output**: Clear visual and textual explanations of diagnostic results.

- 📝 **Input**:
7 CSF Laboratory Features: Essential data points for accurate meningitis diagnosis.

- 📈 **Output**:
Graphical Representation: Visual severity representation using Matplotlib.
Textual Summary: Clear indications of severity levels (e.g., Mild, Severe, Highly Severe).

## 🛠️ Technical Details

- **Programming Language**: Python 3.x
- Libraries:
  - **NumPy**: For efficient numerical data manipulation.
  - **Matplotlib**: For creating visualizations.
- Machine Learning:
  - **Random Forest**: For robust classification.
  - **Gradient Boosting**: Enhances model accuracy through iterative improvements.
  - **Support Vector Machine (SVM)** - Linear: For effective data separation.

## 📝 Conclusion
The Meningitis Diagnostic Aid combines advanced machine learning techniques with a userfriendly interface to offer a practical diagnostic solution, overcoming challenges in under-resourced medical environments.
