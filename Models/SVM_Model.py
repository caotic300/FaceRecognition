from sklearn.svm import SVC

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import expon
from sklearn.utils.fixes import loguniform


class SVM_Model():
    def __init__(self, params_distribs, n_iter):
        self.params_distribs = params_distribs
        self.svm= SVC()
        self.rnd_search =  RandomizedSearchCV(self.svm, params_distribs, n_iter=n_iter, random_state=42, verbose=2)
        
    def fit(self, X_train, y_train):
        self.rnd_search.fit(X_train, y_train)
        
    def predict(self, X_test):
        predicted = self.rnd_search.predict(X_test)
        return predicted
    
    def svm(self):
        return self.rnd_search
    
    def best_params(self):
        return self.rnd_search.best_params_