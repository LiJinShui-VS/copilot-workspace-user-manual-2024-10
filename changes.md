## 📅 18 October 2024

- [Error repair](#error-repair)
- [Follow ups](#follow-ups)
- [Brainstorm enhancements](#brainstorm-enhancements)
- [Plan command enhancements](#plan-command-enhancements)

### Error repair

When a [build/test/run command](#commands) fails, CW now displays a lightbulb button in the command's toolbar. When you click this, it will trigger a [brainstorming](#brainstorming) action, and then offer a suggestion for how to fix the error.

当[构建/测试/运行命令](#commands)失败时，CW现在会在命令的工具栏中显示一个灯泡按钮。当你点击这个按钮时，它会触发一个[头脑风暴](#brainstorming)动作，然后提供一个修复错误的建议。

<img src="https://github.com/user-attachments/assets/db1cc14e-f3b5-49ea-a9e0-80b8b2b98bba" width="450px" />

当建议返回时，它将包括问题的解释，然后以两种形式之一呈现修复：

1. **终端命令**，可以运行以解决问题（例如，安装缺失的环境依赖项）
2. **计划更新**，可以应用，然后在受影响的文件中实现（例如，缺少的导入，类型错误）

| 终端修复 | 计划修复 |
|-|-|
| <img src="https://github.com/user-attachments/assets/f81063fe-deca-455a-9c38-07bbb336b193" width="350px" /> | <img src="https://github.com/user-attachments/assets/029729bd-a50f-4078-b764-a464a35bf4f4" width="350px" /> |

接受建议后，你可以重新运行失败的命令，并希望看到它通过。也就是说，如果你遇到另一个问题（例如，具有多个错误的构建），那么你可以继续命令+修复，直到需要为止🚀

### Follow ups

We've introduced a new capability into CW, that we're calling `Follow up`. And we're pretty excited about it 😃

我们在CW中引入了一项新功能，我们称之为`跟进`。我们对此非常兴奋😃

<img src="https://github.com/user-attachments/assets/bd881a9f-f557-4f9d-8682-25075368ad00" width="400px" />

#### Let's talk about why it's useful!

让我们谈谈为什么它有用！

When you're working against a large repository that has complex/inter-file dependencies, it's possible that a simple change/refactoring can impact many other places across the codebase (e.g. updating a shared method signature). And while the plan can do a great job of identifying the core changes needed for a task (the "primary edits"), it can sometimes miss transitive changes that are needed in response (e.g. updating callers of a changed function).

当你在一个具有复杂/文件间依赖关系的大型存储库中工作时，一个简单的更改/重构可能会影响代码库中的许多其他地方（例���，更新共享方法签名）。虽然计划可以很好地识别任务所需的核心更改（“主要编辑”），但有时会遗漏响应所需的传递更改（例如，更新更改函数的调用者）。

To address this, after you've implemented a plan, you can open up the `Commands` tab and click the new `Follow up` button. This will perform a thorough, fine-grained check on your codebase + edits, to see if any additional changes are required, in order to complete your task. And if any follow-ups are detected, it will edit the neccessary files, and add them to your existing implementation 👍

为了解决这个问题，在你实施了一个计划之后，你可以打开`命令`选项卡并点击新的`跟进`按钮。这将对你的代码库+编辑进行彻底的、细粒度的检查，以查看是否需要任何额外的更改，以完成你的任务。如果检测到任何跟进，它将编辑必要的文件，并将它们添加到你现有的实现中👍

<img src="https://github.com/user-attachments/assets/4c33b6e9-9506-4726-a018-4889b0a2d210" width="400px" />

这个工作流程非常流畅，因为它允许初始CW计划既快速又集中，这使得你更快地进入代码，并更容易审查更改的本质。在更改对整个存储库产生影响的情况下，你可以简单地触发跟进并让Copilot完成其余工作😎

#### How can you try it?

你如何尝试它？

At the moment, this experience supports codebases that are written in TypeScript/JavaScript, Python, Java, and C#. So if you're working in one of those languages, we'd love to hear your feedback! And if not, we'd love to hear whether this capability would be useful, in order to help us prioritize new languages in the future 🙏

目前，此体验支持用TypeScript/JavaScript、Python、Java和C#编写的代码库。因此，如果你正在使用这些语言之一，我们很想听到你的反馈！如果没有，我们也很想知道此功能是否有用，以帮助我们在未来优先考虑新语言🙏

And while we let this capability bake a bit, it's currently disabled by default. So if you'd like to give it a try, simply open the `Experiments` panel (under the avatar menu) and check the `Enable follow up` setting.

虽然我们让这个功能稍微成熟了一些，但它目前默认是禁用的。因此，如果你想尝试一下，只需打开`实验`面板（在头像菜单下）并勾选`启用跟进`设置。

### Brainstorm enhancements

When you open an issue in CW, or click the `Brainstorm` button for ad-hoc tasks, the initially-generated question (`How do I solve this issue?`) is now presented in a "special" structured format. The response includes two sections (`Current behavior` / `Proposed solution`), and has the advantage of allowing you to add/edit/delete/organize any of the steps, in a very granular way.

当你在CW中打开一个问题，或点击`头脑风暴`按钮进行临时任务时，最初生成的问题（`我如何解决这个问题？`）现在以“特殊”的结构化格式呈现。响应包括两个部分（`当前行为`/`建议解决方案`），并且具有允许你以非常细粒度的方式添加/编辑/删除/组织任何步骤的优点。

<img src="https://github.com/user-attachments/assets/d11ad993-6ee7-4899-a3f4-f6c896b0472d" width="700px" />

此外，由于我们将此问题视为“特殊”，因此每当你将额外的头脑风暴问题/想法附加到任务时，它会自动更新。这样，你可以继续进一步头脑风暴，并确保CW对整体解决方案的理解始终保持最新👍

### Plan command enhancements

When a plan includes a `Commands` section (e.g. because your task required installing 3rd-party dependencies), you can now execute an individual command, in addition to the existing "Execute all" support. Additionally, the completion status of commands are now persisted. So when you resume a CW session later, you can see which commands were already run, which failed, and which are still outstanding.

当一个计划包括一个`命令`部分（例如，因为你的任务需要安装第三方依赖项），你现在可以执行单个命令，除了现有的“全部执行”支持。此外，命令的完成状态现在是持久化的。因此，当你稍后恢复CW会话时，你可以看到哪些命令已经运行，哪些失败，哪些仍然未完成。

<img src="https://github.com/user-attachments/assets/ede11071-62a8-4f9c-a8a9-f91a4ddf71c0" width="300px" />

## 📅 11 October 2024

- [Commands](#commands)
   - [Running commands](#running-commands) 
   - [Command setup / inference](#command-setup--inference)
   - [NL command suggestions](#nl-command-suggestions)
   - [Plan commands](#plan-commands)   
- [Action bar mode picker](#action-bar-mode-picker)
- [Open in VS Code](#open-in-vs-code)
- [External URL context](#external-url-context)
- [Auto-completing sessions](#auto-completing-sessions)
- [High contrast mode](#high-contrast-mode)
- [Custom instructions](#custom-instructions)

### Commands

As part of our continued revamp of the CW UX (e.g. brainstorming, the action bar, file tabs/tree, etc.), we've introduced a new capability called `Commands`, which replaces the integrated terminal with a full-height panel, and provides a simplified experience for executing and configuring a build/test/run against your code. Conceptually, you can think of this as being the centralized "hub" for all tasks in the workspace that require executing a shell command.

作为我们对CW UX（例如头脑风暴、操作栏、文件标签/树等）持续改进的一部分，我们引入了一项名为`命令`的新功能，它用一个全高面板替换了集成终端，并提供了一个简化的体验，用于执行和配置针对代码的构建/测试/运行。从概念上讲，你可以将其视为工作区中所有需要执行shell命令的任务的集中“枢纽”。

<img src="https://github.com/user-attachments/assets/bb5aa0b5-c0c0-4209-871d-5079a0b28f04" width="1000px" />

And similar to [brainstorming](#brainstorming), this capability is significant enough in scope, that we need to describe it in four distinct parts 😄

与[头脑风暴](#brainstorming)类似，此功能在范围上足够重要，我们需要将其分为四个不同的部分进行描述😄

- [Running commands](#running-commands) 
- [Command setup / inference](#command-setup--inference)
- [NL command suggestions](#nl-command-suggestions)
- [Plan commands](#plan-commands)  

#### Running commands

To begin using the new `Commands` hub, simply click the existing terminal icon in the header bar. Once opened, it will automatically create and connect to a backing Codespace, so you can start running commands as needed. And if your repository has been configured with a `postAttachCommand` (in your [`devcontainer.json` file](https://containers.dev/implementors/spec/#devcontainerjson)), then you'll see a `Post attach` entry appear, that let's you view the output of its underlying shell commands.

要开始使用新的`命令`中心，只需点击标题栏中的现有终端图标。打开后，它将自动创建并连接到支持的Codespace，以便你可以根据需要开始运行命令。如果你的存储库已配置了`postAttachCommand`（在你的[`devcontainer.json`文件](https://containers.dev/implementors/spec/#devcontainerjson)中），那么你将看到一个`Post attach`条目出现，让你查看其底层shell命令的输出。

Additionally, if you've configured a `build`, `test`, or `launch` task in your `devcontainer.json`, then you can click to run any of those. This will result in the command being displayed in the list on the `Output` tab, and allow you to view its output, stop it, or re-run it once complete (e.g. to re-trigger a build after editing code).

此外，如果你在`devcontainer.json`中配置了`build`、`test`或`launch`任务，那么你可以点击运行其中任何一个。这将导致命令显示在`输出`选项卡的列表中，并允许你查看其输出，停止它，或在完成后重新运行它（例如，在编辑代码后重新触发构建）。

<img src="https://github.com/user-attachments/assets/6a0f0ecc-64f0-4871-b5f3-0840c684b85e" width="450px" />

And just like the existing terminal, if a build/test/run command starts a server, then it will be automatically forwarded, so you can securely view it.

就像现有的终端一样，如果构建/测试/运行命令启动了一个服务器，那么它将被自动转发，以便你可以安全地查看它。

#### Command setup / inference

If you haven't configured any tasks in your `devcontainer.json`, then you can simply click on either the build, test, or run command, and then type the respective shell commands into the task editor. When you do that, the entered commands will be automatically added to a `devcontainer.json` file for you, so you can include them in your subsequent PR.

如果你没有在`devcontainer.json`中配置任何任务，那么你可以简单地点击构建、测试或运行命令，然后将相应的shell命令输入到任务编辑器中。当你这样做时，输入的命令将自动添加到一个`devcontainer.json`文件中，以便你可以将它们包含在后续的PR中。

And if you don't know how to perform a build/test/run on the current repo, then simply click the lightbulb icon next to a task and let CW suggest how to do it for you 🚀

如果你不知道如何在当前存储库上执行构建/测试/运行，那么只需点击任务旁边的灯泡图标，让CW建议如何为你执行🚀

<img src="https://github.com/user-attachments/assets/2db837df-33db-4608-8674-54d36ae5e9f7" width="500px" />

#### NL command suggestions

While we've optimized the UX for building, testing, and running your code, there are many other tasks you might need to perform during a session (e.g. linting, formatting, etc.). And to make that simpler, the action bar now enters "command mode" (when you're focused on the `Commands` tab), which lets you describe a shell command you want to run, using only natural language.

虽然我们已经优化了构建、测试和运行代码的用户体验，但在会话期间你可能还需要执行许多其他任务（例如，代码检查、格式化等）。为了简化这一过程，操作栏现在进入“命令模式”（当你专注于`命令`选项卡时），这让你可以仅使用自然语言描述你想要运行的shell命令。

After typing an NL request, you'll be presented with a command suggestion, which you can edit or regenerate. And if you click the `Run` button, it will open the `Terminal` tab on the `Commands` hub, and execute it on your behalf.

在输入NL请求后，你将看到一个命令建议，你可以编辑或重新生成。如果你点击`运行`按钮，它将打开`命令`中心的`终端`选项卡，并代表你执行它。

<img src="https://github.com/user-attachments/assets/d4dbb27e-3f78-43f7-8e94-d68caa2ae9ce" width="500px" />

#### Plan commands

The "plan commands" feature is now on by default, and when a plan includes shell commands (e.g. running a package manager to include a new dependency), it will execute them via a new `Plan` command entry in the `Commands` tab.

“计划命令”功能现在默认开启，当一个计划包括shell命令（例如，运行包管理器以包含新依赖项）时，它将通过`命令`选项卡中的新`计划`命令条目执行它们。

<img src="https://github.com/user-attachments/assets/60ed8f3d-013f-461f-a143-9d642be5e64e" width="700px" />

### Action bar mode picker

The action bar now allows you to seamlessly switch between its three modes: `Ask`, `Revise`, and `Command`. This ensures that regardless what state your session is in, you can ask a question, revise the plan/implemented files, or execute a terminal command. All using natural language 💙

操作栏现在允许你无缝切换其三种模式：`询问`、`修订`和`命令`。这确保了无论你的会话处于何种状态，你都可以提出问题，修订计划/实施的文件，或执行终端命令。所有这些都使用自然语言💙

<img src="https://github.com/user-attachments/assets/93c6664e-66ad-42a3-96b5-3e9a4cdad099" width="600px" />

Even cooler, you can switch between any of these modes using the following keyboard shortcuts, which make it really easy to navigate a session, while jumping between brainstorming, code iteration, and terminal actions.

更酷的是，你可以使用以下键盘快捷键在这些模式之间切换，这使得在头脑风暴、代码迭代和终端操作之间跳转时，导航会话变得非常容易。

| Mode | Keyboard shortcut |
|-|-|
| 模式 | 键盘快捷键 |
| 询问 | <kbd>?</kbd> |
| 修订 | <kbd>></kbd> |
| 命令 | <kbd>$</kbd> |

Additionally, each mode retains a history of its previous request. So if you realize you wanted to ask a question a slightly different way, or make a subtly different revision, then simply hit the up arrow, edit, and submit👍

此外，每种模式都会保留其先前请求的历史记录。因此，如果你意识到你想以稍微不同的方式提出问题，或进行微妙的修订，那么只需点击向上箭头，编辑并提交👍

> By introducing the new `Commands` tab, and allowing all three of the action bar's modes to be usable at any time, the action bar is now the official "central nervous system" for the entire CW experience. We've really fallen in love with how it feels to start and iterate on tasks now. And we're excited to hear how it feels for everyone else! 👋

> 通过引入新的`命令`选项卡，并允许操作栏的所有三种模式在任何时候都可用，操作栏现在是整个CW体验的官方“中枢神经系统”。我们真的爱上了现在开始和迭代任务的感觉。我们很高兴听到其他人的感受！👋

### Open in VS Code

After a month of _amazing_ feedback from our preview users, we've officially published the [Copilot Workspace extension](https://gh.io/cw-vscode ) to the VS Code marketplace 🥳

在一个月的预览用户_惊人_反馈之后，我们正式将[Copilot Workspace扩展](https://gh.io/cw-vscode)发布到VS Code市场🥳

And in order to make it even easier to use, we've introduced a new `Open in VS Code` button to the CW session header. When you click it, we'll launch VS Code, and open your current session directly from within the editor. That way you can start tasks and brainstorm from the web (or your phone!), and when you want to jump into VS Code to finish it off (e.g. step-debug some code), you can now do that in a single-click💪

为了使其更易于使用，我们在CW会话标题中引入了一个新的`在VS Code中打开`按钮。当你点击它时，我们将启动VS Code，并直接从编辑器中打开你当前的会话。这样，你可以从Web（或手机！）开始任务和头脑风暴，当你想跳到VS Code中完成它时（例如，逐步调试一些代码），你现在可以一键完成💪

<img src="https://github.com/user-attachments/assets/1928f16e-3663-4d6e-becb-8cd409fb4430" width="500px" />

Additionally, the official extension release also includes a ton of new capabilities that make the E2E experience a lot better. In particular, we've enhanced the `Sessions` and `Plan` views in the following ways...

此外，官方扩展发布还包括大量新功能，使E2E体验更好。特别是，我们通过以下方式增强了`会话`和`计划`视图...

#### `Sessions` view

In order to make it easier to manage _many_ sessions, your sessions list is now grouped by repository, and each session displays an icon based on its respective type: issue, task, or PR. Additionally, when you're done with a session, you can now delete it directly from the editor, by hovering over it and clicking the trash can icon.

为了更容易管理_许多_会话，你的会话列表现在按存储库分组，每个会话根据其各自的类型显示一个图标：问题、任务或PR。此外，当你完成一个会话时，你现在可以通过悬停在其上并点击垃圾桶图标直接从编辑器中删除它。

<img src="https://github.com/user-attachments/assets/70513fd2-cb7e-416c-9ee6-90c0780d4f21" width="350px" />

#### `Plan` view

The VS Code extension now has full parity with the CW web client, when it comes to iterating on the plan and code in a session. And in particular, you can now perform the following actions on the plan, directly from the `Plan` view:

VS Code扩展现在在会话中迭代计划和代码时与CW Web客户端完全一致。特别是，你现在可以直接从`计划`视图对计划执行以下操作：

1. Adding, editing, and deleting files
2. Adding, editing, and deleting steps for a file
3. Re-organizing the plan, by moving/indenting files and steps

1. 添加、编辑和删除文件
2. 添加、编辑和删除文件的步骤
3. 通过移动/缩进文件和步骤重新组织计划

To access these new capabilities, simply click the `...` menu next to a file or step in the plan. We're pretty happy with how this experience "feels", and we're looking forwarding to hearing more feedback🙌

要访问这些新功能，只需点击计划中文件或步骤旁边的`...`菜单。我们对这种体验的“感觉”非常满意，并期待听到更多反馈🙌

| 计划文件操作 | 计划步骤操作 |
|-|-|
| <img src="https://github.com/user-attachments/assets/6836d12c-7977-4d34-8760-0456d547e89f" width="400px" /> | <img src="https://github.com/user-attachments/assets/62e0b417-2d64-4597-8055-d7e34bdd70ce" width="360px" /> |

> If you use VS Code Insiders, then set the `Open in VS Code Insiders` setting, and the `Open in VS Code` button which launch Insiders instead of Stable.

> 如果你使用VS Code Insiders，那么设置`在VS Code Insiders中打开`设置，并且`在VS Code中打开`按钮将启动Insiders而不是Stable。

### External URL context

We've enabled external URL fetching by default, and made the following improvements to the overall user experience:

我们默认启用了外部URL获取，并对整体用户体验进行了以下改进：

1. The content of external URLs are now included in the context while brainstorming. This is cool because it allows you to ask questions and ensure they can "see" any meaningful context you've added to the task (e.g. GitHub issues, external documentation)
2. You can now enable/disable individual URLs from the `Task` panel, which allows you to control which external content is used as context, without needing to modify the task description.

1. 在头脑风暴时，外部URL的内容现在包含在上下文中。这很酷，因为它允许你提出问题，并确保他们可以“看到”你添加到任务中的任何有意义的上下文（例如，GitHub问题，外部文档）
2. 你现在可以从`任务`面板启用/禁用单个URL，这允许你控制哪些外部内容用作上下文，而无需修改任务描述。

<img src="https://github.com/user-attachments/assets/3937dcfd-db48-4e4b-8366-a76d1e06fee1" width="350px" />

> Note: If you'd like to disable external URLs from being enabled by default, then you can turn off the `Automatically include external URLs in context` setting in your `Settings` panel (underneath the avatar menu).

> 注意：如果你想禁用默认启用的外部URL，那么你可以在`设置`面板（在头像菜单下）中关闭`自动在上下文中包含外部URL`设置。

### Auto-completing sessions

We introduced a new setting that allows you to automatically mark sessions as complete after creating a PR/branch/repo for them. For users that create many sessions, this can help keep your `Recent sessions` list (on the [dashboard](https://copilot-workspace.githubnext.com)) nice and clean. And if you later decide that you need to continue a session that was marked as complete, you can always resume it from the [Completed sessions list](https://copilot-workspace-dev.githubnext.com/?view=completed) at any time :thumb:

我们引入了一个新设置，允许你在为会话创建PR/分支/存储库后自动将会话标记为完成。对于创建许多会话的用户，这可以帮助保持你的`最近会话`列表（在[仪表板](https://copilot-workspace.githubnext.com)上）整洁干净。如果你稍后决定需要继续一个标记为完成的会话，你可以随时从[已完成会话列表](https://copilot-workspace-dev.githubnext.com/?view=completed)中恢复它:thumb:

> To enable this behavior, open your user `Settings` (underneath the avatar menu in the upper-right), and select the `Mark sessions as complete after committing` option.

> 要启用此行为，请打开用户`设置`（在右上角的头像菜单下），并选择`提交后将会话标记为完成`选项。

### High contrast mode

CW already supports a light and dark color theme, and will match your system preference automatically. However, to further improve usability for all users, we've introduced support for a new high-contrast mode of both color themes.

CW已经支持浅色和深色主题，并将自动匹配你的系统偏好。然而，为了进一步提高所有用户的可用性，我们引入了对两种颜色主题的新高对比度模式的支持。

<img src="https://github.com/user-attachments/assets/e54a0d92-901e-44c5-9d11-d7c3f812a6c5" width="800px" />

> To enable this behavior, open your user `Settings` (underneath the avatar menu in the upper-right), and select the `Enable high contrast mode` option.

> 要启用此行为，请打开用户`设置`（在右上角的头像菜单下），并选择`启用高对比度模式`选项。

### Custom instructions

CW now supports configuring repo-wide custom instructions via a `.github/copilot-instructions.md` file, in addition to the existing file location (`.github/copilot-workspace/CONTRIBUTING.md`). If a repo includes a `.github/copilot-instructions.md` file, then it will take precedence over `.github/copilot-workspace/CONTRIBUTING.md` (we don't "merge" the contents if you define both). Otherwise, both files support the exact same set of features and user experience (e.g. the `Task` panel will show custom instructions as additional context, and external URLs in the instructions will be fetched).

CW现在支持通过`.github/copilot-instructions.md`文件配置整个存储库的自定义指令，除了现有的文件位置（`.github/copilot-workspace/CONTRIBUTING.md`）。如果一个存储库包含一个`.github/copilot-instructions.md`文件，那么它将优先于`.github/copilot-workspace/CONTRIBUTING.md`（如果你定义了两个，我们不会“合并”内容）。否则，这两个文件支持完全相同的功能和用户体验（例如，`任务`面板将显示自定义指令作为附加上下文，并且指令中的外部URL将被获取）。

## 📅 27 September 2024

- [Brainstorming](#brainstorming)
   - [Project exploration / learning](#project-exploration--learning)
   - [Solution proposals](#solution-proposals)
   - [Asking questions](#asking-questions)
   - [Explaining / reviewing code](#explaining--reviewing-code)
- [Create new repository](#create-new-repository)
- [VS Code: Implement/revise specific files](#vs-code-implementrevise-specific-files)
- [File tree filtering](#file-tree-filtering)
- [Plan step filtering](#plan-step-filtering)
- [Improved build/test/run inference](#improved-buildtestrun-inference)
- [Plan + implement](#plan--implement)
- [URL context management](#url-context-management)

### Brainstorming

We've introduced a major new CW capability that we're calling "brainstorming" (💡). And it represents such a significant change, that it needs to be described in four distinct parts 🤗

我们引入了一项重要的新CW功能，我们称之为“头脑风暴”（💡）。它代表了一个如此重大的变化，以至于需要分为四个不同的部分进行描述🤗

- [Project exploration / learning](#project-exploration--learning)
- [Solution proposals](#solution-proposals)
- [Asking questions](#asking-questions)
- [Explaining / reviewing code](#explaining--reviewing-code)

<img src="https://github.com/user-attachments/assets/a4884997-43cb-4b84-a414-d407f3a87e28" width="700px" />

> Note: This feature isn't currently enabled by default. So if you'd like to try it, then enable the `Activate brainstorming` setting in your `Experiments` panel.

> 注意：此功能目前默认未启用。因此，如果你想尝试一下，请在`实验`面板中启用`激活头脑风暴`设置。

#### Project exploration / learning

At its core, CW aspires to be an "AI thought partner" that can enable developers to complete everyday tasks, **while learning along the way**. And while the `Specification` panel has successfully helped preview users create thousands of pull requests, it's been clear for a while that we could do a lot better. And in particular, help reduce the activation energy in getting started, **even before you've typed a single character.**

在其核心，CW致力于成为一个“AI思维伙伴”，可以使开发人员完成日常任务，**同时在此过程中学习**。虽然`规范`面板成功地帮助预览用户创建了数千个拉取请求，但很明显，我们可以做得更好。特别是，帮助减少入门的激活能量，**即使在你输入一个字符之前**。

To that end, when you start a new task in CW, you'll now notice a green `Brainstorm` button in the `Task` panel.

为此，当你在CW中开始一个新任务时，你现在会在`任务`面板中注意到一个绿色的`头脑风暴`按钮。

<img src="https://github.com/user-attachments/assets/0cb62eff-f676-403e-962b-2becf13f7a5c" width="600px" />

If you click it, it will open a new tab (called `Brainstorm`) and suggest a list of questions that might be relevant for you, in either onboarding to the repository, or learning a bit more about specific behavior/topics (e.g. how to buikd VS Code extensions).

如果你点击它，它将打开一个新选项卡（称为`头脑风暴`），并建议一系列可能与你相关的问题，无论是入职存储库，还是了解更多关于特定行为/主题的信息（例如，如何构建VS Code扩展）。

<img src="https://github.com/user-attachments/assets/29cb8a3b-89c6-4479-8c81-2dc95fd8758b" width="850px" />

When you click one of these questions, CW will generate an answer to it, using the same repository-wide context that you've already come to know and love💙

当你点击其中一个问题时，CW将生成一个答案，使用你已经知道和喜爱的相同的存储库范围的上下文💙

<img src="https://github.com/user-attachments/assets/ffa12858-e332-4407-bc9a-fe9c2a8dcd37" width="800px" />

Even cooler, as you select questions, the `Suggestion questions` list will dynamically update to include new, and potentially interesting questions based on your selections. Kind of like a dynamic search engine for code, that can "push" insights at you, instead of waiting for you to ask⭐

更酷的是，当你选择问题时，`建议问题`列表将动态更新，以包括基于你的选择的新问题和潜在有趣的问题。有点像代码的动态搜索引擎，可以“推送”见解给你，而不是等待你提问⭐

And as with all things in CW, a generated answer can be edited, regenerated, or deleted. And if you find something especially useful, you can even add it as context to the task, which will inform the subsequent planning/code generation.

与CW中的所有事物一样，生成的答案可以编辑、重新生成或删除。如果你发现某些特别有用的东西，你甚至可以将其添加为任务的上下文，这将通知后续的计划/代码生成。

<img src="https://github.com/user-attachments/assets/9f6402ca-fdda-461e-a8be-b34feb737bd4" width="300px" />

When a brainstorming question is added to the task, it will show up in the task via a new section called `Ideas from brainstorming`. And while it may seem silly, we love this title so much. Why? Because it represents the notion that ideas are the output of brainstorming. And ultimately, we want CW to help you produce new and better ideas💙

当一个头脑风暴问题被添加到任务中时，它将通过一个名为`头脑风暴的想法`的新部分显示在任务中。虽然这可能看起来很傻，但我们非常喜欢这个标题。为什么？因为它代表了想法是头脑风暴的产物。最终，我们希望CW帮助你产生新的和更好的想法💙

Interestingly enough, this behavior means that you can actually work on tasks with CW, without ever actually typing a task description. You simply perform brainstorming, attach the associated ideas, and then move on to the plan/implementation. However, in order for this to work well, you obviously need to be able to describe your intent or to guide CW in the direction that you want to go. So let's see how that works!

有趣的是，这种行为意味着你实际上可以在没有实际输入任务描述的情况下与CW一起工作。你只需进行头脑风暴，附加相关的想法，然后继续计划/实施。然而，为了使其正常工作，你显然需要能够描述你的意图或引导CW朝你想要的方向前进。所以让我们看看它是如何工作的！

#### Solution proposals

If you click the `Brainstorm` button _after_ you've typed a task description, then instead of simply getting a list of suggested questions, CW will actually present you with a proposal for how to solve your task. And this is where things get really fun😎

如果你在输入任务描述_之后_点击`头脑风暴`按钮，那么CW实际上会向你提出一个解决任务的建议，而不仅仅是获得一系列建议问题。这就是事情变得非常有趣的地方😎

When a brainstorming question can result in multiple solutions/parts, then instead of simply answering it, CW will present you with a list of **ideas**, and allow you to select one, many, or all of them. That way, you can compose your intent by brainstorming with CW, and derive ideas through this collaborative process. Additionally, just like "single answer questions", you can regenerate the question to get new ideas, and then edit/refine them as needed. And as you select ideas, the `Suggested questions` will dynamically update, in order to provide you a pathway towards other interesting questions, which might be worthy of further brainstorming🧠

当一个头脑风暴问题可以产生多个解决方案/部分时，CW不会简单地回答它，而是向你展示一个**想法**列表，并允许你选择一个、多个或全部。这样，你可以通过与CW头脑风暴来构思你的意图，并通过这个协作过程得出想法。此外，就像“单一答案问题”一样，你可以重新生成问题以获得新想法，然后根据需要编辑/完善它们。当你选择想法时，`建议问题`将动态更新，以便为你提供通向其他有趣问题的途径，这些问题可能值得进一步头脑风暴🧠

<img src="https://github.com/user-attachments/assets/21c3d2bb-1e2b-44ff-85ac-499e28018033" width="600px" />

> Note: When you open an issue in CW, it will automatically launch the `Brainstorm` tab, and present you with the same experience as manually entered tasks. In this sense, the default `How do I solve this issue?` brainstorming question represents an alternative to the `Specification` panel, but has the benefit of being much more rich and flexible in nature.

> 注意：当你在CW中打开一个问题时，它会自动启动`头脑风暴`选项卡，并为你提供与手动输入任务相同的体验。从这个意义上说，默认的`我如何解决这个问题？`头脑风暴问题代表了`规范`面板的替代方案，但具有更丰富和灵活的性质。

#### Asking questions

While the default brainstorming experience can help you to learn about repositories, and think through solutions for tasks/issues, it's also important that you can ask arbitrary other questions, in your pursuit of learning/task completion. And to solve that, the existing "NL revision bar" (the pretty textbox that let's you revise the plan/code) has now been converted into an "action bar". This bar is now always visible, and when you start a new task or open an issue/repo, it will present you with a new prompt: `Ask a question...`.

虽然默认的头脑风暴体验可以帮助你了解存储库，并思考任务/问题的解决方案，但在你追求学习/任务完成的过程中，你也可以提出任意其他问题，这一点也很重要。为了解决这个问题，现有的“NL修订栏”（漂亮的文本框，让你修订计划/代码）现在已转换为“操作栏”。此栏现在始终可见，当你开始一个新任务或打开一个问题/存储库时，它会向你显示一个新提示：`提出一个问题...`。

<img src="https://github.com/user-attachments/assets/951c8391-7f42-40d9-a53d-52e0a028a6ce" width="500px" />

When you enter and submit a question, it will launch the `Brainstorm` tab, and start to generate an answer, which will include multiple ideas if relevant, and allow you to edit/refine it as needed. And again, as you ask new and interesting questions, you can attach those as context for the task, and the `Suggested questions` list will continue to provide you would potentially interesting follow-ups.

当你输入并提交一个问题时，它将启动`头脑风暴`选项卡，并开始生成答案，如果相关，将包括多个想法，并允许你根据需要编辑/完善它。再次，当你提出新的和有趣的问题时，你可以将这些问题作为任务的上下文附加，并且`建议问题`列表将继续为你提供潜在有趣的后续问题。

Additionally, questions can be asked at any time. And so while you can ask questions at the start of a task, you can also ask them after planning, impmementing or revising. Which leads up to our next part!

此外，问题可以随时提出。因此，虽然你可以在任务开始时提出问题，但你也可以在计划、实施或修订后提出问题。这引出了我们的下一部分！

#### Explaining / reviewing code

After you've implemented a plan, you'll notice two new buttons in the file diff headers (within the `Files changed` tab), which allow you to enter brainstorming mode in two interesting ways:

在你实施了一个计划之后，你会注意到文件差异标题中有两个新按钮（在`文件更改`选项卡中），这允许你以两种有趣的方式进入头脑风暴模式：


