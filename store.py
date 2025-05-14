from storage_json import StorageJson

def main():
    storage = StorageJson('data.json')
    print(storage.list_movies())
    #storage.add_movie('Ritter der Kokosnuss', 1982, 8.5, "Monty Python")


if __name__ == '__main__':
    main()
