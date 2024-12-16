[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# ATS Resume Expert

This project is a web application designed to help users improve their resumes by providing feedback on how well their resumes align with a given job description. It leverages the power of Google Gemini to analyze resumes and provide actionable insights.

## Features

-   **Resume Analysis:** Upload your resume in PDF format and compare it against a job description.
-   **ATS Simulation:** Simulates an Applicant Tracking System (ATS) to evaluate how well your resume matches the job requirements.
-   **Detailed Feedback:** Provides a percentage match indicating the alignment between your resume and the job description, along with a detailed evaluation of your profile's strengths and weaknesses.
-   **Actionable Improvements:** Offers specific, actionable suggestions on how to improve your resume to better align with the job requirements.
-   **Google Gemini Integration:** Uses Google Gemini to provide intelligent and relevant feedback.

## How to Use

1.  **API Key:** Enter your Google Generative AI API key in the provided field.
2.  **Job Description:** Paste the job description into the "Job Description" text area.
3.  **Upload Resume:** Upload your resume in PDF format using the file uploader.
4.  **Analysis:** Click the "Tell Me About the Resume" button to get a detailed analysis of your resume against the job description.
5.  **Improvement Suggestions:** Click the "How Can I Improve my profile" button to get actionable suggestions on how to improve your resume.

## Technologies Used

-   **Python:** The core programming language for the application.
-   **Streamlit:** A Python library used to create the web application.
-   **PyPDF2:** A Python library used to extract text from PDF files.
-   **Google Gemini:** A large language model used to analyze resumes and provide feedback.

## Getting Started

1.  Make sure you have Python installed on your system.
2.  Install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4.  Open your browser and go to the address provided by Streamlit.

## Contributing

Contributions are welcome! If you have any ideas or suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[contributors-shield]: https://img.shields.io/github/contributors/khawslee/ATS-Resume-Score.svg?style=for-the-badge
[contributors-url]: https://github.com/khawslee/ATS-Resume-Score/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/khawslee/ATS-Resume-Score.svg?style=for-the-badge
[forks-url]: https://github.com/khawslee/ATS-Resume-Score/network/members
[stars-shield]: https://img.shields.io/github/stars/khawslee/ATS-Resume-Score.svg?style=for-the-badge
[stars-url]: https://github.com/khawslee/ATS-Resume-Score/stargazers
[issues-shield]: https://img.shields.io/github/issues/khawslee/ATS-Resume-Score.svg?style=for-the-badge
[issues-url]: https://github.com/khawslee/ATS-Resume-Score/issues
[license-shield]: https://img.shields.io/github/license/khawslee/ATS-Resume-Score.svg?style=for-the-badge
[license-url]: https://github.com/khawslee/ATS-Resume-Score/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/khawslee