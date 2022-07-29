## Набор видеоуроков от Марка Ричардса

[Software Architecture Monday](https://www.developertoarchitect.com/lessons/)

1. [**Request/Reply Pattern**](https://www.youtube.com/watch?v=3bxAm3XIFmk)

Для имитации request/reply используем две разных очереди сообщений. Сообщения можно связывать по CorrelationId (Id моего сообщения превращается в CorrelationId ответа) или через временные очереди (очереди только для одного сообщения, вероятно, будет огромный overhead на создание/удаление очередей).

2. [**Kafka vs Message Broker**](https://www.youtube.com/watch?v=lwMjjTT1Q-Q)

Kafka оптимизирована под постоянный поток простых сообщений key/value, с нагрузкой до 1M/s и только под паттерн Publisher/Subscriber. RabbitMQ удобнее для транзакционных сообщений (в том числе большого размера), нагрузка до 10K/s с поддержкой трех разных паттернов (point-2-point, publisher-subscriber и exchange/routing - распределение сообщения по разным очередям)

3. [**Soft skills: Gaining Technical Breadth**](https://www.youtube.com/watch?v=vRplv975ce0)

Для архитектора важна не только глубина знаний ("знаю, что знаю"), но и ширина знаний ("знаю, что знаю + знаю, что не знаю"). Чтобы повышать ширину знаний, нужно больше читать о новых событиях в мире, например, InfoQueue, Technical Radar или DZone.

4. [**Microservices: Distributed Logging**](https://www.youtube.com/watch?v=S511BgBs_3E)

Микросервисы отличаются сложностью отладки, поэтому нужны хорошие логи. Выбрать инструмент для сбора логов (splunk, logstash, kafka и другие) - половина дела. Полезные приёмы:
- "консолидация логов" - объединение логов от разных микросервисов в один лог
- "идентификатор контекста запроса"
- "иерархия идентификаторов" (если есть userId - используем его, если нет, то requestId, если нет, то applicationId и т.д.), отличное место для извлечения id context - api gateway
- консистентность контекста - принимать его как входной параметр по всех запросах
- собственный wrapper для логов - это хорошо

5. [**Microservices: Reducing Staging Iterations**](https://www.youtube.com/watch?v=dkLriZLXpU8)

При разделении монолита на микросервисы, по возможности, изменение архитектуры стоит вести параллельно с разворачиванием инфраструктуры и CI/CD процессов (силами devops)