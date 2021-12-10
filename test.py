
def acroynym(phrase):
    result = ""
    for word in phrase.split():
        result += word[0:1].upper()
    print(result)

if __name__ == '__main__':
    acroynym('central processing unit')