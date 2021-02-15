# Udacitrivia

# Getting Started
- This api will help you create a question, delete it, and create a quiz.
- Backend code style is [PEP-8](https://www.python.org/dev/peps/pep-0008/)

## Install resources
### Run backend
  - Install Python 3.7
  - Install pip requirements within following code
  ```bash
  pip install -r requirements.txt
  ```
  - Start the server
  ```bash
  export FLASK_APP=flaskr
  export FLASK_ENV=development
  flask run
  ```
  > If you use windows os, you write 'set' to your terminal instead of 'export'

### Run frontend
  - Install node.js and npm(node package manager)
  - Install packages within following code
  ```bash
  npm install
  ```
  - Run the fronend
  ```bash
  npm start
  ```

# Endpoints

- GET '/categories'
- GET '/questions'
- GET '/categories/< id >/questions'
- POST '/questions/'
- DELETE '/questions/< id >'
- POST '/quizzes'

## GET '/categories'

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

## GET '/questions'

- Fetches a dictionary of questions in which the keys are the ids and the value is the corresponding string of the questions
- Request Arguments: None
- Returns: An object with a categories, 10 questions and count of total questions. Questions have a question, answer, category id and difficulty.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

## GET '/categories/< id >/questions'

- Fetches a dictionary of questions related to the category
- Request Arguments: < id > - id of category
- Returns: An object with a questions related to the category, questions and count of total questions.

```json
{
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

## POST '/questions'

- Create or search the questions
- Create

  - Create new question
  - Request Arguments: json object in the following form

    ```json
    {
      "question": "some question",
      "answer": "some answer",
      "difficulty": 5,
      "category": 2
    }
    ```

  - Response: information about the creation of the question

    ```json
    {
      "success": true
    }
    ```

- Search

  - Search question from all question case insensitive
  - Request Arguments: json object in the following form

    ```json
    {
      "searchTerm": "< string to search >"
    }
    ```

  - Response: list of questions found

    ```json
    {
      "success": true,
      "questions": [
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
      ]
    }
    ```

## DELETE '/questions/< id >'

- Delete the question
- Requested Arguments: < id > - id of question
- Returns: json object about successfully deleted
  
  ```json
  {
    "success": true
  }
  ```

## POST '/quizzes'

- Start a quiz
- Requested Arguments: json object category of questions and previos questions
  
  ```json
  {
    "previous_questions": [21, 22],
    "quiz_category": {
      "type": "Science",
      "id": "1"
    }
  }
  ```

- Returns: json object with question

  ```json
  {
    "question": {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    }
  }
  ```
