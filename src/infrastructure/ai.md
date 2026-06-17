# Artificial Intelligence and Machine Learning

To aid AI and ML workflows we offer API based access to various models for chat, embedding, and image recognition. The system is backed by NVIDIA RTX PRO 6000 GPUs.


## Available Models


| Model | Origin | License | Usage |
| - | - | - | - |
| [gpt-oss:20b](https://huggingface.co/openai/gpt-oss-20b) | OpenAI | Apache License Version 2.0 | llm |
| [gpt-oss:120b](https://huggingface.co/openai/gpt-oss-120b) | OpenAI | Apache License Version 2.0 | llm |
| [rednote-hilab/dots.mocr](https://huggingface.co/rednote-hilab/dots.mocr) | Red Note (hilab)	 | MIT License | Image-Text-to-Text |
| [Nomic-embed-text:v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF) | Nomic | Apache License Version 2.0 | embedding |
| [bge-m3:567m](https://huggingface.co/BAAI/bge-m3)  | Beijing Academy of Artificial Intelligence | MIT License | embedding |
| [embeddinggemma:300m](https://huggingface.co/google/embeddinggemma-300m) | Google | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | embedding |

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


## Known issues and restrictions

Our open source based stack using Linux, VLLM, and other components is under active development from a broad community of developers. At the same time, the nature of implementing a de-facto standard like the OpenAI API 
for a wide variety of GPUs, model architectures and an ever growing feature matrix may cause specific compatibility issues. 

To support our customers we provide a list of issues that have had visible impact in the past. This list
is given on a best effort basis and as many AI features have fuzzy behaviour, we suggest to try them
for your specific use case still.

Look-around regular expressions in structured output are not supported
: Using regular expression that leverage look-around/look-ahead/look-behind features
  results in to help guiding structured output may result in errors like this:

  ```
  {
    "error": {
      "message": "Grammar error: regex parse error:\n    ^(?!^[-+.]*$)[+-]?0*[0-9]*\\.?[0-9]*$\n     ^^^\nerror: look-around, including look-ahead and look-behind, is not supported",
      "type": "BadRequestError",
      "param": null,
      "code": 400
    }  
  }
  ```
