from PubMedSearcher import PubMedSearcher
from TitleCounter import TitleCounter


# Example of how to use the class in another file
if __name__ == "__main__":
    term = [
        "(oral health) AND (advanced cancer)",
        "(oral health) AND (terminal cancer)",
        "(oral health) AND (hospice care)",
        "(dental palliative care) AND (advanced cancer)",
        "(dental palliative care) AND (terminal cancer)"
        ]
    files = []
    output_file = "titles"
    filters = ['lang.english', 'lang.greekmodern', 'years.2003-2023', 'hum_ani.humans']
    
    for i in range(0, len(term)):
        files.append(output_file+str(i+1)+".txt")
        searcher = PubMedSearcher(term[i], output_file+str(i+1)+".txt", filters=filters)
        print (i+1,"-",term[i],":", searcher.search(),"results")

    counter = TitleCounter(files)
    unique_titles, duplicate_titles = counter.count_titles()
    
    # Print the results
    print(f"Total unique titles: {unique_titles}")
    print(f"Total duplicate titles: {duplicate_titles}")
