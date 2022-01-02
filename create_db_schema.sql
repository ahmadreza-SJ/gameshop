create table db_country
(
    id   integer      not null
        primary key autoincrement,
    name varchar(100) not null
);

create table db_creator
(
    id         integer      not null
        primary key autoincrement,
    username   varchar(100) not null,
    password   varchar(100) not null,
    email      varchar(254) not null,
    founded_at date         not null,
    created_at datetime     not null,
    country_id integer      not null
        references db_country
            deferrable initially deferred
);

create table db_critic
(
    id         integer      not null
        primary key autoincrement,
    username   varchar(100) not null,
    password   varchar(100) not null,
    email      varchar(254) not null,
    created_at datetime     not null
);

create table db_genre
(
    id   integer      not null
        primary key autoincrement,
    name varchar(100) not null
);

create table db_game
(
    id           integer       not null
        primary key autoincrement,
    name         varchar(100)  not null,
    description  varchar(1000) not null,
    price        integer       not null,
    release_date date          not null,
    created_at   datetime      not null,
    image        varchar(100)  not null,
    creator_id   integer       not null
        references db_creator
            deferrable initially deferred,
    genre_id     integer       not null
        references db_genre
            deferrable initially deferred
);

create table db_criticism
(
    id         integer       not null
        primary key autoincrement,
    title      varchar(100)  not null,
    text       varchar(5000) not null,
    score      integer       not null,
    image      varchar(100)  not null,
    created_at datetime      not null,
    critic_id  integer       not null
        references db_critic
            deferrable initially deferred,
    game_id    integer       not null
        references db_game
            deferrable initially deferred
);

create table db_user
(
    id         integer      not null
        primary key autoincrement,
    username   varchar(100) not null,
    password   varchar(100) not null,
    email      varchar(254) not null,
    created_at datetime     not null
);

create table db_comment
(
    id         integer      not null
        primary key autoincrement,
    text       varchar(500) not null,
    created_at datetime     not null,
    game_id    integer      not null
        references db_game
            deferrable initially deferred,
    user_id    integer      not null
        references db_user
            deferrable initially deferred
);

create table db_receipt
(
    id         integer  not null
        primary key autoincrement,
    paid_cost  integer  not null,
    created_at datetime not null,
    game_id    integer  not null
        references db_game
            deferrable initially deferred,
    user_id    integer  not null
        references db_user
            deferrable initially deferred
);

create table django_migrations
(
    id      integer      not null
        primary key autoincrement,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null
);

create table sqlite_master
(
    type     text,
    name     text,
    tbl_name text,
    rootpage int,
    sql      text
);

create table sqlite_sequence
(
    name,
    seq
);
