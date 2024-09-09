Text Translation App
--------------------
This application translates text to English using Google’s Gemini model and Streamlit for the user interface.

Overview
--------

This platform allows users to translate text to English using a generative AI model. The platform leverages a Google Gemini-based text processing pipeline for efficient and accurate translations.

Technology Stack
----------------

-   **Streamlit**: For creating the user interface.
-   **Google Gemini**: A generative AI model used for translating text.
-   **LangChain**: Used to handle the prompt and chain for the translation task.
-   **Pandas**: For data manipulation and processing.
  Features
  --------
  
### 1\. **Translate Text**
-   **Description**: Users can enter text they want to translate into English.
-   **Input Fields**:
-   **Text**: The text that the user wants to translate.
-   **Function**: The Google Gemini model processes the input text and generates the translated text.
-   **UI Element**:
    -   A text area for entering the text to be translated.
    -   A button to trigger the translation action.
-   **Output**: The translated text is displayed.
