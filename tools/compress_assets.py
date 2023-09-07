import gzip
assets_list = {
    'data/index.html.out': 'data/index.html.out',
    'data/js.js': 'data/js.js.out',
    'data/style.css': 'data/style.css.out',
}


for src_file_name, out_file_name in assets_list.items():
    with open(src_file_name, 'rb') as f:
        content = f.read()
    with open(out_file_name, 'wb') as f:
        f.write(gzip.compress(content, compresslevel=9))
