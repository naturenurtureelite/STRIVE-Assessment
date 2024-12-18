import os
import time
import spacy
nlp = spacy.load("en_core_web_sm")
import openai
openai.api_key="put api key here"
#openai.api_key = os.getenv("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")
#uu=open("UK-Abs/test-data/stats-UK-test.txt")
ll=os.listdir("context/")
#ll=os.listdir("IN-Abs/test-data/judgement/")
read1=open("context.txt","r")
read22=read1.readlines()
read2=open("question.txt","r")
read11=read2.readlines()

no_of_words=0
no_of_words2=0
temp_summary2=""
for i in range(0,len(read11)):
    #temp=ll[i].split("\t")
    #print(temp[0],temp[1],temp[2])
    #if i<71:
    #    continue
        #print(i)
        #continue
    lll=open("context/"+ll[i],"r")
    llll=str(lll.read())
    #temp2=llll.split(".")
    #temp_summary=""
    #parsed=""
    llllll=open("output/"+temp[i],"w+")
    #llllll.write()
    #time.sleep(60)
    last=""
    ttt=""
    counter=0
    #for j in range(0,len(temp2)):
        #temp2[j]=temp2[j].strip("\n")
        #parsed = nlp(temp2[j])
        #no_of_words2=no_of_words
        #no_of_words=no_of_words+len(parsed)
        #print(len(parsed))
        #temp_summary2=temp_summary
        #counter=counter+1
        #last=temp2[j]
        #temp_summary=temp_summary+temp2[j]
        #if temp_summary=="":
        #    temp_summary=temp_summary+last+"."+temp2[j]+"."
        #else:
        #    temp_summary=temp_summary+temp2[j]+"."
        #ratio=int(1024*0.333333333333)
        #last=temp2[j]
        #ratio=int(1024*((int(temp[2])*1.0)/int(temp[1])))
        #if ((no_of_words>1024) and (no_of_words2<=1024)):
    temp_summary2="Given the definition of human evaluation metrics:Grammaticality: Measures the grammatical correctness of the generated question, regardless of the context; Relevance: Measures the degree to which the generated question is pertinent and aligned with the given context.Appropriateness: Examines the semantic correctness of the question irrespective of the context;Novelty: Measures the originality and distinctiveness of the generated question in comparison to the gold standard question for the given context. Complexity: Estimates the level of reasoning or cognitive effort required to answer the generated question. The Context corresponding to the question is:"+read22[i]+"Provide a score between 1 and 5 for the question "+read11[i]+" based on the human evaluation metrics namely Grammaticality, Appropriateness, Relevance, Complexity, and Novelty as well as the context corresponding to the question stated above."
            #try:
    response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content":temp_summary2}],
                temperature=0.7,
                max_tokens=50,
                stop=None
                )
            #except:
            #    cc=0
            #temp_summary=temp_summary+parsed
           # response = openai.Completion.create(
          #  model="text-davinci-003",
          #  prompt="{"+temp_summary2+"}"+"Tl;Dr",
          #  temperature=0.7,
          #  max_tokens=ratio,
          #  top_p=1.0,
          #  frequency_penalty=0.0,
          #  presence_penalty=1
          #  )
           
    for choice in response.choices:
                print(choice)
                #if "text" in choice:
                #    print(choice.text)
                llllll.write(choice["message"]["content"]+"\n")
                #print(choice["message"]["content"])
           # llllll.write(str(response["choices"][0]["text"]))
                print("---------------")
                print(temp[0])
                print("----")
                print(choice["message"]["content"])
                print("----")
                print(temp_summary2)
                print("-------------------------")

            #print(response["choices"][0]["text"])
                temp_summary2=""
                temp_summary=""
            #time.sleep(5)
            #print(response["choices"][0]["text"])
            #llllll.write(str(response["choices"][0]["text"]))
            #print("--------------")
            #print(temp[0])
            #print("----")
            #print(response["choices"][0]["text"])
            #print("----")
            #print(temp_summary2)
            #print("-------------------------")
            #temp_summary2=""
            #temp_summary=""
            #llllll.close()