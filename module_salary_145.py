'''
本模块用于计算公司员工的工资
'''
company="微软"
def yearSalary(monthSalary):
    '''根据传入的月薪，计算出年薪'''
    return monthSalary*12

def daySalary(monthSalary):
    '''根据传入的月薪，计算出每天的薪资'''
    return monthSalary/22.5
if __name__=="__main__":
    print(yearSalary(3000))
    print(daySalary(3000))