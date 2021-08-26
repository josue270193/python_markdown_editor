animals_file = open("animals.txt")
new_animals_file = open("animals_new.txt", "w")
list_animals = [animal.strip() for animal in animals_file]
new_animals_file.write(" ".join(list_animals))
animals_file.close()
new_animals_file.close()
