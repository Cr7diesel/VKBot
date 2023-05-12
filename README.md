Приложение состоит из следющих модулей:

main.py - функции, работающие с ВК-ботом, обрабатывающие пользовательский INPUT, а также обращающиеся к модулям запросов ВК и базе данных.

vk_users.py - функции, посылающие и обрабатывающие ВК запросы.

db_manager.py - содержит класс DBObject, экземпляр которого инициализируется через название БД, пароль и пользователя из configures.py. 
В классе присутствует метод подключения и отключения от базы данных, а также методы для сохранения данных о пользователях, фаворитах и черном списке и их выборке. 

VKUser.py - вспомогательный класс, который отображает пользователя ВК с нужными атрибутами.

configures.py - содержит токены для бота, пользователя и данные для БД: название, пароль и имя пользователя.

tests - с помощью pytest тестирует функции получения данных пользователя ВК.

Использование:

Пользователь заносит личные токены и данные БД в configures.py. 

Стартует main.py, в группе ВК пишет 'Привет', далее следуя указаниям бота, вводит запрос типа: 'женский 25-30 Москва 10' 
(Последняя цифра указывает максимальное количество желаемых результатов. Эта цифра не должна привышать 99 из-за долгого выполнения запросов). 
В результате выводятся пользователи, подходящие под запрос, с именем, фамилией, ссылкой на профиль и 3-мя (или меньше) фото с наибольшим количеством лайков.

С помощью кнопки next можно посмотреть следующего пользователя. 

Кнопка save заносит пользователя в фавориты.

Кнопка block заносит пользователя в черный список.

Кнопки favorites list и black list показывают список фаворитов и заблокированных пользователей соответственно.

Кнопка restart отключает связь с БД, затем снова включает и создает пустую БД, при этом бот предлагает пользователю начать поиск сначала.