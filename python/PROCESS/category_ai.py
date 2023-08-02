import os
import warnings
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import json
from PROCESS import MODEL_FILE, LABEL_FILE, AAC_FILE

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.simplefilter(action='ignore', category=FutureWarning) # FutureWarning 제거
INDEX = 0

class Classifier():
    def __init__(self):
        self.text = []
        self.tokenizer = Tokenizer(char_level = True, oov_token='<OOV')
        self.__get_aac_category()
        self.__get_labels()

    # get labels
    def __get_labels(self):
        with open(LABEL_FILE, 'r', encoding='UTF-8') as f:
            self.labels = json.load(f)

    # model
    def __model_predict(self, seq_text):
        model = tf.keras.models.load_model(MODEL_FILE)
        predict = model.predict(seq_text)

        predict = predict.tolist()
        pred = predict[INDEX]
        return pred
    
    # data preprocess (to seq)
    def __preprocess(self, real_text):
        self.text.append(real_text)
        self.tokenizer.fit_on_texts(real_text)

        # text to number
        seq_text = self.tokenizer.texts_to_sequences(self.text)

        seq_text = pad_sequences(seq_text, maxlen = 20)
        seq_text.tolist()
        return seq_text
    
    # load aac_category
    def __get_aac_category(self):
        self.aac_category = []
        with open(AAC_FILE, 'r', encoding='UTF-8') as f:
            raw_aac = json.load(f)
        for AAC_NAME in raw_aac['AAC']:
            self.aac_category.append(AAC_NAME['name'])
        

    # 현재 제공하는 AAC에 포함되어있는지 확인
    def __check_category(self, txt):
        if txt in self.aac_category:
            return {'key' : txt}
        else:
            return {'key' : 'default'}


    # 카테고리 분석기
    def classifier(self, text):
        seq_text = self.__preprocess(text)
        pred = self.__model_predict(seq_text)

        for key, value in self.labels.items():
            if value == pred:
                result = key
             
        return_data = self.__check_category(result)
        return return_data



        
