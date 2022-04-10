from aiohttp import web
from aiohttp_cors import setup, ResourceOptions
from classifier_model import classify, load_model_and_tokenizer

app = web.Application()
load_model_and_tokenizer()


async def get_text(request: web.Request):
    data = await request.post()
    classified = classify(data.get('text'))
    return web.json_response({'reviewed': bool(classified[0])})


urls = [
    web.post('/neural/', get_text)
]
app.add_routes(urls)

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

web.run_app(app, port=8080)
