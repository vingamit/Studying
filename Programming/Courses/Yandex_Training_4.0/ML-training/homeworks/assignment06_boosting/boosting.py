import numpy as np


class SimplifiedBoostingRegressor:
    def __init__(self):
        pass

    @staticmethod
    def loss(targets, predictions):
        loss = np.mean((targets - predictions) ** 2)
        return loss
    
    @staticmethod
    def loss_gradients(target, predictions):
        gradients = (target - predictions)
        assert gradients.shape == target.shape
        return gradients
    

    def fit(self, model_constructor, data, targets, num_steps=10, lr=0.1, max_depth=5, verbose=False):
        '''
        Fit sequence of models on the provided data.
        Model constructor with no parameters (and with no ()) is passed in this funcion.
        If

        example:

        boosting_regressor = SimplifiedBoostingRegressor()
        boosting_regressor.fit(DecisionTreeRegressor, X, y, 100, 0.5, 10)
        '''
        new_target = targets
        self.models_list = []
        self.lr = lr
        self.loss_log = []
        for step in range(num_steps):
            try:
                model = model_constructor(max_depth=max_depth)
            except TypeError:
                print('max depth keyword not found. Ignoring!')
                model = model_constructor()
            self.models_list.append(model.fit(data, new_target))
            predictions = self.predict(data)
            self.loss_log.append(self.loss(targets, predictions))
            gradients = self.loss_gradients(targets, predictions)
            new_target = gradients
        if verbose:
            print('Finished! Loss=', self.loss_log[-1])
        return self
    
    def predict(self, data):
        predictions = np.zeros(len(data))
        for model in self.models_list:
            predictions += self.lr * model.predict(data)
        return predictions