CREATE TABLE dim_location
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_country
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_state
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_country_id INTEGER,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_district
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_state_id INTEGER,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_county
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_district_id INTEGER,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_postal_code
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_county_id INTEGER,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_port
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_postal_code_id INTEGER,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_gps
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE fact_log
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	caller_id INTEGER,
	txn_type INTEGER,
	flags INTEGER
);

CREATE INDEX idx_fact_log ON fact_log(dim_gps_id);

CREATE TABLE fact_ro
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	concern VARCHAR(255),
	report_time TIMESTAMP,
	vessel_id INTEGER,
	penalty REAL
);

CREATE INDEX idx_fact_ro ON fact_ro(dim_gps_id);

CREATE TABLE fact_score_hazardous_transport
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel INTEGER,
	penalty REAL
);

CREATE INDEX idx_fact_score_hazardous_transport ON fact_score_hazardous_transport(dim_gps_id);

CREATE TABLE fact_score_berthing_risk
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	penalty REAL
);

CREATE INDEX idx_fact_score_berthing_risk ON fact_score_berthing_risk(dim_gps_id);

