# join склеивает список в одну строку разделяя их символом '/'
data = [ 'https:','', 'habr.com', 'ru', 'users''dzhoker1', 'posts']
url = '/'.join (data)
print (url)