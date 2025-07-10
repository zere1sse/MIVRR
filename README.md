# IP Geo-Reputation Analyzer

---

## 📝 Project Description

This command-line tool, written in Python, allows users to gather detailed information about IP addresses. It combines **geographical data** (country, city, ISP, etc.) using the **ip-api.com API** with **reputation intelligence** and potential abuse reports from **AbuseIPDB**.

This is a useful tool for basic threat intelligence analysis, cybersecurity reconnaissance, or simply for exploring the origin and status of an IP address.

---

## ✨ Features

* **Geographical Analysis:** Retrieves data such as country, city, region, ISP, latitude, and longitude.
* **Reputation Analysis:** Queries the abuse confidence score, total reports, and the last time an IP was reported for malicious activities (spam, attacks, etc.).
* **Interactive Input:** Users can input a single IP address via the keyboard or load multiple IPs from a text file.
* **Robust IP Validation:** Employs Python's `ipaddress` library to ensure only valid IP addresses are processed.
* **CSV Export:** Saves all analysis results to a CSV file (`informacion_ip_completa.csv`) for easy further analysis in spreadsheets.
* **Secure API Key Handling:** Uses environment variables (`.env`) to keep API keys out of the source code, ensuring security when sharing the project on public repositories like GitHub.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your_username/your_repository.git](https://github.com/your_username/your_repository.git)
    cd your_repository
    ```
    *(Replace `your_username` and `your_repository` with your GitHub username and repository name)*

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` yet, create it with `pip freeze > requirements.txt` after installing `requests`, `pandas`, `python-dotenv`.)*

3.  **Obtain your AbuseIPDB API Key:**
    * Go to [AbuseIPDB.com](https://www.abuseipdb.com/) and sign up for a free account.
    * Log in and find/generate your API Key in the "API" or "My Account" section.

4.  **Configure your environment variables:**
    * Create a file named `.env` in the root of your project (at the same level as `Mivrr.py`).
    * Inside `.env`, add the following line, replacing `YOUR_API_KEY_HERE` with your actual AbuseIPDB key:
        ```
        ABUSEIPDB_API_KEY=YOUR_API_KEY_HERE
        ```
    * **Important!** This `.env` file is included in `.gitignore` and **will not be uploaded to GitHub** to protect your key.

---

## 🏃 How To Use

1.  **Run the script:**
    ```bash
    python Mivrr.py
    ```

2.  **Choose an option:** The program will ask you how you'd like to provide the IP addresses:
    * `1`: To enter a single IP via the keyboard.
    * `2`: To read IPs from a text file (one IP per line).

3.  **Provide the IP or file:**
    * If you choose `1`, enter the IP when prompted.
    * If you choose `2`, enter the name of your text file (e.g., `ips.txt`). Ensure the file exists in the same directory or provide the full path.

4.  **Results:** The script will process the IPs, showing progress in the console. Once completed, it will generate a CSV file named `informacion_ip_completa.csv` in the same directory, containing all collected data. It will also print the first few rows of the CSV to the console.

---

## 📚 Technologies Used

* **Python 3.x**
* **Requests:** For making HTTP calls to APIs.
* **Pandas:** For data manipulation and CSV export.
* **`ipaddress` (Python standard library):** For IP address validation.
* **`python-dotenv`:** For secure management of environment variables (API Keys).
* **`time` (Python standard library):** To add pauses between API calls and prevent rate limiting.

---

## ⚠️ API Limitations

* **ip-api.com:** The free tier allows up to 45 requests per minute from the same IP address.
* **AbuseIPDB:** The free tier typically allows up to 1,000 requests per day.

The script includes small pauses between calls to help mitigate the risk of exceeding these limits.

---

## 🤝 Contributions

Contributions are welcome! If you have ideas to improve the project, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Implement your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

By: zere1sse

---
