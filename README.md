# 💻 Coffee & Wifi

A Flask website listing cafes that are good for working remotely, rated on coffee, wifi strength and power sockets. Visitors can browse the table of cafes and add new ones through a validated form; everything is stored in a simple CSV file.

## Features

- Dark-themed Bootstrap 5 pages
- Add-a-cafe form with validation (required fields, valid Google Maps URL)
- Emoji ratings for coffee ☕, wifi 💪 and power 🔌
- Data saved to `cafe-data.csv`

## Built with

Python, Flask, Flask-WTF, WTForms, Bootstrap 5

## How to run

Requires Python 3.10+.

```bash
pip install -r requirements.txt
python main.py
```

Then open **http://127.0.0.1:5000** in your browser.
