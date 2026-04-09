# DevOps Automation Project (AWS + Bash + Python)

## Project Overview

This project demonstrates a real-world DevOps workflow combining:

- AWS EC2 provisioning using Python (Boto3)
- System monitoring using Bash scripting
- Reusable automation via GitHub
- Production-ready scripting practices

---

## Features

- Automated EC2 instance creation
- Disk usage monitoring (`df -h`)
- Memory usage calculation with alert system
- CPU core detection
- Safe scripting using:
  - `set -e` (fail fast)
  - `set -o pipefail` (pipeline safety)
- Global command execution (`monitor`)

---

## Project Structure

```
│
├── aws/
│ └── create_ec2.py
│
├── scripts/
│ └── monitor.sh
│
├── docs/
│ └── architecture.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶How to Run

### 1️. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/devops-automation-project.git
cd devops-automation-project

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Create EC2 Instance

```bash
python aws/create_ec2.py

```

### 4. SSH into Instance

```bash
ssh -i <your-key.pem> ubuntu@<public-ip>

```

### 5. Run Monitoring Script

```bash
chmod +x scripts/monitor.sh
./scripts/monitor.sh

```

### 6. Global Command (Pro Feature)

Run script from anywhere:

```bash
sudo ln -s $(pwd)/scripts/monitor.sh /usr/local/bin/monitor
monitor

```

## Sample Output

```bash
Checking system...
Filesystem Size Used Avail Use%
/dev/root 6.8G 2.5G 4.3G 37%

Memory usage: 45.54 %

CPU cores:
2
```

---

## Demo / Proof

![alt text](<Screenshot 2026-04-09 122531.png>) ![alt text](<Screenshot 2026-04-09 121628.png>) ![alt text](<Screenshot 2026-04-09 122147.png>) ![alt text](<Screenshot 2026-04-09 122158.png>)

---

## Architecture

Detailed architecture explanation:  
`docs/architecture.md`

---

## Concepts Used

- Bash scripting
- Linux system monitoring
- AWS EC2
- Python Boto3
- DevOps automation practices

---

## 👨Author

**Dasun Sandeepa**  
Software Engineering Undergraduate  
DevOps Enthusiast
