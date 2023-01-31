--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 15.0

-- Started on 2022-11-07 18:02:43 GMT

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
-- TOC entry 216 (class 1259 OID 82071)
-- Name: article; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public.article (
    article_id smallint NOT NULL,
    article_owner_id smallint NOT NULL,
    article_blog_source_id smallint NOT NULL,
    article_ref_id text NOT NULL,
    article_title text NOT NULL,
    article_published boolean DEFAULT true NOT NULL,
    article_published_date date NOT NULL,
    article_url text NOT NULL,
    article_date_added date DEFAULT now() NOT NULL
);


ALTER TABLE public.article OWNER TO neil;

--
-- TOC entry 215 (class 1259 OID 82070)
-- Name: article_article_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.article_article_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_article_id_seq OWNER TO neil;

--
-- TOC entry 3656 (class 0 OID 0)
-- Dependencies: 215
-- Name: article_article_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.article_article_id_seq OWNED BY public.article.article_id;


--
-- TOC entry 222 (class 1259 OID 82123)
-- Name: article_comments; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public.article_comments (
    article_comments_id smallint NOT NULL,
    article_comments_article_id smallint NOT NULL,
    article_comments_change smallint NOT NULL,
    article_comments_date_added date DEFAULT now() NOT NULL
);


ALTER TABLE public.article_comments OWNER TO neil;

--
-- TOC entry 221 (class 1259 OID 82122)
-- Name: article_comments_article_comments_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.article_comments_article_comments_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_comments_article_comments_id_seq OWNER TO neil;

--
-- TOC entry 3657 (class 0 OID 0)
-- Dependencies: 221
-- Name: article_comments_article_comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.article_comments_article_comments_id_seq OWNED BY public.article_comments.article_comments_id;


--
-- TOC entry 220 (class 1259 OID 82110)
-- Name: article_likes; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public.article_likes (
    article_likes_id smallint NOT NULL,
    article_likes_article_id smallint NOT NULL,
    article_likes_change smallint NOT NULL,
    article_likes_date_added date DEFAULT now() NOT NULL
);


ALTER TABLE public.article_likes OWNER TO neil;

--
-- TOC entry 219 (class 1259 OID 82109)
-- Name: article_likes_article_likes_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.article_likes_article_likes_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_likes_article_likes_id_seq OWNER TO neil;

--
-- TOC entry 3658 (class 0 OID 0)
-- Dependencies: 219
-- Name: article_likes_article_likes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.article_likes_article_likes_id_seq OWNED BY public.article_likes.article_likes_id;


--
-- TOC entry 218 (class 1259 OID 82092)
-- Name: article_tag; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public.article_tag (
    article_tag_id smallint NOT NULL,
    article_tag_blog_tag_id smallint NOT NULL,
    article_tag_article_id smallint NOT NULL,
    article_tag_date_added date DEFAULT now() NOT NULL
);


ALTER TABLE public.article_tag OWNER TO neil;

--
-- TOC entry 217 (class 1259 OID 82091)
-- Name: article_tag_article_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.article_tag_article_tag_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_tag_article_tag_id_seq OWNER TO neil;

--
-- TOC entry 3659 (class 0 OID 0)
-- Dependencies: 217
-- Name: article_tag_article_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.article_tag_article_tag_id_seq OWNED BY public.article_tag.article_tag_id;


--
-- TOC entry 212 (class 1259 OID 82040)
-- Name: blog_source; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public.blog_source (
    blog_source_id smallint NOT NULL,
    blog_source_name text NOT NULL,
    blog_source_url text NOT NULL,
    blog_source_date_added date DEFAULT now() NOT NULL
);


ALTER TABLE public.blog_source OWNER TO neil;

--
-- TOC entry 211 (class 1259 OID 82039)
-- Name: blog_source_blog_source_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.blog_source_blog_source_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_source_blog_source_id_seq OWNER TO neil;

--
-- TOC entry 3660 (class 0 OID 0)
-- Dependencies: 211
-- Name: blog_source_blog_source_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.blog_source_blog_source_id_seq OWNED BY public.blog_source.blog_source_id;


--
-- TOC entry 214 (class 1259 OID 82050)
-- Name: blog_tag; Type: TABLE; Schema: public; Owner: neil
--

