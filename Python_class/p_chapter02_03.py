# Chapter02-02
# 객체 지향 프로그래밍(OOP)
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author: Kim
    Date: 2021.07.13
    Description: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)
    
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})




print(car1)


