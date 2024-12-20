
# def tokenize_(text, tokenizer):
#     """
#         Experimental !!!
#     """
#     # char_window_size = 512
#     # start = 0
#     # end = start + char_window_size
#     # tokens = []
#     # while end <= len(text) :
#     #     batch_text = text[start:end]
#     #     tokenized = tokenizer.encode(batch_text,
#     #                                  max_length = 128,
#     #                                  padding = "max_length",
#     #                                  truncation=True,
#     #                                  return_tensors="pt")
#     #     print(tokenized.size())
#     #     tokens.extend(tokenized)
#     #     start += char_window_size
#     #     end += char_window_size
#     # return tokens

#     MAX_SENTENCE_LENGTH = 32
#     sents = nltk.sent_tokenize(text)
#     tokens = []
#     for sent in sents :
#         tokenized = tokenizer.encode(sent,
#                                      max_length = MAX_SENTENCE_LENGTH,
#                                      padding = "max_length",
#                                      truncation = True,
#                                      return_tensors="pt")
#         # print(tokenized)
#         # print(tokenized.size())
#         tokenized = tokenized.squeeze()
#         tokens.append(tokenized)

#     return torch.stack(tokens)

# tokenize(text, tokenizer = bert_tokenizer).size()


""" Sentence tokenization """

# # Sentence tokenization

# START_TOKEN = '<START>'
# PADDING_TOKEN = '<PADDING>'
# END_TOKEN = '<END>'


# english_vocabulary = [START_TOKEN, ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
#                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#                         ':', '<', '=', '>', '?', '@', 
#                         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
#                         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
#                         'Y', 'Z',
#                         '[', '\\', ']', '^', '_', '`', 
#                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
#                         'y', 'z', 
#                         '{', '|', '}', '~', PADDING_TOKEN, END_TOKEN]


""" index """
# english_to_index = {v:k for k,v in enumerate(english_vocabulary)}
# index_to_english = {k:v for k,v in enumerate(english_vocabulary)}

# print(len(english_to_index), len(index_to_english))


""" tokenize sentence """
# def tokenize_sentence(sentence, language_to_index, max_sequence_length, start_token=True, end_token=True):
#     sentence_word_indices = [language_to_index[token] for token in sentence ]
#     if start_token :
#         sentence_word_indices.insert(0, language_to_index[START_TOKEN])
#     if end_token :
#         sentence_word_indices.append(language_to_index[END_TOKEN])

#     for _ in range(len(sentence_word_indices), max_sequence_length):
#         sentence_word_indices.append(language_to_index[PADDING_TOKEN])

#     return torch.tensor(sentence_word_indices)

# def tokenize_text(text, language_to_index, max_sequence_length):
#     sentences = sent_tokenize(text)
#     # print(type(sentences), len(sentences))
#     # print([(len(s),s) for s in sentences])
#     tokenized_sentences = []
#     for sentence in sentences :
#         tokenized_sentence = tokenize_sentence(sentence, language_to_index=language_to_index, max_sequence_length = max_sequence_length, start_token=True, end_token=True)
#         tokenized_sentences.append(tokenized_sentence)

#     return torch.stack(tokenized_sentences)
# tokenize_text(text, language_to_index=english_to_index, max_sequence_length=256).size()