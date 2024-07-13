# High Blood Pressure Checkup Analysis

This repository contains the analysis of high blood pressure checkup data collected over a five-day period at National Hospital Abuja.

## Table of Contents

1. [Introduction](#introduction)
2. [Data Description](#data-description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

High blood pressure is a significant health concern. This project aims to analyze the data collected during a free checkup camp at National Hospital Abuja. The analysis includes statistical summaries, visualizations, and insights derived from the data.

## Data Description

The dataset includes daily records of patients who attended the high blood pressure checkup camp. The fields in the dataset are:
- **Day**: Date of checkup
- **Total Number Seen**: Total number of patients seen
- **<15, 15-19, 20-24, 25-29, 30-34, 35-40, >40**: Age group distributions
- **Male**: Number of male patients
- **Female**: Number of female patients

## Installation

To run the analysis, you need to have Python installed. Follow the steps below to set up the environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hbp-checkup-analysis.git
    cd hbp-checkup-analysis
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To perform the analysis, run the `analysis.py` script:

```bash
python analysis.py
