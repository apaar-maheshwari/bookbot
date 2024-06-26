from pathlib import Path
def main():
    absolute_path=Path('/Users/apaarmaheshwari/workspace/github.com/apaar-maheshwari/bookbot/books/frankenstein.txt') 
    with open(absolute_path) as f:
        file_contents=f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count=count_words(file_contents)
        print(f"{count} words were found in this document")
        characters_frequency(file_contents)

def count_words(string):
    words=string.split()
    return len(words)

def characters_frequency(string):

    string=string.lower()
    freq_dict={}
    for char in string:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1
    create_list(freq_dict)
    

def create_list(dict):
    list_of_dict=[]
    for key,value in dict.items():  
        list_of_dict.append({'char':key,'freq':value})
    list_of_dict.sort(reverse=True,key=sort_on)
    generate_report(list_of_dict)


def sort_on(dict):
    return dict['freq']

def generate_report(list_of_dict):
    for item in list_of_dict:
        if item['char'].isalpha():
            character=item['char']
            frequency=item['freq']
            print(f"The '{character}' character was found {frequency} times")
    print("--- End report ---")


main()