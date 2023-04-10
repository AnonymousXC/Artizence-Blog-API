from fastapi import FastAPI, HTTPException
from pathlib import Path
import re


app = FastAPI()

@app.get('/')
def index():
    return {
            'server': '200',
            'status_code': 'running',
            'github': 'https://github.com/AnonymousXC/Artizence-Blog-API' 
        }


@app.get('/blog')
def indexBlog():
    
    all_blogs = []

    for child in Path('blogs').iterdir():
        if(child.is_file()):
            all_blogs.append(
                    {
                        'article_name': child.name,
                        'heading': 'anything',
                        'author': 'anyone'
                    }
                )

    return {'blogs' : all_blogs}



@app.get('/blog/{blogID}')
def getBlog(blogID):

    for child in Path('blogs').iterdir():
        if child.is_file() and child.name == blogID + '.md':

            markdown = child.read_text()
            rm_markdown = re.sub(r'---\n.*\n.*\n.*\n---', "", markdown)

            # extract text after heading in line 4 of a file
            md_split = markdown.split('\n')
            for i in range(1, 4):
                if re.search(r'author', md_split[i]):
                    author = re.sub(r'author.*\:', "", md_split[i]).strip()
                elif re.search(r'heading', md_split[i]):
                    heading = re.sub(r'heading.*\:', "", md_split[i]).strip()

            return {
                'heading': heading,
                'author': author,
                'markdown': rm_markdown
            }
    
    raise HTTPException(status_code=404, detail="Blog not found")