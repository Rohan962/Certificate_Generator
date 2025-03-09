# Certificate Generator Sender

The Automatic Certificate Generator and Sender is a Django-based web tool that simplifies the process of creating and distributing certificates. 

## Key features include

- CSV Data Import: Upload student data from a CSV file.
- Custom Certificate Templates: Use PowerPoint (.pptx) templates with custom tags.
- Tag-Based Customization: Replace tags with student-specific information.
- Automatic Merging: Merge data and templates seamlessly.
- Email Notifications: Automatically send certificates via email.
- User-Friendly Dashboard: Manage tasks and monitor progress.

### Project Video Explanation


[Watch](https://youtu.be/6yTYP39d9Gs) my project video on YouTube for a detailed walkthrough. Simplify your certificate creation and distribution process with our tool.

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/embrizon.git
cd embrizon
```

---

### 2️⃣ Setup a Virtual Environment
```bash
python -m venv venv
```
- **On Linux/macOS:**  
  ```bash
  source venv/bin/activate
  ```
- **On Windows:**  
  ```bash
  venv\Scripts\activate
  ```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables
- **Create a `.env` file** in the project root:
  ```bash
  touch .env
  ```
- **Add the following credentials inside `.env`:**
  ```
  DJANGO_SECRET_KEY=your-secret-key
  DJANGO_DEBUG=True
  DJANGO_ALLOWED_HOSTS=embrizon.co.in,www.embrizon.co.in
  AWS_ACCESS_KEY_ID=your-aws-key
  AWS_SECRET_ACCESS_KEY=your-aws-secret
  ```

---

### 5️⃣ Install these packages LibreOffice and unoconv (if not installed)
```bash
sudo apt install libreoffice
sudo apt install unoconv
```

---

### 6️⃣ Apply Migrations
```bash
python manage.py migrate
```


---

### 7️⃣ Run the Development Server
```bash
python manage.py runserver
```
The app will be available at:  
🔗 **http://127.0.0.1:8000/**  

---

## 📦 Deployment on cPanel
If you're deploying the project on cPanel:
1. Ensure that **LibreOffice** and **Unoconv** are installed on the server.
2. Set environment variables in **cPanel > Python App > Edit**.
3. Restart the Python application from cPanel.

---

## ❓ Troubleshooting
- **Issue:** `ImportError: No module named 'django'`  
  ✅ Solution: Ensure the virtual environment is activated before running commands.

- **Issue:** `Permission Denied for venv/Scripts/activate`  
  ✅ Solution: Try `chmod +x venv/Scripts/activate` and then run the activation command.

---

## 👤 Author
- **Name:** [Your Name]  
- **Email:** [your-email@example.com]  
- **Website:** [your-website.com]

---

### 🎯 Happy Coding! 🚀


