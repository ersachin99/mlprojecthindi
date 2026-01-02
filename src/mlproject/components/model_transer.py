import os
from pyexpat import model
import sys
from dataclasses import dataclass


from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR     
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

# for model evaluation we importing utils file and in 
# utils file we imported  model evaluation functions

from src.mlproject.utils import evaluate_model
from src.mlproject.utils import save_object




# create data class to store model transer config
@dataclass
class ModelTransferConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')



# create model transer class
class ModelTrainer:
    def __init__(self):
        self.model_transer_connfig = ModelTransferConfig()


    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('split training and test input data')

            # split the data into train test split
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]

            )
        # now we getting all the modesl list
            models={
                'Random Forest':RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'K-Neighbors Regressor': KNeighborsRegressor(),
                'SVR': SVR(),

            }
            
            # create a hyperparameter for each model 
            params ={
                'Decision Tree':{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    
                },
                'Random Forest':{
                    'n_estimators':[8,16,32,64,128,256]
                },
                'Gradient Boosting':{
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'n_estimators':[8,16,32,64,128,256]
                },
                'Linear Regression':{},
                'K-Neighbors Regressor':{
                    'n_neighbors':[3,5,7,9,11],
                },
                'SVR':{
                    'C':[1,10,100],
                    'kernel':['linear', 'rbf', 'poly'],
                    'gamma':['scale', 'auto']
                },

            }

            # create a  model evaluation function

            model_report: dict = evaluate_model(x_train,y_train,x_test,y_test,models,params)


            # to get the best model score from dict

            best_model_score  = max(sorted(model_report.values()))

            # to get the best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)

            ]
            best_model = models[best_model_name]

            # create some threshold for model accuracy
            # we create custom exception if model accuracy is less than 60%
            if best_model_score < 0.6:
                raise CustomException('No best model found')
            logging.info(f'Best model found on training and testing dataset')   

            # save the best model

            save_object(
                file_path=self.model_transer_connfig.trained_model_file_path,
                obj=best_model
            )

            # we predict the data with best model

            predicted = best_model.predict(x_test)

            r2_square = r2_score(y_test,predicted)

            return r2_square


        except Exception as e:
            raise CustomException(e, sys)




