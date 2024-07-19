# Email-Spam-Detection

**Overview:**

This project aims to provide a robust solution for spam detection in emails using machine learning techniques. We have developed a model capable of distinguishing between spam and non-spam emails with high accuracy. Users can interact with the model through a user-friendly web application interface, enabling real-time spam detection for any provided email content.

**Project Structure:**

**Data Collection:**
  <br>Scrape data from emails using email and imaplib library.
  
**Data Handling:**
  <br>We utilized pandas for efficient data manipulation and analysis, along with numpy for numerical operations.

**Text Preprocessing:**
  <br>For preprocessing the email content, we employed nltk for tasks such as tokenization, stop words removal, stemming, and lemmatization, ensuring clean and standardized text data.

**Model Selection:**
  <br>After experimenting with various machine learning algorithms, we opted for the Multinomial Naive Bayes classifier from scikit-learn, which demonstrated superior performance in handling textual data.

**Model Evaluation:**
  <br>We evaluated the model using standard metrics such as accuracy, precision, recall, and F1-score, ensuring its reliability and effectiveness in distinguishing between spam and non-spam emails.

**Web Application Development:**
  <br>We deployed the model using FastAPI along with HTML and CSS for creating a user-friendly web interface. This enables users to input email content and receive real-time predictions regarding its spam classification.

