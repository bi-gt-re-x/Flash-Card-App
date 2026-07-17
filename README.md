# 🇫🇷 French Flash Cards

A simple and interactive flash card application built with **Python** and **Tkinter** to help users learn common French vocabulary. The app displays French words on digital flash cards, automatically flips them to reveal the English translation, and tracks which words you've already mastered.

## Features

* 🇫🇷 Learn French vocabulary with digital flash cards
* 🔄 Automatically flips each card after a few seconds
* 🎲 Randomized word selection for varied practice
* ✅ Mark words as learned
* 💾 Saves your learning progress between sessions
* 📚 Continues where you left off the next time you open the app
* 🖼️ Clean flash card interface using custom images

## How It Works

1. Launch the application.
2. A French word appears on the front of the flash card.
3. After a short delay, the card flips to reveal the English translation.
4. Click:

   * ✅ **Right** if you know the word.
   * ❌ **Wrong** if you'd like to review it again later.
5. Continue practicing until you've learned every word in the deck.

## Technologies Used

* **Python**
* **Tkinter**
* **Pandas**
* **CSV** for vocabulary storage
* **Object-Oriented Programming concepts**

## Project Structure

```text
Flash-Card-App/
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
├── main.py
└── README.md
```

## Vocabulary Data

The application reads vocabulary from a CSV file containing French and English word pairs. As words are marked as learned, they are removed from your active study list and saved to a separate progress file, allowing you to continue learning across multiple sessions.

## Future Improvements

* 🔊 Audio pronunciation for each word
* 📈 Learning statistics and progress tracking
* ⭐ Favorite difficult words
* 🎯 Multiple difficulty levels
* 🌍 Support for additional languages
* ⏱️ Customizable card flip timer
* 🔍 Search and filter vocabulary
* 🎨 Additional themes and interface customization

## Example Workflow

```text
French Card

Bonjour

↓

(Card flips automatically)

↓

English Card

Hello

↓

✓ I knew this word!

↓

Progress saved automatically.
```

## Purpose

This project was created to practice Python programming while building a practical language-learning application. It demonstrates working with graphical user interfaces, file handling, timers, randomization, and persistent data storage to create an engaging study experience.
