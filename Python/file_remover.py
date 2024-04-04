import os

def delete_file(file_name: str, file_index: int, file_amount: int):
    try:
        for i in range(file_index, file_index - file_amount, -1):
            file_path = folder_name + "/" + file_name.format(index = i)
            os.remove(file_path)
            print(f'{file_name.format(index = i)} has been removed successfully!') 
    except OSError as e:
        print(f"Error deleting {file_name}: {e}")

path = "Python/"
folder_name = path + "Python_basic_(Part -I)"
file_name = "task_{index}.py"


file_index = int(input("Current index of file: "))
file_amount = int(input("Amount of files to remove: "))

delete_file(file_name, file_index, file_amount)
