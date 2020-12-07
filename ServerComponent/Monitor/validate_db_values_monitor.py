from pythonrv import rv


@rv.monitor()
@rv.spec(when=rv.POST)
def validate_db_value():
    pass
