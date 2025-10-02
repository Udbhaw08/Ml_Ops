# MLOps Udemy Course Project

This repository contains the projects, notebooks, and exercises for the MLOps Udemy course. It covers tracking machine learning experiments, hyperparameter tuning, and model logging using MLflow, along with deep learning and standard machine learning libraries.

## Repository Structure

- **`1-MLproject/`**: Contains introductory ML projects and notebooks (e.g., [gettingstarted.ipynb](file:///f:/Udbhaw_Work/ML_OPS_UDEMY/1-MLproject/gettingstarted.ipynb)).
- **`2-Deeplearning/`**: Contains deep learning notebooks and starter code (e.g., [starter.ipynb](file:///f:/Udbhaw_Work/ML_OPS_UDEMY/2-Deeplearning/starter.ipynb)).
- **[get-started.ipynb](file:///f:/Udbhaw_Work/ML_OPS_UDEMY/get-started.ipynb)**: Root-level Jupyter notebook demonstrating basic MLflow connection and metric logging.
- **[requirements.txt](file:///f:/Udbhaw_Work/ML_OPS_UDEMY/requirements.txt)**: Core dependencies including `mlflow`, `scikit-learn`, `pandas`, `numpy`, `tensorflow`, `hyperopt`, and `keras`.
- **`venv/`**: Local Python 3.10 virtual environment.

---

## Setup and Activation

To work with this project, you need to activate your Python 3.10 virtual environment and install the required libraries.

### 1. Activate the Virtual Environment

Depending on your Operating System and terminal shell, run the appropriate command:

#### Windows (PowerShell) - *Default OS Shell*
```powershell
.\venv\Scripts\Activate.ps1
```
> [!NOTE]
> If PowerShell blocks execution of scripts, run the following command in your session first:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

#### Windows (Command Prompt)
```cmd
.\venv\Scripts\activate.bat
```

#### macOS / Linux (Bash or Zsh)
```bash
source venv/bin/activate
```

---

### 2. Install Dependencies

Once the environment is active (you will see `(venv)` prepended to your command prompt), install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 3. Run the MLflow Tracking Server

The notebooks configure the MLflow client to track metrics locally at `http://127.0.0.1:5000`. Run the following command in a separate terminal window (with the venv activated) to start the local MLflow backend and UI dashboard:

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts --host 127.0.0.1 --port 5000
```

Once running, open your browser and navigate to `http://127.0.0.1:5000` to inspect experiment runs, metrics, and models.

<!-- dev history update ML_OPS_UDEMY update 2025-09-02T18:46:40 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-02T21:36:45 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-08T18:03:51 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-08T21:30:05 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-12T21:14:04 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-12T22:42:30 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-22T18:34:50 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-22T19:43:46 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-24T18:17:23 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-24T22:24:21 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-27T19:16:05 -->

<!-- dev history update ML_OPS_UDEMY update 2025-09-27T22:48:47 -->

<!-- dev history update ML_OPS_UDEMY update 2025-10-02T18:46:40 -->

<!-- dev history update ML_OPS_UDEMY update 2025-10-02T21:36:45 -->
