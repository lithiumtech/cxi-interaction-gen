# internal
from ast import Continue
from containers import Application
from controllers import cdqa

#site-packages
from fastapi import FastAPI


def create_app()->FastAPI:
    # setting up DI
    application = Application()
    application.wire(modules=[__name__,cdqa])

    # creating app and setting up routing 
    app = FastAPI() 
    app.include_router(cdqa.router)

    return app

app = create_app()

if __name__=="__main__":
    app.run()