your_project/                     ←  run the command from HERE
│
├── train_session.py              ←  your existing script
├── diagnostics.py                ←  the new script (place it here)
│
├── features/
│   ├── new_app/                  ←  the CSVs the diagnostic reads
│   │   ├── samanth_training_sessions.csv
│   │   ├── samanth_testing_sessions.csv
│   │   ├── vinay_training_sessions.csv
│   │   ├── vinay_testing_sessions.csv
│   │   └── ...
│   │
│   ├── samanth_training_sessions.csv     ← (used by train_session.py, different folder)
│   └── ...
│
├── models/                       ←  created by train_session.py
├── plots/                        ←  created by train_session.py
│
└── diagnostics/                  ←  AUTO-CREATED by diagnostics.py
    ├── selected_features.json
    ├── diagnostic_summary.txt
    ├── global_drift_summary.csv
    ├── diagnostics.log
    ├── user_specific/
    └── global_plots/

# 1. Navigate to the project folder
cd your_project

# 2. Install dependencies (one-time)
pip install pandas numpy scipy matplotlib tqdm statsmodels scikit-learn seaborn

# Optional (for extra diagnostics)
pip install diptests ruptures

# 3. Run the diagnostics
python diagnostics.py




















pip install pandas numpy scipy scikit-learn statsmodels diptest
project/
├── diagnose_features.py
├── selected_features.json
└── features/
    └── new_app/
        ├── srikanth_training_sessions.csv
        ├── srikanth_testing_sessions.csv
        ├── Samarth_training_sessions.csv
        ├── Samarth_testing_sessions.csv
        ├── harshit_training_sessions.csv
        └── harshit_testing_sessions.csv


python diagnostics_features.py









