# Sparkify – Data modeling with Postgres <!-- omit in toc -->

<!-- Add buttons here -->
[![Open in Colab](https://img.shields.io/badge/-Open%20in%20Colab-e8710a?logo=google-colab)](https://colab.research.google.com/github/dewith/sparkify_postgres)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-black)](https://www.python.org/)
![Status](https://img.shields.io/badge/Project%20status-Completed-black)
![Last commit](https://img.shields.io/github/last-commit/dewith/sparkify_postgres?color=black)
![License](https://img.shields.io/github/license/dewith/sparkify_postgres?color=black)
<!-- End buttons here -->

This project uses Postgres (with psycopg2, its interface in Python) to create a relational database and a ETL pipeline for a non-real music streaming app called Sparkify.

<details>
<summary><b>Table of content</b></summary>

- [Motivation](#motivation-)
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

## Process ✍

1. Creation of tables.
  - Understanding the needs for the database
  - Design of schema for the relational database
  - Writing SQL queries for creation in a Python script.
2. Building of ETL processes.
  - Development of ETL process for each table in a notebook.
  - Checking successful insertion of records.
3. Building of ETL pipeline.
  - Development of script to process the entire datasets.
  - Checking the correct operation of the pipeline for inserting records.

### Methods used 📜

- Data modeling
- ETL pipeline building

### Tools 🧰

- Python
- PostgreSQL
- Psycopg2
- Pandas

## Results 📣 to-do

Lorem ipsum

### Next steps 💡

To improve the performance and quality of the pipeline, the following steps could be taken:

1. Insert data using the COPY command to bulk insert log files instead of using INSERT on one row at a time
2. Add data quality checks
3. Create a dashboard for analytic queries on your new database

## Installation 💻

- **Udacity's AWS Workspace:** The code was originally developed in JupyterLab, mainly using the libraries `Psycopg2` and `Pandas`.

- **Local machine:** The project can be executed locally by meeting these requirements:
  - python==3.6.3
  - conda==4.6.14
  - jupyterlab==1.0.9
  - ipython-sql==0.3.9
  - psycopg2==2.7.4
  - pandas==0.23.3

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
