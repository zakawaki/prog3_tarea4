
def test_add_and_delete_contact(browser):
    browser.get("http://localhost:5000/login")  # Primero hacer login correctamente
    browser.find_element("name", "username").send_keys("admin")
    browser.find_element("name", "password").send_keys("admin")
    browser.find_element("tag name", "button").click()
    
    # Esperar a que cargue el dashboard
    browser.implicitly_wait(2)
    
    # Añadir contacto
    browser.find_element("name", "name").send_keys("Juan")
    browser.find_element("name", "email").send_keys("juan@example.com")
    browser.find_element("name", "phone").send_keys("8090000000")
    browser.find_element("tag name", "form").submit()
    
    # Esperar y verificar
    browser.implicitly_wait(2)
    assert "Juan" in browser.page_source
    
    # Eliminar contacto - usar XPath más específico
    delete_button = browser.find_element("xpath", "//li[contains(., 'Juan')]//a[contains(text(), 'Eliminar')]")
    delete_button.click()
    
    # Aceptar la alerta
    alert = browser.switch_to.alert
    alert.accept()
    
    # Esperar y verificar eliminación
    browser.implicitly_wait(2)
    assert "Juan" not in browser.page_source