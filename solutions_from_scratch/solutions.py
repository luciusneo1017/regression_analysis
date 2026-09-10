class OLSNormalEquation:

    def __init__(self):
        self.coef_ = None

    @staticmethod
    def has_perfect_multicollinearity(X):
        '''
        to check if design matrix X has perfect multicollinearity. perfect multicollinearity makes XTX singular, so (XTX)-1 does not exist
        '''

        rank = np.linalg.matrix_rank(X)
        n_cols = X.shape[1]
        return rank < n_cols

    def fit(self,X,y):
        '''
        input is design matrix X and response matrix y
        '''
        if self.has_perfect_multicollinearity(X):
            raise ValueError("Perfect multicollinearity detected")

        XtX = X.T @ X
        Xty = X.T @ y
        self.coef_ = np.linalg.inv(XtX) @ Xty
        return self

    def predict(self,X):
        if self.coef_ is None:
            raise ValueError("Model has not been fitted yet")

        return X @ self.coef_

