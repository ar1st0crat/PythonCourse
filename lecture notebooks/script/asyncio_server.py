from aiohttp import web
import jinja2
import aiohttp_jinja2


routes = web.RouteTableDef()


async def hello(request):
    return web.Response(text="Hello, world")


@routes.get('/wow')
async def wow(request):
    return web.Response(text="Wow")


@routes.get('/page')
@aiohttp_jinja2.template('page.html')
async def page(request):
    return { 'cars': [ { 'model': 'Toyota Lexus', 'no': 'A123AH' }, 
                       { 'model': 'Ford Focus', 'no': 'A765OO' } ] }


app = web.Application()
app.add_routes([web.get('/', hello)])   # 1-ый способ
app.add_routes(routes)                  # 2-ой способ (декораторы)

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

web.run_app(app)
