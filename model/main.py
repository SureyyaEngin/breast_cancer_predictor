import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def get_clean_data():
    data = pd.read_csv("data/data.csv")
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    return data

def create_and_save_model(name, model, X_train, y_train, scaler):
    model.fit(X_train, y_train)
    with open(f'model/{name}_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open(f'model/{name}_scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

def main():
    os.makedirs('model', exist_ok=True)
    data = get_clean_data()
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    models = {
        "Logistic Regression": LogisticRegression(),
        "Naive Bayes": GaussianNB(),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "SVM": SVC(probability=True)
    }

    for name, model in models.items():
        print(f"Training {name} model...")
        create_and_save_model(name, model, X_train, y_train, scaler)
        y_pred = model.predict(X_test)
        print(f"{name} Accuracy: ", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))

if __name__ == '__main__':
    main()
