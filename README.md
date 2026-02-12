# ASSIGNMENT-NLP-1
# 🧠 NLP Text Preprocessing Techniques

This project demonstrates essential **Natural Language Processing (NLP) preprocessing techniques** used to clean and prepare raw text data before applying Machine Learning models.

The main objective is to convert unstructured text into meaningful and analyzable format.

---

## 📂 Project Files

| File Name | Description |
|-----------|------------|
| Lower.py | Converts text to lowercase |
| ReHtml.py | Removes HTML tags |
| Removeurl.py | Removes URLs |
| Reemoji.py | Removes emojis |
| Remove punctuation.py | Removes punctuation |
| Removestop.py | Removes stopwords |
| Stemming.py | Applies stemming |
| Lemmazation.py | Applies lemmatization |
| sample_*.csv | Input dataset |

---

## ⚙️ NLP Techniques Used

### 1. Lowercasing
Converts all characters into lowercase for consistency.

Example:
```
Hello WORLD → hello world
```

---

### 2. Removing HTML Tags
Removes HTML elements from text.

Example:
```
<p>This is text</p> → This is text
```

---

### 3. Removing URLs
Removes website links.

Example:
```
Visit https://google.com → Visit
```

---

### 4. Removing Emojis
Removes emojis from text.

Example:
```
I love NLP 😊 → I love NLP
```

---

### 5. Removing Punctuation
Removes symbols like `. , ! ?`

Example:
```
Hello!!! → Hello
```

---

### 6. Removing Stopwords
Removes common words that do not add much meaning.

Example:
```
This is a good book → good book
```

---

### 7. Stemming
Reduces words to root form.

Example:
```
playing, played, plays → play
```

---

### 8. Lemmatization
Converts words into meaningful base form.

Example:
```
better → good
```

---

## 📊 Dataset

The project uses a CSV dataset:

```
sample_5f9a63760f3d35a228057d9963b31eb6.csv
```

Text is cleaned step-by-step using the above NLP techniques.

---

## 🚀 Applications

These preprocessing techniques are useful in:

- Sentiment Analysis
- Spam Detection
- Text Classification
- Chatbots
- POS Tagging
- Machine Learning NLP Models

---

## 🛠️ Technologies Used

- Python
- NLTK
- Pandas
- Regular Expressions

---

## 📌 Conclusion

Text preprocessing is an important step in NLP pipelines.  
This project demonstrates how raw text can be transformed into structured data using standard preprocessing techniques.
