from text_blocks_markdown import markdown_to_htmlnode, extract_title
import shutil
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()
        content_html = markdown_to_htmlnode(markdown).to_html()
        title = extract_title(markdown)
    with open(template_path, "r", encoding="utf-8") as file:
        template_html = file.read()
    output_html = template_html.replace("{{ Title }}", title).replace("{{ Content }}", content_html)
    output_html = output_html.replace("href=\"/", f"href={basepath}").replace("src=\"/", f"src={basepath}")
    with open(dest_path, "w") as file:
        file.write(output_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, file)
        dst_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(src_path):
            dst_path = dst_path.replace(".md", ".html")
            generate_page(src_path, template_path, dst_path, basepath)
        elif os.path.isdir(src_path):
            os.mkdir(dst_path)
            generate_page_recursive(src_path, template_path, dst_path, basepath)
    

def clean_public_dir():
    if os.path.exists("docs/"):
        shutil.rmtree("docs/")
        os.mkdir("docs")
    else:
        os.mkdir("docs")
def copy_content_to_public(src_dirc, dst_dirc):
    if not os.path.exists(src_dirc):
        raise FileNotFoundError("this path does not exist")
    for file in os.listdir(src_dirc):
        src_path = os.path.join(src_dirc, file)
        dst_path = os.path.join(dst_dirc, file)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copying {src_path} to {dst_path}")
        elif os.path.isdir(src_path):
            print(f"Entering Directory {src_path}")
            os.mkdir(dst_path)
            copy_content_to_public(src_path, dst_path)