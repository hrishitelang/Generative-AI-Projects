# Calorie Advisor: AI-Powered Food Analysis App

## Problem Statement

Maintaining a healthy diet is crucial for overall well-being, but it can be challenging to track the nutritional content and caloric intake of daily meals. Many individuals struggle to assess whether their food choices are balanced and healthy, leading to potential health issues over time.

---

## Project Description

**Calorie Advisor** is a Large Image Model (LIM) application powered by Google Gemini Pro Vision API. This app enables users to analyze their meals by simply uploading an image of their food. The app provides:
- A breakdown of the food items and their calorie content.
- An assessment of whether the meal is healthy or not.
- Insights into the macronutrient distribution (carbohydrates, fats, fiber, sugar, etc.).

The goal of this app is to encourage healthier food choices by providing actionable nutritional insights in real time.

---

## Methodology and Steps

### 1. **Problem Understanding and Objective Setting**
   - Identify the challenge of tracking nutrition and caloric intake from meals.
   - Define the app's objectives to provide detailed and accurate food analysis.

### 2. **Application Architecture**
   - **Frontend**: Built using Streamlit for an intuitive interface where users can upload food images.
   - **Backend**: Leveraged Google Gemini Pro Vision API for image analysis and nutritional insights.

### 3. **Steps to Build**
   - **Environment Setup**: Created a virtual environment and configured dependencies.
   - **Input Handling**: Enabled users to upload images and converted the input into a format compatible with the Google Gemini Pro Vision API.
   - **Custom Prompt Design**: Developed a custom prompt to instruct the model to analyze images for food items, calorie counts, and nutritional balance.
   - **Data Processing**: Integrated the Vision API to retrieve detailed insights based on the uploaded food images.
   - **Result Display**: Presented calorie breakdown and health assessment on the app's interface.

---

## Tools and Technologies

- **Models**: Google Gemini Pro Vision API
- **Frameworks**: Streamlit
- **Libraries**: `google-generative-ai`, `python-dotenv`, `Pillow` (for image handling)
- **Development Environment**: Python (3.10), Conda for virtual environment management

---

## Challenges Faced

- **Prompt Engineering**: Crafting an input prompt to ensure the Google Gemini Pro Vision API provided detailed and relevant responses.
- **Data Format Conversion**: Adapting the uploaded image to the format required by the Vision API.
- **Accuracy**: Balancing accuracy in calorie and nutrient breakdowns based on image analysis, which can be limited by the quality and composition of the uploaded image.

---

## Outcome

- Developed a fully functional **Calorie Advisor** app capable of analyzing meal images in real time.
- Successfully identified food items, calculated calorie counts, and provided macronutrient breakdowns for uploaded images.
- Encouraged healthier eating habits by offering insights into the nutritional quality of meals.

---

## What I Learned

- Gained expertise in integrating Google Gemini Pro Vision API for image-based AI applications.
- Enhanced skills in **prompt engineering** for fine-tuning large model responses.
- Improved knowledge of building end-to-end applications using **Streamlit**.
- Strengthened understanding of food nutrition and calorie tracking from a technical perspective.

---

## Future Scope

- **Multi-Language Support**: Enable analysis for meals labeled in different languages.
- **Expanded Database**: Incorporate a larger database for recognizing more food items and cuisines.
- **Mobile Integration**: Develop a mobile version of the app for easier access and usage.

---

## How to Run the Application

1. **Set up the Environment**:
   ```bash
   conda create -n calorie-advisor python=3.10
   conda activate calorie-advisor
   pip install -r requirements.txt

2. **Create the .env File:**
  ```bash
  Add your Google API key:
  GOOGLE_API_KEY=your_google_api_key_here

3. **Run the App:**
  ```bash
  streamlit run app.py

4. **Upload a Food Image:**
  ```bash
  Upload an image of your meal to analyze its nutritional content.
