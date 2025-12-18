def similarity_check(string1,string2):
        
            import re
            import numpy as np
            from pprint import pprint
#normalization and tokenization
            def clean_text(string):

        
                text = re.sub(r'[^a-z0-9\s]','',string.lower())
        

                text_read = text.split()
        

                return text_read

            speech1_tokenized = clean_text(string1)
            speech2_tokenized = clean_text(string2)

    # pprint(melina_tokenized)
            from stop_words import stop_words

#clean
            def remove_support_words(list):
    
                list_sp = [words for words in list if words not in stop_words]

                return list_sp
    
            speech1_sp_rm = remove_support_words(speech1_tokenized)

            speech2_sp_rm = remove_support_words(speech2_tokenized)

#creating vecotors
            def word_frequency(list):
                word_frequency = {}
                for word in list:
                    if word in word_frequency:
                        word_frequency[word]+=1
                    else:
                        word_frequency[word]=1
                return word_frequency
    
            speech1_freq = word_frequency(speech1_sp_rm)
            speech2_freq = word_frequency(speech2_sp_rm)

            comlpete_vocabulary = set(speech2_freq.keys())|set(speech1_freq.keys())

    # pprint(comlpete_vocabulary)



            def create_vector(list):
                vector = []
                for word in comlpete_vocabulary:
                    count = list.get(word,0)

            #.get(key,default_value)

                    vector.append(count)
                return vector
    
            speech1_vector = create_vector(speech1_freq)
            speech2_vector = create_vector(speech2_freq)
            vector1 = np.array(speech1_vector)
            vector2 = np.array(speech2_vector)

    # print(len(melina_vector),len(michelle_vector))

            similary_score = (np.dot(vector1,vector2)/((np.linalg.norm(vector1))*(np.linalg.norm(vector2))))*100
            return f"{similary_score:.2f}%"


    