import pytest
from modules.common.database import Database
from sqlite3 import IntegrityError


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_products_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_field_by_id('quantity', 1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_products (4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_field_by_id('quantity', 4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_products (99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_field_by_id('quantity', 99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders =db.get_detailed_orders()
    print("Замовлення", orders)

    # Check quantity of orders equal to 1
    assert len(orders) >= 1

    # Check structure of data
    assert orders [0][0] == 1
    assert orders [0][1] == 'Sergii'
    assert orders [0][2] == 'солодка вода'
    assert orders [0][3] == 'з цукром'


@pytest.mark.database
def test_products_description_update():
    db = Database()
    db.updade_product_description_by_id(4, 'шоколадне з апельсином')
    biscuit_description = db.select_product_field_by_id('description', 4)

    assert biscuit_description[0][0] == 'шоколадне з апельсином'


@pytest.mark.database
def test_user_insert():
    db = Database()
    db.insert_users(33, 'Mariia', 'Voli 7', 'Lutsk', '43012', 'Ukraine')
    user = db.get_users_field_by_id('name', 33)

    assert user [0][0] == 'Mariia'


@pytest.mark.database
def test_address_update():
    db = Database()
    db.update_user_address(33, 'Rivnenska 22')
    new_address = db.get_users_field_by_id('address', 33)

    assert new_address [0][0] == 'Rivnenska 22'


@pytest.mark.database
def test_insert_order():
    db = Database()
    db.insert_order(23, 33, 3)
    orders = db.get_detailed_orders()
    
    assert orders [1][0] == 23
    assert orders [1][1] == 'Mariia'
    assert orders [1][2] == 'молоко'
    assert orders [1][3] == 'натуральне незбиране'


@pytest.mark.database
def test_update_order():
    db = Database()
    db.update_order(23, 2)
    orders = db.get_detailed_orders()

    assert orders [1][0] == 23
    assert orders [1][1] == 'Mariia'
    assert orders [1][2] == 'солодка вода'
    assert orders [1][3] == 'з цукрозамінником'


@pytest.mark.database
def tesr_delete_order():
    db = Database()
    orders = db.get_detailed_orders()

    assert len(orders) == 2
    
    db.delete_order(23)
    orders = db.get_detailed_orders()

    assert len(orders) == 1
    assert orders [0][0] != 23


@pytest.mark.database
def test_user_delete():
    db = Database()
    db.delete_user_by_id(33)
    user = db.get_users_field_by_id('id', 33)

    assert len(user)  == 0  


@pytest.mark.database
def test_insert_product_with_duplicated_id():
    db = Database()
    try:
        db.insert_product_with_duplication(1, 'milk')
    except Exception as error:
        db.connection.commit()
        assert type(error) == IntegrityError
        


@pytest.mark.database
def test_insert_user_with_dudlicated_id():
    db = Database()
    try:
        db.insert_user_with_duplication(2, 'two')
    except Exception as error:
        db.connection.commit()
        assert type(error) == IntegrityError


