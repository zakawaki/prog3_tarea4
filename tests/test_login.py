def test_login_success(browser, screenshot):
    # Paso 1: Ir a la página de login
    browser.get("http://localhost:5000/login")
    screenshot("1_page_loaded")
    
    # Paso 2: Ingresar credenciales
    browser.find_element("name", "username").send_keys("admin")
    browser.find_element("name", "password").send_keys("admin")
    screenshot("2_credentials_entered")
    
    # Paso 3: Enviar formulario
    browser.find_element("tag name", "button").click()
    screenshot("3_form_submitted")
    
    # Verificaciones
    assert "dashboard" in browser.current_url.lower()
    screenshot("4_verified")

def test_login_fail(browser, screenshot):
    # Paso 1: Ir a la página de login
    browser.get("http://localhost:5000/login")
    screenshot("1_page_loaded")
    
    # Paso 2: Ingresar credenciales incorrectas
    browser.find_element("name", "username").send_keys("wrong")
    browser.find_element("name", "password").send_keys("wrong")
    screenshot("2_wrong_credentials")
    
    # Paso 3: Enviar formulario
    browser.find_element("tag name", "button").click()
    screenshot("3_form_submitted")
    
    # Verificaciones
    assert "incorrect" in browser.page_source.lower()
    screenshot("4_error_shown")