import glob
from pathlib import Path

def process_files(ufile, sfile):
    with open(ufile, encoding='utf-8', errors='replace') as fin:
        with open(sfile, 'w', encoding='cp932', errors='replace') as fout:
            fout.write(fin.read())

def process_folder(folder_u, folder_s):
    ufiles = list(folder_u.glob("*.txt"))
    sfiles = [folder_s / ufile.name for ufile in ufiles]
    files_dict = dict(zip(ufiles, sfiles))

    for ufile, sfile in files_dict.items():
        process_files(ufile, sfile)

def process_subfolders(root_u, root_s):
    for subfolder_u in root_u.iterdir():
        if subfolder_u.is_dir():
            subfolder_s = root_s / subfolder_u.name
            subfolder_s.mkdir(exist_ok=True)
            process_folder(subfolder_u, subfolder_s)

root_path_u = Path("./text")
root_path_s = Path("./cp932")

process_subfolders(root_path_u, root_path_s)
