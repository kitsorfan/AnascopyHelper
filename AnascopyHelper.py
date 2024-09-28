from PubMedSearcher import PubMedSearcher  # Adjust the import based on your file structure


# Example of how to use the class in another file
if __name__ == "__main__":
    term = [
        "(oral health) AND (advanced cancer)",
        "(oral health) AND (terminal cancer)",
        "(oral health) AND (hospice care)",
        "(dental palliative care) AND (advanced cancer)",
        "(dental palliative care) AND (terminal cancer)"
        ]
    output_file = "titles"
    filters = ['lang.english', 'lang.greekmodern', 'years.2003-2023', 'hum_ani.humans']
    
    for i in range(0, len(term)):
        searcher = PubMedSearcher(term[i], output_file+str(i+1)+".txt", filters=filters)
        print (i+1,"-",term[i],":", searcher.search(),"results")
