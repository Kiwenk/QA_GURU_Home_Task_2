from selene import browser, be, have

#проверяем, что гугл отдаёт нам корректный результат
def test_positive_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

#проверяем, что УткаУткаГо отдаёт нам корректный результат
def test_positive_duckduckgo():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[data-result="snippet"]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))

#проверяем, что УткаУткаГо отдаёт нам корректный результат при случайном наборе символов, по которому нет результатов
def test_negative_duckduckgo():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('апвапавпавпрывфывыфа').press_enter()
    browser.element('[id="react-layout"]').should(have.text('По запросу апвапавпавпрывфывыфа результаты не найдены.'))
