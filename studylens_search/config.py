from typing import Dict, Any


class Config_OpenAI_MODELS:
    GPT4 = "gpt-4"
    GPT4_TURBO = "gpt-4-1106-preview"
    GPT3_5_TURBO = "gpt-3.5-turbo-1106"


class Config_OpenAI:
    model_name = Config_OpenAI_MODELS.GPT4_TURBO
    max_tokens = 1000
    prompts: Dict[str, str] = {
        "data_enrichment": "Providing you with metadata on few {} to analyze their learning difficulty, primary subjects/domains they belong to and their relevance to data science, machine learning, and analytics. Make sure the output response is in the following format: {{ 'resource_id':'this needs to map exactly to the resource id for which this json output is. This is used to map this json output to the actual resource in database.' ,'relevance':true/false, 'difficulty': '<beginner/intermediate/upper intermediate/advanced/expert>', 'domains': ['<domain1>', '<domain2>',....], 'reason_relevance':'reason why the selected relevance is selected', 'reason_difficulty':'reason why the selected difficulty level is selected' }} "
    }
    embedding_field_types: Dict[str, list] = {
        "general_fields": [
            {
                "field_name": "title",
                "field_type": "text",
            },
            {
                "field_name": "subtitle",
                "field_type": "text",
            },
            {
                "field_name": "description",
                "field_type": "text",
            },
            {
                "field_name": "domains",
                "field_type": "text",
            },
            {
                "field_name": "difficulty",
                "field_type": "text",
            },
            {
                "field_name": "reason_relevance",
                "field_type": "text",
            },
            {
                "field_name": "reason_difficulty",
                "field_type": "text",
            },
        ],
        "book_fields": [
            {
                "field_name": "publisher",
                "field_type": "text",
            },
            {
                "field_name": "authors",
                "field_type": "text",
            },
            {
                "field_name": "last_publish_year",
                "field_type": "text",
            },
        ],
        "video_fields": [
            {
                "field_name": "channel_title",
                "field_type": "text",
            },
            {
                "field_name": "tags",
                "field_type": "array",
            },
        ],
        "course_fields": [
            {
                "field_name": "instructor",
                "field_type": "text",
            },
            {
                "field_name": "course_rating",
                "field_type": "number",
            },
            {
                "field_name": "course_rating_count",
                "field_type": "number",
            },
        ],
        "research_paper_fields": [
            {
                "field_name": "authors",
                "field_type": "text",
            },
            {
                "field_name": "published_date",
                "field_type": "text",
            },
        ],
    }


class Config_Qdrant:
    host = "http://localhost"
    port = 6333
    vector_size = 1536
    collection_name = "resources_test_collection_2"
    distance = "Cosine"
