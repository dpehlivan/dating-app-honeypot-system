
🐝 Honeypot & Attacker Behavior Analytics

This project is a lightweight cybersecurity honeypot designed to attract unauthorized login attempts and analyze real attacker behavior. It simulates a vulnerable web login page, captures all interaction data, and provides a data-driven analysis of attack patterns such as common usernames, password trends, time-based activity, and IP distribution.

🚀 Project Overview

The honeypot acts as a decoy system that appears to attackers as a legitimate login interface. Instead of granting access, every login attempt is recorded and safely isolated for analysis.

This setup provides insights into:

Brute-force attack behavior

Common credentials used by bots

Frequency and timing of attacks

Geographical distribution of attacker IPs

Patterns in attacker tools and scripts

This project blends cybersecurity, data engineering, and data science into one practical, real-world defensive security tool.

🛠️ Features
🔐 Low-Interaction Honeypot

Fake login page built with Flask

Captures:

Timestamps

Source IP addresses

Usernames/passwords submitted

No real backend system to compromise

Lightweight and safe for beginners

📊 Data Analysis

Using Python (Pandas + Matplotlib), the project analyzes:

Most attempted usernames and passwords

Attack frequency over time

IP clustering and geolocation lookup

Visualizations of attack trends

📁 Logging System

Attempts stored in CSV or SQLite

Structured dataset for exploratory analysis

Easy export for further machine learning experiments
