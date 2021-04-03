import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Loading Data
DATA_PATH = r"data.csv"

data = pd.read_csv(DATA_PATH, index_col=0)
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# Train/Test split
X, y = data.content, data.language
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model params
token_pattern = r"""(\b[A-Za-z_]\w*\b|[!\#\$%\&\*\+:\-\./<=>\?@\\\^_\|\~]+|[ \t\(\),;\{\}\[\]`"'])"""


def preprocess(x):
    return pd.Series(x).replace(r'\b([A-Za-z])\1+\b', '', regex=True)\
        .replace(r'\b[A-Za-z]\b', '', regex=True)


# Pipe steps
transformer = FunctionTransformer(preprocess)
vectorizer = TfidfVectorizer(token_pattern=token_pattern, max_features=3000)
clf = RandomForestClassifier(n_jobs=4)

pipe_RF = Pipeline([
    ('preprocessing', transformer),
    ('vectorizer', vectorizer),
    ('clf', clf)]
)

# Setting best params
best_params = {
    'clf__criterion': 'gini',
    'clf__max_features': 'sqrt',
    'clf__min_samples_split': 3,
    'clf__n_estimators': 300
}

pipe_RF.set_params(**best_params)

# Fitting
pipe_RF.fit(X_train, y_train)


# Evaluation
print(f'Accuracy: {pipe_RF.score(X_test, y_test)}')
