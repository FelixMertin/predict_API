import pickle
import numpy as np
from tensorflow.keras.preprocessing.text import text_to_word_sequence


import nltk
from nltk import tokenize

from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')


def clean_string(single_observation):
    """
     Specification:
     - Presupposition: A text "single_observation" as a string, containing several sentences is given. NLTK needs to be loaded.
     - Result: Turns the text into a list of string words and punctuation. Before the words are lowercased and lemmatized. Stopwords of the NLTK framework are removed.
     - Effect: None
    """

    lemmatizer = WordNetLemmatizer()
    returnString = ""
    sentence_token = tokenize.sent_tokenize(single_observation)
    idx_list = []
    for j in range(len(sentence_token)):
        single_sentence = tokenize.word_tokenize(sentence_token[j])
        sentences_filtered = [(idx, lemmatizer.lemmatize(w.lower())) for idx, w in enumerate(single_sentence)
                              if w.lower() not in stopwords.words('english') and w.isalnum()]
        idx_list.append([x[0] for x in sentences_filtered])
        word_list = [x[1] for x in sentences_filtered]
        returnString = returnString + ' '.join(word_list) + ' . '

    return returnString, idx_list


def tokenization(clean_obs, MAX_SENTENCE_NUM, MAX_FEATURES, MAX_WORD_NUM):
    """
     - Presupposition: The text is given as a clean version. The Tokenizer is prepared as a pickled object.
     - Result: Turns the Observation into an Array of shape (94, 34)
     - Effect: None
    """


    """
    MAX_SENTENCE_NUM: There is a maximum (Quantile 95 %) of 94 sentences in an essay.
    MAX_WORD_NUM: There is a maximum (Quantile 95 %) of 34 words in a sentence.
    MAX_FEATURES: There is a maximum (Quantile 95 %) of 1182 words in a essay.
    """
    # To read already cleaned essays
    print("The Observation after lemmatization and lower casing: ")
    print(clean_obs)

    sentences = tokenize.sent_tokenize(clean_obs)
    print("The Observation after splitting up the Sentences")
    print(sentences)

    # Unpickle the tokenizer which is a tokenizer.pickle a stream of bytes
    with open('./python_api/app/pretrained/pretrained_tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Initialize data matrix
    data = np.zeros((MAX_SENTENCE_NUM,
                     MAX_WORD_NUM), dtype='int32')

    # Transfer the text into the data matrix
    for j, sent in enumerate(sentences):
        if j < MAX_SENTENCE_NUM:
            wordTokens = text_to_word_sequence(sent)
            k = 0
            for _, word in enumerate(wordTokens):
                if k < MAX_WORD_NUM and word in tokenizer.word_index and tokenizer.word_index[word] < MAX_FEATURES:
                    data[j, k] = tokenizer.word_index[word]
                    k = k + 1

    print('Shape of data tensor:', data.shape)
    print('The tokenized sentences:', data)

    return data


def run_tokenization(text):
    """
     - Presupposition: A text file containing english written words needs to be given.
     - Result: Returns the transcript in an Array of shape (94, 34).
     - Effect: None
    """
    single_observation = text
    clean_observation, idx_list = clean_string(single_observation)
    data = tokenization(clean_obs=clean_observation, MAX_SENTENCE_NUM=94, MAX_FEATURES=1182, MAX_WORD_NUM=34)
    return data




