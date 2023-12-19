import numpy as np


class SimplifiedBaggingRegressor:
    

    def __init__(self, num_bags, oob=False):
        self.num_bags = num_bags
        self.oob = oob
    
    def _generate_splits(self, data: np.ndarray):
        '''
        Generate indices for every bag and store in self.indices_list list
        '''
        self.indices_list = []
        data_length = len(data)
        for bag in range(self.num_bags):
            some_bag = np.random.randint(data_length, size=data_length)
            self.indices_list.append(some_bag)
    

    def fit(self, model_constructor, data, target):
        '''
        Fit model on every bag.
        Model constructor with no parameters (and with no()) is passed to this function.

        example:

        bagging_regressor = SimplifiedBaggingRegressor(num_bas=10, oob=True)
        bagging_regressor.fit(LinearRegression, X, y)
        '''
        self.data = None
        self.target = None
        self._generate_splits(data)
        assert len(set(list(map(len, self.indices_list)))) == 1, 'All should be on the same length!'
        assert list(map(len, self.indices_list))[0] == len(data), 'All bags should contain `len(data)` number of elements!'
        self.model_list = []
        for bag in range(self.num_bags):
            model = model_constructor()
            i_bag = self.indices_list[bag]
            data_bag, target_bag = data[i_bag], target[i_bag]
            self.model_list.append(model.fit(data_bag, target_bag))
        if self.oob:
            self.data = data
            self.target = target
        
    
    def predict(self, data):
        '''
        Get agerage prediction for every object from passed dataset
        '''
        predictions = [model.predict(data) for model in self.model_list]
        predictions = np.array(predictions)
        return np.mean(predictions, axis=0)
    

    def _get_oob_predictions_from_every_model(self):
        '''
        Generates list of lists, where list i contains predictions for self.data[i] object
        from all models which have not seen this object during training phase
        '''
        list_of_predictions_lists = [[] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(self.num_bags):
                if i not in self.indices_list[j]:
                    list_of_predictions_lists[i].append(self.model_list[j].predict(self.data[[i]])[0])

        self.list_of_predictions_lists = np.array(list_of_predictions_lists, dtype=object)
    

    def _get_averaged_oob_predictions(self):
        '''
        Compute average predictions for every object from training set.
        If object has been used in all bagson training phase, return None instead of prediction
        '''
        self._get_oob_predictions_from_every_model()
        self.oob_predictions = np.array(list(np.array(mas).mean() if len(mas) > 0 else np.nan for mas in self.list_of_predictions_lists))
    

    def OOB_score(self):
        '''
        Compute mean square error for all objects, which have at least one prediction
        '''
        self._get_averaged_oob_predictions()
        ind = ~np.isnan(self.oob_predictions)
        return np.sum((self.oob_predictions[ind] - self.target[ind]) ** 2)