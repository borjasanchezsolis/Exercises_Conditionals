name = input('Whats the name of the file? ').lower()

if '.gif' in name:   # or if name.endswith('.gif'):
    print('image/gif')
if name.endswith('.jpeg'):
    print('image/jpeg')
if name.endswith('.pdf'):
    print('document/pdf')