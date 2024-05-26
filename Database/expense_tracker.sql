CREATE DATABASE expense_tracker_db_2
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


CREATE TABLE IF NOT EXISTS public.users
(
    user_id integer NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
    username character varying(50) COLLATE pg_catalog."default" NOT NULL,
    password character varying(50) COLLATE pg_catalog."default" NOT NULL,
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    balance numeric(10,2) DEFAULT 0.0,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.categories
(
    category_id integer NOT NULL DEFAULT nextval('categories_category_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT categories_pkey PRIMARY KEY (category_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.categories
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS public.expenses
(
    expense_id integer NOT NULL DEFAULT nextval('expenses_expense_id_seq'::regclass),
    user_id integer,
    category_id integer,
    amount numeric(10,2) NOT NULL,
    date date NOT NULL,
    description text COLLATE pg_catalog."default",
    payment_method character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT expenses_pkey PRIMARY KEY (expense_id),
    CONSTRAINT expenses_category_id_fkey FOREIGN KEY (category_id)
        REFERENCES public.categories (category_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT expenses_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.expenses
    OWNER to postgres;