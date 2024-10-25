# Copilot Workspace: Overview

[Copilot Workspace](https://githubnext.com/projects/copilot-workspace/) is a _task-centric_ AI assistant. Each day as a developer you start with a task, and make the journey to explore, understand, refine, and complete that task, a journey that can be exciting, challenging, fascinating, and rewarding. Copilot Workspace takes this journey with you, every step of the way — the journey from task to working code. 

Copilot Workspace 是一个以任务为中心的 AI 助手。作为开发人员的每一天，你都从一个任务开始，进行探索、理解、完善和完成任务的旅程，这个旅程可能是令人兴奋、充满挑战、引人入胜和有回报的。Copilot Workspace 会在每一步都陪伴你，从任务到工作代码的旅程。

Copilot Workspace is built on a set of principles that guide its design and development:

Copilot Workspace 基于一组指导其设计和开发的原则：

* Copilot Workspace is _contextual_. It is deeply integrated with GitHub, and is aware of the context of your task — the repository, the issue, the pull request.

* Copilot Workspace 是有上下文的。它与 GitHub 深度集成，并且了解你的任务的上下文——仓库、问题、拉取请求。

* Copilot Workspace is _assistive_. It offers a canvas for you to navigate unfamiliar tasks, augmenting your development skills with a new kind of AI assistance.

* Copilot Workspace 是辅助性的。它为你提供了一个画布，让你可以导航不熟悉的任务，并通过一种新的 AI 辅助来增强你的开发技能。

* Copilot Workspace is _pervasive_. It is ready and waiting for you, available on every issue in every enabled repository on GitHub. And Copilot Workspace is even there for you when starting new code, available on every template repository, to create new software using natural language.

* Copilot Workspace 是普遍的。它已经准备好并等待着你，在 GitHub 上每个启用的仓库中的每个问题上都可以使用。而且，当你开始编写新代码时，Copilot Workspace 也会在那里，在每个模板仓库中都可以使用，使用自然语言创建新软件。

* Copilot Workspace is _iterative_. Copilot Workspace encourages you to check, review, refine and iterate on AI-generated outputs. You, the developer, are in control.

* Copilot Workspace 是迭代的。Copilot Workspace 鼓励你检查、审查、完善和迭代 AI 生成的输出。你，开发人员，掌握着控制权。

* Copilot Workspace is _collaborative_. You can share sessions with your team and publish links to your sessions on issues and pull requests. And, if you're a repository maintainer, we give you controls to help manage the use of AI-assisted development with your repositories.

* Copilot Workspace 是协作的。你可以与团队共享会话，并在问题和拉取请求上发布会话链接。而且，如果你是仓库维护者，我们会为你提供控制，帮助管理 AI 辅助开发在你的仓库中的使用。

* Copilot Workspace is _configurable_. You can integrate Copilot Workspace into your workflows via deep links to Copilot Workspace that specify common tasks.

* Copilot Workspace 是可配置的。你可以通过深度链接将 Copilot Workspace 集成到你的工作流程中，这些链接指定了常见任务。

In this manual, we will guide you through the concepts and features of Copilot Workspace, and help you get started with using it effectively.

在本手册中，我们将引导你了解 Copilot Workspace 的概念和功能，并帮助你有效地开始使用它。

<img src="images/overview/session.png" width="600" alt="A fully-implemented workspace session">

*一个完全实现的工作区会话*

## Features

## 功能

1. [Task](#task)
1. [任务](#task)
1. [Specification](#specification)
1. [规范](#specification)
1. [Plan](#plan)
1. [计划](#plan)
1. [Implementation](#implementation)
1. [实施](#implementation)
1. [Iterating on Files](#iterating-on-files)
1. [文件迭代](#iterating-on-files)
1. [Integrated Terminal](#integrated-terminal)
1. [集成终端](#integrated-terminal)
1. [Session Sharing](#session-sharing)
1. [会话共享](#session-sharing)
1. [Task Completion](#task-completion)
1. [任务完成](#task-completion)
1. [Session Dashboard](#session-dashboard)
1. [会话仪表板](#session-dashboard)

## Task

## 任务

Everything in Copilot Workspace begins with a “task”, which is a natural language description of intent. The task always has a context: a GitHub repository.
For this technical preview, Copilot Workspace supports four types of tasks: solving issues, [refining pull requests](pull-request-tasks.md), [creating repositories from templates](creating-repos.md) and [ad-hoc tasks](adhoc-tasks.md). Here we focus on solving issues, which are the most common entry point.

Copilot Workspace 中的所有内容都始于一个“任务”，这是一个自然语言描述的意图。任务总是有一个上下文：一个 GitHub 仓库。
在这个技术预览中，Copilot Workspace 支持四种类型的任务：解决问题、[完善拉取请求](pull-request-tasks.md)、[从模板创建仓库](creating-repos.md)和[临时任务](adhoc-tasks.md)。这里我们重点介绍解决问题，这是最常见的入口点。

Once enrolled in the technical preview, then on every issue in GitHub you will find a new "Open in Workspace" button:

一旦注册了技术预览版，那么在 GitHub 上的每个问题中，你都会发现一个新的“在工作区中打开”按钮：

<img src="images/general/open-in-workspace.png" width=400 alt="Button on issue page to open in Copilot Workspace">

*在 Copilot Workspace 中打开问题的按钮*

This will open Copilot Workspace contextualized to this issue. For issue tasks, the task is based in the title and body of the issue, plus the issue’s comment thread. Copilot Workspace will immediately progress to the next step in the timeline. This looks like this:

这将打开与此问题相关的 Copilot Workspace。对于问题任务，任务基于问题的标题和正文，加上问题的评论线程。Copilot Workspace 将立即进入时间线中的下一步。看起来像这样：

<img src="images/overview/issue-timeline-representation.png" width=600 alt="Issue task timeline representation">

*任务被标记为“问题”，并开始分析*

## Specification

## 规范

In order to help summarize a non-trivial task definition (e.g. an issue with a long comment thread), Copilot Workspace first generates a “topic” for the task, which takes the form of a question that can be posed against the codebase, and used to define the before/after success criteria (see the [specification](#specification) section below). 

为了帮助总结一个非平凡的任务定义（例如，一个有长评论线程的问题），Copilot Workspace 首先为任务生成一个“主题”，它以一个可以针对代码库提出的问题的形式出现，并用于定义前后的成功标准（见下面的[规范](#specification)部分）。

<img src="images/overview/topic-question.png" width=600 alt="Topic question">

*注意主题如何引入在问题标题中完全缺失的清晰度*

You can think of the topic as a way to distill the task down to its essence, and to give you an early and fast opportunity to see if Copilot Workspace is on the right track. If the topic is wrong, you don't need to continue. But if the topic is right, it helps you better understand the task, and to focus on the most important aspects of the codebase that are relevant to the task.

你可以将主题视为将任务提炼到其本质的一种方式，并为你提供一个早期和快速的机会，以查看 Copilot Workspace 是否在正确的轨道上。如果主题是错误的，你不需要继续。但如果主题是正确的，它可以帮助你更好地理解任务，并专注于与任务相关的代码库的最重要方面。

After producing the topic, Copilot Workspace generates a bulleted list describing the current behavior of the codebase, based on the task and topic being posed. This helps build your confidence that Copilot Workspace is on the right track, and serves as a means of onboarding you to the context, in cases where you might not fully understand the current state.

在生成主题之后，Copilot Workspace 会根据所提出的任务和主题生成一个描述代码库当前行为的项目符号列表。这有助于建立你对 Copilot Workspace 在正确轨道上的信心，并作为你进入上下文的一种手段，以防你可能不完全理解当前状态。

<img src="images/overview/current-spec.png" width=600 alt="Current specification">

*当前规范根据当前状态回答主题中的问题*

And if Copilot Workspace gets anything wrong, then you can easily edit/delete steps from the current spec, or even choose to regenerate an entirely new spec (“try again”). In practice, we find that these tend to be pretty good on the first try.

如果 Copilot Workspace 出现任何错误，那么你可以轻松地从当前规范中编辑/删除步骤，甚至选择重新生成一个全新的规范（“再试一次”）。在实践中，我们发现这些在第一次尝试时往往非常好。

After the current specification, Copilot Workspace generates a “proposed specification”, which is a bulleted list which articulates the state that the codebase would be in after resolving the task (effectively answering the question in the topic). And in particular, the proposed specification is focused on defining the success criteria of the task, as opposed to getting into implementation details (which is the role of the [plan](#plan)).

在当前规范之后，Copilot Workspace 会生成一个“拟议规范”，这是一个项目符号列表，阐明了解决任务后代码库的状态（有效地回答了主题中的问题）。特别是，拟议规范侧重于定义任务的成功标准，而不是进入实现细节（这是[计划](#plan)的角色）。

<img src="images/overview/proposed-spec.png" width=600 alt="Proposed specification">

*拟议规范指示如何编辑代码库以解决任务*

## Content Selection

## 内容选择

To generate the current and proposed specifications, and for all following steps, Copilot Workspace needs to identify which files in the codebase are relevant to understanding and completing the task. It does this by a combination of LLM techniques and traditional code search. The contents of the highest-ranked files are then used as context for nearly all steps in the workflow.

为了生成当前和拟议的规范，以及所有后续步骤，Copilot Workspace 需要识别代码库中哪些文件与理解和完成任务相关。它通过 LLM 技术和传统代码搜索的结合来实现这一点。然后，最高排名文件的内容被用作几乎所有工作流程步骤的上下文。

Users may review the files selected by Copilot Workspace using the "View references" button in the Specification panel. To adjust which files are selected, users can edit the task and use natural language to specify which files are relevant.

用户可以使用规范面板中的“查看参考”按钮查看 Copilot Workspace 选择的文件。要调整选择的文件，用户可以编辑任务并使用自然语言指定相关文件。

<img src="images/overview/references.png" width=600 alt="Show references dialog">

*模型用于生成原始和修改规范的参考*

## Plan

## 计划

Once you are happy with the current and proposed specs, you can request Copilot Workspace to generate a plan, which is a list of the files that need to be modified (e.g. edited, created, deleted, moved, or renamed) in order to accomplish the success criteria of the proposed spec. Additionally, each changed file includes a list of specific steps that indicate the exact changes that need to be made.

一旦你对当前和拟议的规范感到满意，你可以请求 Copilot Workspace 生成一个计划，这是一个需要修改的文件列表（例如，编辑、创建、删除、移动或重命名），以实现拟议规范的成功标准。此外，每个更改的文件都包含一个特定步骤的列表，指示需要进行的确切更改。

Like the spec, the plan is fully editable and regeneratable, which allows you to refine and steer Copilot Workspace in the right direction.

与规范一样，计划是完全可编辑和可再生的，这使你可以在正确的方向上完善和引导 Copilot Workspace。

<img src="images/overview/plan.png" width=600 alt="Plan">

*一个计划，显示了编辑一个文件和添加第二个文件所需的步骤*

## Implementation

## 实施

When you are happy with the plan, you can click the “Implement” button in order to begin implementing it. This will update the UI to display a series of queued file updates on the right side, and then begin generating the updated file contents one-by-one. When a file begins generating, its associated entry in the plan will show it as being in progress. And when it completes, the plan will indicate it as being done.

当你对计划感到满意时，你可以点击“实施”按钮以开始实施它。这将更新 UI，在右侧显示一系列排队的文件更新，然后开始逐个生成更新的文件内容。当一个文件开始生成时，其在计划中的关联条目将显示为正在进行中。当它完成时，计划将指示它已完成。

Once a file is implemented, Copilot Workspace renders a diff view for it, and automatically scrolls to the first change. The diff editors are editable, which allows making minor tweaks directly to the code, as opposed to iterating via changes to the task, spec, or plan.

一旦文件被实现，Copilot Workspace 会为其呈现一个差异视图，并自动滚动到第一个更改。差异编辑器是可编辑的，这允许直接对代码进行微调，而不是通过对任务、规范或计划的更改进行迭代。

## Iterating on Files

## 文件迭代

Copilot Workspace doesn't always get everything right, and so it makes it easy for users to iterate on the implementations file by file. Simply add, remove, edit the items in the plan steps for each file, select the checkbox, and click the "Update selected files" button. This will re-generate the contents of the selected files and update the diff view.

Copilot Workspace 并不总是能把所有事情都做对，因此它使用户可以轻松地逐个文件地迭代实现。只需添加、删除、编辑每个文件的计划步骤中的项目，选择复选框，然后点击“更新选定文件”按钮。这将重新生成选定文件的内容并更新差异视图。

For example, you can edit the diff directly, or you can go back to the plan and make changes there. And if you need to make more extensive changes, you can regenerate the plan entirely.

例如，你可以直接编辑差异，或者你可以返回计划并在那里进行更改。如果你需要进行更广泛的更改，你可以完全重新生成计划。

<img src="images/overview/file-iteration.png" width=600 alt="Plan panel with file iteration">

*计划面板使用户可以逐个文件地迭代实现*

## Integrated Terminal

## 集成终端

Once you have implemented the plan, Copilot Workspace enables you to validate the changes for correctness by bringing up an integrated terminal and executing shell commands. This allows performing a build, lint, test, etc. against the changes, and can be a quick and effective way to gain confidence about the task and its completion status. The terminal is backed by a Codespace, so it is a secure sandbox with a full development environment installed. 

一旦你实施了计划，Copilot Workspace 使你能够通过调出集成终端并执行 shell 命令来验证更改的正确性。这允许对更改执行构建、lint、测试等，并且可以是一种快速有效的方式来获得对任务及其完成状态的信心。终端由 Codespace 支持，因此它是一个安装了完整开发环境的安全沙箱。

<img src="images/overview/terminal.png" width=600 alt="Integrated terminal">

*集成终端，显示生成的分支名称和即时计算访问*

If you want to make any more extensive changes or leverage rich editor features (e.g. step debugging), you can open the Copilot Workspace session in a Codespace, using any of Codespace’s supported clients.

如果你想进行更广泛的更改或利用丰富的编辑器功能（例如，步骤调试），你可以在 Codespace 中打开 Copilot Workspace 会话，使用 Codespace 支持的任何客户端。

## Session Sharing

## 会话共享

In order to make it easy to share a workspace session with others (e.g. for doing an ad-hoc code review or sharing an initial implementation idea), Copilot Workspace allows users to generate shared links. These links can be shared with guests, even if they are not part of the Copilot Workspace preview.

为了便于与他人共享工作区会话（例如，进行临时代码审查或共享初始实现想法），Copilot Workspace 允许用户生成共享链接。这些链接可以与访客共享，即使他们不是 Copilot Workspace 预览版的一部分。

Shared sessions are copies of the original session. Non-guest users can use them as a starting point to continue the task or explore alternative solutions without interfering with the original session. Guest users can view the session but cannot use the workspace to make changes.

共享会话是原始会话的副本。非访客用户可以使用它们作为继续任务或探索替代解决方案的起点，而不会干扰原始会话。访客用户可以查看会话，但不能使用工作区进行更改。

<img src="images/overview/share-link.png" width=600 alt="Generating a share link">

*从标题栏生成共享链接*

When working with issues and pull requests, you can also

在处理问题和拉取请求时，你还可以

* Publish to issue comment. Copilot Workspace automatically generates a comment with a share link for the session, which is included in the issue. This allows reviewers to quickly access the workspace session and see the proposed changes.

* 发布到问题评论。Copilot Workspace 会自动生成一个带有会话共享链接的评论，该评论包含在问题中。这使审阅者可以快速访问工作区会话并查看拟议的更改。

* Publish to pull request comment. Similar to the issue comment, Copilot Workspace automatically generates a comment with a share link for the session, which is included in the pull request. This allows reviewers to quickly access the workspace session and see the proposed changes.

* 发布到拉取请求评论。与问题评论类似，Copilot Workspace 会自动生成一个带有会话共享链接的评论，该评论包含在拉取请求中。这使审阅者可以快速访问工作区会话并查看拟议的更改。

## Task Completion

## 任务完成

When a task is implemented, validated, and reviewed, you can complete the task in different ways, depending on the type of task you’re working on.

当一个任务被实现、验证和审查后，你可以根据你正在处理的任务类型以不同的方式完成任务。

<img src="images/overview/task-completion.png" width=600 alt="Creating a pull request">

*为已实现的更改创建拉取请求*

| Task type | Available completions | 
|-----------| -------------------- |
| Issue | — Create pull request <br> — Create draft pull request <br> — Push to new branch <br> — Push changes to current branch (only available if you have commit permissions to the repo) <br> <br> These may fork the repository if you do not have write access |
| 任务类型 | 可用完成方式 | 
| Issue | — 创建拉取请求 <br> — 创建草稿拉取请求 <br> — 推送到新分支 <br> — 推送更改到当前分支（仅在你有仓库提交权限时可用） <br> <br> 如果你没有写入权限，这些可能会分叉仓库 |
| Ad-hoc task | — *As for issues* |
| 临时任务 | — *与问题相同* |
| PR task | — Update pull request (pushes a new commit with the changes) <br> — *As for issues* |
| PR 任务 | — 更新拉取请求（推送一个包含更改的新提交） <br> — *与问题相同* |
| Repo task | — Create repository (creates a new repo from the selected template repo, and includes the changes) |
| 仓库任务 | — 创建仓库（从选定的模板仓库创建一个新仓库，并包含更改） |

## Session Dashboard

## 会话仪表板

Copilot Workspace automatically saves your work. It also provides a session dashboard, which allows you to easily resume your work later. You can start a task from your phone and then finish up on your laptop, or vice versa.

Copilot Workspace 会自动保存你的工作。它还提供了一个会话仪表板，使你可以轻松地稍后恢复工作。你可以从手机开始一个任务，然后在笔记本电脑上完成，反之亦然。

<img src="images/general/dashboard.png" width=600 alt="Copilot Workspace dashboard">

*Copilot Workspace 仪表板显示最近的、书签和已完成的会话*

Undo and redo are supported within the session via buttons on the toolbar.

会话中通过工具栏上的按钮支持撤销和重做。

## Appendix: Glossary

## 附录：术语表

| Term | Definition |
|------|------------|
| Copilot Workspace | A Copilot-native dev environment that’s designed for exploring and completing every day tasks  |
| Copilot Workspace | 一个 Copilot 原生的开发环境，旨在探索和完成日常任务 |
| Target | A branch of a codebase at a specific commit | 
| 目标 | 在特定提交时的代码库分支 | 
| Task | A natural language description of a change to a target | 
| 任务 | 对目标更改的自然语言描述 | 
| Topic | A brief single-sentence summary of a task, usually in question form |
| 主题 | 任务的简短单句摘要，通常以问题形式 |
| Specification | A description of the current and proposed state of the target as it relates to the task |
| 规范 | 与任务相关的目标当前和拟议状态的描述 |
| Plan | A list of files to add, remove or change, with notes about each of them, that together transform the target from its current state to its proposed state |
| 计划 | 要添加、删除或更改的文件列表，并附有每个文件的说明，这些文件共同将目标从当前状态转变为拟议状态 |
| Implementation | A set of changes to the target that, when applied, will complete the task |
| 实施 | 对目标的一组更改，应用后将完成任务 |
| Session | A user’s saved progress towards completing a task, a single task can have many sessions |
| 会话 | 用户完成任务的保存进度，一个任务可以有多个会话 |
| Snapshot session | A snapshot of a user’s session, created when you click “Share link”, including both the task progress and UX state |
| 快照会话 | 用户会话的快照，在你点击“共享链接”时创建，包括任务进度和用户体验状态 |
