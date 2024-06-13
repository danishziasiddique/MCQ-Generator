# Quiz Craft

Quiz Craft is an intelligent MCQ (Multiple Choice Questions) generator that uses the power of AI to create and evaluate quizzes. This application is built using Streamlit and Langchain, leveraging OpenAI's GPT model to generate and review quiz questions.

## **Preview**
![Screenshot 2024-06-12 at 12 17 43 PM](https://github.com/danishziasiddique/MCQ-Generator-Using-LangChain-and-OpenAI/assets/82972335/a1cc15d1-f750-467e-a5cd-b2c568994940)


## Features

- Upload a PDF or text file as input for the quiz.
- Generate multiple-choice questions based on the input text.
- Evaluate the complexity of the generated questions to ensure they are appropriate for the target audience.
- View the generated questions and their evaluations in a user-friendly format.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/quiz-craft.git
    cd quiz-craft
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

2. **Upload a PDF or text file:**

    In the web interface, upload a PDF or text file containing the text you want to generate MCQs from.

3. **Input quiz details:**

    - Specify the number of MCQs.
    - Enter the subject.
    - Set the complexity level of the questions.

4. **Generate and evaluate the quiz:**

    Click on the "Create MCQs" button to generate and evaluate the quiz. The results will be displayed in a table format along with a complexity review.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features you'd like to see.


Feel free to customize this README file further according to your specific needs or preferences.

