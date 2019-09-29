from pymed import PubMed
from os import path

pubmed = PubMed(tool="paperList", email="kirtan.701@gmail.com")

query = 'Correia BE[author]'

publications = pubmed.query(query, max_results=500)

## Defining functions
def get_filename(article):
    words = '-'.join(article.title.split(' ')[:3])
    date = '-'.join([str(article.publication_date.year), 
                     str(article.publication_date.month), 
                     str(article.publication_date.day)])
    title = '-'.join([date, words]) + '.md'
    return(title)

def get_authors(article):
    author_list = []
    for author in article.authors:
        name =  author['lastname'] + ' ' + author['initials']
        author_list.append(name)
        authors = ', '.join(author_list)
    return(authors, author_list[0])

def clean_journal_name(journal):
    if(journal.find('(') > 0):
        cleaned_name = journal[:journal.find('(')]
        return(cleaned_name.rstrip())
    elif(journal.find(':') > 0):
        cleaned_name = journal[:journal.find(':')]
        return(cleaned_name.rstrip())
    else:
        return(journal)


def get_acronym(journal):
    if(journal == 'Proceedings of the National Academy of Sciences of the United States of America'):
        return('PNAS')    
    else:
        return(clean_journal_name(journal))
    
def get_shortref(article):
    if(len(article.authors) == 1):
        shortref = (article.authors[0]['lastname'] + ' ' + 
        get_acronym(article.journal) + ' '+ 
        str(article.publication_date.year))
        return(shortref)
    elif(len(article.authors) == 2):
        shortref = (article.authors[0]['lastname'] + ' and ' 
        + article.authors[1]['lastname'] + ' '
        + get_acronym(article.journal) + ' '
        + str(article.publication_date.year))
        return(shortref)
    else:
        shortref = (article.authors[0]['lastname'] + ' et al. ' 
        + get_acronym(article.journal) + ' '
        + str(article.publication_date.year))
        return(shortref)

## Generating files for papers for which they do not already exist
for article in publications:
    filename = get_filename(article)
    title = article.title.rstrip('.').replace(':', '-')
    authors, first_author = get_authors(article)
    journal = clean_journal_name(article.journal)
    journal_acronym = get_acronym(article.journal)
    pmid = article.pubmed_id.split('\n')[0]
    doi = article.doi
    abstract = article.abstract
    year = str(article.publication_date.year)
    shortref = get_shortref(article)
    
    if(path.exists('../papers/_posts/'+filename)):
        continue
    else:
        f = open('../papers/_posts/' + filename,"w+")
        f.write('---\r\n')
        f.write('layout: paper\r\n')
        f.write('published: true\r\n')
        f.write('category: paper\r\n')
        f.write('image: /assets/images/papers/default-paper.svg\r\n')
        f.write('title : %s\r\n' % title)
        f.write('year : %s\r\n' % year)
        f.write('shortref : %s\r\n' % shortref)
        f.write('journal : %s\r\n' % journal)
        f.write('pmid : %s\r\n' % pmid)
        f.write('authors : %s\r\n' % authors)
        f.write('doi : %s\r\n' % doi)
        f.write('---\r\n')
        f.write('{% include JB/setup %}\r\n\n')
        f.write('# Abstract\r\n\n')
        f.write('%s' % abstract)
        f.close()
        i = i + 1
