import sys
import unittest
from importlib.util import find_spec
from types import ModuleType
from unittest.mock import Mock, patch


def _mock_module(name, **attributes):
    module = ModuleType(name)
    for attribute, value in attributes.items():
        setattr(module, attribute, value)
    return module


mock_modules = {
    "backend.services.retrieval_service": _mock_module(
        "backend.services.retrieval_service",
        search_knowledge_base=Mock(),
    )
}
if find_spec("requests") is None:
    mock_modules["requests"] = ModuleType("requests")
if find_spec("dotenv") is None:
    mock_modules["dotenv"] = _mock_module("dotenv", load_dotenv=Mock())

with patch.dict(sys.modules, mock_modules):
    from backend.services import llm_service


class GenerateAnswerHistoryTests(unittest.TestCase):
    def setUp(self):
        self.search_patch = patch.object(
            llm_service,
            "search_knowledge_base",
            return_value=[
                {
                    "content": "The portfolio project uses Python.",
                    "metadata": {
                        "source_name": "projects",
                        "title": "Portfolio project",
                    },
                }
            ],
        )
        self.search = self.search_patch.start()
        self.addCleanup(self.search_patch.stop)

        self.post_patch = patch.object(
            llm_service,
            "requests",
        )
        self.requests = self.post_patch.start()
        self.addCleanup(self.post_patch.stop)
        self.requests.post.return_value = Mock(
            ok=True,
            json=lambda: {
                "choices": [
                    {"message": {"content": "It uses Python."}}
                ]
            },
        )

        self.api_key_patch = patch.object(
            llm_service,
            "OPENROUTER_API_KEY",
            "test-key",
        )
        self.api_key_patch.start()
        self.addCleanup(self.api_key_patch.stop)

    def test_includes_history_but_retrieves_from_latest_user_turn(self):
        history = [
            {"role": "user", "content": "How many projects has he built?"},
            {"role": "assistant", "content": "He built one project."},
            {"role": "user", "content": "Tell me about the portfolio project."},
            {
                "role": "assistant",
                "content": "It is an AI portfolio project, according to earlier evidence.",
            },
        ]

        answer = llm_service.generate_answer(
            "What tech stack does it use?",
            history=history,
        )

        self.assertEqual(answer, "It uses Python.")
        self.search.assert_called_once_with(
            "Tell me about the portfolio project.\nWhat tech stack does it use?",
            top_k=4,
        )
        messages = self.requests.post.call_args.kwargs["json"]["messages"]
        self.assertEqual(
            [message["role"] for message in messages],
            ["system", "user", "assistant", "user", "assistant", "user"],
        )
        self.assertEqual(messages[1:5], history)
        self.assertIn(
            "Previous assistant messages are not evidence",
            messages[0]["content"],
        )
        self.assertIn(
            "How many projects has he built?",
            messages[1]["content"],
        )
        self.assertIn(
            "Question: What tech stack does it use?",
            messages[-1]["content"],
        )

    def test_limits_history_to_the_latest_ten_messages(self):
        history = [
            {"role": "user", "content": f"Message {index}"}
            for index in range(11)
        ]

        llm_service.generate_answer("Latest question", history=history)

        messages = self.requests.post.call_args.kwargs["json"]["messages"]
        self.assertEqual(len(messages), 12)
        self.assertEqual(messages[1]["content"], "Message 1")
        self.search.assert_called_once_with(
            "Message 10\nLatest question",
            top_k=4,
        )


if __name__ == "__main__":
    unittest.main()
