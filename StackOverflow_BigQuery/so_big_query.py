import csv
import io
from google.cloud import bigquery

def query_stackoverflow():
    # initialize client
    client = bigquery.Client()

    # specify query
    query_job = client.query(
    """ 
    SELECT
        answer.id AS a_id,
        answer.body AS answer_body,
        (SELECT users.reputation FROM `bigquery-public-data.stackoverflow.users` users
            WHERE users.id = answer.owner_user_id) AS a_user_reputation,
        answer.score AS a_score,
        answer.creation_date AS answer_date,
        answer.comment_count AS answer_comment_count,
        questions.tags as q_tags,
        questions.body AS q_body, 
        questions.score AS q_score,  
        questions.answer_count AS answer_count, 
        (SELECT users.reputation FROM `bigquery-public-data.stackoverflow.users` users
            WHERE users.id = questions.owner_user_id) AS q_user_reputation,
        questions.view_count AS q_view_count,
        questions.creation_date AS q_date,
        questions.comment_count AS q_comment_count,
        IF(questions.accepted_answer_id = answer.id, 1, 0) AS is_accepted_answer
    FROM
       `bigquery-public-data.stackoverflow.posts_answers` AS answer LEFT JOIN
       `bigquery-public-data.stackoverflow.posts_questions` AS questions
          ON
            answer.parent_id = questions.id
    WHERE
        (questions.tags LIKE '%javascript%' AND
        questions.tags LIKE '%xss%' OR
        questions.tags LIKE '%cross-site%' OR
        questions.tags LIKE '%exploit%' OR
        questions.tags LIKE '%cybersecurity%')
        AND (questions.accepted_answer_id IS NOT NULL)
    """
    )

    # wait for job to complete and get results
    results = query_job.result()

    # google.cloud.bigquery.table.row -> dictionary
    rows = []
    for row in results:
        rowAsDict = dict(row)
        rows.append(rowAsDict)

    # save to CSV file
    with io.open("StackOverflowData.csv", "w", encoding="utf-8", newline="") as csvFile:
        header = rows[0].keys()
        dictWriter = csv.DictWriter(csvFile, header)
        dictWriter.writeheader()
        dictWriter.writerows(rows)
        csvFile.close()

if __name__ == "__main__":
    query_stackoverflow()