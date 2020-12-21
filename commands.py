async def help_command(channel):
    lista_de_comandos = '''
        LISTA DE COMANDOS
        !help => esse cara aqui
    '''
    await channel.send(lista_de_comandos)


async def save_movie(channel, author, movie):
    with open('lista.csv', 'a') as f:
        f.write(f'{author},{movie}\n')
    await channel.send(f'Filme {movie} foi salvo com sucesso')


async def list_movies(channel):
    with open('lista.csv', 'r') as f:
        lista = f.readlines()
    await channel.send('Listando filmes')
    for movie in lista:
        _, mv = movie.split(',')
        await channel.send(f'{mv}')
