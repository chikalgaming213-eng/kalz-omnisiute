import json
import threading
import urllib.error
import urllib.request

from kalz.api.rest import serve


def test_plan_rejects_invalid_package_names():
    server = serve('127.0.0.1', 18766)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    request = urllib.request.Request('http://127.0.0.1:18766/api/v1/plan', data=json.dumps({'packages': ['curl; rm -rf /']}).encode(), headers={'Content-Type': 'application/json'}, method='POST')
    try:
        urllib.request.urlopen(request)
        assert False, 'invalid input must be rejected'
    except urllib.error.HTTPError as error:
        assert error.code == 400
    finally:
        server.shutdown(); server.server_close()
