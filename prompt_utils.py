from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')  # 384 dimensional


def create_prompt(context, query, selected_option):
    header = "Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry Not Sufficient context to answer query'. "
    if selected_option == 'Short':
        header += "Give a short-length answer. \n"
    if selected_option == 'Medium':
        header += "Give a medium-length answer. \n"
    if selected_option == 'Long':
        header += "Give a long answer. \n"
    return header + context + "\n\n" + query + "\n"