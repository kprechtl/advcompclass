use kprecht2_chado;

-- Question 1
SELECT f.feature_id, f.uniquename, c.name, p.value
FROM feature f 
	JOIN cvterm c on f.type_id = c.cvterm_id
	JOIN featureprop p on f.feature_id = p.feature_id
WHERE c.name LIKE 'polypeptide'
	AND p.value like '%bifunctional%';
