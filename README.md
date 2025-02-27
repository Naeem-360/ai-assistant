# 🤖 AI Assistant

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Assistant](https://img.shields.io/badge/Feature-Voice%20Commands-red.svg)](https://en.wikipedia.org/wiki/Virtual_assistant)

A command-line Python-based AI assistant with voice interaction, capable of playing music, managing files, opening applications, and more. Powered by `pyttsx3` for text-to-speech and `pywhatkit` for YouTube playback.

## ✨ Features

- 🎙️ Voice responses using text-to-speech (`pyttsx3`)
- 🎵 Plays songs on YouTube with the `play` command
- 📂 Creates and deletes files/folders with custom content
- 🚀 Opens applications or files by path
- 🍎 Integrates a calorie calculator (via `calories_calculator`)
- 📝 Reads and appends text to files
- ❓ Built-in help menu with command list
- 🖥️ User-friendly command-line interface

## 📋 Requirements

- Python 3.x
- `pyttsx3` (for text-to-speech)
- `pywhatkit` (for YouTube playback)
- `calories_calculator` (custom module, must be in the same directory)
- Windows OS (due to `sapi5` and `os.startfile` usage)

## 🚀 Installation

### Clone the Repository

Clone this project from GitHub using the following commands:

```bash
# Clone the repository
git clone https://github.com/Naeem-360/ai-assistant.git