CREATE TABLE public.blog_tag (
    blog_tag_id smallint NOT NULL,
    blog_tag_name text NOT NULL,
    blog_tag_date_added date DEFAULT now() NOT NULL
);


ALTER TABLE public.blog_tag OWNER TO neil;

--
-- TOC entry 213 (class 1259 OID 82049)
-- Name: blog_tag_blog_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: neil
--

CREATE SEQUENCE public.blog_tag_blog_tag_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_tag_blog_tag_id_seq OWNER TO neil;

--
-- TOC entry 3661 (class 0 OID 0)
-- Dependencies: 213
-- Name: blog_tag_blog_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.blog_tag_blog_tag_id_seq OWNED BY public.blog_tag.blog_tag_id;


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
-- TOC entry 3662 (class 0 OID 0)
-- Dependencies: 209
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: neil
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public."user".user_id;


--
-- TOC entry 3468 (class 2604 OID 82074)
-- Name: article article_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article ALTER COLUMN article_id SET DEFAULT nextval('public.article_article_id_seq'::regclass);


--
-- TOC entry 3475 (class 2604 OID 82126)
-- Name: article_comments article_comments_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_comments ALTER COLUMN article_comments_id SET DEFAULT nextval('public.article_comments_article_comments_id_seq'::regclass);


--
-- TOC entry 3473 (class 2604 OID 82113)
-- Name: article_likes article_likes_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_likes ALTER COLUMN article_likes_id SET DEFAULT nextval('public.article_likes_article_likes_id_seq'::regclass);


--
-- TOC entry 3471 (class 2604 OID 82095)
-- Name: article_tag article_tag_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_tag ALTER COLUMN article_tag_id SET DEFAULT nextval('public.article_tag_article_tag_id_seq'::regclass);


--
-- TOC entry 3464 (class 2604 OID 82043)
-- Name: blog_source blog_source_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.blog_source ALTER COLUMN blog_source_id SET DEFAULT nextval('public.blog_source_blog_source_id_seq'::regclass);


--
-- TOC entry 3466 (class 2604 OID 82053)
-- Name: blog_tag blog_tag_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.blog_tag ALTER COLUMN blog_tag_id SET DEFAULT nextval('public.blog_tag_blog_tag_id_seq'::regclass);


--
-- TOC entry 3461 (class 2604 OID 82032)
-- Name: user user_id; Type: DEFAULT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public."user" ALTER COLUMN user_id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- TOC entry 3643 (class 0 OID 82071)
-- Dependencies: 216
-- Data for Name: article; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public.article (article_id, article_owner_id, article_blog_source_id, article_ref_id, article_title, article_published, article_published_date, article_url, article_date_added) FROM stdin;
\.


--
-- TOC entry 3649 (class 0 OID 82123)
-- Dependencies: 222
-- Data for Name: article_comments; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public.article_comments (article_comments_id, article_comments_article_id, article_comments_change, article_comments_date_added) FROM stdin;
\.


--
-- TOC entry 3647 (class 0 OID 82110)
-- Dependencies: 220
-- Data for Name: article_likes; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public.article_likes (article_likes_id, article_likes_article_id, article_likes_change, article_likes_date_added) FROM stdin;
\.


--
-- TOC entry 3645 (class 0 OID 82092)
-- Dependencies: 218
-- Data for Name: article_tag; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public.article_tag (article_tag_id, article_tag_blog_tag_id, article_tag_article_id, article_tag_date_added) FROM stdin;
\.


--
-- TOC entry 3639 (class 0 OID 82040)
-- Dependencies: 212
-- Data for Name: blog_source; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public.blog_source (blog_source_id, blog_source_name, blog_source_url, blog_source_date_added) FROM stdin;
\.


--
-- TOC entry 3641 (class 0 OID 82050)
-- Dependencies: 214
-- Data for Name: blog_tag; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public.blog_tag (blog_tag_id, blog_tag_name, blog_tag_date_added) FROM stdin;
\.


--
-- TOC entry 3637 (class 0 OID 82029)
-- Dependencies: 210
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: neil
--

COPY public."user" (user_id, user_email_adrs, user_first_name, user_last_name, user_password, user_locked, user_disabled, user_date_added) FROM stdin;
\.


