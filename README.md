# Attendance Monitoring Automation

    py -3.13 -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    playwright install chromium
    copy .env.example .env   # then fill in values
    pytest --headed
