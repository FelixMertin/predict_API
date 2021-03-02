import spacy

nlp = spacy.load("de_core_news_md")

def run_spacy_predict(model_name, text_input):
    doc = nlp(text_input)

    doc_dict = doc.to_json()
    entities_labels_dict = doc_dict["ents"]
    entities = doc.ents
    payload = dict()
    # Construct the payload with key = word and value = label
    # e.g. "Donald Trump" = "Person"
    for i, entity in enumerate(entities_labels_dict):
        payload[str(entities[i][0])] = entities_labels_dict[i]["label"]


    return payload