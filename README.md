# Sparkify – Data modeling with Postgres <!-- omit in toc -->

<!-- Add buttons here -->
[![Open in Colab](https://img.shields.io/badge/-Open%20in%20Colab-e8710a?logo=google-colab)](https://colab.research.google.com/github/dewith/sparkify_postgres)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-black)](https://www.python.org/)
![Status](https://img.shields.io/badge/Project%20status-Completed-black)
![Last commit](https://img.shields.io/github/last-commit/dewith/sparkify_postgres?color=black)
![License](https://img.shields.io/github/license/dewith/sparkify_postgres?color=black)
<!-- End buttons here -->

This project uses Postgres (with its Python interface) to create a relational database and a ETL pipeline for a non-real music streaming app called Sparkify.

<details>
<summary><b>Table of content</b></summary>

- [Motivation 🎯](#motivation-)
- [Datasets 💾](#datasets-)
- [Process ✍](#process-)
  - [Methods used 📜](#methods-used-)
  - [Tools 🧰](#tools-)
- [Results 📣](#results-)
  - [Next steps 💡](#next-steps-)
- [Installation 💻](#installation-)
- [File structure 📓](#file-structure-)
- [Contact 📞](#contact-)

</details>

---

## Motivation 🎯

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. So they would like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis.

> The **objective** is then to design an star schema for the database and write an ETL pipeline to transfer data from files into the tables in Postgres.

## Datasets 💾

- **Song Dataset** — subset from [Million Song Dataset](http://millionsongdataset.com/)

    Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset. <br>
    ```
    song_data/A/B/C/TRABCEI128F424C983.json
    song_data/A/A/B/TRAABJL12903CDCF1A.json
    ```
- **Log Dataset** — generated with [Eventsim](https://github.com/Interana/eventsim)

  The log files are in JSON format and were generated based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.
  The log files in the dataset are partitioned by year and month. For example, here are filepaths to two files in this dataset.
  ```
  log_data/2018/11/2018-11-12-events.json
  log_data/2018/11/2018-11-13-events.json
  ```

## Process ✍ to-do

1. Data loading
   - Load subset from JSON
   - Assess missing values

2. Exploratory data analysis
   - Overview of numerical columns: descriptive statistics
   - Overview of non-numerical columns: possibel categories
   - Define churn as cancellation of service
   - Compare behavior of churn vs. non-churn users in terms of:
     - Usage at different hours of the day
     - Usage at different days of a week
     - User level (free vs. paid)
     - Event types (e.g. add a friend, advertisement, thumbs up)
     - Device used (e.g. Mac, Windows)
     - User location (e.g. New England, Pacific)
     - Time from downgrade to churn

3. Feature engineering for machine learning
   - Create features on per user basis:
     - Latest user level
     - Time since registration
     - Gender of user
     - Time, number of artists, number of songs, and number of session that user has engaged
     - Mean and standard deviation of the number of songs listened per artist, the number of songs listened per session, and time spent per session
     - Device used
     - Count and proportion of each event type
     - User location
   - Remove strongly correlated features (one from each pair)
   - Transform features to have distributions closer to normal
   - Compile feature engineering code to scale up later

4. Develop machine learning pipeline
   - Split training and testing sets
   - Choose evaluation metrics
   - Create functions to build cross validation pipeline, train machine learning model, and evaluate model performance
   - Initial model evaluation with:
     - Naive predictor
     - Logistic regression
     - Random forest
     - Gradient-boosted tree

5. Scale up machine learning on the full dataset on AWS
   - Tune hyperparameters of gradient-boosted tree
   - Evaluate model performance
   - Evaluate feature importance

### Methods used 📜

- Data modeling
- ETL pipelines

### Tools 🧰

- Python
- PostgreSQL
- Psycopg2
- Pandas

## Results 📣 to-do

In the project I studied in detail the predictor variables and their relationships with the target variable. Based on the exploratory analysis I found that the variables that best predict the price of a property are the surface area_covered and the number of bathrooms. An average error of 49k USD was achieved with the best model (XGBoost), which is equivalent to 16.8% average error:

|testing accuracy score|testing F1 score|
|--------|--------|
| 0.8387 | 0.8229 |

Churns relate to users who have received more advertisements, disliked songs more often than liked, and registered more recently.

<img src="feature_importance.png" width=500>

### Next steps 💡

To improve the performance and quality of the pipeline, the following steps could be taken:

1. Insert data using the COPY command to bulk insert log files instead of using INSERT on one row at a time
2. Add data quality checks
3. Create a dashboard for analytic queries on your new database

## Installation 💻 to-do

- **Prototype on local machine:** The code was developed using the Anaconda distribution of Python, versions 3. Libraries used include `PySpark`, `Pandas`, `Seaborn`, and `Matplotlib`.

- **Cloud deployment on [AWS EMR](https://aws.amazon.com/):**
  - Release: emr-5.20.0
  - Applications: Spark: Spark 2.4.0 on Hadoop 2.8.5 YARN with Ganglia 3.7.2 and Zeppelin 0.8.0
  - Instance type: m4.xlarge
  - Number of instance: 3

## File structure 📓

- `create_tables.py` drops and creates the tables.
- `etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook was made to test the code before using in _etl.py_.
- `etl.py` reads and processes files from _song_data_ and _log_data_ and loads them into the tables.
- `sql_queries.py` contains all the sql queries, and is imported into the last three files above.
- `test.ipynb` displays the first few rows of each table to check the database.

## Contact 📞

- You can visit my [**personal website**](https://dewith.co/),
- follow me on [**Twitter**](https://twitter.com/DewithMiramon/),
- connect with me on [**LinkedIn**](https://linkedin.com/in/dewithmiramon/),
- or check out the rest of my projects on my [**GitHub**](https://github.com/dewith/) profile.

[(Back to top)](#motivation-)
