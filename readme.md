# ATS Resume Expert

A Streamlit web application that leverages Google Generative AI to analyze resumes against job descriptions and provide professional feedback. This tool helps job seekers tailor their resumes to specific job descriptions and improve their chances of landing their desired jobs.

## Features

- **Resume Analysis**: Upload your resume in PDF format and get a professional evaluation.
- **Skill Improvement Suggestions**: Receive suggestions on how to improve your skills based on the job description.
- **Percentage Match**: Evaluate how well your resume matches the job description with a percentage match score.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- Streamlit
- Python-dotenv
- Pillow
- pdf2image
- google-generativeai

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/ats-resume-expert.git
    cd ats-resume-expert
    ```

2. **Install the required packages**:
    ```sh
    pip install streamlit python-dotenv Pillow pdf2image google-generativeai
    ```

3. **Set up your Google API key**:
    - Create a `.env` file in the project root directory.
    - Add your Google API key to the `.env` file:
      ```env
      Google_api_key=YOUR_GOOGLE_API_KEY
      ```

### Usage

1. **Run the Streamlit application**:
    ```sh
    streamlit run app.py
    ```

2. **Using the application**:
    - **Upload Resume**: Click on "Upload your Resume (PDF)..." and select your resume file.
    - **Input Job Description**: Enter the job description in the provided text area.
    - **Get Feedback**: Click on the respective buttons to get professional feedback, skill improvement suggestions, or percentage match.

### Example Prompts

- **Tell me about the resume**:
    ```markdown
    You are an experienced HR with Tech Experience in the field of data science, full stack, web development,
    Big Data engineering, DEVOPS, Data Analyst. Your task is to review the provided resume against the job description for these profiles.
    Please share your professional evaluation on whether the candidate's profile aligns with the role, highlighting the strengths and weaknesses
    of the applicant in relation to the specified job role.
    ```

- **How can I improve my skills**:
    ```markdown
    You are an experienced HR with Tech Experience in the field of data science, full stack, web development,
    Big Data engineering, DEVOPS, Data Analyst. Your task is to review the provided resume against the job description for these profiles.
    Please share your professional evaluation on whether the candidate's profile aligns with the role, highlighting the strengths and weaknesses
    of the applicant in relation to the specified job role.
    ```

- **Percentage match**:
    ```markdown
    You are an experienced HR with Tech Experience in the field of data science, full stack, web development,
    Big Data engineering, DEVOPS, Data Analyst. Your task is to evaluate the percentage match of the provided resume against the job description
    for these profiles. Please provide the percentage match and any key observations.
    ```

## Contributing

Contributions are welcome! If you have suggestions for improving the application, please fork the repository and create a pull request. You can also submit issues for any bugs or feature requests.

1. **Fork the repository**:
    - Click the "Fork" button at the top right of this page.

2. **Create a new branch**:
    ```sh
    git checkout -b feature/AmazingFeature
    ```

3. **Commit your changes**:
    ```sh
    git commit -m 'Add some AmazingFeature'
    ```

4. **Push to the branch**:
    ```sh
    git push origin feature/AmazingFeature
    ```

5. **Open a pull request**.

## Author

Rudraksh Tiwari


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [Google Generative AI](https://developers.google.com/generative-ai)
- [Pillow](https://python-pillow.org/)
- [pdf2image](https://github.com/Belval/pdf2image)

---

Feel free to reach out if you have any questions or need further assistance.
