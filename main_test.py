def test():
    print('This is test method in com.richard.other')

def main():
    test()

if __name__ == '__main__':
    print('just run', __name__)
    main()
else:
    # 导入时被执行
    print('导入时，__name__属性：', __name__)