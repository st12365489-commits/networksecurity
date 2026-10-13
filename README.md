# NetworkSecurity — Phishing Website Detection

An end-to-end Machine Learning project for detecting phishing-related patterns using a structured network security data pipeline. The project includes data ingestion, validation, transformation, model training, evaluation, and application integration.

## Overview

Phishing is a common cybersecurity threat in which attackers use deceptive websites and links to trick users into sharing sensitive information.

**NetworkSecurity** is a modular machine learning project designed to process network security datasets and train a classification model for phishing detection. It follows a pipeline-based architecture to organize data processing, model training, artifact management, and evaluation.

## Key Features

- **MongoDB Integration:** Retrieves datasets from a MongoDB collection.
- **Data Ingestion:** Exports data into a feature store and creates training and testing datasets.
- **Data Validation:** Checks incoming data against the expected schema.
- **Data Drift Detection:** Generates a drift report to identify potential changes in data distributions.
- **Data Transformation:** Prepares data for model training through appropriate preprocessing and missing-value handling.
- **Model Training:** Trains a classification model and saves the trained model as a serialized artifact.
- **Model Evaluation:** Evaluates model performance using F1-score, precision, and recall.
- **Custom Exception Handling:** Provides structured error reporting.
- **Logging:** Supports debugging and pipeline execution monitoring.
- **Modular Architecture:** Separates components, configuration, artifacts, utilities, and pipeline orchestration.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Data preprocessing, model training, and evaluation |
| MongoDB | Dataset storage and retrieval |
| PyYAML | YAML configuration and report handling |
| Python-dotenv | Environment variable management |
| MLflow | Experiment tracking infrastructure, if configured in the application |
| Docker | Containerization support |

## Project Architecture

```text
                 MongoDB
                    |
                    v
              Data Ingestion
                    |
                    v
                Feature Store
                    |
                    v
               Train-Test Split
                    |
                    v
              Data Validation
                    |
                    v
            Data Transformation
                    |
                    v
               Model Training
                    |
                    v
              Model Evaluation
                    |
                    v
            Trained Model Artifact
                 model.pkl
```

## Model Performance

The trained model produced the following evaluation metrics.

### Training Metrics

| Metric | Score |
|---|---:|
| F1-Score | 99.16% |
| Precision | 98.94% |
| Recall | 99.37% |

### Testing Metrics

| Metric | Score |
|---|---:|
| F1-Score | 97.27% |
| Precision | 96.69% |
| Recall | 97.85% |

### Performance Summary

The model achieved a **97.27% F1-score on the test dataset**, indicating a strong balance between precision and recall on the evaluated data.

The training and testing scores differ, so further evaluation on independent data and a confusion matrix can help assess generalization and identify false-positive and false-negative predictions.

*Note: These scores represent the reported evaluation results. They do not guarantee the same performance on every real-world dataset.*

## Project Structure

```text
NetworkSecurity/
│
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── constant/
│   ├── entity/
│   │   ├── artifact_entity.py
│   │   └── config_entity.py
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── training_pipeline.py
│   └── utils/
│
├── data_schema/
├── notebooks/
├── templates/
├── valid_data/
├── venv/                    # Local virtual environment
├── venv_old/                # Previous local environment
│
├── app.py
├── main.py
├── push_data.py
├── test_connection.py
├── mlflow.db                # Local MLflow database, if used
├── requirements.txt
├── setup.py
├── Dockerfile
├── .env                     # Local environment variables
├── .gitignore
└── README.md
```

*The tree above describes the main project layout. Optional files such as `model_trainer.py` and `test_connection.py` should match the files present in your final repository.*

## Getting Started

### 1. Clone the Repository

```bash
git clone <https://github.com/st12365489-commits/networksecurity>
cd NetworkSecurity
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv venv
```

Activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your MongoDB connection string:

```env
MONGO_DB_URL=your_mongodb_connection_string
```

Replace the placeholder with your actual connection string. Use the exact environment variable name expected by your code.

**Important:** Never commit `.env` files, passwords, API keys, or database credentials to GitHub.

### 5. Configure MongoDB

1. Create or select your MongoDB database.
2. Configure the collection name according to the project constants.
3. Create a database user with the required permissions.
4. Configure MongoDB network access for your application.
5. Ensure the dataset is available in the expected collection.

### 6. Run the Pipeline

Execute the main script from the project root:

```bash
python main.py
```

The pipeline runs the components configured in `main.py` and generates artifacts according to the project configuration.

## Pipeline Components

### Data Ingestion

- Connects to MongoDB.
- Exports collection documents into a Pandas DataFrame.
- Stores data in the configured feature store.
- Splits the dataset into training and testing sets.

### Data Validation

- Checks datasets against the expected schema.
- Identifies schema or data validation issues.
- Produces a data drift report.

### Data Transformation

- Prepares validated data for machine learning.
- Handles missing values using configured imputation techniques.
- Applies preprocessing steps required by the training pipeline.

### Model Training

- Trains a classification model using transformed data.
- Evaluates the trained model using classification metrics.
- Saves the trained model as a serialized artifact.

### Artifact Management

The pipeline maintains references to generated files, including ingested datasets, validation reports, and the trained model.

Example trained model artifact:

```text
Artifacts/
└── <timestamp>/
    └── model_trainer/
        └── trained_model/
            └── model.pkl
```

The actual path depends on the pipeline execution timestamp and configuration.

## Model Evaluation Metrics

- **Precision:** Measures the proportion of predicted positive cases that are actually positive.
- **Recall:** Measures the proportion of actual positive cases correctly identified.
- **F1-Score:** Provides a harmonic mean of precision and recall.

These metrics are useful for evaluating classification performance, especially when both missed phishing cases and false alarms matter.

## Error Handling and Logging

The project includes custom exception handling and logging utilities to make errors easier to diagnose and execution easier to monitor.

Generated logs and artifacts can contain local paths or diagnostic details. Review them before sharing publicly.

## Future Improvements

- Evaluate the model on additional independent datasets.
- Add a confusion matrix and per-class classification report.
- Compare multiple classification algorithms.
- Implement automated hyperparameter tuning.
- Add automated tests and continuous integration.
- Extend the application with a prediction interface or API, where applicable.
- Improve model monitoring and deployment workflows.

## Security Considerations

- Keep credentials in environment variables.
- Exclude `.env`, virtual environments, and generated logs from Git tracking.
- Avoid committing unnecessary datasets, local databases, and large generated artifacts.
- Do not expose sensitive information in logs or exception messages.

## Author

**Suraj Thakur**

GitHub: [https://github.com/st12365489-commits]

## License

Add a `LICENSE` file if you intend to distribute this project publicly. Select a license that matches your intended usage and distribution requirements.

