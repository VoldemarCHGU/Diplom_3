# Diplom_3

1. Установка нужных пакетов
pip install -r requirements.txt

2. Запуск тестов

`pytest tests --alluredir=allure_results`

По умолчанию запускается в браузере chrome без графического интерфейса
При необходимости можно изменить значения:

`pytest tests --alluredir=allure_results --browser=firefox --headless=false`
3. Просмотр отчёта
`allure serve allure_results`