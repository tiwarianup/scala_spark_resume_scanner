# Resume Scanner AI

## Overview

The Resume Scanner AI is a POC designed to help users evaluate potential Scala/Spark candidate resumes against specific job descriptions given by clients. Utilizing Gemini LLM, the application provides detailed feedback on the alignment between the resume and job description, including a percentage match and identification of missing keywords, detailed analysis, recommendations and final verdict.

## Features

- **Resume Upload**: Users can upload their resumes in PDF format.
- **Job Description Input**: Users can input the job description they are targeting.
- **Detailed Analysis**: The tool generates a detailed evaluation of the resume, highlighting strengths and weaknesses.
- **Percentage Match**: The application calculates and displays the percentage match between the resume and the job description, listing missing keywords and final thoughts.

## Installation

### Prerequisites

- Python 3.10 or higher
- A python virtual environment (prefferably conda managed)

### Required Libraries

Create a virtual environment to setup necessary packages:

```bash
conda create -n genai_resume
```

Install the required libraries in your virtual environment using pip:

```bash
pip install streamlit python-dotenv pillow pdf2image google-generativeai
```

## Setup

1. **Clone the Repository**: Clone the project repository and navigate into the project directory.

   ```bash
   git clone https://github.com/tiwarianup/scala_spark_resume_scanner.git
   ```

2. **Environment Variables**: Create a `.env` file in the root directory of the project and add your Google API key.

   Add the following line to the `.env` file:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

3. **Run the Application**: Start the Streamlit application.

   ```bash
   streamlit run app.py
   ```

## Usage

### Uploading a Resume

- Click on the "Browse files" button to upload your resume in PDF format.
- The application will confirm the successful upload of the file.

### Inputting Job Description

- Enter the job description in the provided text area.

### Analyzing the Resume (Scoring, Analysis, Recommendation & Verdict)

- Click on the "Summarize the Resume" button to receive a professional evaluation of your resume.
- Alternatively, click on the "Check Percentage match" button to get a percentage match along with missing keywords and final thoughts.

## Application Screenshots

1. Main Screen - to input dob description and resume upload
  ![Main Screen - to input dob description and resume upload](https://github.com/tiwarianup/scala_spark_resume_scanner/blob/main/images/Main_screen.PNG)
2. Candidate Evaluation Summary
   ![Candidate Evaluation Summary](https://github.com/tiwarianup/scala_spark_resume_scanner/blob/main/images/Candidate_profile_summary.PNG)
3. Candidate Percentage Match & Verdict
   ![Candidate Percentage Match & Verdict](https://github.com/tiwarianup/scala_spark_resume_scanner/blob/main/images/Percentage_match.PNG)
