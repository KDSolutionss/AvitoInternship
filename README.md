# Автоматизация позитивного тест-кейса
В репозитории содержатся файлы test_avito.py, который содержит непосредственно тесты необходимой в задании функциональности, и settings.py, в котором содержатся строковые константы, необходимые для запуска автоматизации.\
В файле test_avito.py имеется 21 тест функциональности добавления в избранное объявления(https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363) с карточки объявления.\
Все тесты, за исключением 1 и 3, обладают тем же названием, что и в плане тестирования(для 1 и 3 теста в этом файле подписаны комментарии).
Перед запуском автоматизации необходимо в терминале,запущенному из директории, содержащей скопированные с репозитория файлы, выполнить команду __pip install selenium__
необходимую для установки библиотеки selenium для языка программирования Python.\
Запускать автоматизацию возможно как целиком (вызвав в терминале,запущенному из директории, содержащей скопированные с репозитория файлы,команду __python -W  ignore test_avito.py FavouritesFunctionalityTest__),
так и по отдельности каждый тест. Кроме того, запускать тесты можно в интегрированной среде разработки PyCharm, нажав либо кнопку RUN(зеленый треугольник) около названия class FavouritesFunctionalityTest для запуска всех тестов сразу, либо кнопку RUN, расположенную около функции отвечающей за тест, для запуска конкретного теста. Для тестов был написан развернутый комментарий на случай его невыполнения. Всюду далее в файле README, под названием каждого теста будет написана команда, необходимая для его вызова.

### Тесты 
1. Проверка того, что при нажатии на кнопку "Добавить в избранное" возникнет всплывающее оповещение(Этот тест и тест 3, являются программной проверкой теста 1 из плана тестирования)\
   __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_pop_up_screen_created_after_click__
2. Проверка отсутствия оповещения из теста 1 в области видимости пользователя при отсутствии нажатия на “Добавить в избранное”.\
   __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_pop_up_screen_not_created_without_click__
3. Текст всплывающего оповещения из теста 1 сигнализирует о добавление товара в избранное("Добавлено в избранное") (Этот тест и тест 1, являются программной проверкой теста 1 из плана тестирования)\
   __python -W  ignore test_avito.py FavouritesFunctionalityTesttest_pop_up_screen_correct_text__
4. Проверка появления оповещения об удалении из избранного при двойном нажатии на кнопку, содержащую текст “Добавить в избранное” со страницы объявления.\
  __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_pop_up_screen_correct_text_after_double_add__
5. Наличие доступной для нажатия части во всплывающем оповещении (см. тест 1).\
 __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_pop_up_text_after_add_is_clickable__
6. Нажатие на кнопку, содержащую текст “Добавить в избранное”, изменит ее текст.\
   __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favourites_button_text_changed_after_click__
7. Двойное нажатие на кнопку, содержащую текст, “Добавить в избранное” дважды изменит ее текст и приведет к первоначальному значению текста кнопки.\
   __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favourites_button_text_unchanged_after_double_click__
8. Нажатие на подсвеченную синим часть текста всплывающего оповещения (см. тест 1), переводит пользователя на страницу избранного.\
  __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_go_to_favs_click__
9. Нажатие на кнопку "Добавить в избранное" приводит к добавлению элемента в избранное.\
  __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favs_contains_added_item_after_add__
10. Двойное нажатие на кнопку "Добавить в избранное" не приводит к добавлению элемента в избранное.\
  __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favs_does_not_contains_added_item_after_double_add__
11. При добавлении товара в избранное, на странице избранных товаров возле каждого товара будет отображаться красное сердце.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_red_heart_button_on_favs_screen_after_add_to_favs__
12. Нажатие на красное сердце на странице избранных товаров приводит к удалению товара из избранных.\
  __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favs_does_not_contains_added_item_after_click_on_red_heart__
13. Товар, добавленный в список избранных, на странице избранных товаров обладает той же категорией, что и на странице самого объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_correct_category_in_favs_screen_after_add__
14. Товар, добавленный в список избранных, на странице избранных товаров обладает тем же названием, что и на странице самого объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favs_correct_label_on_added_item__
15. В карточке товара, добавленного в список избранных, на странице избранных товаров указан тот же город, что и на странице самого объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_correct_city_on_added_item__
16. В карточке товара, добавленного в список избранных, на странице избранных товаров указана такая же цена, что и на странице самого объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_correct_price_on_added_item__
17. В карточке товара, добавленного в список избранных, на странице избранных товаров указана такая же дата публикации, что и на странице самого объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_correct_date_of_advert_on_added_item__
18. Удаление товара из избранных со страницы избранных товаров приводит к первоначальному состоянию текста кнопки, отвечающей за добавление в избранное на странице объявления.\
   __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_product_screen_favs_button_correct_text_after_click_on_red_heart_button_on_favs_screen__
19. При нажатии на картинку, расположенную на карточке добавленного в список избранных товара, происходит переход на страницу объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favs_screen_correct_behavior_after_click_on_advert_image__
20. При нажатии на заголовок карточки добавленного в список избранных товара, происходит переход на страницу объявления.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_favs_screen_correct_behavior_after_click_on_advert_name__
21. Нажатие на кнопку "Показать телефон" приводит к появлению всплывающего окна авторизации.\
    __python -W  ignore test_avito.py FavouritesFunctionalityTest.test_get_phone_pop_up_on_main_screen_correct_behavior__
    \
    \
Рекомендуется запуск тестов в режиме одиночного запуска. Запуск автоматизации целиком приводит к обнаружению подозрительной активности со стороны сайта Авито и мешает дальнейшему выполнению тестов. Кроме того рекомендуется запуск каждого теста отдельно ввиду следующей ситуации: единожды было замечено, что при запуске тестов целиком, в одном из тестов происходила бесконечная загрузка страницы, что приводило к невыполнению теста, однако повторный запуск отдельно этого теста увенчался успехом.  
В планах было проверить соответствие картинок, расположенных на странице объявления и на карточке добавленного в избранное объявления. Однако различия в разрешениях, наличие водяного знака помешали выполнению данной проверки.

    

   
