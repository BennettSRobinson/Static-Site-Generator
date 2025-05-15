from enum import Enum
import re
from htmlnode import ParentNode
from text_inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered list"
    ULIST = "unordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.strip().split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            lines = stripped_block.split("\n")
            cleaned_block = "\n".join(line.strip() for line in lines)
            new_blocks.append(cleaned_block)
    return new_blocks

def block_to_blocktype(text):
    match text:
        case _ if re.match(r'^(#{1,6})\s+(.*)', text):
            return BlockType.HEADING
        case _ if re.match(r'^```(?:\w+)?\n([\s\S]*?)\n```', text):
            return BlockType.CODE
        case _ if re.match(r'^(>\s?.+(\n>.*)*)', text):
            return BlockType.QUOTE
        case _ if re.match(r'^(-\s.+(\n-\s.+)*)', text):
            return BlockType.ULIST
        case _ if re.match(r'^([1]\.\s.+(\n[2-9]\.\s.+)*)', text):
            return BlockType.OLIST
        case _:
            return BlockType.PARAGRAPH

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        html_node = block_to_htmlnode(block)
        block_nodes.append(html_node)
    return ParentNode("div", block_nodes)

def block_to_htmlnode(text):
    block_type = block_to_blocktype(text)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_htmlnode(text)
        case BlockType.HEADING:
            return heading_to_htmlnode(text)
        case BlockType.CODE:
            return code_to_htmlnode(text)
        case BlockType.QUOTE:
            return quote_to_htmlnode(text)
        case BlockType.OLIST:
            return olist_to_htmlnode(text)
        case BlockType.ULIST:
            return ulist_to_htmlnode(text)
        case _:
            raise ValueError("Not a valid block")
        
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError("incorrect level of heading")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_htmlnode(block):
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("Not a valid code text")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    children = text_node_to_html_node(raw_text_node)
    code_node  = ParentNode("code", [children])
    return ParentNode("pre", [code_node])

def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("not a valid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_htmlnode(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        content = line[2:]
        children = text_to_children(content)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)
def olist_to_htmlnode(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        content = line[3:]
        children = text_to_children(content)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)