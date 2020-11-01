import json
import random

welcome = input("Welcome to the Tandem Trivia.  Would like to play press [y/n]?")
if welcome == "n":
    print ("Aw... I understand next time.")
if welcome == "y":
    with open('tandem.json') as json_file:
        jsondata = json.load(json_file)
        score = 0
        i = 1
        # looping through the json data
        for data in jsondata:
            print(data['question'])

            # combining incorrect and correct list into a new list called options. 
            # also create variable for correct answer
            options = []
            correct = data['correct']
            options.append(data['correct'])
            for incorrect in data['incorrect']:
                    options.append(incorrect)
            random.shuffle(options)

            # indexing the option list    

            for idx, val in enumerate(options):
                print(f'{idx}.  {val}')
            while True:
                try:
                    res = int(input("your response is... "))  
                    assert res >= 0 and res <= len(options) -1
                except IndexError and AssertionError:
                    print(f' Please enter a response between 0 and {len(options) - 1}')
                except ValueError:
                    print(f' Your response has to be an integer')
                else:
                    break
            
            # converted the integer response to a variable that grabs the value of the index
            # position in the options list.

            res = options[res]

            # checking to see if the response matches the value in the variable correct

            if res == correct:
                score += 100
                print(f'\n\nThat is Correct.  Your score is {score}. Keep going!!\n\n')
            else:
                print (f'\n\nGood try, but the correct answer is {correct}\n\n')

            # each time it loops through a the i variable increments.  once it reaches
            # 10 it breaks out of the loop and displays the final score.

            i += 1  
            if i == 11:
                print(f'\n\n\nYour final score is {score}!!\n\n\n')
                break



                





            
            
            
            
            
            
            
            
        
            
        
   

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
          


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
