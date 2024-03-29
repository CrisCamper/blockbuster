from tools.utils import clean_screen,load_json, code_generator, save_json, key_to_continue

gender_list = load_json("generos")

def create_gender(): # create gender
    num_entry = 0
    genders = {}

    while True:
        try:
            # Solicitar el nombre del género
            name_gender = input('Ingrese el nombre del género: ')
            num_entry += 1

            # Código generador
            code_gender = code_generator('G', num_entry, num_entry)

            # Crear un diccionario con la información del género
            if name_gender:
                for code in code_gender:
                    genders[code] = {
                        "id": code,
                        "nombre": name_gender
                    }

            # Salvar información en json
            save_json(genders, 'generos')

            # Mostrar el diccionario de géneros actualizado
            print("Diccionario de géneros actualizado:", genders)

            # Preguntar si quiere agregar otro género
            another_entry = input('¿Desea agregar otro género? [y/n]: ')
            if another_entry.lower() == 'y':
                clean_screen()
            elif another_entry.lower() == 'n':
                break
            else:
                print('Opción no reconocida')
                break

        except Exception as e:
            print(f"Error: {e}")

def list_genders(): # list genders
    lista_genders = load_json('generos')
    print(f'GENEROS:')
    for gender_code, gender_data in lista_genders.items():
        print(f'{gender_code}: {gender_data["nombre"]}')
        print('----------------------------------')
    key_to_continue()