import nltk
# Sometimes a response causes an nltk package error.
# To counter that need to make sure this is downloaded before starting the program.
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import time
import numpy
import tflearn
import tensorflow
import random
import json
import pickle

class Chatbots:
    words = []
    model = 0
    labels = []
    data = []
    results_index = 0
    results = 0

    @classmethod
    def train_model(self):
        global model
        global labels
        global words
        global data
        try:
            print("Successfully opened the intents.json file.")
            with open("intents.json") as file:
                data = json.load(file)
        except:
            print("Couldn't find intents.json file. Make sure that file is in the same directory as Chatbot.py")
            raise

        # If there exists already a pickle file use it.
        # For retraining the model with new intents delete the data.pickle file. (make sure to comment out try/except below)
        # This will force it to automatically generate a new one.
        try:
            with open("data.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
        # For generating the data.pickle file.
            print("Successfully opened the data.pickle file.")
        except:
            print("Did not found data.pickle file. Going to train new model now.")
            words = []
            labels = []
            docs_x = []
            docs_y = []

            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])

                if intent["tag"] not in labels:
                    labels.append(intent["tag"])

            words = [stemmer.stem(w.lower()) for w in words if w != "?"]
            words = sorted(list(set(words)))
            labels = sorted(labels)
            training = []
            output = []
            out_empty = [0 for _ in range(len(labels))]

            for x, doc in enumerate(docs_x):
                bag = []
                wrds = [stemmer.stem(w.lower()) for w in doc]
                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)
                output_row = out_empty[:]
                output_row[labels.index(docs_y[x])] = 1
                training.append(bag)
                output.append(output_row)

            training = numpy.array(training)
            output = numpy.array(output)
            # Saves the new pickle file
            with open("data.pickle", "wb") as f:
                pickle.dump((words, labels, training, output), f)
                print("Sucessfully created new data.pickle file")

        tensorflow.reset_default_graph()

        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)

        # Try loading the existing model. If not train it.
        #try:
         #    model.load("model.tflearn")
         #    print("Found a model!")
        #except:
        #     print("Didn't found the model going through training now.")
             #time.sleep(2)
        model.fit(training, output, n_epoch=3000, batch_size=8, show_metric=True)
        model.save("model.tflearn")

        print("Hello! My name is Subot. How can I help you today?")

    @classmethod
    def bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

    def get_results_index(self):
        global results_index
        global results
        return results[results_index]

    @classmethod
    def chat(self, user_input):
        global words
        global labels
        global data
        global results_index
        global results
        goodbye = "It was nice to meet you!"
        inp = user_input
        if inp.lower() == "bye":
            # speak_tts(goodbye)
            print(goodbye)
            return goodbye
            time.sleep(2)
            # Wait 2 seconds to finish audio from goodbye message

        try:
            model.load("model.tflearn")
        except:
            print("ERROR: Failed to fetch the model.tflearn")

        results = model.predict([self.bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        print(tag)
        # USEFUL FOR TESTING NEW TAGS
        print(results[results_index])
        print(results_index)

        print(results)

        # ----- TWEAK THE ACCURACY NUMBER -----
        if results[results_index] > 0.6:
            if tag == 'time':
                print("SHOW TIME")
                return "show time"
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            response = random.choice(responses)
            print(response)
            # speak_tts(response)
            return response

        else:
            unknownresponse = "I didn't understand your question"
            print(unknownresponse)
            return unknownresponse
