# CSCI461 - Assignment 1: Big Data Processing Pipeline with Docker

## 👥 Team Members

| Name                  | Student ID   |
|-----------------------|--------------|
| Reem Hussin Mostafa   | 221000241    |
| Jihad Hamdy           | 221001055    |
| Mahmoud Essa          | 221001619    |
| Abdelrahman Ahmed     | 221001199    |
| Ibrahim Alaa          | 221000837    |

---

## 📘 Project Overview

This project demonstrates a complete data processing pipeline using Docker and Python. The dataset used is from MovieLens, focusing on two key files: `ratings.csv` and `movies.csv`.

We processed the data through the following steps:
1. Loading
2. Data Cleaning & Transformation
3. Exploratory Data Analysis (EDA)
4. Visualization
5. K-Means Clustering

Each step is implemented in its own Python file, and all are chained together in a pipeline that runs inside a Docker container.

---

## 📂 Dataset Used

- `movies.csv` — contains movie titles and genres  
- `ratings.csv` — contains user ratings for movies  

Source: https://grouplens.org/datasets/movielens/

---

## 🐳 Docker Setup & Commands

### Dockerfile Features

Our Dockerfile:
- Uses Ubuntu as base image
- Installs Python3 and essential libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `scikit-learn`, and `scipy`
- Copies the dataset into the container
- Sets the working directory to `/home/doc-bd-a1`
- Starts with a bash shell

### Building and Running the Container

```bash
docker build -t bd-a1-img .
```

```bash
docker run -it --name bd-a1-container bd-a1-img
```

```bash
python3 load.py ratings.csv
```

---

## 📜 Python File Descriptions

### `load.py`
- Reads `ratings.csv` passed as argument
- Saves it as `res_load.csv`
- Calls `dpre.py` automatically

### `dpre.py`
- Merges `ratings.csv` with `movies.csv`
- Cleans nulls and duplicates
- Extracts the main genre
- Computes average rating and number of ratings per movie
- Discretizes ratings into levels (Low, Medium, High)
- Saves as `res_dpre.csv`
- Calls `eda.py`

### `eda.py`
- Computes and saves 3 insights:
  - Average rating per genre (`eda-in-1.txt`)
  - Top 5 most-rated movies (`eda-in-2.txt`)
  - Total number of unique movies (`eda-in-3.txt`)
- Calls `vis.py`

### `vis.py`
- Creates a barplot of the top 10 most-rated movies
- Saves it as `vis.png`
- Calls `model.py`

### `model.py`
- Runs K-Means clustering with `k=3` using average rating and rating count
- Saves number of records per cluster in `k.txt`

---

## 📁 Output Files Generated

After running the full pipeline, these files are created:

| File Name       | Description                          |
|----------------|--------------------------------------|
| `res_load.csv` | Raw loaded ratings                  |
| `res_dpre.csv` | Cleaned and processed data          |
| `eda-in-1.txt` | Insight: Avg rating per genre       |
| `eda-in-2.txt` | Insight: Most-rated movies          |
| `eda-in-3.txt` | Insight: Total unique movies        |
| `vis.png`      | Barplot: Top 10 most-rated movies   |
| `k.txt`        | K-means cluster record count        |

---

## 📤 Final Script: Copying Files from Container to Host

### `final.sh`

This script:
- Creates a folder: `service-result/`
- Copies all result files from the Docker container to your PC
- Stops the container

### Run it like this:

```bash
sh final.sh
```

### Folder Structure After Running

```
bd-a1/
├── Dockerfile
├── final.sh
├── load.py
├── dpre.py
├── eda.py
├── vis.py
├── model.py
├── ratings.csv
├── movies.csv
├── service-result/
│   ├── res_dpre.csv
│   ├── eda-in-1.txt
│   ├── eda-in-2.txt
│   ├── eda-in-3.txt
│   ├── vis.png
│   ├── k.txt
```

---

## ✅ Submission Checklist

✔️ Dockerfile  
✔️ Python Scripts (`load.py`, `dpre.py`, etc.)  
✔️ `final.sh` script  
✔️ `README.md`  
✔️ Output Files in `service-result/`  
✔️ All zipped into one file and submitted on Moodle  
✔️ Team form submitted

---

### 🎉 Great job team!