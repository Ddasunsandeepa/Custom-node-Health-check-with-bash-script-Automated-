# DevOps Automation Project - Architecture

## Overview

This project demonstrates a simple DevOps workflow that combines **infrastructure provisioning** and **system monitoring automation**.

The architecture includes:

- AWS EC2 instance creation using Python (Boto3)
- Bash-based system monitoring script
- Manual or automated execution on the provisioned server

---

## 1. EC2 Instance Creation (Infrastructure Layer)

The infrastructure is provisioned using a Python script powered by the AWS SDK:

- File: `aws/create_ec2.py`
- Tool: Boto3

### Process Flow:

1. Connect to AWS using configured credentials
2. Request creation of an EC2 instance
3. Specify:
   - AMI (Ubuntu)
   - Instance type (t3.micro)
   - Key pair (for SSH access)
   - Security group (network rules)
   - Subnet (VPC placement)

4. Wait until the instance is in **running state**
5. Retrieve and display:
   - Instance ID
   - Public IP address

### Outcome:

A ready-to-use virtual machine is created in AWS cloud.

---

## 2. Script Execution Layer

Once the EC2 instance is created:

### Steps:

1. Connect to the instance using SSH:

```bash
ssh -i <key.pem> ubuntu@<public-ip>

```

2. Transfer or clone the repository:

```bash
git clone <your-repo-link>
cd devops-automation-project

```

3. Make the script executable:

```bash
chmod +x scripts/monitor.sh
```

4. Run the script:

```bash
./scripts/monitor.sh
```

## 3. Monitoring Flow (Application Layer)

The monitoring script (`monitor.sh`) performs system checks:

### Checks Performed:

- Disk usage → `df -h`
- Memory usage → `free`
- CPU cores → `nproc`

### Alert Logic:

- Calculates memory usage percentage
- If usage > 80%:
  - Displays alert message

### Script Safety Features:

- `set -e` → stops on errors
- `set -o pipefail` → detects pipeline failures

---

## 4. End-to-End Workflow

1. Run Python script → creates EC2 instance
2. Retrieve public IP
3. SSH into instance
4. Execute monitoring script
5. Analyze system health output

---

## 5. Optional Enhancements

Future improvements can include:

- Automating script execution using cron jobs
- Sending alerts via email or Slack
- Dockerizing the monitoring script
- Using Terraform for infrastructure provisioning
- Integrating with monitoring tools like Prometheus

---

## Conclusion

This project demonstrates how DevOps engineers:

- Automate infrastructure provisioning
- Write safe and reusable scripts
- Monitor system health efficiently

It serves as a foundational example of **Infrastructure as Code + Automation + Monitoring**.
