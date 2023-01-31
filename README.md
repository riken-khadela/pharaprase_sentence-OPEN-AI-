# pharaprase_sentence-OPEN-AI-

## Paraphrasing Sentence with ChatGPT3

This project allows you to paraphrase a sentence 50 times using the ChatGPT3 model.

## Setting up the Project

1. To set up the project, follow these steps:

```python
python3 -m venv env
```
2. Activate the virtual environment:
```python
source env/bin/activate
```
3. Obtain an API key from OpenAI by creating an account and generating an API key at [here](https://platform.openai.com/account/api-keys)

4. Add your API key to the phara.py file located at home/management/commands/phara.py:
openai.api_key = <API_KEY>
5. Configure your MySQL database in the settings.py file.

6. Run the following commands to apply migrations:
```python
python manage.py makemigrations
python manage.py migrate
```
Your project setup is now complete.


## Usage
To run the project, follow these steps:

1. Create a data.json file containing the text you wish to paraphrase.

2. Run the following command to add the text to your database:
```python
python manage.py add_text
```
3. Run the following command to paraphrase all added sentences:
```python
python manage.py phara
```