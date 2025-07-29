# 🔐 PCI DSS Simulation Web App

This project simulates a small-scale, secure payment processing application to demonstrate **PCI DSS compliance** concepts. Built using **Python Flask**, the app encrypts cardholder data, implements access controls, and securely logs transactions — all core principles of PCI DSS.

---

## 📌 Features

- 🧾 **Secure Credit Card Form**  
  Simulated payment input form with no real data processed

- 🔐 **Fernet Encryption**  
  Card numbers are encrypted before being logged/stored (PCI Req. 3)

- 🔒 **Role-Based Access Control**  
  Admin login (session-based) required to view transaction logs (PCI Req. 7)

- 📁 **Secure Logging**  
  Logs only encrypted/masked data to avoid exposing PANs (PCI Req. 10)

- 📜 **PCI DSS Compliance Checklist**  
  Documentation outlining how each PCI requirement is addressed

- 💻 **Clean UI**  
  Styled HTML/CSS for a more professional appearance

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Cryptography (Fernet)
- HTML/CSS

---

## 📂 Project Structure

```
├── app.py                   # Main Flask app
├── secret.key               # Fernet encryption key
├── logs/
│   └── payment.log          # Encrypted payment logs
├── docs/
│   └── pci_checklist.md     # PCI DSS requirement breakdown
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## ⚙️ Installation & Usage

1. **Clone this repository:**
```bash
git clone https://github.com/Froyli/pci-dss-simulation.git
cd pci-dss-simulation
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
python app.py
```

4. **Visit in your browser:**
```
http://localhost:5000
```

- Use dummy credit card data
- Login as admin to view logs:
  - Username: `admin`
  - Password: `password123`

---

## 📋 PCI DSS Requirements Simulated

| Requirement | Description                          | Status |
|-------------|--------------------------------------|--------|
| Req 3       | Encrypt stored cardholder data       | ✅     |
| Req 7       | Restrict access to cardholder data   | ✅     |
| Req 8       | Identify and authenticate users      | ✅     |
| Req 10      | Track and monitor access             | ✅     |
| Others      | Documented in `/docs/pci_checklist.md` | ✅/⚠️  |

---

## 🎯 Why I Built This

As a computer science student and aspiring **SOC Analyst**, I wanted to demonstrate:
- Real-world understanding of security frameworks
- Technical ability to build secure applications
- Awareness of compliance standards like **PCI DSS**

---

## 📬 Contact

**Carlton Jackson**  
🛡️ Aspiring SOC Tier 1 Analyst  
📧 carltonjackson56@gmail.com  
🔗 [[LinkedIn Profile](https://www.linkedin.com/in/carlton-jackson-1b0038255/]

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
