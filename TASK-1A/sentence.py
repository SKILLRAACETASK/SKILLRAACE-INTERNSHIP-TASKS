def generate_sentences():
   subjects = ["I", "You"]
   verbs = ["play", "Love"]
   objects = ["Cricket", "Ludo"]

   sentences = []
   for subject in subjects:
       for verb in verbs:
           for obj in objects:
               sentence = f"{subject} {verb} {obj}}."
               sentences.append(sentence)
               return sentences
   if_name_== "_main_":
      all_sentences =
   generate_sentences()
      for sentence in all_sentences:
          print(sentence)