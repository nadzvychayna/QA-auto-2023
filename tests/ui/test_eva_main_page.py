from modules.ui.page_objects.eva_main_page import EvaMainPage
import pytest


@pytest.mark.ui
def test_cart_usage():
    eva = EvaMainPage()
    
    eva.go_to()
    
    eva.try_add_item_to_cart()
    
    assert eva.check_add_to_card_success_message()
    
    eva.try_change_quantity()
    
    assert eva.check_change_qnt_success_message()
    
    eva.add_always_needed()
    
    assert eva.check_add_always_needed_success_message()

    cart_amount = eva.get_current_cart_amound()
    
    eva.delete_item_from_cart()

    cart_amount_after_delete = eva.get_current_cart_amound()
    
    assert cart_amount_after_delete < cart_amount

    eva.make_purchase()

    assert eva.check_checkout_url()

