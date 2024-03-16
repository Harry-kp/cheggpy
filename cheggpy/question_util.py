"""This module contains utility functions for the question on chegg."""

import json
from .custom_exceptions import EmptyQueue, NoQuestionToSkip


def fetch_latest_question(session):
    '''
        Fetch the latest question in the queue.
        Returns dict with question_id, body, etc. if question is present.
        Otherwise, returns None or raises an Exception.
        '''
    chegg_question_url = "https://gateway.chegg.com/nestor-graph/graphql"
    payload = json.dumps({
        "operationName": "NextQuestionAnsweringAssignment",
        "variables": {},
        "query": "query NextQuestionAnsweringAssignment {\n  nextQuestionAnsweringAssignment {\n    question {\n      body\n      id\n      uuid\n      subject {\n        id\n        name\n        subjectGroup {\n          id\n          name\n          __typename\n        }\n        __typename\n      }\n      imageTranscriptionText\n      lastAnswerUuid\n      __typename\n    }\n    langTranslation {\n      body\n      translationLanguage\n      __typename\n    }\n    questionGeoLocation {\n      countryCode\n      countryName\n      languages\n      __typename\n    }\n    questionRoutingDetails {\n      answeringStartTime\n      bonusCount\n      bonusTimeAllocationEnabled\n      checkAnswerStructureEnabled\n      hasAnsweringStarted\n      questionAssignTime\n      questionSolvingProbability\n      routingType\n      allocationExperimentId\n      questionQualityFactor\n      __typename\n    }\n    __typename\n  }\n}"
    })
    headers = {
        'authority': 'gateway.chegg.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9',
        'apollographql-client-name': 'chegg-web-producers',
        'content-type': 'application/json',
        'origin': 'https://expert.chegg.com',
        'referer': 'https://expert.chegg.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    session.headers.update(headers)
    response = json.loads(session.request(
        "POST", chegg_question_url, data=payload).text)
    if response.get('errors') is not None:
        error = response['errors'][0]
        if error['extensions']['errorType'] == 'NO_QUESTION_ASSIGNED':
            raise EmptyQueue('No more question left in queue to answer.')
        raise NotImplementedError(response['errors'][0]['message'])
    return response


def skip_latest_question(session, question):
    """Skip the latest question in the queue."""
    if question is None or question.id is None:
        raise NoQuestionToSkip('No question to skip.')
    chegg_question_url = "https://gateway.chegg.com/nestor-graph/graphql"
    payload = json.dumps({
        "operationName": "SkipQuestionAssignment",
        "variables": {
            "questionId": question.id,
            "skipPageFlow": "DECISION",
            "skipPrimaryReason": {
                "noKnowledge": True
            }
        },
        "query": "mutation SkipQuestionAssignment($questionId: Long!, $skipPageFlow: QnaCurrentPageFlow!, $skipPrimaryReason: QuestionSkipPrimaryReasons, $newSkipReason: QuestionNewSkipReasons) {\n  skipQuestionAssignment(\n    questionId: $questionId\n    skipPageFlow: $skipPageFlow\n    skipPrimaryReason: $skipPrimaryReason\n    newSkipReason: $newSkipReason\n  ) {\n    message\n    questionId\n    __typename\n  }\n}"
    })
    response = json.loads(session.request(
        "POST", chegg_question_url, data=payload).text)
    if response.get("errors") is not None:
        raise NotImplementedError(response['errors'][0]['message'])


def analyze_question(question, keywords):
    """Analyze the question and return the result"""
    ques_text = question.body + ' ' + question.transcription
    if any(word in ques_text for word in keywords):
        return True
    return False
