import os
from PIL import Image
os.makedirs('wp/assets',exist_ok=True);os.makedirs('wp/covers',exist_ok=True)
tot0=tot1=0
def conv(src,dst):
    global tot0,tot1
    im=Image.open(src); png=src.lower().endswith('.png')
    if png:
        im=im.convert('RGBA') if (im.mode in('P','RGBA','LA') or 'transparency' in im.info) else im.convert('RGB')
        im.save(dst,'WEBP',lossless=True,method=6); a=os.path.getsize(dst)
        im.save('/tmp/_l.webp','WEBP',quality=90,method=6); b=os.path.getsize('/tmp/_l.webp')
        if b<a*0.6: os.replace('/tmp/_l.webp',dst)
    else:
        im=im.convert('RGB'); im.save(dst,'WEBP',quality=85,method=6)
    tot0+=os.path.getsize(src);tot1+=os.path.getsize(dst)
for f in os.listdir('src_assets'):
    if f.lower().endswith(('.jpg','.jpeg','.png')): conv('src_assets/'+f,'wp/assets/'+os.path.splitext(f)[0]+'.webp')
for f in os.listdir('covers'):
    if f.lower().endswith(('.jpg','.jpeg','.png')): conv('covers/'+f,'wp/covers/'+os.path.splitext(f)[0]+'.webp')
print(tot0,tot1)
