def generator():
    base = 'http://archive.org/download/QiroahSyaikhEmadAl-mansary/juz{}.mp3'
    links = []
    for i in range(1,31):
        # print(base.format(i))
        links.append(base.format(i))
    return links

generator()