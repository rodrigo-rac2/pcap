class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class SubL(Left, Right):
    pass


class SubR(Right, Left):
    pass


obj = SubL()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

obj = SubR()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