--
-- TOC entry 3663 (class 0 OID 0)
-- Dependencies: 215
-- Name: article_article_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.article_article_id_seq', 1, false);


--
-- TOC entry 3664 (class 0 OID 0)
-- Dependencies: 221
-- Name: article_comments_article_comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.article_comments_article_comments_id_seq', 1, false);


--
-- TOC entry 3665 (class 0 OID 0)
-- Dependencies: 219
-- Name: article_likes_article_likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.article_likes_article_likes_id_seq', 1, false);


--
-- TOC entry 3666 (class 0 OID 0)
-- Dependencies: 217
-- Name: article_tag_article_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.article_tag_article_tag_id_seq', 1, false);


--
-- TOC entry 3667 (class 0 OID 0)
-- Dependencies: 211
-- Name: blog_source_blog_source_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.blog_source_blog_source_id_seq', 1, false);


--
-- TOC entry 3668 (class 0 OID 0)
-- Dependencies: 213
-- Name: blog_tag_blog_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.blog_tag_blog_tag_id_seq', 1, false);


--
-- TOC entry 3669 (class 0 OID 0)
-- Dependencies: 209
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neil
--

SELECT pg_catalog.setval('public.user_user_id_seq', 1, false);


--
-- TOC entry 3490 (class 2606 OID 82129)
-- Name: article_comments article_comments_pkey; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_comments
    ADD CONSTRAINT article_comments_pkey PRIMARY KEY (article_comments_id);


--
-- TOC entry 3488 (class 2606 OID 82116)
-- Name: article_likes article_likes_pkey; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_likes
    ADD CONSTRAINT article_likes_pkey PRIMARY KEY (article_likes_id);


--
-- TOC entry 3484 (class 2606 OID 82080)
-- Name: article article_pkey; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article
    ADD CONSTRAINT article_pkey PRIMARY KEY (article_id);


--
-- TOC entry 3486 (class 2606 OID 82098)
-- Name: article_tag article_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_tag
    ADD CONSTRAINT article_tag_pkey PRIMARY KEY (article_tag_article_id);


--
-- TOC entry 3480 (class 2606 OID 82048)
-- Name: blog_source blog_source_pkey; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.blog_source
    ADD CONSTRAINT blog_source_pkey PRIMARY KEY (blog_source_id);


--
-- TOC entry 3482 (class 2606 OID 82058)
-- Name: blog_tag blog_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.blog_tag
    ADD CONSTRAINT blog_tag_pkey PRIMARY KEY (blog_tag_id);


--
-- TOC entry 3478 (class 2606 OID 82038)
-- Name: user user_id; Type: CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_id PRIMARY KEY (user_id);


--
-- TOC entry 3496 (class 2606 OID 82130)
-- Name: article_comments article_comments_article_id; Type: FK CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_comments
    ADD CONSTRAINT article_comments_article_id FOREIGN KEY (article_comments_id) REFERENCES public.article(article_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3495 (class 2606 OID 82117)
-- Name: article_likes article_likes_article_id; Type: FK CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_likes
    ADD CONSTRAINT article_likes_article_id FOREIGN KEY (article_likes_article_id) REFERENCES public.article(article_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3493 (class 2606 OID 82104)
-- Name: article_tag article_tag_article_id; Type: FK CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_tag
    ADD CONSTRAINT article_tag_article_id FOREIGN KEY (article_tag_article_id) REFERENCES public.article(article_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3494 (class 2606 OID 82099)
-- Name: article_tag article_tag_blog_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article_tag
    ADD CONSTRAINT article_tag_blog_tag_id FOREIGN KEY (article_tag_blog_tag_id) REFERENCES public.blog_tag(blog_tag_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3491 (class 2606 OID 82081)
-- Name: article blog_source_id; Type: FK CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article
    ADD CONSTRAINT blog_source_id FOREIGN KEY (article_blog_source_id) REFERENCES public.blog_source(blog_source_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3492 (class 2606 OID 82086)
-- Name: article owner_id; Type: FK CONSTRAINT; Schema: public; Owner: neil
--

ALTER TABLE ONLY public.article
    ADD CONSTRAINT owner_id FOREIGN KEY (article_owner_id) REFERENCES public."user"(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3655 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2022-11-07 18:02:43 GMT

--
-- PostgreSQL database dump complete
--

