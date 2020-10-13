import sqlite3
import time

def add_to_database(url):
    #creating data_base
    url_data = sqlite3.connect('data_base/URLs.db')
    cursor = url_data.cursor()

    try:
        cursor.execute('''INSERT INTO url VALUES ('ecf', 'elv');''' ) #is url table already created???
    except sqlite3.OperationalError:  #no, so create it!
        cursor.execute('''CREATE TABLE url(
                    shortened TEXT PRIMARY KEY,
                    real_url TEXT);''')
        url_data.commit()
    else: #yes, okay, cancel the test on line 10
        url_data.rollback()
    finally: #after the test
        #search the url in the data base and return all occurences
        shortened = list(cursor.execute('''SELECT shortened FROM url WHERE real_url = "{}";'''.format(url)))
        if len(shortened)==1: #the url already exists
            shortened = list(shortened)[0][0] #return his shortened url. The select returns a list of tuple or something like that. So, we hava add two indexes
        elif len(shortened) > 1: #more than one occurence??? There is a problem
            exit() #stop program
        else: #ah, there is no occurence, created a shortened address and add the url and the shortened address
            shortened = int(time.time())
            cursor.execute('''INSERT INTO url VALUES ("{}", "{}");'''.format(shortened, url) )
            url_data.commit()    
        return str(shortened)
    
def get_url(index):
    url_data = sqlite3.connect('data_base/URLs.db')
    cursor = url_data.cursor()

    real = list(cursor.execute('''SELECT real_url FROM url WHERE shortened = "{}";'''.format(index)))
    if len(real)==1: #the corresponded url exists
        real = list(real)[0][0] #return the real url
    else: #ah, there is no occurence
        real = None
    return real

        
            
add_to_database('elsea')