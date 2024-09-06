# PEP Scraper

PEP Scraper — это проект для парсинга информации о PEP 

## Установка

1. **Клонируйте репозиторий:**

   ```
   git clone https://github.com/heydolono/scrapy_parser_pep.git
   cd scrapy_parser_pep
   ```

2. **Создайте и активируйте виртуальное окружение:**

    ```
    python -m venv venv
    source venv/Scripts/activate 
    ```

3. **Установите зависимости:**

    ```
    pip install -r requirements.txt
    ```

4. **Запустите парсер с помощью Scrapy:**

    ```
    scrapy crawl pep
    ```