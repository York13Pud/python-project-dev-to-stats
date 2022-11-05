--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 15.0

-- Started on 2022-11-05 16:06:28 GMT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 82029)
-- Name: user; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public."user" (
    user_id smallint NOT NULL,
    user_email_adrs text NOT NULL,
    user_first_name text NOT NULL,
    user_last_name text NOT NULL,
    user_password text NOT NULL,
    user_locked boolean,
    user_disabled boolean DEFAULT false NOT NULL,
    user_date_added date DEFAULT now()
);


ALTER TABLE public."user" OWNER TO neil;

--
-- TOC entry 209 (class 1259 OID 82028)
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.user_user_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO neil;

--
-- TOC entry 3583 (class 0 OID 0)
-- Dependencies: 209
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public."user".user_id;


--
-- TOC entry 3431 (class 2604 OID 82032)
-- Name: user user_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public."user" ALTER COLUMN user_id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- TOC entry 3576 (class 0 OID 82029)
-- Dependencies: 210
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public."user" (user_id, user_email_adrs, user_first_name, user_last_name, user_password, user_locked, user_disabled, user_date_added) FROM stdin;
\.


--
-- TOC entry 3584 (class 0 OID 0)
-- Dependencies: 209
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.user_user_id_seq', 1, false);


--
-- TOC entry 3435 (class 2606 OID 82038)
-- Name: user user_id; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_id PRIMARY KEY (user_id);


--
-- TOC entry 3582 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2022-11-05 16:06:28 GMT

--
-- PostgreSQL database dump complete
--

