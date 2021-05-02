# Sparkify – Data modeling with Postgres <!-- omit in toc -->

<!-- Add buttons here -->
[![Open in Colab](https://img.shields.io/badge/-Open%20in%20Colab-e8710a?logo=google-colab)](https://colab.research.google.com/github/dewith/property_prices)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-black)](https://www.python.org/)
![Status](https://img.shields.io/badge/Project%20status-Completed-black)
![Last commit](https://img.shields.io/github/last-commit/dewith/property_prices?color=black)
![License](https://img.shields.io/github/license/dewith/property_prices?color=black)
<!-- End buttons here -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

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

The company's property appraisers do the valuation in the traditional way, this means that the process is subjective to the appraiser's criteria.
Currently the process is slow, and there is a risk of under- or over-valuing a property. This in turn generates customer dissatisfaction.

> The **objective** is then to create a model based on advanced machine learning techniques to predict real estate prices based on their attributes.

## Datasets 💾

- **User activity dataset** from [Udacity](https://www.udacity.com/) <br>
    The dataset logs user demographic information (e.g. user name, gender, location State) and activity (e.g. song listened, event type, device used) at individual timestamps.

- **Census regions table** from [cphalpert's GitHub](https://github.com/cphalpert/census-regions) <br>
  The table links State names to geographical divisions.

A small subset (\~120MB) of the full dataset was used for exploratory data analysis and pilot modeling; the full dataset (\~12GB) was used for tuning the machine learning model.

## Process ✍

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

- Descriptive statistics
- Data visualization
- Feature engineering
- Machine learning

### Tools 🧰

- Python
- Numpy, Pandas, Scipy
- Matplotlib, Seaborn
- Scikit-Learn, XGBoost

## Results 📣

- In the project I studied in detail the predictor variables and their relationships with the target variable. Based on the exploratory analysis I found that the variables that best predict the price of a property are the surface area_covered and the number of bathrooms. An average error of 49k USD was achieved with the best model (XGBoost), which is equivalent to 16.8% average error.:
|testing accuracy score|testing F1 score|
|--------|--------|
| 0.8387 | 0.8229 |

- Churns relate to users who have received more advertisements, disliked songs more often than liked, and registered more recently.
<img src="feature_importance.png" width=500>

### Next steps 💡

To improve the performance of the model the following steps could be taken (ordered by ascending complexity):

1. Only work with data from one city when training a model, this reduces variability and therefore decreases error
2. Add the neighborhood variable in the training (this will increase the computer cost but can generate a non-spectacular but considerable gain)
3. Create a model by type of property: one for apartments and another for houses, because although both are habitable properties they have very different behaviors. In this way you can focus actions to reduce the error independently.
4. Complement the dataset with more specific data on the property's environment, such as the crime rate by area, socioeconomic status, and the number of businesses in the vicinity, among others.
5. Work with geolocation data combined with an API map to obtain the number of stores and areas of interest around automatically, as well as prices of nearby houses.

## Installation 💻

- **Prototype on local machine:** The code was developed using the Anaconda distribution of Python, versions 3. Libraries used include `PySpark`, `Pandas`, `Seaborn`, and `Matplotlib`.

- **Cloud deployment on [AWS EMR](https://aws.amazon.com/):**
  - Release: emr-5.20.0
  - Applications: Spark: Spark 2.4.0 on Hadoop 2.8.5 YARN with Ganglia 3.7.2 and Zeppelin 0.8.0
  - Instance type: m4.xlarge
  - Number of instance: 3

## File structure 📓

- `Sparkify.ipynb`: exploratory data analysis, data preprocessing, and pilot development of machine learning model on local machine using data subset.
- `Sparkify_AWS.ipynb`: data preprocessing and model tuning on AWS using the full dataset.
- `mini_sparkify_event_data.json`: subset of user activity data.
- `region.csv`: census regions table.

## Contact 📞

- You can visit my [**personal website**](https://dewith.co/),
- follow me on [**Twitter**](https://twitter.com/DewithMiramon/),
- connect with me on [**LinkedIn**](https://linkedin.com/in/dewithmiramon/),
- or check out the rest of my projects on my [**GitHub**](https://github.com/dewith/) profile.

[(Back to top)](#motivation)
