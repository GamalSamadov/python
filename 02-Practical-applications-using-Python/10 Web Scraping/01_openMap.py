import webbrowser, sys

adress = ''
if len(sys.argv) > 1:
    print(sys.argv[1:])
    adress = ' '.join(sys.argv[1:])
    print(adress)

else:
    print('Please enter the adress')
    exit()

webbrowser.open('https://www.google.com/maps/place/' + adress)