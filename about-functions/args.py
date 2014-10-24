'''
Take a look at how Python handles arguments, (which code.org and others
sometimes call 'parameters'). This is the stuff that gets passed into a
function. Python's creators have really mastered all the many ways
arguments are passed to functions making them all just work.

* Positional arguments with no default are required

'''

def test_all_args(one,two,foo='bar',*args,**kwargs):
    print()
    print('one: {}'.format(one))
    print('two: {}'.format(two))
    print('foo: {}'.format(foo))
    print('args: {}'.format(args))
    print('kwargs: {}'.format(kwargs))

def test_kwargs(**kwargs):
    print()
    print('kwargs: {}'.format(kwargs))

mydictionary = {"bar":100,"spam":"gross"}

demo_args = [
    '1',
    '1,2',
    '\'1\',2',
    '1,2,3',
    'foo=100,1,2',
    '1,2,foo=100',
    '1,2,3,4,5,6,foo=100',
    '1,2,bar=100',
    '1,2,3,bar=100,spam="gross"',
    '1,2,3,{"bar":100,"spam":"gross"}',
    '1,2,3,mydictionary',
    'bar=100,spam="gross"',
    '{"bar":100,"spam":"gross"}',
    ]

def do_test(function_name):
    for args in demo_args:
        print('-' * 76)
        call = function_name + '(' + args + ')'
        print(' called: ' + call)
        try: 
            eval(call)
        except Exception as e:
            print()
            print('FAIL: {}'.format(e), end='')
        print()

do_test('test_all_args')
do_test('test_kwargs')
