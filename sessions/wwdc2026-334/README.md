# Build AI-powered scripts with the fm CLI and Python SDK

**Topic:** AI & Machine Learning · **Platforms:** macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-334](https://developer.apple.com/videos/play/wwdc2026/334)

Explore all the new ways to leverage Apple Foundation Models on macOS. The Foundation Models SDK for Python lets you integrate with popular tooling and evaluation packages in the Python ecosystem. Find out how to use the brand new fm command introduced in macOS 27 to streamline scripting, automate model workflows, and accelerate your development process.

**Keywords:** `ai`, `machine learning`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Foundation Models SDK for Python on GitHub](https://github.com/apple/python-apple-fm-sdk) _documentation_
- [Foundation Models SDK for Python Documentation on GitHub](https://apple.github.io/python-apple-fm-sdk/) _documentation_

## Code Snippets

### Prompt the on-device model with fm respond — [5:07]

```bash
$ fm respond "Provide a basic regex in Swift to parse an email address"
# Here is a basic regex to parse an email address in Swift: [...]

$ fm respond "Provide a comprehensive regex in Swift to parse an email address" --model pcc
# [...] Here's a robust Swift implementation using 'NSRegularExpression' to validate a typical email address:

$ fm respond "What app is the user using in this screenshot?" --model pcc \
	--image Screenshot.png
# The user is using the Mail app.

$ fm schema object --name AppsIdentified --string app_names --array > schema.json 
$ fm respond "What apps are the user actively using in this screenshot?" \
	--image Screenshot.png --model pcc --schema schema.json
# {"app_names": ["Messages", "Mail", "Calendar"]}

$ fm respond --help
```

### Sort files with fm respond and a schema — [7:55]

```bash
fm schema object --name "TriagedFileList" \
    --string 'final_files' --array \
    --string 'draft_files' --array > /tmp/schema.json

output=$(fm respond \
    --instructions "I just completed a project, and I need help triaging the latest version of the files from the previous versions. I will give you a list of files. Return a list of the latest files (i.e., all files that, you can infer from their name in the list, are the latest versions), and then return separately a list of all draft files (i.e., all files that weren't considered final)." \
    "This is the list of all files:\n\n${files_list}" \
    --schema /tmp/schema.json
)

echo "${output}" | jq -r '.final_files[]' | while read -r file; do
    cp "${DIRECTORY_TO_TRIAGE}/${file}" "${FINAL_FILES_STORAGE_DIRECTORY}"
done

echo "${output}" | jq -r '.draft_files[]' | while read -r file; do
    mv "${DIRECTORY_TO_TRIAGE}/${file}" "${DRAFT_FILES_STORAGE_DIRECTORY}"
done
```

### Install the Foundation Models Python SDK — [8:54]

```bash
pip install apple_fm_sdk
```

### Create a session and respond to a prompt — [10:00]

```python
import apple_fm_sdk as fm

INSTRUCTIONS = "You're an AI assistant for Cupertino Mart, a grocery store with in-app ordering."

async def answer_question(prompt: str) -> str:
	session = fm.LanguageModelSession(instructions=INSTRUCTIONS)
  return await session.respond(prompt)
```

### Define a Tool for the language model — [10:21]

```python
class GetPastOrdersTool(fm.Tool):
  name = "get_past_orders"
  description = "Retrieves information about this user's past orders."

  @fm.generable("Past orders query parameter")
  class Arguments:
  	number_orders: str = fm.guide("How many of the last orders to retrieve")

  @property
  def arguments_schema(self) -> fm.GenerationSchema:
  	return self.Arguments.generation_schema()

async def call(self, args: fm.GeneratedContent) -> str:
	number_orders = args.value(int, for_property="number_orders")
  return await Orders.load_last_orders(user_id=user_id, amount=number_orders)
```

### Generate structured output with @fm.generable — [10:35]

```python
@fm.generable("Suggested items")
class ItemsSuggestion:
	item_names: list[str] = fm.guide("Names of the suggested items")

INSTRUCTIONS = "You're an AI assistant tasked with returning potential grocery items that the user might be interested in."

async def generate_suggested_cart_items(user_input: Optional[str]) -> ItemsSuggestion:
	session = fm.LanguageModelSession(instructions=INSTRUCTIONS, tools=load_tools())
	prompt = """Using the tools to load the user's previous orders, \
              return a list of items the user has already ordered \
              and that they might be interested in again \
              as they're getting ready to place a new grocery order."""
	if user_input is not None:
    prompt += f"\nAccount for the following request from the user: {user_input}"
    return await session.respond(prompt, generating=ItemsSuggestion)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/334/4/65b71eea-f323-4f86-9096-889b6da91bdd/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/334/4/65b71eea-f323-4f86-9096-889b6da91bdd/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._