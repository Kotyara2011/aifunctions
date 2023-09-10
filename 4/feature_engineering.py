# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Import scikit-learn libraries for feature engineering and selection
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, f_classif

# Read the data from the CSV file
df = pd.read_csv("data.csv")

# Separate the input features and the output label
X = df.drop("label", axis=1)
y = df["label"]

# Normalize the numerical features using StandardScaler
scaler = StandardScaler()
num_cols = ["click_through_rate", "session_duration"]
X[num_cols] = scaler.fit_transform(X[num_cols])

# Encode the categorical features using OneHotEncoder
encoder = OneHotEncoder(sparse=False)
cat_cols = ["device_type", "browser"]
X_cat = encoder.fit_transform(X[cat_cols])
X_cat = pd.DataFrame(X_cat, columns=encoder.get_feature_names(cat_cols))

# Extract the text features using TfidfVectorizer
vectorizer = TfidfVectorizer()
text_cols = ["user_agent", "referrer"]
X_text = vectorizer.fit_transform(X[text_cols].apply(lambda x: " ".join(x), axis=1))
X_text = pd.DataFrame(X_text.toarray(), columns=vectorizer.get_feature_names())

# Concatenate the processed features into one dataframe
X = pd.concat([X.drop(cat_cols + text_cols, axis=1), X_cat, X_text], axis=1)

# Encode the output label using LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Select the best features using SelectKBest with ANOVA F-value
selector = SelectKBest(f_classif, k=20)
X_new = selector.fit_transform(X, y)
X_new = pd.DataFrame(X_new, columns=X.columns[selector.get_support()])

# Save the processed features and label to a new CSV file
pd.concat([X_new, y], axis=1).to_csv("data_processed.csv", index=False)
