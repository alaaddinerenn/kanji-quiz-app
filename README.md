# Kanji Quiz Application

This is a Kanji quiz application built using PyQt5. The application provides two types of quizzes to help users learn Kanji characters: one for meanings and another for onyomi/kunyomi matching.

## Features

- **Meaning Quiz**: Users are presented with a Kanji character and four English options to choose the correct meaning.
- **Reading Quiz**: Users are shown a Kanji character and must match it with the correct onyomi or kunyomi reading from four options.

## Project Structure

```
kanji-quiz-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── ui                     # User interface components
│   │   ├── __init__.py
│   │   ├── main_window.py      # Main window setup
│   │   ├── meaning_quiz.py     # Meaning quiz logic
│   │   └── reading_quiz.py     # Reading quiz logic
│   ├── models                  # Data models
│   │   ├── __init__.py
│   │   ├── kanji.py            # Kanji character representation
│   │   └── quiz.py             # Quiz management
│   ├── data                   # Data files
│   │   └── kanji_data.json     # Kanji data in JSON format
│   └── utils                  # Utility functions
│       ├── __init__.py
│       └── data_loader.py      # Data loading functions
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kanji-quiz-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will launch the Kanji quiz application, allowing you to choose between the meaning quiz and the reading quiz.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.