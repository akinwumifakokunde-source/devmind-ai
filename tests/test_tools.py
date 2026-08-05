from agent.tools import list_files, read_file

print("=" * 60)
print("PROJECT FILES")
print("=" * 60)

files = list_files.invoke({"directory": "."})
print(files)

print("\n" + "=" * 60)
print("FIRST 500 CHARACTERS OF main.py")
print("=" * 60)

content = read_file.invoke({"file_path": "main.py"})
print(content[:500])