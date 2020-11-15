template = ['template.py']

kata_dir = 'katas'
solved_katas_file = 'codewars/solved_katas.txt'

with open(solved_katas_file, 'r') as f:
    kata_paths = [f'{kata_dir}/{f_name}.py' for f_name in f.read().splitlines()]

collect_ignore = template + kata_paths
