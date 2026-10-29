# Environmental Health Risk Score Calculator

A beginner-friendly, console-based Python project that estimates a person's **health risk level (Low / Moderate / High)** by combining **environmental conditions** (temperature, humidity, wind speed, AQI, UV index) with **personal factors** (age, occupation, existing health condition).

**Author:** Shourya Vardhan Singh

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Scoring Rules](#scoring-rules)
5. [Weights and Risk Bands](#weights-and-risk-bands)
6. [Getting Started](#getting-started)
7. [Input Guide](#input-guide)
8. [Project Structure](#project-structure)
9. [Concepts Used](#concepts-used)
10. [Advantages](#advantages)
11. [Limitations and Future Improvements](#limitations-and-future-improvements)
12. [Demo Output](#demo-output)

---

## Overview

The same weather can be harmless for one person and dangerous for another. A 35 °C day with poor air quality is a minor inconvenience for a young office worker, but a serious concern for an outdoor worker with asthma.

This program takes both sides of the picture, the **environment** and the **human**, converts each factor into a simple score of **0, 1 or 2**, applies a **weight** to each factor based on how strongly it affects health, and adds everything up into a single **total risk score**. That score is then mapped to a **Low, Moderate or High** risk level.

---

## Features

- Collects 5 environmental and 3 human inputs from the user
- Converts raw values into standard risk levels using dedicated functions
- Uses a **weighted scoring model** (AQI, temperature and health condition count the most)
- Displays the raw data, the per-factor risk scores, and the final result
- Pure Python with no external libraries, so it runs anywhere Python 3 is installed

---

## How It Works

```
 User Input  ──►  Store in dictionaries  ──►  Scoring functions (0 / 1 / 2)
                                                        │
                                                        ▼
 Final Risk Level  ◄──  Risk band check  ◄──  Weighted total risk score
```

1. **Input:** the user enters 8 values; they are stored in two dictionaries, `Data_of_Enviorment` and `Data_of_Human`.
2. **Scoring:** each value is passed to its own function, which returns `0` (safe), `1` (caution) or `2` (high risk).
3. **Storage of scores:** the scores are stored in `risk_Data_of_Enviorment` and `risk_Data_of_Human`.
4. **Weighted total:** every score is multiplied by its weight and the products are added together.
5. **Classification:** the total is compared against fixed ranges to produce the final label.

---

## Scoring Rules

| Factor | Score 0 (low) | Score 1 (moderate) | Score 2 (high) |
|---|---|---|---|
| **Temperature (°C)** | 15 to 30 | below 15 | above 30 |
| **Humidity (%)** | 30 to 60 | below 30, or 61 to 80 | above 80 |
| **Wind Speed** | 0 to 15 | 16 to 30 | above 30 |
| **AQI** | 0 to 50 | 51 to 100 | above 100 |
| **UV Index** | 0 to 2 | 3 to 5 | 6 and above |
| **Age** | 13 to 59 | 0 to 12 or 60+ | n/a |
| **Occupation** | Indoor (or unrecognised) | Mixed | Outdoor |
| **Health Condition** | `nil` | any other condition | `Asthma` or `respiratory related problems` |

---

## Weights and Risk Bands

Not every factor affects health equally, so each score is multiplied by a weight:

| Factor | Weight |
|---|---|
| AQI | ×4 |
| Health Condition | ×4 |
| Temperature | ×3 |
| Humidity | ×2 |
| UV Index | ×2 |
| Wind Speed | ×1 |
| Occupation | ×1 |
| Age | ×1 |

```
Total Risk = (AQI×4) + (Temp×3) + (Health×4) + (Humidity×2) + (UV×2) + Wind + Occupation + Age
```

| Total Score | Risk Level |
|---|---|
| 0 to 8 | **Low** |
| 9 to 18 | **Moderate** |
| 19 and above | **High** |

The maximum possible score is **35**.

---

## Getting Started

**Requirements:** Python 3.x (no extra packages needed)

```bash
# 1. Clone or download the project
git clone <your-repository-link>
cd <project-folder>

# 2. Run the program
python Main.py
```

---

## Input Guide

The program asks for the following, in this order:

| Prompt | Type | Example |
|---|---|---|
| Temperature | number (decimal allowed) | `34` |
| Age | whole number | `45` |
| Occupation | text: `Indoor`, `Mixed` or `Outdoor` | `Outdoor` |
| AQI | number | `160` |
| Human Disease | text: `nil`, `Asthma`, `respiratory related problems`, or any other condition | `Asthma` |
| Humidity | whole number | `70` |
| Wind Speed | number | `10` |
| UV Index | whole number | `8` |

> **Note:** text inputs are **case-sensitive**. Type `Outdoor`, not `outdoor`, and `nil` if there is no health condition.

---

## Project Structure

```
.
├── Main.py       # Complete program: input, scoring functions, total, result
└── README.md     # Project documentation
```

Inside `Main.py` the code is organised in this order:

1. Input collection into dictionaries
2. Eight scoring functions: `temperature()`, `humidity()`, `wind_speed()`, `AQI()`, `UV_Index()`, `age()`, `occupation()`, `health_condition()`
3. Calling each function to get the individual scores
4. Calculating the weighted total
5. Classifying and printing the final result

---

## Concepts Used

| Concept | Where it is used in this project |
|---|---|
| **Variables and data types** | `float` for temperature, AQI and wind speed; `int` for age, humidity and UV; `str` for occupation and condition |
| **Type casting** | `float(input(...))` and `int(input(...))` convert the typed text into numbers |
| **User input / output** | `input()` collects data and `print()` shows data and results |
| **Dictionaries (key-value pairs)** | Four dictionaries keep raw data and risk scores organised and labelled instead of scattered across many variables |
| **Functions** | Each factor has its own function that takes a value and `return`s a score, so each rule is written once and is easy to change |
| **Conditional statements** | `if / elif / else` ladders decide which score each value earns |
| **Chained comparisons** | `0 <= ws <= 15` checks a range in a single readable expression |
| **Logical operators** | `and` is used in the humidity function to check the 30 to 60 range |
| **Arithmetic operators** | Multiplication and addition build the weighted total |
| **Weighted scoring model** | More harmful factors (AQI, health) get larger multipliers so they influence the result more |
| **Rule-based classification** | The final score is placed into Low, Moderate or High using fixed thresholds |
| **Modular / structured programming** | The program is divided into clear stages: input, scoring, combining, output |

---

## Advantages

- **Simple and easy to understand:** the logic is plain `if/else` rules that anyone can read and verify.
- **Personalised:** it accounts for the person (age, occupation, health) and not just the weather.
- **Transparent:** the per-factor scores are printed, so the user can see *why* the result came out as it did.
- **Weighted:** it reflects reality better than a flat sum, because air quality and respiratory health matter more than wind speed.
- **Easy to modify:** thresholds and weights live in one place each, so tuning the model means changing a number, not rewriting the program.
- **Lightweight:** no libraries, no internet, no database; runs instantly on any machine with Python.
- **Good base to grow from:** it can be extended into a GUI, a web app, or one that fetches live weather and AQI data.
- **Practical use:** can be used for quick awareness about whether it is safe to work or exercise outdoors.

---

## Limitations and Future Improvements

- Add **input validation** (reject negative age, invalid humidity above 100, etc.) with `try/except`
- Make text inputs **case-insensitive** (`.strip().lower()`)
- Show a **safety recommendation** with each result (for example, "Avoid outdoor activity")
- Fetch **live weather and AQI** using an API instead of manual entry
- Store results in a **file** to track risk over time
- Build a **GUI or web interface** for easier use

---

## Demo Output

**Sample input:** a 45-year-old outdoor worker with asthma on a hot, polluted, high-UV day.

```
Enter Temperature =34
Enter Age =45
Enter occupation = Outdoor
Enter AQI =160
Enter Human Disease if any =Asthma
Enter Humidity =70
Enter wind speed = 10
Enter UI index =8
{'Temperature': 34.0, 'AQI': 160.0, 'Humidity': 70, 'Wind Speed': 10.0, 'UV Index': 8}
{'Age': 45, 'Occupation': 'Outdoor', 'Human Condition': 'Asthma'}
{'Temperature': 2, 'AQI': 2, 'Humidity': 1, 'Wind Speed': 0, 'UV Index': 2}
{'Age': 0, 'Occupation': 2, 'Human Condition': 2}
{'Total risk score': 30, 'Risk': 'High'}
```

**How the score of 30 was calculated:**

| Factor | Input | Score | Weight | Contribution |
|---|---|---|---|---|
| AQI | 160 | 2 | ×4 | 8 |
| Temperature | 34 | 2 | ×3 | 6 |
| Health Condition | Asthma | 2 | ×4 | 8 |
| Humidity | 70 | 1 | ×2 | 2 |
| UV Index | 8 | 2 | ×2 | 4 |
| Wind Speed | 10 | 0 | ×1 | 0 |
| Occupation | Outdoor | 2 | ×1 | 2 |
| Age | 45 | 0 | ×1 | 0 |
| **Total** | | | | **30 → High** |

Since 30 is above 18, the final risk level is **High**.

---

*Developed by Shourya Vardhan Singh*
