import spacy

def generate_two_word_token(sentence):
    # Load the spaCy English model
    nlp = spacy.load('en_core_web_sm')

    # Process the sentence using spaCy
    doc = nlp(sentence.lower())

    # Define the labels of interest
    labels_of_interest = ['PERSON', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART',
                          'DATE', 'TIME', 'MONEY', 'PERCENT', 'QUANTITY', 'ORDINAL', 'CARDINAL']

    # Extract the two most relevant words based on spaCy's Named Entity Recognition (NER)
    relevant_words = []
    for ent in doc.ents:
        if ent.label_ in labels_of_interest:
            relevant_words.append(ent.text.lower())
            if len(relevant_words) == 2:
                break
    
    # If less than two relevant words were found, extract the two most relevant words in general
    if len(relevant_words) < 2:
        for token in doc:
            if token.is_stop or token.is_punct:
                continue
            relevant_words.append(token.lemma_.lower())
            if len(relevant_words) == 2:
                break
    
    # Return the four-word meaning
    return ' '.join(relevant_words)