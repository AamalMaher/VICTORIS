#  translation model 
### I utilize Google’s Gemini translation model to convert text into English by providing it with specific prompts.<br>
# translation api


Base URL<br>
`http://127.0.0.1:5000`
  
## API Endpoint<br>
### 1.Translate Text (/translate)
- **URL**: `/translate`
- **Method**: `POST`<br>
- **Description**:`Translates the provided text to English`.
#### **Request Body**:
```
{
  "text": "text that you want to translate"
}
```
#### **Success Response**:
- **Code**: `200 OK`
#### **Response Body**:<br>
```
{
  "Translated text": "translated text here"
}
```
## here is live api from streamlit , lets try it:
https://victoris-jpg3zajivdafw3u72e6sa7.streamlit.app/

