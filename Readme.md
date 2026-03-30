# 📝 AI Grammar Corrector & Paraphraser

A simple web application built using **Python (Flask)** that:

* ✅ Corrects English grammar and spelling mistakes
* 🔁 Paraphrases the corrected text
* 🎨 Provides a clean modern UI (black + lavender theme)

---

## 🚀 Features

* Grammar & spelling correction using **LanguageTool API**
* Basic paraphrasing (offline logic)
* Responsive and modern frontend
* Easy to run locally

---

## 📁 Project Structure

```
project/
│── app.py
└── templates/
    └── index.html
```

---

## ⚙️ Installation

### 1. Clone or Download Project

```bash
git clone <your-repo-url>
cd project
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install flask requests
```

---

## ▶️ Run the Application

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Input

```
i has went to the market yesterday and buyed some vegetable.
```

### ✅ Output

**Corrected Text:**

```
I went to the market yesterday and bought some vegetables.
```

**Paraphrased Text:**

```
I visited to the market yesterday and purchased some vegetables.
```

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML, CSS, JavaScript**
* **LanguageTool API**
---

## 💡 Future Improvements

* 🤖 Add AI-based paraphrasing (ChatGPT / OpenAI)
* ⚡ Real-time typing correction
* 📋 Copy-to-clipboard feature
* 🌙 Dark/Light mode toggle
* 🌐 Deploy online

---

## 📄 License

This project is open-source and free to use.
