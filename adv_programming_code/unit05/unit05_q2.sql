use kprecht2_chado;

-- Question 2
SELECT f.feature_id, f.uniquename, c.name, p.value, l.fmin, l.fmax, l.strand
FROM feature f 
	JOIN cvterm c on f.type_id = c.cvterm_id
	JOIN featureprop p on f.feature_id = p.feature_id
	JOIN featureloc l on l.feature_id = p.feature_id
    JOIN cvterm pp ON p.type_id = pp.cvterm_id
WHERE c.name LIKE 'polypeptide'
	AND p.value like '%bifunctional%';
