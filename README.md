# 🔐 Password + OTP Verification System using Twilio

This Python project is a simple command-line based login system that:
1. Verifies a user's password (with limited attempts).
2. Sends a randomly generated OTP to the user's phone using Twilio.
3. Verifies the OTP entered by the user for successful login.

---

## 🚀 Features

- Password-based authentication with a limit of 5 attempts.
- OTP (One-Time Password) generation and SMS delivery via Twilio API.
- Error handling for failed SMS delivery or incorrect OTP input.
- Easy-to-understand CLI interaction.

---

## 🧱 Prerequisites

- Python 3.x installed
- Twilio account with:
  - `account_sid`
  - `auth_token`
  - A verified Twilio phone number


