import os
import random
import string

from gatco.response import json
from gatco import Blueprint

import aiofiles

from application.server import app

upload = Blueprint('image', url_prefix='/image')

@upload.route('/')
async def bp_root(request):
    return json({'image': 'blueprint'})


@upload.route('/upload', methods=['POST'])
async def imgupload(request):
    ret = None
    url = app.config['IMAGE_SERVICE_URL']
    fsroot = app.config['FS_ROOT']
    if request.method == 'POST':
        file = request.files.get('image', None)
        if file :
            rand = ''.join(random.choice(string.digits) for _ in range(5))
            file_name = os.path.splitext(file.name)[0]
            extname = os.path.splitext(file.name)[1]
            newfilename = file_name + "-" + rand + extname
            
            async with aiofiles.open(fsroot + newfilename, 'wb+') as f:
                await f.write(file.body)
            
            ret = {
                "link": url  + "/" + newfilename  ,
                #"link": "/" + newfilename  ,
                "width": None,
                "height": None
            }
    return json(ret)