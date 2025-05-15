from textnode import TextNode, TextType
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Not a Valid String")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = re.split(r'((?<!\!)\[[^\]]+\]\([^)]+\))', node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                link = extract_markdown_links(sections[i])

                if link:
                    label, url = link[0]
                    new_nodes.append(TextNode(label, TextType.LINK, url))
    return new_nodes
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = re.split(r"(!\[.*?\]\(.*?\))", node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                image = extract_markdown_images(sections[i])
                if image:
                    label, url = image[0]
                    new_nodes.append(TextNode(label, TextType.IMAGE, url))
    return new_nodes
def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', text)
    return matches