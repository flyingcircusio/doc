# Artificial Intelligence and Machine Learning

To aid AI and ML workflows we offer API based access to various models for chat, embedding, and image recognition. The system is backed by AMD W7900 GPUs.


## Available Models


| Model | Origin | Usage |
| - | - | - |
| gpt-oss:20b | OpenAI | llm |
| gpt-oss:120b | OpenAI | llm |
| mistral-small3.2:latest | Mistral AI | Multi / vision |
| Nomic-embed-text:v1.5 | Nomic | embedding |
| bge-m3:567m  | Beijing Academy of Artificial Intelligence | embedding |
| embeddinggemma:300m | Google | embedding |

## APIs and Access

We provide location-specific OpenAI-compatible API endpoints.
Access to the AI API can be enabled for any resource group via our customer portal https://my.flyingcircus.io/.
Manager permissions are required to do this.

To use the API, an authentication token is required as a bearer token.
We recommend using application specific token.
These tokens can be created in our customer portal by any user with manager permissions in the resource group.

Public endpoints:

- RZOB: https://ai.rzob.fcio.net/openai/v1
- RZHAL: https://ai.whq.fcio.net/openai/v1

Customer-owned hardware is available via custom endpoints.
