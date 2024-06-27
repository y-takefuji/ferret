import pandas as pd
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv('ferret.csv')

# Drop the 'Ferret' independent variable as requested
data = data.drop(columns=['Ferret'])

# Fill missing values with zeros
data = data.fillna(0)

# Convert string variables to numerical values
string_cols = ['lethal','Virus', 'units', 'expt', 'NW_typical', 'RD_trans', 'HPAI', 'HPAI_MBAA', 'HA', 'NA', 'Origin']
for col in string_cols:
    data[col] = data[col].astype(str)
    encoder = LabelEncoder()
    data[col] = encoder.fit_transform(data[col])

# Separate independent variables (features) and dependent variable (target)
X = data.drop(columns=['lethal'])

# Check unique values in 'lethal' column
print("Unique values in 'lethal' column:", data['lethal'].unique())

y = data['lethal']

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest Classifier for feature importance on binary classification task
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)
rf_feature_importances = rf_classifier.feature_importances_
rf_predictions = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

# Extra Trees Classifier for feature importance on binary classification task
et_classifier = ExtraTreesClassifier()
et_classifier.fit(X_train, y_train)
et_feature_importances = et_classifier.feature_importances_
et_predictions = et_classifier.predict(X_test)
et_accuracy = accuracy_score(y_test, et_predictions)

# Create a DataFrame for feature importances and sort it
rf_importances = pd.DataFrame({'feature': X.columns, 'importance': rf_feature_importances})
rf_importances = rf_importances.sort_values('importance', ascending=False)

et_importances = pd.DataFrame({'feature': X.columns, 'importance': et_feature_importances})
et_importances = et_importances.sort_values('importance', ascending=False)

# Print sorted feature importances and accuracy
print("Sorted Feature Importances using Random Forest:\n", rf_importances)
print("Random Forest Accuracy:", format(rf_accuracy, '.5f'))
print("Sorted Feature Importances using Extra Trees:\n", et_importances)
print("Extra Trees Accuracy:", format(et_accuracy, '.5f'))