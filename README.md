
# Project Documentation for RateBeer Data Analysis

## Introduction

This project uses a comprehensive dataset from RateBeer to perform detailed data analysis, feature engineering, model training, and deployment aimed at predicting overall beer ratings based on user feature, such as reviews. It covers mulitple aspects of data handling and machine learning using  Hopsworks, whici showcases the steps from data ingestion and all the way to model depolyment and predictions.

## Project Scope

The objective of this project is to develop a predictive model capable of predicting beer ratings from  features derived from the diffrent user reviews. The scope includes:

- Acquriring data and then preprocessing it to create a clean dataset.
- Then the devolopment of a database, using HopsWorks, along with the creation of feature stores to help manageing the data efficently.
- Then the implementation of machine learning algorithms to understand which factors is influencing the beer ratings.
- Lastly deploying a predictive model to provide real-time beer rating predictions.

## Installation and Setup

So make sure that the notebook is able to run, please ensure that your eviroment is prepared with the right libraries, whihc is listed here:

```bash
pip install pandas numpy gdown xgboost joblib matplotlib hopsworks hsfs hsml sklearn
```

## Detailed Description of Jupyter Notebooks

### Notebook 1: Data Preparation and Feature Engineering

**Functionality**:
- **Data Loading**: Automates the downloading of the RateBeer dataset from a shared Google Drive link, as the orginal dataset was stored as an .txt file, which gave issuses, this can then directly be loaded into a pandas DataFrame for immediate use.
- **Feature Engineering**: Next some feature enfineering was done to extract time-based features from "review timestamps", which was then aggregated into metrics about the diffrent beers and reviewers.
- **Feature Group Creation**: Lastly featuregroups was created and ingested with the data using Hopsworks, which helps facilitaing the data for furhter use.

**Technologies Used**:
- Pandas for data manipulation.
- gdown for downloading files from Google Drive.
- Hopsworks and HSFS for feature store interactions.

### Notebook 2: Feature View Creation and Data Splits

**Functionality**:
- **Feature View Creation**: A feature view was created, which contains multiple feature groups for efficently retrivee the data for model training in the next notebook.
- **Data Splitting**: Lastly the data was splitted into training and testing sets based on the review_time column, to try and imitate a realistic simulation of predicting.

**Technologies Used**:
- Hopsworks Feature Store for managing and versioning data.

### Notebook 3: Model Training and Evaluation

**Functionality**:
- **Model Training**: Using XGBoost regressor, the notebook focuses on learning from the feature-engineereing which was done to the dataset.
- **Model Evaluation**: Multiple metrics was collected, including Mean Squared Error (MSE), Mean Absolute Error (MAE), and the R² statistic, to evaluate the models performance. Additionally, plots residuals were made to visually see the prediction accuracy.

**Technologies Used**:
- XGBoost for model training.
- sklearn for evaluation metrics.
- Matplotlib for plotting.

### Notebook 4: Model Deployment

**Functionality**:
- **Deployment Preparation**: The notebook focusses on scripting the code, which packages the trained model, and the models prediction logic aswell.
- **Model Deployment**: The model was then deployed to HopsWorks using their API.


**Technologies Used**:
- Hopsworks Model Registry.
- Joblib for saving the data.

### Notebook 5: Online Production

**Functionality**:
- **Model Serving**: The notebook lays the step for initiating and the manageing real-time serving of the model, which enables it to make online predictions.

**Technologies Used**:
- Hopsworks Model Serving for deploying and serving the models.

### Notebook 6: Batch Prediction Pipeline

**Functionality**:
- **Batch Prediction Setup**: The notebook shows how to prepare and run the batch prediction pipeline, which focuses on sampling the dataset using pickle and using the depolyed model for batch predictions.

**Technologies Used**:
- Hopsworks for model and data management.
- Pickle for data storing.

## Usage Instructions

To effectively use this project, follow these notebooks in order:

1. Set up your Python environment as detailed in the Installation section.
2. Run Notebook 1 to prepare your data and establish the feature store structure.
3. Proceed with Notebook 2 to define feature views and splitting the dataset.
4. Utilize Notebook 3 for training and evaluating the predictive model.
5. Deploy the model with Notebook 4 and initiate the online serving with Notebook 5.
6. Run Notebook 6 to perform batch predictions.

## Limitations and Known Issues

- The notebooks are not yet fully functional as a complete end-to-end system but can showcase the capabilities of the data processing and analysis methods used. These notebooks are a preliminary demonstration, with further refinements and functionality enhancements planned for future updates.

## Conclusion

This documentation covers the implementation, details and guidelines for a project, which is desinged to predict beer ratings, using machine learning. By following the guide, it is possible to replicate the workflow, to make data ingestions and deploying a predictive model using hopsworks.
