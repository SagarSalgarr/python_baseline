ENTITY_LIST = ["job", "course", "training", "skill centre", "skill", "center", "centre", "apprenticeship", "internship", "intern", "apprentice", "book", "pdf", "ebook", "content", "scheme"]

TRAINING_LIST = ['skill india centres', "iti", "jss", "pmkvy", "niesbud", "skill university"]

main_list = ENTITY_LIST + TRAINING_LIST
print(main_list)

# def categorize_entity(input_text):
#     for entity in ENTITY_LIST:
#         if entity in input_text.lower():
#             if entity in ENTITY_LIST:
#                 return f"{input_text} belongs to the ENTITY_LIST"
            
#             elif entity in TRAINING_LIST:
#                 return f"{input_text} belongs to the TRAINING_LIST"
#         else:
#             return f"{input_text} doesn't belong to any specific list."
# user_input = input("Enter a text to categorize: ")
# result = categorize_entity(user_input)
# print(result)