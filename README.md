# Программа "Практический анализ данных и машинное обучение"

## Основные темы программы

- **Адаптационные математические курсы**
- Математический анализ
- Линейная алгебра
- Теория вероятностей
- Математическая статистика
- Методы оптимизации
- **Основы машинного обучения**
- Обучение с учителем. Задачи классификации и регрессии
- Оценка качества алгоритмов машинного обучения
- Обучение без учителя и задача кластеризации
- Поиск выбросов и аномалий в данных
- Индивидуальный проект по анализу данных
  - Ваши личные либо общедоступные данные и задачи
  - 1.5 месяца работы по четкому плану под руководством преподавателей
  - Презентации и обсуждение проектов
- **Продвинутые методы машинного обучения**
- Ансамбли алгоритмов классификации и регрессии. Градиентный бустинг
- Смешивание моделей классификации и регрессии. Стекинг моделей классификации и регрессии
- Соревнования по анализу данных, обзор решений
- **Поиск зависимостей в данных**
- Поиск часто покупаемых товаров (Frequent Itemset Mining). Алгоритм Apriori. Алгоритм FP-growth
- Признаковые зависимости в данных. Импликации и ассоциативные правила (Association Rules)
- Компактное представление закономерностей. Замкнутые и максимальные частые множества. Алгоритмы GenMax и Charm (или Close-by-One)
- Анализ частых последовательностей. Примеры из демографии. Библиотека SPMF
- Меры качества закономерностей. Корреляция как мера связи признаков. Статистическая оценка качества
- **Анализ социальных сетей**
- Введение в анализ социальных сетей. Модели формирования социальных сетей
- Анализ структуры социальных связей. Каскады в сетях
- Сообщества в социальных сетях
- Распространение информации в социальных сетях
- **Автоматическая обработка текстов**
- Введение в анализ текстов. Частотный анализ текстов
- Морфологический анализ. Выделение ключевых слов и словосочетаний
- Выявление скрытых тем. Введение в корпусную лингвистику
- Синтаксический анализ. Визуализация текстов
- **Масштабируемое машинное обучение и анализ больших данных с Apache Spark**
- Парадигма MapReduce в машинном обучении
- Онлайн-обучение
- Концепции вычислений в памяти и устойчивых распределенных наборов данных
- Введение в Apache Spark для анализа данных
- Машинное обучение с библиотекой MLLib Apache Spark
- **Нейронные сети и глубинное обучение**
- Введение в нейронные сети
- Обучение сетей прямого распространения
- Сверточные нейронные сети
- Сети прямого распространения в анализе текстов
- Рекуррентные нейронные сети
- Модели сопоставления последовательностей (sequence to sequence)

## Преподаватели

#### Илья Щуров 
Выпускник механико-математического факультета МГУ, кандидат физико-математических наук, доцент кафедры высшей математики НИУ ВШЭ. Лауреат конкурса молодых математиков фонда «Династия». Разработал и прочитал ряд курсов по программированию, в том числе обещуниверситетский факультатив «Программирование на языке Python для сбора и обработки данных». 

#### Юрий Кашницкий
Преподаватель факультета компьютерных наук НИУ ВШЭ, научный сотрудник  Международной научно-учебной лаборатории интеллектуальных систем и структурного анализа.  Имеет публикации, представленные на семинарах топовых конференций по искусственному интеллекту (IJCAI и ECAI) и машинному обучению (ECML/PKDD). Преподаватель языка Python и машинного обучения в MLClass. В прошлом — разработчик Hadoop, бизнес-аналитик и Java-программист РДТЕХ.

#### Дмитрий Игнатов
Кандидат технических наук, преподаватель факультета компьютерных наук НИУ ВШЭ, доцент Департамента анализа данных и искусственного интеллекта, научный сотрудник Международной научно-учебной лаборатории интеллектуальных систем и структурного анализа.  Проходил обучение по PhD программе в Техническом университете Дрездена (Германия) в рамках гранта DAAD.

#### София Докука 
Кандидат социологических наук, научный сотрудник Института институциональных исследований НИУ ВШЭ. Преподает курсы по компьютерному моделированию в социологии, анализу социальных сетей и динамике социальных сетей. Работала в университете Гронингена (Нидерланды) в рамках программы международной мобильности Erasmus Mundus.

#### Екатерина Черняк 
Старший преподаватель Департамента анализа данных и искусственного интеллекта факультета компьютерных наук, научный сотрудник Международной научно-учебной лаборатории анализа и выбора решений.

#### Вячеслав Дубров 
Кандидат технических наук, аналитик больших массивов данных в IQmen - Business Intelligence. Проходил обучение по PhD программе в Техническом университете Ильменау (Германия) в рамках гранта DAAD и научные стажировки в ТУ Брауншвайг и ТУ Дортмунд. Ранее — разработчик систем машинного обучения в сфере сетевой безопасности (ЗАО "Перспективный мониторинг") и младший научный сотрудник ЮРГПУ(НПИ) имени М.И.Платова.

#### Святослав Елизаров 
Выпускник факультета компьютерных наук. Data Scientist и программист в alterra.ai

# Инструкция по установке Docker-контейнера
В курсе используется сборка библиотек Anaconda, тетрадки Jupyter, Apache Spark, Xgboost и некоторые другие библиотеки. Все это можно не устанавливать, а использовать Docker-контейнер (требования: около 4 Гб места на диске, 4 Гб RAM). [Введение](https://habrahabr.ru/post/310460/) в Docker. Рекомендуется тем, кто использует Windows, c \*NIX проще самостоятельно установить необходимое (см. Dockerfile). 

Инструкция:
- скачать данный репозиторий
- на Windows скорее всего придется [включить](http://www.sysprobs.com/disable-enable-virtualization-technology-bios) в BIOS виртуализацию, если раньше не использовали виртуальные машины или Docker
- установить [Docker](https://docs.docker.com/engine/installation/)
- установить [Docker Compose](https://docs.docker.com/compose/install/)
- перейти в командной строке/терминале в скачанный каталог HSE_BigML_AddProfEduc
- убедиться, что порт 8888 не занят серверами Jupyter
- выполнить docker-compose up. Это может занять продолжительное время
- открыть localhost:8888

Контейнеры Docker как правило занимают много места на диске.
- *docker ps* – посмотреть весь список контейнеров
- *docker stop $(docker ps -a -q)* – остановить все контейнеры
- *docker rm $(docker ps -a -q)* – удалить все контейнеры



