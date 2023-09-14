def check(*, key, value):
    def set_target():
        for bank in Bank.banks:
            for user in bank:
                if user.__getitem__(key) == value:
                    return user
        return None

    return set_target


class Bank:
    total_count = 3
    banks = [[] for i in range(total_count)]

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money
        self.object = self

    @classmethod
    def open_account(cls, owner: str, account_number: str, phone: str, password: str, money: int, bank_choice: int):
        bank = [
            ShinHan(owner, account_number, phone, password, money),
            KookMin(owner, account_number, phone, password, money),
            KaKao(owner, account_number, phone, password, money)
        ][bank_choice - 1]
        cls.banks[bank_choice - 1].append(bank.__dict__)
        return bank

    @staticmethod
    def check_account_number(account_number: str) -> dict:
        return check(key='account_number', value=account_number)()

    @staticmethod
    def check_phone(phone: str) -> dict:
        return check(key='phone', value=phone)()

    def deposit(self, money: int):
        self.money += money

    def withdraw(self, money: int):
        self.money -= money

    def show_balance(self) -> int:
        return self.money

    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):
    def deposit(self, money: int):
        money /= 2
        super().deposit(money)


class KookMin(Bank):
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    def show_balance(self) -> int:
        self.money /= 2
        return super().show_balance()


if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 카카오 뱅크\n" \
                "3. 국민 은행\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        while True:
            menu_choice = int(input(menu))
            if menu_choice == 5:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    if password.__len__() == 4:
                        break

                money = int(input(money_message))

                user = None

                # 아래의 분기별 은행 분석을 한 줄로 변경!
                user = Bank.open_account(owner, account_number, phone, password, money, bank_choice)

                # # 신한 은행
                # if bank_choice == 1:
                #     user = ShinHan.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 카카오 뱅크
                # elif bank_choice == 2:
                #     user = KaKao.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 국민 은행
                # elif bank_choice == 3:
                #     user = KookMin.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # print(user, Bank.banks, sep="\n")

            # 입금
            elif menu_choice == 2:
                # 입금은 개설한 은행에서만 가능
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        deposit_money = int(input(deposit_message))
                        # 객체를 가져와서 deposite()실행
                        user.__getitem__("object").deposit(deposit_money)
                else:
                    print(error_message)
            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        withdraw_money = int(input(withdraw_message))
                        if user.__getitem__("object").money >= withdraw_money:
                            user.__getitem__("object").withdraw(withdraw_money)
                        else:
                            print("대출을 진행할까요?")
                else:
                    print(error_message)
            # 잔액
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        print(f'현재 잔액: {user.__getitem__("object").show_balance()}')

                else:
                    print(error_message)
