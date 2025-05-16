from gencontent import clean_public_dir, copy_content_to_public, generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting Public Directory")
    clean_public_dir()

    print("Copying Static Files to Public")
    copy_content_to_public(dir_path_static, dir_path_public)

    print("Generating Content....")
    generate_page_recursive(dir_path_content, template_path, dir_path_public)


main()