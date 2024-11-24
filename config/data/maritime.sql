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

CREATE TABLE dim_fleet
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_origin_country
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_origin_port
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_origin_country_id INTEGER,
	value VARCHAR(255),
	display VARCHAR(255),
	type INTEGER,
	status INTEGER,
	ref VARCHAR(255)
);

CREATE TABLE dim_vessel
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	dim_origin_port_id INTEGER,
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
	crs VARCHAR(255),
	report_time TIMESTAMP,
	vessel_id INTEGER,
	penalty REAL
);

CREATE INDEX idx_fact_ro ON fact_ro(dim_gps_id);

CREATE TABLE fact_heading
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_heading ON fact_heading(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_velocity
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_velocity ON fact_velocity(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_acceleration
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_acceleration ON fact_acceleration(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_jerk
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_jerk ON fact_jerk(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_angular_velocity
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_angular_velocity ON fact_angular_velocity(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_angular_acceleration
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_angular_acceleration ON fact_angular_acceleration(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_yaw
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_yaw ON fact_yaw(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_pitch
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_pitch ON fact_pitch(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_roll
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_roll ON fact_roll(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_heave
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_heave ON fact_heave(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_vertical_motion
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_vertical_motion ON fact_vertical_motion(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_vertical_acceleration
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_vertical_acceleration ON fact_vertical_acceleration(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_relative_velocity
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	trarget INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_relative_velocity ON fact_relative_velocity(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_relative_heading
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	trarget INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_relative_heading ON fact_relative_heading(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_relative_phase
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	trarget INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_relative_phase ON fact_relative_phase(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_dcpa
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	trarget INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_dcpa ON fact_dcpa(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_tcpa
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	trarget INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_tcpa ON fact_tcpa(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_vcro
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	trarget INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_vcro ON fact_vcro(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_displacement
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_displacement ON fact_displacement(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_draft
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_draft ON fact_draft(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_submerged_volume
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_submerged_volume ON fact_submerged_volume(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_weight
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_weight ON fact_weight(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_payload
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value REAL,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_payload ON fact_payload(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_passengers
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value INTEGER,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_passengers ON fact_passengers(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crew
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	value INTEGER,
	unit INTEGER,
	start_time TIMESTAMP,
	end_time TIMESTAMP,
	report_time TIMESTAMP,
	error_pct REAL,
	sigma REAL,
	min_val REAL,
	max_val REAL,
	num_val INTEGER,
	gradient REAL,
	checksum INTEGER,
	tag VARCHAR(255)
);

CREATE INDEX idx_fact_crew ON fact_crew(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_score_hazardous_transport
(
	dim_gps_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
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
	penalty REAL
);

CREATE INDEX idx_fact_score_berthing_risk ON fact_score_berthing_risk(dim_gps_id);

CREATE TABLE fact_colreg_r01
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r01 ON fact_colreg_r01(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r02
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r02 ON fact_colreg_r02(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r03
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r03 ON fact_colreg_r03(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r04
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r04 ON fact_colreg_r04(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r05
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r05 ON fact_colreg_r05(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r06
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r06 ON fact_colreg_r06(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r07
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r07 ON fact_colreg_r07(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r08
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r08 ON fact_colreg_r08(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r09
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r09 ON fact_colreg_r09(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r10
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r10 ON fact_colreg_r10(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r11
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r11 ON fact_colreg_r11(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r12
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r12 ON fact_colreg_r12(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r13
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r13 ON fact_colreg_r13(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r14
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r14 ON fact_colreg_r14(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r15
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r15 ON fact_colreg_r15(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r16
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r16 ON fact_colreg_r16(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r17
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r17 ON fact_colreg_r17(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r18
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r18 ON fact_colreg_r18(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r19
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r19 ON fact_colreg_r19(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r20
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r20 ON fact_colreg_r20(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r21
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r21 ON fact_colreg_r21(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r22
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r22 ON fact_colreg_r22(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r23
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r23 ON fact_colreg_r23(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r24
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r24 ON fact_colreg_r24(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r25
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r25 ON fact_colreg_r25(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r26
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r26 ON fact_colreg_r26(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r27
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r27 ON fact_colreg_r27(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r28
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r28 ON fact_colreg_r28(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r29
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r29 ON fact_colreg_r29(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r30
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r30 ON fact_colreg_r30(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r31
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r31 ON fact_colreg_r31(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r32
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r32 ON fact_colreg_r32(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r33
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r33 ON fact_colreg_r33(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r34
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r34 ON fact_colreg_r34(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r35
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r35 ON fact_colreg_r35(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r36
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r36 ON fact_colreg_r36(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r37
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r37 ON fact_colreg_r37(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r38
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r38 ON fact_colreg_r38(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r39
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r39 ON fact_colreg_r39(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r40
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r40 ON fact_colreg_r40(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_colreg_r41
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_colreg_r41 ON fact_colreg_r41(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c01
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c01 ON fact_solas_c01(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c02
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c02 ON fact_solas_c02(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c03
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c03 ON fact_solas_c03(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c04
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c04 ON fact_solas_c04(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c05
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c05 ON fact_solas_c05(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c06
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c06 ON fact_solas_c06(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c07
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c07 ON fact_solas_c07(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c08
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c08 ON fact_solas_c08(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c09
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c09 ON fact_solas_c09(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c10
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c10 ON fact_solas_c10(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c11
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c11 ON fact_solas_c11(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c12
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c12 ON fact_solas_c12(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c13
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c13 ON fact_solas_c13(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c14
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c14 ON fact_solas_c14(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_solas_c15
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	clause VARCHAR(255),
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_solas_c15 ON fact_solas_c15(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_misc
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_misc ON fact_crs_highsea_misc(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_plan
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_plan ON fact_crs_highsea_plan(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_comfort
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_comfort ON fact_crs_highsea_comfort(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_grounding
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_grounding ON fact_crs_highsea_grounding(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_day_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_day_time ON fact_crs_highsea_day_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_night_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_night_time ON fact_crs_highsea_night_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_headon
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_headon ON fact_crs_highsea_headon(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_berthing
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_berthing ON fact_crs_highsea_berthing(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_overtaking
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_overtaking ON fact_crs_highsea_overtaking(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_give_way
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_give_way ON fact_crs_highsea_give_way(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_speed
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_speed ON fact_crs_highsea_speed(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_signal
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_signal ON fact_crs_highsea_signal(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_discipline
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_discipline ON fact_crs_highsea_discipline(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_highsea_collision
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_highsea_collision ON fact_crs_highsea_collision(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_misc
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_misc ON fact_crs_coastal_misc(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_plan
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_plan ON fact_crs_coastal_plan(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_comfort
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_comfort ON fact_crs_coastal_comfort(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_grounding
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_grounding ON fact_crs_coastal_grounding(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_day_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_day_time ON fact_crs_coastal_day_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_night_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_night_time ON fact_crs_coastal_night_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_headon
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_headon ON fact_crs_coastal_headon(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_berthing
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_berthing ON fact_crs_coastal_berthing(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_overtaking
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_overtaking ON fact_crs_coastal_overtaking(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_give_way
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_give_way ON fact_crs_coastal_give_way(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_speed
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_speed ON fact_crs_coastal_speed(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_signal
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_signal ON fact_crs_coastal_signal(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_discipline
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_discipline ON fact_crs_coastal_discipline(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_coastal_collision
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_coastal_collision ON fact_crs_coastal_collision(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_misc
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_misc ON fact_crs_domestic_misc(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_plan
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_plan ON fact_crs_domestic_plan(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_comfort
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_comfort ON fact_crs_domestic_comfort(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_grounding
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_grounding ON fact_crs_domestic_grounding(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_day_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_day_time ON fact_crs_domestic_day_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_night_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_night_time ON fact_crs_domestic_night_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_headon
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_headon ON fact_crs_domestic_headon(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_berthing
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_berthing ON fact_crs_domestic_berthing(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_overtaking
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_overtaking ON fact_crs_domestic_overtaking(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_give_way
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_give_way ON fact_crs_domestic_give_way(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_speed
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_speed ON fact_crs_domestic_speed(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_signal
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_signal ON fact_crs_domestic_signal(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_discipline
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_discipline ON fact_crs_domestic_discipline(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_domestic_collision
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_domestic_collision ON fact_crs_domestic_collision(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_misc
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_misc ON fact_crs_interior_misc(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_plan
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_plan ON fact_crs_interior_plan(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_comfort
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_comfort ON fact_crs_interior_comfort(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_grounding
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_grounding ON fact_crs_interior_grounding(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_day_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_day_time ON fact_crs_interior_day_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_night_time
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_night_time ON fact_crs_interior_night_time(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_headon
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_headon ON fact_crs_interior_headon(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_berthing
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_berthing ON fact_crs_interior_berthing(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_overtaking
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_overtaking ON fact_crs_interior_overtaking(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_give_way
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_give_way ON fact_crs_interior_give_way(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_speed
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_speed ON fact_crs_interior_speed(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_signal
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_signal ON fact_crs_interior_signal(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_discipline
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_discipline ON fact_crs_interior_discipline(dim_gps_id,dim_vessel_id);

CREATE TABLE fact_crs_interior_collision
(
	dim_gps_id INTEGER,
	dim_vessel_id INTEGER,
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creation_time TIMESTAMP,
	audit_status INTEGER,
	report_time TIMESTAMP,
	type INTEGER,
	penalty REAL,
	situation VARCHAR(255),
	info VARCHAR(255)
);

CREATE INDEX idx_fact_crs_interior_collision ON fact_crs_interior_collision(dim_gps_id,dim_vessel_id);

