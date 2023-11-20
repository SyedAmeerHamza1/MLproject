from src.components.Data_ingestion import Dataingestion

from src.components.Data_transformation import Datatransformation
from src.components.Data_transformation import DatatransformationConfig

from src.components.model_trainer import ModelTrainer




obj=Dataingestion()
train_data, test_data=obj.initiate_data_ingestion()

data_transformation=Datatransformation()
train_arr, test_arr,_= data_transformation.initiate_data_transformation(train_data, test_data)

model_trainer= ModelTrainer()
print(model_trainer.initiate_model_trainer(train_arr, test_arr))