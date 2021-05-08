
Пример RESTful-проекта - веб-приложение генерации шпаргалок и конспектов по университетским дисциплинам, которое позволяет просматривать и редактировать список дисциплин, тем и материалов занятий. Пользователь может добавлять новые материалы, курсы, преподавателей и инициировать создание удобных кратких шпаргалок: при загрузке PDF или PPTX-файла программа автоматически извлекает из него текстовыей контент и добавляет в базу.

Серверная часть приложения базируется на Python-микрофреймворке Flask-restx и написана в соответствии с его рекомендациями. Структура проекта:

    - файл manage.py, в котором прописан код управления Flask-приложением;
    - файл api.py, в котором прописан код настройки и подготовки REST-API Flask-приложения;
    - файл config.py, в котором хранится конфигурация проекта (прописаны значения глобальных переменных);
    - директория models, в которой содержатся py-файлы с моделями данных предметной области, синхронизируемые с базой данных SQLite;
    - директория controllers, в которой хранятся py-файлы с контроллерами – обработчиками http-запросов (в формате JSON) от клиентов в виде т.н. Flask-ресурсов;
    - директория services, в которой хранятся py-файлы с классами-сервисами для реализации CRUD-операций с моделями приложения;
    - директория uploads, в которой хранятся загруженные файлы материалов лекций в формате PDF и PPTX, и доступные для скачивания на клиентах.

Библиотека flask-script позволяет писать декораторы @manager.Command для варьирования режимов запуска скрипта из командной строки:
    
    > python manage.py run – запуск сервера приложения
    
    > python manage.py seed – инициализация базы данных (ее заполнение первоначальными данными)

    > python manage.py migrate – миграции базы данных

Модели хранятся в директории models:

    - Teacher
    - Degree
    - Position
    - Course
    - Topic
    - Synopsis

Клиентская часть приложения написана с использованием Angular и MaterialDesign. Состоит из компонентов, моделей и сервисов. Все компоненты приведены ниже:

```ts

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,        // заголовок сайта с навигацией
    CourselistComponent,    // список курсов (карточек)
    CourseComponent,        // курс
    TopiclistComponent,     // список тем   
    SynopsisComponent,      // конспект/шпаргалка
    TeacherlistComponent,   // псисок преподавателей
    TopicComponent,         // тема
    CourseDialog,           // окно редактирования курса
    TeacherDialog           // окно редактирования преподавателя
  ],
  entryComponents: [
    CourseDialog,
    TeacherDialog
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatButtonModule,        // Модули MaterialDesign
    MatCardModule,
    MatIconModule,
    MatExpansionModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatExpansionModule,
    MatToolbarModule,
    MatSelectModule,
    MatTableModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule
)

```

Модели принципиально аналогичны моделям серверной части. Сервисы предоставляют CRUD-методы.
