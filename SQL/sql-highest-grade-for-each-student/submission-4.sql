-- Write your query below
SELECT exam_results.student_id, MIN(exam_id) as exam_id, MAX(score) as score
FROM exam_results
JOIN (SELECT student_id, MAX(score) as max_score FROM exam_results GROUP BY student_id) AS highest_scores
ON exam_results.student_id = highest_scores.student_id AND exam_results.score = highest_scores.max_score
GROUP BY exam_results.student_id
