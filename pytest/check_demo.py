def inc(x):
    return x + 1

def check_answer():
    print("这是我的第一条测试用例")
    assert inc(4) == 5
def test_foo():
    print("这是我的第二条测试用例")
    assert inc(4) == 5