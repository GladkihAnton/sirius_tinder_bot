1. Бот-календарь, с помощью которого можно создать свое расписание, напоминать о дедлайнах. Приходько Кирилл
   - Из функционала должна быть возможность:
     - запомнить учетку, чтобы в любой момент я мог посмотреть свое расписание
     - Создать дело со сроком когда оно должно закончится. 
     - Оповестить за день, за 12ч и за 1ч до начала этого дела

2. Тема: Бот для изучения программирования на Python
   Из функционала должна быть возможность:
   - запомнить учетку, чтобы в любой момент человек мог посмотреть свои решенные задачи
   - Выбрать рандомно из существующего списка задачу
     - при выборе задачи в ответ ожидается код, который нужно скомпилить и выполнить.
     - при успешном выполнении простановка статуса об успешности
     - при неуспешном соответствующее сообщение с ошибкой
     - P.S В разработке не будем думать об безопаности, что могут заслать плохой код
   - создать задачу в этапы
     - название задачи
     - описание задачи
     - кол-во примеров
     - пример
     - ответ

3. Реализация бота для поддержки клиентов и обработки запросов через чат - Пружинина Арина
   - Несколько видов учеток - админ и клиент.
     - если клиент шлет сообщение то оно рандомно доставляется одному из админов
     - когда сообщение приходит, то ответ админа на это сообщение уходит к клиенту. 
     - В моменте у админа может быть только одно сообщение от клиента
     - Если приходит сообщение от клиента, а админы заняты, то нужно подождать пока хотя бы один админ освободится

4. Разработка бота для организации и проведения опросов и анкетирования. - Снопов Даниил
   - У бота должны быть две роли:
     - админ, который умеет создавать опросники в формате
       - кол-во вопросов = N
       - вопрос
       - ... (N штук)
       - вопрос
     - опрашиваемый
       - После регистрации админ может прислать этому пользователю опрос, с подтверждением согласия на проходждение опрос
       - если пользователь соглашается, то начинается опрос по вопросам из опросника

5. Морской бот с ИИ - Шутова Анна
   - пользователь нужен только для отслеживания статуса игры
   - можно посмотреть статусы игр
   - сама игра:
     - реализации морского боя на питоне можно взять из интернета
     - при вводе пользователь отправляет клетку которую собирается атаковать. Тут важна обработка ошибок
     - если успешно, в ответ бот присылает текущий бот пользователя + следующий от бота. С ходом бота
     - Саму отрисовку поля боя можно сделать с помощью символов массива.

6. Бот для хранения фотографий - Пушкарева Алина
   - пользователь нужен для возможности получить загруженные фото
   - можно посмотреть все загруженные фото в разрезе месяца и потом дня
   - в разрезе дня можно нажать на нужную фотку и подгрузить ее
   - Саму фото можно грузить на любое хранилище, можно использовать яндекс диса или гугл диск или любое другое хранилище.

7. Бот для заказа еды - Нестеров Владислав
   - две роли пользователя:
     - курьер - ему приходят готовые заказы на доставку
     - пользователь - умеет выбирать из меню товары, которые готовы к выдаче
   - выбор товаров:
     - В базе должен быть список товаров с категориями
     - при запросе выбора товаров изначально кидается список категорий в которых есть хотя бы один товар
     - далее по кнопке можно выбрать нужную категории и посмотреть список товаров
     - сам список товаров небольшой, сделать пагинацию через offset + limit на 10 товаров.
   - У товара есть возможность нажать "добавить в корзину", тогда он попадает в корзину
   - отдельной кнопкой можно оформить заказ, тогда все товары в заказе должны попасть в чат с курьером
     - если их несколько, то одному из них рандомно

8. Бот для подбора рецепта - Вечернина Вероника
   - роль пользователя одна:
     - можно посмотреть свои созданные рецепты
   - меню бота:
     - создать новый рецепт
     - получить рецепт по продуктам
     - подобрать самый популярный рецепт
   - создать новый рецепт
     - записать в бд сам рецепт и ингредиенты
     - ингредиенты в формате название + граммы (пусть все в граммах будет)
   - получить рецепт
     - запрашиваются имеющиеся продукты
     - после описание всех продуктов можно нажать "подобрать рецепт"
     - должна быть пагинация рецептов
     - предложенные рецепты можно лайкнуть и дизлайкнуть (пусть просто счетчик лайков у рецепта)
   - получить самый популярный рецепт по лайкам

9. Бот для подсчета калорий - Корабельников Никита
   - пользователь для которого считаем калории
   - меню
     - внести калории
     - вывести статистику по калориям
       - после нажатия выпадающие кнопки
         - посмотреть статистику за день
         - посмотреть статистику за неделю
         - посмотреть статистику за месяц
     - возможность изменить время ежедневного уведомления
   - ежедневное уведомление о статистике за день

10. Бот для тайм менеджмента
   - пользователь для которого мы считаем время
   - меню
     - вывести статистику по делам
       - после нажатия выпадающие кнопки
         - посмотреть статистику дел за день
         - посмотреть статистику дел за неделю
         - посмотреть статистику дел за месяц
     - начать дело
       - выбор дела с кнопкой старт таймера
       - отправка завершения о финише дела
     - добавить дело
   - ежедневное уведомление о статистике за день

11. Бот для документа-хранения 
   - пользователь для который будет управлять документами
   - меню
     - добавить документ 
       - после нажатия диалог с помощью которого можно добавить тип документа, его название
     - показать документы
       - первым на выбор идут типы документов (в разрезе типа может быть много объектов)
       - после нажатия на тип, сам выбор документа

12. Бот для мемов - Кульгавых Валентина
   - пользователь 
   - меню
     - добавить мем (фото + текст) 
       - после нажатия диалог с помощью которого можно добавить фото + текст
       - возможность добавить в общую корзину мемов и в личную
     - выбрать рандомный мем из общей
       - оценить лайк или дизлайк
     - выбрать рандомный мем из личной
     - посмотреть свой список мемов
     - выбрать самый популярный

13. Бот крестики-нолики 
   - пользователь 
   - меню
     - посмотреть статистику прошлый игр (результат и с кем) 
     - поиск игры 
       - после нажатия вы встаете в "очередь"
       - как нашелся второй игрок, то игра начинается
       - рандомно назначается первый ходящий, второй ходящий при этом так же получает игру, но с оговоркой, что он ждет
       - дальше ходим по очереди. Обработка ошибок, если походил тот кто не должен или тот кто должен, но не корректный выбор ячейки

14. Бот помошник в поездку - Назаров Виктор
   - пользователь
   - возможность создать вещи, которые нужно взять с собой
     - данные вещи можно привязать отдельное к длительности поездке, например 1д, 2д, 3д и тд
   - меню
     - проверка на сбор вещей
       - указывается длительность поездки
       - выскакивает меню с тем, что нужно взять
         - при нажатии этот объект считается взятый и уходит из списка
     - добавить предмет
     - добавить длительность (тут можно и переиграть как-то, возможно удобнее диапазонами)

15. Бот знакомства - Уварова Ангелина
   - пользователь
   - возможность создать анкету, загрузить туда фото и описание
   - при старте просит загрузить описание и анкету, только потом пускает в бота
   - меню
     - поиск знакомств
       - подбирает следующую анкету (пусть будет рандом из бд)
         - лайк или дизлайк
       - при нажатии на лайк, если вас тоже уже лайкнул этот пользователь, то присылается ссылка на телеграм в оба чата
