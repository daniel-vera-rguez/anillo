from anillo.app import application
from anillo.utils.common import chain
from anillo.http import Ok
from anillo.middlewares.session import wrap_session, MemoryStorage
from anillo.middlewares.json import wrap_json
from anillo.middlewares.cookies import wrap_cookies


def index(request):
    value = request.session.get('value', 0)
    request.session['value'] = value + 1
    return Ok(request.session, headers={"Content-Type": "application/json"})


app = application(chain(
    wrap_json,
    wrap_cookies,
    wrap_session(storage=MemoryStorage),
    index,
))


if __name__ == '__main__':
    from anillo import serving
    serving.run_simple(app, port=5000)
