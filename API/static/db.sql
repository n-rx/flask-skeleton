CREATE TABLE IF NOT EXISTS public.api_data
(
    id serial NOT NULL,
    data character varying NOT NULL,
	CONSTRAINT api_data_pkey PRIMARY KEY (id)
);