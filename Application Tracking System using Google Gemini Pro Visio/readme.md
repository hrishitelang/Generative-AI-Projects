# ATS (Application Tracking System) for Resumes using Google Gemini Pro

An **Application Tracking System (ATS)** designed to evaluate resumes against job descriptions. This project leverages the power of **Google Gemini Pro API** to analyze resumes, highlight matching keywords, suggest improvements, and compute a match percentage. It helps candidates optimize their resumes for specific roles, increasing the likelihood of passing ATS filters used by employers.

---

## Features

- **Upload Resumes**: Upload resumes in PDF format for analysis.
- **Job Description Matching**: Compare resumes with job descriptions to assess suitability.
- **Match Percentage**: Compute how well the resume aligns with the job description.
- **Keyword Analysis**: Highlight missing and matched keywords.
- **Suggestions for Improvement**: Get actionable advice to make your resume stand out.
- **Resume Insights**: Summarize strengths and weaknesses in the resume.

---

## Demo

1. **Step 1**: Enter the job description into a text box.
2. **Step 2**: Upload the resume in PDF format.
3. **Output**:
   - **Match Percentage**: See how well the resume matches the job description.
   - **Missing Keywords**: Identify critical keywords missing from the resume.
   - **Suggestions**: Get guidance on how to improve the resume.
   - **Detailed Insights**: Summarize the strengths and weaknesses in the resume.

---

## Technology Stack

- **Backend**:
  - Google Gemini Pro API for text and resume analysis.
  - Python for implementing the logic.
- **Frontend**:
  - Streamlit for creating a user-friendly web interface.
- **Libraries**:
  - `google.generativeai`: Access Google Gemini Pro's capabilities.
  - `pdf2image`: Convert PDF resumes into image format.
  - `Pillow (PIL)`: Process images for analysis.
  - `python-dotenv`: Securely manage environment variables like API keys.

---

## Prerequisites

1. **Python 3.10 or higher**: Required for compatibility with Google Gemini Pro.
2. **Google Gemini Pro API Key**:
   - Obtain your API key from [Maker Suite](https://makersuite.google.com).
   - Add the API key to a `.env` file in the project root:
     ```
     GOOGLE_API_KEY=<your_api_key>
     ```
3. **Poppler for Windows**:
   - Download and install Poppler for converting PDFs to images using `pdf2image`.
   - Add the Poppler `bin` directory to your system PATH.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ats-resume.git
   cd ats-resume
   ```

2. Create a virtual environment:
   ```bash
   conda create -p venv python=3.10
   conda activate ./venv
   ```
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the application:
  ```bash
   streamlit run app.py
  
2. Enter the job description and upload a resume to see results.
