"""Azure OpenAI LLM client with endpoint fallback."""

import json
import os
import time

from .utils import get_logger

LOGGER = get_logger(__name__)
_MAX_RETRIES = 3
_RETRY_BACKOFF = 2


class LLMClient:
    def __init__(self, model="gpt-4o", temperature=0.3, max_tokens=4096):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._client = None
        self._resolved = False

    def _get_client(self):
        if self._client is not None:
            return self._client
        from openai import AzureOpenAI
        ep2 = os.environ.get("AZURE_ENDPOINT_2", "")
        key2 = os.environ.get("AZURE_API_KEY_2", "")
        ver2 = os.environ.get("AZURE_API_VERSION_2", "2024-12-01-preview")
        if ep2 and key2 and not self._resolved:
            try:
                probe = AzureOpenAI(azure_endpoint=ep2, api_key=key2, api_version=ver2)
                probe.chat.completions.create(model=self.model, messages=[{"role":"user","content":"ping"}], max_tokens=1)
                self._client = probe
                self._resolved = True
                LOGGER.info("Using AZURE_ENDPOINT_2 model=%s", self.model)
                return self._client
            except Exception:
                LOGGER.warning("ENDPOINT_2 %s unavailable, fallback to gpt-4o", self.model)
        self._client = AzureOpenAI(azure_endpoint=os.environ["AZURE_ENDPOINT"], api_key=os.environ["AZURE_API_KEY"], api_version=os.environ.get("AZURE_API_VERSION","2024-12-01-preview"))
        self.model = "gpt-4o"
        self._resolved = True
        LOGGER.info("Using AZURE_ENDPOINT fallback model=gpt-4o")
        return self._client

    def generate(self, system, user, json_mode=False, temperature=None, max_tokens=None):
        client = self._get_client()
        kwargs = {"model": self.model, "messages": [{"role":"system","content":system},{"role":"user","content":user}], "temperature": temperature if temperature is not None else self.temperature, "max_tokens": max_tokens or self.max_tokens}
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        for attempt in range(1, _MAX_RETRIES + 1):
            try:
                LOGGER.info("LLM [%s] attempt=%d json=%s", self.model, attempt, json_mode)
                resp = client.chat.completions.create(**kwargs)
                text = resp.choices[0].message.content
                LOGGER.info("LLM response: %d chars", len(text))
                return text
            except Exception as exc:
                LOGGER.warning("LLM attempt %d failed: %s", attempt, exc)
                if attempt < _MAX_RETRIES:
                    time.sleep(_RETRY_BACKOFF ** attempt)
                else:
                    raise

    def generate_json(self, system, user, temperature=None, max_tokens=None):
        raw = self.generate(system, user, json_mode=True, temperature=temperature, max_tokens=max_tokens)
        return json.loads(raw)
