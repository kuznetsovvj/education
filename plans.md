# Материалы для изучения

Актуальная версия плана: 2

Дата составления: февраль 2023 года

В связи со сменой работы материалы по управлению командами, стратегическому управлению технологическими предприятиями (то есть задачами CTO) снижаются в приоритете. Повышаются в приоритете материалы по архитектуре приложений и систем. Материалы по разработке и практика в OpenSource откладываются на более позднее время.

## Актуальное

### Архитектура приложений

- [X] Уроки "Архитектурный понедельник" Марка Ричардса [Конспекты](https://github.com/kuznetsovvj/education/blob/main/Software%20Architecture%20Monday.md)

### Видео и выступления по теме "Архитектура"

Плейлисты с конференций. Просматривать все подряд не рационально и нет времени, задача: пройти по всему плейлисту, наиболее ценные видео или посмотреть сразу же или добавить в список отдельно, после этого отметить плейлист как "пройденный".

- [X] [HighLoad Foundation 2022](https://www.youtube.com/playlist?list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao)
- [ ] [HighLoad 2022](https://www.youtube.com/playlist?list=PLH-XmS0lSi_z45jTyyS4ZebvZnNWbhO4K)
- [ ] [TeamLeadConf 2022](https://www.youtube.com/playlist?list=PL_L_HiHe5k_2sEh1wpJUQoEoTDjqralLV)
- [ ] [DevOpsConf 2022](https://www.youtube.com/playlist?list=PLrFmwYyxJyVMCJzIwqiAQx9-p8UGi4Kci)
- [ ] [TestDrivenConf 2022](https://www.youtube.com/playlist?list=PL3K8pTggFkO4jyuJZDMF0EkL2n7hWeV7G)
- [ ] [CodeFest 12 2022](https://www.youtube.com/playlist?list=PL8761XQAJnra2OI2zSXwiymJrCDqehhxG)
- [ ] [TechLeadConf 2021](https://www.youtube.com/playlist?list=PLH-XmS0lSi_xSkWvzkT0C5JkwP9mgcAP-)
- [ ] [HighLoad 2021 Весна](https://www.youtube.com/playlist?list=PLH-XmS0lSi_xQtVkWsUMSVUScK_3G_LUP)
- [ ] [TeamLeadConf 2021](https://www.youtube.com/playlist?list=PL_L_HiHe5k_3-tsj1bGSsHf4MVaEFaelB)
- [ ] [TechLead Podlodka Crew 2](https://www.youtube.com/playlist?list=PLNSmyatBJig4nv7SPXWxvroj7Rw4vCpWc)
- [ ] [SECR 2019](https://www.youtube.com/playlist?list=PLNcc67qYVXQ2S80h02rN8ZCeUX_lzyVhn)
- [ ] [DDDevotion](https://www.youtube.com/@DDDevotion/videos)
- [ ] [DotNetRu](https://www.youtube.com/@DotNetRu)

Видео россыпью:

| Просмотр | Видео | Описание |
| --- | --- | --- |
| | [Александр Коптин - Автоматизированная сортировка](https://www.youtube.com/watch?v=gMCz7xzLdEk&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao) | Как работает автоматическая сортировка почтовых отправления в масштабе страны |
| | [Алексей Мерсон - Идеальный шторм: когда готовил систему к росту нагрузки, но не успел](https://www.youtube.com/watch?v=MFPpaMIgcCU&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao&index=39) | История о том, как мы воевали с инцидентами под растущей нагрузкой и какие выводы сделали. Действующие лица: высоконагруженная система из монолита и микросервисов, кластер posgtres, кластер kubernetes, несколько команд разработки и тестирования, менеджеры в ассортименте |
| | [Андрей Аксенов - Как выжать 1 000 000 RPS](https://www.youtube.com/watch?v=UyRBouT6vZQ&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao) | Как мы в порядке эксперимента выжимали 1 миллион запросов в секунду из 1 физического сервера и СУБД, никогда при этом НЕ рассчитанной на именно такой workload (спойлер: СУБД всё ещё Сфинкс) |
| | [Владимир Озеров, Алексей Гончарук - Архитектура высокопроизводительных распределенных SQL-движков](https://www.youtube.com/watch?v=JJ5wGKo_F74&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao&index=74) | Распределенные SQL-движки должны эффективно обрабатывать данные, расположенные на нескольких серверах. В докладе Владимир Озеров и Алексей Гончарук расскажут, какие подходы используют распределенные SQL-системы для увеличения производительности запросов |
| | [Дмитрий Пичугин, Роман Митасов - Как мы в Тинькофф Data Catalog создавали](https://www.youtube.com/watch?v=jMATH538qsA&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao&index=92) | В чем главная задача аналитика? Думать головой и принимать решения. Правильные решения можно принять только при наличии нужных данных. А как найти данные в большой компании? Традиционно мы решали проблему с помощью ручного ведения документации в Confluence, но с ростом объема данных этот подход становился все менее и менее эффективным. Проблема встала ребром, мы поняли, что пришло время что-то менять, и решили внедрять у себя Data Catalog |
| | [Алексей Афошин - ZFS как архитектурное решение для резервного копирования хостинга](https://www.youtube.com/watch?v=4qeHKn5pTWo&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao&index=113) | Этот доклад может быть интересен тем, кто занимается построением серверной инфраструктуры, планирует делать бэкапы и заботится о бесперебойной работе систем |
| | [Сергей Баранов - Многоликий DDD](https://www.youtube.com/watch?v=2WHarUW0PjI) | |
| | [Дмитрий Цветцих - Аспектно-ориентированное программирование на .NET](https://www.youtube.com/watch?v=XVJvsqTPeYY) | |
| | [Андрей Зорин - GraphQL: нестандартная реализация потоков данных](https://www.youtube.com/watch?v=L0caEdAls9g) | |
| | [Дмитрий Нестерук - Черная магия паттерна "посетитель"](https://www.youtube.com/watch?v=H7TjVnpXA5o) | |
| | [Дмитрий Цветцих - Модульный монолит](https://www.youtube.com/watch?v=MBZLYQ84ieY) | |
| | [Станислав Сидристый - Гибридная архитектура: разделяемый на модули монолит](https://conf.ontico.ru/videos/4536828) | |
| | [Максим Юнусов - Свобода принятия архитектурного решения](https://www.youtube.com/watch?v=8ueXk66NozU) | |

### Книги по теме "Архитектура программного обеспечения"

**Tier1:**

- [ ] Mark Richards. Fundamentals of Sotfware Architecute
- [ ] John Ousterhout. A Philosophy of Software Design
- [ ] Martin Fowler. Patterns of Enterprise Application Architecture
- [ ] Bruce Cameron, Edward Crawley, Daniel Selva. Systems Architecture, Strategy and Product Development for Complex System
- [ ] Len Bass, Paul Clements, Rick Kazman. Software Architecte in Practice
- [ ] Вон Вернон. Реализация методов предметно-ориентированного программирования
- [ ] Дин Леффингуэлл. Принципы работы с требованиями к программному обеспечению
- [ ] Эрик Эванс. Предметно-ориентированное проектирование (*перечитать еще раз с вниманием к деталям*)

**Tier2:**

- [ ] Орам, Уилсон. Идеальная разработка ПО
- [ ] Mauricio Aniche. Effecting Software Testing
- [ ] Милетт, Тьюн. Предметно-ориентированное проектирование
- [ ] Физерс. Эффективная работа с унаследованным кодом
- [ ] Eppinger, Browning. Design
- [ ] Abbruzzese, Baptista. Software Architecture with C# 9 and .NET 5
- [ ] Michal Nygard. Release It! Design and Deploy Production-Ready Software
- [ ] [Microsoft: Cloud Design Patterns](https://docs.microsoft.com/en-us/azure/architecture/patterns/)
- [ ] [Microsoft: dotnet-architecture books](https://github.com/dotnet-architecture/eShopOnContainers/wiki/eBooks)
- [ ] ISO IEC IEEE 42020 Architecture processes
- [ ] ISO 15288-2015 System life cycle processes
- [X] ГОСТ 57100 (ISO 42010) Описание архитектуры
- [ ] ГОСТ 27193-2016 Процессы жизненного цикла системы
- [ ] DAMA-DMBoK. Свод знаний по управлению данными

**Tier3:**

- [ ] Framework for Cyber-Physical Systems. Release 1.0

## Выполненное

### Видео

- [X] [Григорий Кошелев - Kafka: от теории к практике](https://www.youtube.com/watch?v=ghKnX5fuW5s)
- [x] [Андрей Парамонов - gRPC](https://www.youtube.com/watch?v=y5nLqQPSPBI)
- [X] [Денис Тарасов, Дмитрий Афанасьев - Атакуем цепочку поставнок](https://www.youtube.com/watch?v=v2C_Nu-y_TQ)
- [X] [Сергей Васильев - Обработка XML-файлов как угроза безопасности](https://www.youtube.com/watch?v=7L21g7eedtA)
- [X] [Огородников, Просин, Хабаров - Аутентификация на платформе ASP.NET Core](https://www.youtube.com/watch?v=hFwIAPG6V4I)
- [X] [Станислав Флусов - Миграция с MS SQL на PostgreSQL](https://www.youtube.com/watch?v=3DcCX89Mz78)
- [X] [Евгений Пешков - Клиентский HTTP в .NET: от WebRequest до SocketHttpHandler](https://www.youtube.com/watch?v=YvczsQP1SLM)
- [X] [Максим Лапшин - История онлайн видео](https://conf.ontico.ru/videos/4536776)
- [X] [Александр Кривощеков - Паттерны отказоустойчивой архитектуры](https://www.youtube.com/watch?v=WWTq-tbZwUE&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao&index=6)
- [X] [Александр Тоболь - VK Видео: архитектура крупнейшей видеоплатформы](https://www.youtube.com/watch?v=8ICxQ-UPVn0&list=PLH-XmS0lSi_zCq4H_OZrXD509X23xwvao&index=3)
- [X] [Артем Рудневский - Exactly-once в микросервисной среде](https://www.youtube.com/watch?v=SKR1FK6qkZk)
- [X] [Александр Поломодов - Как подготовиться и пройти System Design интервью](https://www.youtube.com/watch?v=jUbOm0B-eKQ)
- [X] [Александр Поломодов - "Канал. Продукт. Платформа". Эволюция подходов к развитию мобильного банка Тинькофф](https://conf.ontico.ru/videos/4536831)
- [X] [Алексей Обровец - Питательная среда для качественной внутренней коммуникации](https://www.youtube.com/watch?v=DxgFO9E1Hn8&list=PL_L_HiHe5k_2sEh1wpJUQoEoTDjqralLV&index=4)

### Книги

- [X] Джон Смит. Entiry Framework Core в действии
- [X] Ибрам, Хасс. Паттерны Kubernetes.
- [x] "Делай как в Google. Разработка программного обеспечения" [Обзор](https://vk.com/miyau?w=wall602216_2278%2Fall)
- [X] Роджер Ловенстайн. Когда гений терпит поражение [Обзор](https://vk.com/miyau?w=wall602216_2280%2Fall)

### Прочее

- [X] Участие в open-source проектах [GlazeWM](https://github.com/lars-berger/GlazeWM/pulls?q=is%3Apr+author%3Akuznetsovvj) [efcore](https://github.com/dotnet/efcore/pulls?q=is%3Apr+author%3Akuznetsovvj)
- [X] Регулярный разбор алгоритмических задач leetcode и участие в турнирах на codeforces [codeforces](https://codeforces.com/profile/minm) [leetcode](https://leetcode.com/vjkuznetsov/)

## Отложенное

### Книги по разработке

- [ ] Jopesh Albahari. C# 10 in a Nutshell

### Книги по управлению командой

- [ ] Александр Фридман. Пожиратели времени
- [ ] Лалу. Открывая организации будущего
- [ ] Доши, МакГрегор. Заряженные на результат. Культура высокой эффективности на практике
- [ ] Пейл. Реальная стратегия. Как планировать только то, что можно воплотить
- [ ] Рыбаков, Пайвина. Развитие живой компании. Практикум по организационной терапии в гештальт-подходе
- [ ] Ицхак Адизес. Развитие лидеров

### Видео по теме "Процесс управления разработкой"

- [ ] [Даниил Разумов - Общий флоу разработки в Ozon. Как сделать жизнь разработчиков проще?](https://conf.ontico.ru/videos/4536853)
- [ ] [Даниил Подольский - Под красным флагом: как инженер может понять, что в проекте происходит что-то не то](https://conf.ontico.ru/videos/4536805)
- [ ] [Дмитрий Пичугин, Роман Митасов - Как мы в Тинькофф Data Catalog создавали](https://conf.ontico.ru/videos/4380330)
- [ ] [Александр Поломодов - Рост команды на порядок](https://www.youtube.com/watch?v=UUnM8_-PXt0)

### Управление проектами

Основная цель: глубокое понимание принципов PMBoK и гибких методологий разработки

- [ ] SAFe 5.0 Distilled
- [ ] PMI PMBoK Guide 7th edition (сокращенный agile PMBoK)
- [ ] PMI PMBoK Guide 6th edition (классический PMBoK)
- [ ] BPM CBoK. Свод знаний по управлению бизнес-процессами

- [ ] Шервуд. Системное мышление для руководителей. Практика решения бизнес-проблем
- [ ] Получить сертификат Professional Scrum Master I

### Программирование (разное)

- [ ] Ахо, Лам, Сети, Ульман. Компиляторы - принципы, технологии, инструментарий
- [ ] Харрис. Цифровая схемотехника и архитектура компьютера
- [ ] Харрис. Цифровая схемотехника и архитектура компьютера (ARM)

### Неклассифицируемое

- [ ] [Александр Макаров - Теория программирования: пакетный принцип](https://www.youtube.com/watch?v=esGaBY-LVlo)
- [ ] [Игорь Беспальчук - Язык на пути к DevArch](https://www.youtube.com/watch?v=3QvzlFIuepQ)
- [ ] Кузин. На линии огня (публичные выступления)
- [ ] Шахиджанян. Ораторское искусство для начинающих

## Отмененное

- [ ] ~~Разработка open-source .NET библиотеки для фреймворка Twirp~~ # Twirp не актуален на текущей работе, занимаюсь разработкой общей библиотек для текущего работодателя.
- [ ] ~~Дэвид Льюис. Управление стрессом. Как найти дополнительные 10 часов в неделю~~ # Книга не заинтересовала
- [ ] ~~Шонесси, Голдинг. 12 шагов к гибкому бизнесу~~ # Книга не заинтересовала
- [ ] ~~Джеффри Лайкер. Дао Toyota. 14 принципов менеджмента ведущий компании мира~~
