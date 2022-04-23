import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler


class Module:
    def __init__(self, classifiers) -> None:
        """
        Initialize a class item with a list of classificators
        """
        self.classifiers = classifiers
        self.count = len(self.classifiers)

    def fit(self, X, y):
        """
        Fit classifiers from the initialization stage
        """
        for classifier in self.classifiers:
            classifier.fit(X, y)

    def predict(self, X):
        """
        Get predicts from all the classifiers and return
        the most popular answers
        """
        y_preds = []

        for classifier in self.classifiers:
            y_preds.append(classifier.predict(X))

        y_preds = np.stack(y_preds)

        return y_preds.sum(axis=0) / self.count


if __name__ == "__main__":
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    3. Prepare classifiers to initialize <StructuralPatternName> class.
    4. Train the ensemble
    """

    X, y = load_iris(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state=1)

    classifiers = [make_pipeline(StandardScaler(), RandomForestClassifier(max_depth=5, random_state=1)),
                   make_pipeline(StandardScaler(), KNeighborsClassifier(5)),
                   make_pipeline(StandardScaler(), GaussianNB()),]

    mix = Module(classifiers)
    mix.fit(X_train, y_train)

    y_pred = mix.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f'Accuracy score achieved with ensemble = {accuracy}')
