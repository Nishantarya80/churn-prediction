from keras.models import load_model

def run_example(list):
    model = load_model(".\predictionmodel\my_model.h5")
    result = model.predict([list])
    return result[0][0]


