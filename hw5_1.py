import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier

class Builder:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, df_share):
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """
        X = self.X_train
        y = self.y_train
        X, y = shuffle(X, y, random_state = 1)

        n = int(len(y) * df_share / 100)

        return X[:n,:], y[:n]

if __name__ == "__main__":
   
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """
    from sklearn.datasets import load_iris
    from sklearn.metrics import accuracy_score
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1)
    
    clf = RandomForestClassifier(max_depth=5, n_estimators=1, random_state=1)

    pattern_item = Builder(X_train, y_train)
    for df_share in range(10, 101, 10):
        curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)
        clf.fit(curr_X_train, curr_y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"share = {df_share}%, accuracy on test = {accuracy}")

        """
        1. Preprocess curr_X_train, curr_y_train in the way you want
        2. Train Linear Regression on the subsample
        3. Save or print the score to check how df_share affects the quality
        """
    #