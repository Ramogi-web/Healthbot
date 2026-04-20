import pandas as pd

# load your data through a dataframe
df = pd.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, I'm your health assistance bot. Ask me about any symptoms.")

while True:
    #1. get the user inputs and store them in a variable
    user_text = input("\n You: ").lower()

    #2. check if the users want to exit
    if user_text == "quit":
        print("Healthbot: Goodbye! Nice to have been on service to you. Stay healthy")
        break

    # create a variable wich will storethe details structured in the csv file
    found_answer = False

    # come upwith a loop thatloops through the entire data frame created before
    for index,row in df.iterrows():
        # clean up the keywords
        keywords_list = str(row['Keywords']).split(',')

        # below we check every keyword in that given row (keyword)
        for word in keywords_list:
            clean_word = word.strip().lower()

            #if the keyword is inside of the of the users sentence
            if clean_word in user_text:
                print("Healthbot:", row["Response"])
                found_answer=True
                break#stop looking at other keywords

        if found_answer:
            break#stop looking at the other answers    

        #4. if we went through the entire /whole csv and never found any match of the keywords
        #we need to display a message to the user

        if not found_answer:
            print("Healthbot: Sorry ,I dont know that one.Try something else")
            break