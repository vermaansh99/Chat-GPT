import openai


#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

openai.api_key = "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"




def GetAnswer(question):
    return openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[ {"role":"user","content":question} ]
    )



while True:
    print("1.Ask Question")
    print("2.Exit")
    choice = int(input())
    if choice == 1:
        question = input("Enter your question: ")
        answer = GetAnswer(question)
        print(answer.choices[0]["message"]["content"])
    elif choice == 2:
        break

