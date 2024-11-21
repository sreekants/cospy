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
	dim_port_id INTEGER,
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
	vessel_id INTEGER,
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

CREATE TABLE fact_colreg_r01
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r01 ON fact_colreg_r01(dim_gps_id);

CREATE TABLE fact_colreg_r02
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r02 ON fact_colreg_r02(dim_gps_id);

CREATE TABLE fact_colreg_r03
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r03 ON fact_colreg_r03(dim_gps_id);

CREATE TABLE fact_colreg_r04
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r04 ON fact_colreg_r04(dim_gps_id);

CREATE TABLE fact_colreg_r05
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r05 ON fact_colreg_r05(dim_gps_id);

CREATE TABLE fact_colreg_r06
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r06 ON fact_colreg_r06(dim_gps_id);

CREATE TABLE fact_colreg_r07
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r07 ON fact_colreg_r07(dim_gps_id);

CREATE TABLE fact_colreg_r08
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r08 ON fact_colreg_r08(dim_gps_id);

CREATE TABLE fact_colreg_r09
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r09 ON fact_colreg_r09(dim_gps_id);

CREATE TABLE fact_colreg_r10
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r10 ON fact_colreg_r10(dim_gps_id);

CREATE TABLE fact_colreg_r11
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r11 ON fact_colreg_r11(dim_gps_id);

CREATE TABLE fact_colreg_r12
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r12 ON fact_colreg_r12(dim_gps_id);

CREATE TABLE fact_colreg_r13
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r13 ON fact_colreg_r13(dim_gps_id);

CREATE TABLE fact_colreg_r14
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r14 ON fact_colreg_r14(dim_gps_id);

CREATE TABLE fact_colreg_r15
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r15 ON fact_colreg_r15(dim_gps_id);

CREATE TABLE fact_colreg_r16
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r16 ON fact_colreg_r16(dim_gps_id);

CREATE TABLE fact_colreg_r17
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r17 ON fact_colreg_r17(dim_gps_id);

CREATE TABLE fact_colreg_r18
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r18 ON fact_colreg_r18(dim_gps_id);

CREATE TABLE fact_colreg_r19
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r19 ON fact_colreg_r19(dim_gps_id);

CREATE TABLE fact_colreg_r20
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r20 ON fact_colreg_r20(dim_gps_id);

CREATE TABLE fact_colreg_r21
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r21 ON fact_colreg_r21(dim_gps_id);

CREATE TABLE fact_colreg_r22
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r22 ON fact_colreg_r22(dim_gps_id);

CREATE TABLE fact_colreg_r23
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r23 ON fact_colreg_r23(dim_gps_id);

CREATE TABLE fact_colreg_r24
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r24 ON fact_colreg_r24(dim_gps_id);

CREATE TABLE fact_colreg_r25
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r25 ON fact_colreg_r25(dim_gps_id);

CREATE TABLE fact_colreg_r26
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r26 ON fact_colreg_r26(dim_gps_id);

CREATE TABLE fact_colreg_r27
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r27 ON fact_colreg_r27(dim_gps_id);

CREATE TABLE fact_colreg_r28
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r28 ON fact_colreg_r28(dim_gps_id);

CREATE TABLE fact_colreg_r29
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r29 ON fact_colreg_r29(dim_gps_id);

CREATE TABLE fact_colreg_r30
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r30 ON fact_colreg_r30(dim_gps_id);

CREATE TABLE fact_colreg_r31
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r31 ON fact_colreg_r31(dim_gps_id);

CREATE TABLE fact_colreg_r32
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r32 ON fact_colreg_r32(dim_gps_id);

CREATE TABLE fact_colreg_r33
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r33 ON fact_colreg_r33(dim_gps_id);

CREATE TABLE fact_colreg_r34
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r34 ON fact_colreg_r34(dim_gps_id);

CREATE TABLE fact_colreg_r35
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r35 ON fact_colreg_r35(dim_gps_id);

CREATE TABLE fact_colreg_r36
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r36 ON fact_colreg_r36(dim_gps_id);

CREATE TABLE fact_colreg_r37
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r37 ON fact_colreg_r37(dim_gps_id);

CREATE TABLE fact_colreg_r38
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r38 ON fact_colreg_r38(dim_gps_id);

CREATE TABLE fact_colreg_r39
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r39 ON fact_colreg_r39(dim_gps_id);

CREATE TABLE fact_colreg_r40
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r40 ON fact_colreg_r40(dim_gps_id);

CREATE TABLE fact_colreg_r41
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	vessel_id INTEGER,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r41 ON fact_colreg_r41(dim_gps_id);

