from aiohttp import web
from aiohttp_cors import setup, ResourceOptions


app = web.Application()

router = web.RouteTableDef()


@router.post('/')
async def get_text(request: web.Request):
    data = await request.post()
    # тут нейронка делает свои дела
    return web.json_response({'title': })


cors = setup(app, defaults={
    '*': ResourceOptions(
        allow_credentials=True,
        expose_headers='*',
        allow_headers='*',
        allow_methods='*'
    )
})
for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app)
