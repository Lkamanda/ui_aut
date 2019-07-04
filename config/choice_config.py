def choiceConfig():
    """
    根据config_number 来选择不同配置
    config_number: 0 ： 研发版
                   1 ： 发布版
    """
    config_number = int(input("请输入当前版本号：‘研发版’：0，发布版：‘1’"))
    return config_number
