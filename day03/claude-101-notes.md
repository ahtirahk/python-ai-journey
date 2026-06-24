Module 1: Meet Claude

What is Claude?


Claude is an AI assistant built by Anthropic
Designed to be helpful, harmless, and honest
Not just a chatbot — it can reason, write, code, analyse, and create
Built on Constitutional AI principles — safety is built into how it thinks, not bolted on top
Different from a search engine: Claude doesn't just retrieve information, it understands context and reasons through problems
Claude has a knowledge cutoff — it doesn't have real-time internet access by default (unless search tools are connected)


Your First Conversation with Claude


How you phrase a prompt directly affects the quality of the response
Claude responds to the full context of a conversation — earlier messages shape later ones
You can correct Claude mid-conversation and it will adjust
Claude can hold multi-turn conversations — it remembers what was said earlier in the same chat
Tone, format, and detail level can all be guided through how you write your prompt


Getting Better Results


Be specific — vague prompts get vague answers
Give context — tell Claude who you are and what you're trying to do
Specify the format — ask for bullet points, a table, a numbered list, short answer, etc.
Iterate — if the first response isn't right, follow up and refine rather than starting over
Role prompting — you can tell Claude to act as a specific expert ("Act as a senior Python developer...")
Examples help — showing Claude an example of what you want (few-shot prompting) improves accuracy
Claude can handle long, complex instructions — don't be afraid to be thorough


Claude Desktop App: Chat, Cowork, Code


Chat — standard conversational interface for everyday tasks
Cowork — works alongside your real files and projects; handles multi-step workflows
Code (Claude Code) — agentic coding tool that can read, write, and execute code in your environment
The desktop app connects these three modes in one place
Each mode is suited to different types of tasks — choosing the right one matters



Module 2: Organizing Your Work and Knowledge

Introduction to Projects


Projects are a way to organise related conversations and files together
A Project keeps context persistent — Claude remembers what you've told it across multiple chats within that Project
You can give a Project a name, description, and custom instructions
Custom instructions in a Project act like a persistent system prompt — they apply to every conversation in that Project
Use Projects when you have an ongoing body of work (e.g. a study plan, a codebase, a research topic)
CCA-F relevance: Projects are a form of context management 


Creating with Artifacts


Artifacts are standalone outputs Claude creates — documents, code files, diagrams, HTML pages
They appear in a separate panel alongside the conversation
Artifacts can be edited, copied, and downloaded
Useful for: writing documents, generating code, creating structured outputs
Artifacts persist within a conversation and can be iterated on
CCA-F relevance: Understanding structured outputs is part of Domain 4 (Prompt Engineering)


Working with Skills


Skills are reusable instructions that Claude applies automatically to the right tasks
Defined using markdown files (SKILL.md)
Skills tell Claude how to behave for specific types of work without you having to re-explain every time
Can be shared across a team so everyone gets consistent Claude behaviour
CCA-F relevance: Skills are directly tested in Domain 1 (Agentic Architecture) and Domain 3 (Claude Code)



Module 3: Expanding Claude's Reach

Connecting Your Tools


Claude can connect to external tools and services via integrations
Examples: Google Drive, Gmail, Calendar, Slack, GitHub
Connected tools allow Claude to read real files, check calendars, search emails
This is powered by the Model Context Protocol (MCP) under the hood
CCA-F relevance: This is the user-facing version of what Domain 2 (MCP Integration) covers technically


Enterprise Search


Claude can search across connected data sources to find relevant information
Useful when working in large organisations with documents spread across multiple systems
Returns sourced answers, not just retrieved documents


Research Mode for Deep Dives


Research mode lets Claude run extended, multi-step research on a topic
It searches, synthesises, and produces a structured report
Takes longer than a regular response but produces more thorough results
You can steer the direction mid-research
CCA-F relevance: This is an example of an agentic workflow — multi-step, tool-using, autonomous — connects to Domain 1



Module 4: Putting It All Together

Claude in Action: Use Cases by Role

Writers/Marketers: drafting, editing, repurposing content, tone adjustment
Developers: code generation, debugging, documentation, code review
Analysts: data interpretation, summarisation, report writing
Managers: meeting prep, email drafting, decision support
The same underlying Claude model is used across all roles — what changes is how you prompt it


Other Ways to Work with Claude


Claude.ai — web and mobile interface
Claude API — for developers building applications on top of Claude (covered in Week 2)
Claude Code — agentic coding in your terminal or IDE (covered in Week 4)
Amazon Bedrock / Google Vertex AI — access Claude through cloud platforms
Claude in Microsoft/Google tools — integrations with Word, Excel, Docs, Sheets (via extensions)



Key Concepts to Remember for CCA-F Exam

Context Window

The amount of text Claude can "see" at one time in a conversation. Think of it like a whiteboard — when it gets full, older stuff gets wiped to make space.

Multi-turn Conversations

When you go back and forth with Claude across multiple messages in the same chat. Claude remembers everything said earlier in that same chat only.

Projects = Persistent Context

A folder where Claude remembers your files and instructions across ALL chats inside it. Unlike a normal chat, you don't have to re-explain yourself every time.

Skills = Reusable Instructions

A markdown file (SKILL.md) that tells Claude how to behave for a specific task. Write it once, Claude applies it automatically every time that task comes up.

Tools/Integrations

External apps Claude can connect to — like Google Drive, Gmail, or Slack. Claude reads and acts on your real data inside those apps, not just in the chat.

Artifacts = Structured Outputs

When Claude creates a standalone file — a document, code, or webpage — that appears in its own panel. You can edit, download, and reuse it directly.

Research Mode = Agentic Workflow

Claude plans, searches, reads multiple sources, and writes a full report ON ITS OWN without you guiding each step. It works autonomously from start to finish.

Prompting Principles

The rules for getting good results from Claude — be specific, give context, set the format, use examples, and iterate. Bad prompt = bad output, good prompt = great output.



The difference between Chat, Cowork, and Code modes — when to use which
Something to discuss or write → Chat
Something to do with your files → Cowork
Something to do with your code → Code
How Skills and Projects interact with each other
A Project sets up the environment — your files, your custom instructions, your memory across chats. A Skill defines how Claude acts when a specific task comes up — what format to use, what steps to follow, what to avoid.Projects answer "what does Claude know?" — Skills answer "how does Claude behave?"