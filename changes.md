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

当你在一个具有复杂/文件间依赖关系的大型存储库中工作时，一个简单的更改/重构可能会影响代码库中的许多其他地方（例如，更新共享方法签名）。虽然计划可以很好地识别任务所需的核心更改（“主要编辑”），但有时会遗漏响应所需的传递更改（例如，更新更改函数的调用者）。

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

1. Explaining the changes that were made to the file
2. Exploring ideas about how to improve the file further

1. 解释对文件所做的更改
2. 探索如何进一步改进文件的想法

<img src="https://github.com/user-attachments/assets/3968d4ba-a5b5-42bf-96f4-0df4ecf241b9" width="600px" />

These allow you to extend the learning process into a specific change, and make sure that you fully understand the "what?" and "why?" behind an edit, before you ever send a PR.

这些允许你将学习过程扩展到特定的更改中，并确保在你发送PR之前，完全理解编辑背后的“是什么？”和“为什么？”。

<img src="https://github.com/user-attachments/assets/16d6f4f9-5e78-4964-8233-177fcacba980" width="800xp" />

Additionally, by being able to brainstorm with CW on a changed file, you can effectively perform a lightweight code review with it, and get some simple follow-up suggestions. Just in case there's anything else worth doing👍

此外，通过能够在更改的文件上与CW进行头脑风暴，你可以有效地进行轻量级代码审查，并获得一些简单的后续建议。以防还有其他值得做的事情👍

<img src="https://github.com/user-attachments/assets/36193fcb-a5f8-4e72-abe0-0822eb3a7440" width="800px" />

And as if that wasn't enough...the next section is effectively also an extension of brainstorming. But I felt like this section was getting long enough, so I decided to break it up😄

如果这还不够...下一部分实际上也是头脑风暴的扩展。但我觉得这一部分已经够长了，所以我决定把它分开😄

### Create new repository

You can now easily create new repositories from CW, by visiting the [dashboard](https://copilot-workspace.githubnext.com) and clicking the `Create new repository` button at the bottom of the `Recent repositories` section.

你现在可以通过访问[仪表板](https://copilot-workspace.githubnext.com)并点击`最近的存储库`部分底部的`创建新存储库`按钮，从CW轻松创建新存储库。

<img src="https://github.com/user-attachments/assets/bf25ea62-db58-489b-ba81-55aeaf49d796" width="500px" />

This will take you into a new session where you can define (or brainstorm!) what you want the new repo to include. And when you finish planning/implementing the code, you can click the `Create repository` button to create the repository and then commit your changes.

这将带你进入一个新会话，你可以在其中定义（或头脑风暴！）你希望新存储库包含的内容。当你完成计划/实施代码时，你可以点击`创建存储库`按钮来创建存储库，然后提交你的更改。

<img src="https://github.com/user-attachments/assets/e1c8b1b9-ca3a-40ea-a25f-3929772aa19e" width="800px" />

Additionally, if you'd like to create a repository from an existing template (as opposed to a blank repo), then simply click the `Choose a repository` link from the dashboard, search for the template you want to use (e.g. `express starter`), and then select it. This will take you into the same "new repo" flow as above, but will display a `Template` panel with the template's `README` contents in it. Between the new repo + template repo flow, and the addition of brainstorming, we're excited to see how much we can improve the process of bootstrapping new projects💙

此外，如果你想从现有模板创建一个存储库（而不是一个空白存储库），那么只需从仪表板中点击`选择一个存储库`链接，搜索你想要使用的模板（例如`express starter`），然后选择它。这将带你进入与上述相同的“新存储库”流程，但会显示一个包含模板`README`内容的`模板`面板。在新存储库+模板存储库流程之间，以及头脑风暴的添加，我们很高兴看到我们可以在多大程度上改进引导新项目的过程💙

### VS Code: Implement/revise specific files

The CW extension for VS Code now allows you to select specific files in the plan that you'd like to implement (by selecting their respective checkboxes in the `Plan` view). Additionally, you can now NL-revise specific files as well, by clicking the target icon in their file tab, and then entering the change you'd like to make.

VS Code的CW扩展现在允许你选择计划中你想要实现的特定文件（通过在`计划`视图中选择各自的复选框）。此外，你现在还可以通过点击文件标签中的目标图标，然后输入你想要进行的更改来NL修订特定文件。

Even cooler, you can NL-revise a file that isn't even part of the plan, and it will be added + revised automatically for you. These two changes match the behavior of the CW web/mobile client, and effectively round out the core iteration/feedback loop within VS Code.

更酷的是，你可以NL修订一个甚至不是计划一部分的文件，它将自动为你添加+修订。这两个更改与CW Web/移动客户端的行为相匹配，并有效地完善了VS Code中的核心迭代/反馈循环。

<img src="https://github.com/user-attachments/assets/a57ac8d8-d7a4-4cb9-b3da-c24bd91412a6" width="800px" />

> Note: Since this extension is early, we're still not quite ready to publish it to the marketplace. We'll likely do that in the next couple of weeks, but until then, simply hit us up in [Discord](https://gh.io/next-discord) to grab the latest VSIX😎

> 注意：由于此扩展尚处于早期阶段，我们仍未准备好将其发布到市场。我们可能会在接下来的几周内这样做，但在此之前，只需在[Discord](https://gh.io/next-discord)中联系我们以获取最新的VSIX😎

### File tree filtering

The integrated file tree now allows filtering it to show only the files that have changed in the session (along with their parent directories). This makes it easier to contextualize the changes being made, through the lens of your repository's folder structure. Additionally, this setting is persisted as part of the session, and so if you toggle it, it will remain filtered whenever you resume working on it later (including from your phone!).

集成文件树现在允许过滤它以仅显示会话中已更改的文件（以及它们的父目录）。这使得通过存储库的文件夹结构来上下文化所做的更改变得更容易。此外，此设置作为会话的一部分持久化，因此如果你切换它，每当你稍后继续工作时，它将保持过滤状态（包括从手机上）。

<table>
   <tr>
      <th>Before filtering</th>
      <th>After filtering</th>
   </tr>
   <tr>
      <td><img src="https://github.com/user-attachments/assets/9b98e458-bc2d-464b-ab23-9e7aace17802" width="300px" /></td>
      <td><img src="https://github.com/user-attachments/assets/d57dfe8e-7d13-448f-a41a-294d92b6e314" width="300px" /></td>
   </tr>
</table>

### Plan step filtering

The `Plan` panel now allows filtering it to show only the steps that were introduced in the last revision/edit (and their associated files). As a plan grows in size/complexity, this filter can make it alot easier to focus your attention on only the steps that were recently made, and therefore, would benefit from a closer review. This filter builds upon the previously-added blue dots (which indicate an "unseen" plan step), and represent another step towards making plan revision feel much more incremental and easy to follow:muscle:

`计划`面板现在允许过滤它以仅显示上次修订/编辑中引入的步骤（及其关联文件）。随着计划的规模/复杂性增加，此过滤器可以使你更容易专注于最近做出的步骤，因此，这些步骤将受益于更仔细的审查。此过滤器基于先前添加的蓝点（表示“未见”计划步骤），并代表了使计划修订感觉更加增量和易于遵循的另一步骤:muscle:

<table>
   <tr>
      <th>Before filtering</th>
      <th>After filtering</th>
   </tr>
   <tr>
      <td><img src="https://github.com/user-attachments/assets/88a5e18f-cfce-4cc1-8291-d807e9e92908" width="300px" /></td>
      <td><img src="https://github.com/user-attachments/assets/550dc719-890f-4b43-9c65-6a6460901a00" width="400px" /></td>
   </tr>
</table>

### Improved build/test/run inference

When you click the `Build`, `Test` or `Run` buttons in the integrated terminal, CW will now provide better suggestions for the neccessary shell commands needed to run them. In particular, we now include any Actions workflows, package manifests (e.g. `package.json`), and the `CONTRIBUTING.md` file (if it exists) in the context, which allows CW to more properly infer the best way to build/test/run your code.

当你点击集成终端中的`构建`、`测试`或`运行`按钮时，CW现在将为运行它们所需的必要shell命令提供更好的建议。特别是，我们现在在上下文中包含任何Actions工作流、包清单（例如`package.json`）和`CONTRIBUTING.md`文件（如果存在），这使得CW能够更正确地推断出构建/测试/运行代码的最佳方式。

<img src="https://github.com/user-attachments/assets/d0a89f46-d447-49d6-84f1-b623e41441f2" width="600px" />

### Plan + implement

After writing/editing a task, you can now generate the plan and implementation in a single step. As opposed to generating the plan, and then clicking the `Implement` button after its done. For simple/straight-forward tasks, this gives you the option to jump straight to code, and then refine things further from there. And if you notice that the plan isn't quite right while the code is being generated, you can easily cancel, revise the plan, and then re-implement. That way you don't lose any steerability when taking advantage of this shortcut😎

在编写/编辑任务后，你现在可以在一个步骤中生成计划和实施。与生成计划相反，然后在完成后点击`实施`按钮。对于简单/直接的任务，这使你可以选择直接跳到代码，然后从那里进一步完善。如果你注意到在生成代码时计划不太正确，你可以轻松取消，修订计划，然后重新实施。这样，在利用此快捷方式时，你不会失去任何可控性😎

<img src="https://github.com/user-attachments/assets/827a850a-ca2b-4e05-8abf-15eec6d3609b" width="400px" />

### URL context management

When a task references external URLs (e.g. docs), you can now exclude them from the session context, by clicking their associated trash can icon (within the `Additional context` section of the `Task` panel). Behind the scenes, this simply updates the task description by wrapping the selected URL in backticks (so that it's treated as raw markdown). But since a URL might be buried in an issue description/call stack, or could occur multiple times within the task definition, this new button should make it a lot easier to properly manage the context that you want CW to consider👍

当一个任务引用外部URL（例如，文档）时，你现在可以通过点击其关联的垃圾桶图标（在`任务`面板的`附加上下文`部分内）将其排除在会话上下文之外。在幕后，这只是通过将选定的URL用反引号包裹来更新任务描述（以便将其视为原始markdown）。但由于URL可能埋在问题描述/调用堆栈中，或可能在任务定义中多次出现，此新按钮应使你更容易正确管理你希望CW考虑的上下文👍

<img src="https://github.com/user-attachments/assets/0366732a-b949-4f6f-b471-8e4bb1526081" width="600px" />

## 📅 20 September 2024

- [Plan commands](#plan-commands)
- [Integrated file tree](#integrated-file-tree)
- [New plan step indicators](#new-plan-step-indicators)
- [Latest changes filter](#latest-changes-filter)
- [Devcontainer tasks improvements](#devcontainer-tasks-improvements)
- [VS Code: Planning & implementing](#vs-code-planning--implementing)
- [URL task context](#url-task-context)
- [Cancellation improvements](#cancellation-improvements)

### Plan commands

In addition to adding/editing/deleting code, the `Plan` can now include terminal commands, whenever they're needed to properly complete a task. For example, if a task requires the use of a new 3rd-party dependency, then instead of editing a package manifest file (e.g. `package.json`), the plan will now suggest running the appropriate package manager (e.g. `npm install`). This has the advantage of ensuring you install the latest dependency version, as well as updating any respective lock files.

除了添加/编辑/删除代码外，`计划`现在可以包括终端命令，只要它们是正确完成任务所需的。例如，如果一个任务需要使用新的第三方依赖项，那么计划现在将建议运行适当的包管理器（例如`npm install`），而不是编辑包清单文件（例如`package.json`）。这具有确保你安装最新依赖项版本以及更新任何相应锁定文件的优点。

Like everything else in CW, this new `Commands` section is fully editable, and so you can take, tweak, or ignore the provided suggestions. However, once you're happy with them, you can simply click the `Execute all` button, which will spin up the integrated terminal (if needed), run the commands, and then display their status. Any files that are edited as a result of these commands being executed, will then be displayed in the `Files changed` list, just like if you edited them directly🙌

与CW中的其他所有内容一样，这个新的`命令`部分是完全可编辑的，因此你可以接受、调整或忽略提供的建议。然而，一旦你对它们感到满意，你只需点击`全部执行`按钮，这将启动集成终端（如果需要），运行命令，然后显示其状态。由于执行这些命令而编辑的任何文件将显示在`文件更改`列表中，就像你直接编辑它们一样🙌

<img src="https://github.com/user-attachments/assets/98e82301-450e-45f0-8f02-3ff422cc3695" width="400px" />

> Note: This feature isn't currently enabled by default. So if you'd like to give it a try, you'll need to open your avatar menu in the upper-right, select `Experiments`, and then check the `Allow shell command generation in the plan` setting.

> 注意：此功能目前默认未启用。因此，如果你想尝试一下，你需要打开右上角的头像菜单，选择`实验`，然后勾选`允许在计划中生成shell命令`设置。

### Integrated file tree

We've replaced the file explorer modal with a new integrated file tree, which is displayed as a right-side panel, and retains all of the same features as before (e.g. file name filtering, change annotations). This has the advantage of allowing you to navigate the repository's files, while simultaneously viewing the task/spec/plan and code. Additionally, when you select a file from the tree, it now opens the file as a tab. This is nice, because you can then immediately perform an NL revision to it, which makes the flow of editing new files extremely simple: filter for it in the tree, open it, then revise it💙

我们用一个新的集成文件树替换了文件资源管理器模式，它显示为右侧面板，并保留了以前的所有相同功能（例如，文件名过滤，更改注释）。这具有允许你导航存储库文件的优点，同时查看任务/规范/计划和代码。此外，当你从树中选择一个文件时，它现在作为一个标签打开文件。这很好，因为你可以立即对其进行NL修订，这使得编辑新文件的流程非常简单：在树中过滤它，打开它，然后修订它💙

![image](https://github.com/user-attachments/assets/24c299a9-54d8-4d15-8b35-f28489997403)

### New plan step indicators

When you perform an NL revision against the plan, new plan steps are now annotated with a blue dot. This is meant to indicate that they are "unseen", and help focus your attention on the net-new changes that were made, as a result of your request. This experience builds upon the previous change to make plan revision incremental, and we think it makes the overall iteration flow feel a lot more predictable (e.g. you don't have to try to spot what changes CW made based on your request).

当你对计划执行NL修订时，新计划步骤现在用蓝点注释。这意味着它们是“未见”的，并帮助你专注于由于你的请求而做出的净新更改。这种体验基于先前的更改，使计划修订增量化，我们认为这使得整体迭代流程感觉更加可预测（例如，你不必尝试发现CW根据你的请求做出了哪些更改）。

In order to prevent these dots from becoming noisy, they're only visible until the next time you 1) edit the plan, or 2) perform a subsequent revision/implementation. That way, they always indicate steps you haven't "seen", and don't accumulate as you further iterate on your session. Additionally, the dots aren't added to plan steps you add/edit yourself. And they don't persist across browser refreshes. That way, they simply represent AI-contributed changes, that were introduced by a just-made revision👍

为了防止这些点变得嘈杂，它们仅在下次1）编辑计划或2）执行后续修订/实施之前可见。这样，它们总是表示你没有“看到”的步骤，并且在你进一步迭代会话时不会累积。此外，这些点不会添加到你自己添加/编辑的计划步骤中。它们不会在浏览器刷新时持久存在。这样，它们只是代表AI贡献的更改，这些更改是由刚刚进行的修订引入的👍

<img src="https://github.com/user-attachments/assets/88d2cb07-0897-46c4-b4e3-6c5c61b1b006" width="400px" />

### Latest changes filter

The `Files changed` section has a new filter called `Latest changes`, which allows you to focus on the edits that were made by the most recent NL revision/implementation. This makes it a lot easier to perform iterations, and then immediately see the impact of that change (as opposed to all the changes from the session). And when combined with the new plan step indicators, this makes NL revision a lot nicer, since you can perform a revision, and then quickly spot the resulting change in both the plan and the code.

`文件更改`部分有一个新的过滤器，称为`最新更改`，这允许你专注于最近的NL修订/实施所做的编辑。这使得执行迭代变得更加容易，然后立即看到该更改的影响（而不是会话中的所有更改）。当与新的计划步骤指示器结合使用时，这使得NL修订变得更加愉快，因为你可以执行修订，然后快速发现计划和代码中的结果更改。

<img src="https://github.com/user-attachments/assets/c15376cd-e2e1-4fba-b115-34036fda2698" width="300px" />

### Devcontainer tasks improvements

When you open the integrated terminal, the `Build`, `Test`, `Run` buttons are now always visible, even if the repo you're working against doesn't define them in a `devcontainer.json` file. And when you click any of them, CW will generate an AI-suggestion for the appropriate command(s) needed to run them (e.g. `npm run compile`).

当你打开集成终端时，`构建`、`测试`、`运行`按钮现在始终可见，即使你正在处理的存储库没有在`devcontainer.json`文件中定义它们。当你点击其中任何一个时，CW将为运行它们所需的适当命令生成AI建议（例如`npm run compile`）。

<img src="https://github.com/user-attachments/assets/d0a89f46-d447-49d6-84f1-b623e41441f2" width="600px" />

If the command looks right, then you can submit it, which will execute it in the terminal, and then persist it to the `devcontainer.json` file. You can then include this file in your PR/commit, and then all subsequent runs of that task (either build, test, or run) will be able to use this configured command in a single-click. The nice thing about this flow, is that it makes it easier for every repo to configure their build/test/run commands, without needing to remember how to do it. Simply click the buttons, and then let CW suggest and configure it for you🚀

如果命令看起来正确，那么你可以提交它，这将在终端中执行它，然后将其持久化到`devcontainer.json`文件中。然后你可以在你的PR/提交中包含此文件，然后该任务的所有后续运行（无论是构建、测试还是运行）都可以在单击中使用此配置的命令。此流程的好处在于，它使每个存储库更容易配置其构建/测试/运行命令，而无需记住如何执行。只需点击按钮，然后让CW为你建议和配置它🚀

<img src="https://github.com/user-attachments/assets/86555379-98cd-4314-bf5b-9d481dc6ff8d" width="600xp" />

### VS Code: Planning & implementing

The CW extension for VS Code now allows you to generate, regenerate, revise, and implement the plan. Entirely within the editor🔥 We still require you to **start** sessions from the CW web/mobile client, but once you have a task started, you can resume it within VS Code, and perform the most common iteration operations from there.

VS Code的CW扩展现在允许你生成、重新生成、修订和实施计划。完全在编辑器内🔥我们仍然要求你从CW Web/移动客户端**开始**会话，但一旦你开始了一个任务，你可以在VS Code中恢复它，并从那里执行最常见的迭代操作。

> Note: Since this extension is early, we're still not quite ready to publish it to the marketplace. We'll likely do that in the next couple of weeks, but until them, simply hit us up in [Discord](https://gh.io/next-discord) to grab the latest VSIX😎

> 注意：由于此扩展尚处于早期阶段，我们仍未准备好将其发布到市场。我们可能会在接下来的几周内这样做，但在此之前，只需在[Discord](https://gh.io/next-discord)中联系我们以获取最新的VSIX😎

### URL task context

When a task references URLs, they will now be displayed in the `Additional context` section of the `Task` panel. This ensures that you're always aware of any external context being considered, and you can control if it needed (e.g. deleting a link that is confusing the plan/etc.).

当一个任务引用URL时，它们现在将显示在`任务`面板的`附加上下文`部分。这确保你始终了解正在考虑的任何外部上下文，并且你可以控制是否需要（例如，删除一个使计划混淆的链接等）。

<img src="https://github.com/user-attachments/assets/ce02119f-35c4-49dc-bd3e-c4c831f41e01" width="400px" />

> Note: By default, CW will spider URLs that point at GitHub issues, PRs, and repo files. However, if you want it to spider external web URLs, then you need to enable the `Utilize referenced generic web content in analysis` setting in the `Experiments` dialog (underneath your avatar menu).

> 注意：默认情况下，CW将抓取指向GitHub问题、PR和存储库文件的URL。但是，如果你希望它抓取外部Web URL，那么你需要在`实验`对话框（在头像菜单下）中启用`在分析中利用引用的通用Web内容`设置。

### Cancellation improvements

When a plan or implementation is in-progress, clicking the cancel button should now feel immediate. Additionally, if you cancel a file implementation mid-way, it will now revert the file back to its previous state (before editing it), as opposed to the previous behavior (which marked the file as `Cancelled`, and looked pretty weird). This is meaningful because when you perform an NL revision, CW automatically updates the plan and then implements it. And in order to make this UX feel delightful, we wanted to make sure you could cancel it at any time, and get the immediate/expected results.

当一个计划或实施正在进行时，点击取消按钮现在应该感觉立即生效。此外，如果你在中途取消文件实施，它现在将文件恢复到其先前状态（在编辑之前），而不是先前的行为（将文件标记为`已取消`，看起来很奇怪）。这是有意义的，因为当你执行NL修订时，CW会自动更新计划然后实施它。为了使这种用户体验感觉愉快，我们希望确保你可以随时取消它，并获得立即/预期的结果。

## 📅 13 September 2024

- [VS Code session continuation](#vs-code-session-continuation)
- [Incremental plan revision](#incremental-plan-revision)
- [Improved task context](#improved-task-context)
- [New specification UX](#new-specification-ux)
- [Planned file placeholders](#planned-file-placeholders)
- [Branch switching](#branch-switching)
- [Whitespace changes](#whitespace-changes)

### VS Code session continuation

We're introducing a new VS Code extension, which allows you to resume CW sessions within your editor. This allows you to start tasks from the CW web app/PWA, and after feeling good about the implementation, finish the task from the comfort of your fully-configured dev environment (e.g. using your favorite extensions, color theme, keybindings, etc.)🤗

我们引入了一个新的VS Code扩展，允许你在编辑器中恢复CW会话。这使你可以从CW Web应用程序/PWA开始任务，并在对实施感到满意后，从你完全配置的开发环境的舒适性中完成任务（例如，使用你最喜欢的扩展、颜色主题、键绑定等）🤗

Additionally, this extension allows you to debug and run arbitrary client/desktop projects (e.g. mobile apps, Chrome extensions, etc.), without needing to push/pull the session's code to an intermediate branch. This works because the VS Code extension supports bi-directional file syncing with the CW service/web client. And so as you make changes in one client, they're immediately available in the other. Collectively, this allows you to start and finish work from whichever client is most convenient😎

此外，此扩展允许你调试和运行任意客户端/桌面项目（例如，移动应用程序，Chrome扩展等），而无需将会话的代码推送/拉取到中间分支。这是因为VS Code扩展支持与CW服务/Web客户端的双向文件同步。因此，当你在一个客户端中进行更改时，它们会立即在另一个客户端中可用。总的来说，这使你可以从最方便的客户端开始和完成工作😎

<img src="https://github.com/user-attachments/assets/5ae9c6fb-c4de-4f4e-b37a-83b93e373c74" width="700px" /><br />
     
> Note: This extension is very early, and therefore, we're not publishing it to the VS Code marketplace just yet. So if you'd like to give it a try and send us feedback, hit us up on the [GitHub Next Discord server](https://gh.io/next-discord) and we'll send you the VSIX.

> 注意：此扩展还处于非常早期阶段，因此，我们尚未将其发布到VS Code市场。因此，如果你想尝试一下并向我们发送反馈，请在[GitHub Next Discord服务器](https://gh.io/next-discord)上联系我们，我们将向你发送VSIX。
     
### Incremental plan revision

When you perform a NL revision (using the pretty input bar at the bottom💙), the plan is now updated incrementally, as opposed to being completely regenerated. This not only makes it faster to perform iterations, but it also makes it clearer what did and didn't change as a result of your request. To get a sense for how much nicer this feels, check out the following demo😻

当你执行NL修订时（使用底部的漂亮输入栏💙），计划现在是增量更新的，而不是完全重新生成的。这不仅使执行迭代更快，而且使你更清楚地了解由于你的请求而发生了哪些变化和未发生哪些变化。要了解这种感觉有多好，请查看以下演示😻

<img src="https://github.com/user-attachments/assets/155e0f56-2707-44dc-98f4-9f704b119496" width="800px" />

### Improved task context

The `Task` panel now includes an `Additional context` footer, which is visible when you open an issue (that has comments), or when you're working on a project that includes repository-wide instructions (e.g. a `.github/copilot-workspace/CONTRIBUTING.md` file).

`任务`面板现在包括一个`附加上下文`页脚，当你打开一个有评论的问题时，或当你正在处理一个包含存储库范围指令的项目时（例如`.github/copilot-workspace/CONTRIBUTING.md`文件），它是可见的。

<img src="https://github.com/user-attachments/assets/2a8494fd-adcb-48a6-9414-658b72e62ad2" width="500px" />
     
This is helpful, because it provides visibility into the external context that will be taken into account when analyzing/planning your task. Additionally, it lets you better predict and control the outcome of your session. For example, if you see a `Repository instructions` context item, then you can click it and immediately see the contents of the file (e.g. so you can know what it defines). And if you're working on an issue, that has comments you don't want included (e.g. becuase they're just "conversational noise"), then you can click the trash can icon next to them, and remove them consideration.

这是有帮助的，因为它提供了对在分析/计划任务时将考虑的外部上下文的可见性。此外，它使你能够更好地预测和控制会话的结果。例如，如果你看到一个`存储库指令`上下文项，那么你可以点击它并立即查看文件的内容（例如，这样你可以知道它定义了什么）。如果你正在处理一个有评论的问题，而你不希望包含这些评论（例如，因为它们只是“对话噪音”），那么你可以点击它们旁边的垃圾桶图标，并将其删除。

### New specification UX

In order to simplify the CW workflow, we're removing the `Specification` panel from the timeline, and introducing it as optional context to the `Task`. That way, if your task description already defines the sufficient details for your intent, then you can jump straight to planning. However, if you'd like CW to help expand/ellaborate/explore on your description, then you can ask it to add a spec, and then treat that as additional input to the plan🚀 (along with any comments and repo-wide instructions).

为了简化CW工作流程，我们将从时间线中删除`规范`面板，并将其作为`任务`的可选上下文引入。这样，如果你的任务描述已经定义了你的意图的足够细节，那么你可以直接跳到计划。然而，如果你希望CW帮助扩展/详细说明/探索你的描述，那么你可以要求它添加一个规范，然后将其视为计划的附加输入🚀（以及任何评论和存储库范围的指令）。

Since this is a noticeable change, we're initially introducing it as an opt-in setting, which you can enable via the `Move specficiation to task panel` option in the `Experiments` dialog. When enabled, you'll see an `Add specification` button in the `Additional context` section of the `Task` panel. When you click that, it will generate the spec as usual, and then display a `Specification` entry in the context section for the task. If you click this, it will open the spec as a file tab, which let's you edit, revise, or regenerate the content. But with a much nicer, and full-screen view⭐

由于这是一个显着的变化，我们最初将其作为选择加入设置引入，你可以通过`实验`对话框中的`将规范移动到任务面板`选项启用它。启用后，你将在`任务`面板的`附加上下文`部分看到一个`添加规范`按钮。当你点击它时，它将像往常一样生成规范，然后在任务的上下文部分显示一个`规范`条目。如果你点击此条目，它将规范作为文件标签打开，这让你可以编辑、修订或重新生成内容。但具有更好和全屏视图⭐


<img src="https://github.com/user-attachments/assets/41b2864a-3b9f-45e0-a62e-071b3b9a6412" width="800px" />

### Planned file placeholders

计划文件占位符

After a plan has been generated, the `Files changed` section now immediately displays placeholders for all of the to-be-implemented files. This helps clarify the state you're in (i.e. there are files that are "planned", but not implemented), and creates a stronger association between the plan and the code.

在生成计划后，“更改的文件”部分现在会立即显示所有待实现文件的占位符。这有助于澄清你所处的状态（即有文件是“计划”中的，但尚未实现），并在计划和代码之间创建更强的关联。

Additionally, the new `Planned` placeholders contain a delete icon, which let's you quickly delete a file from the plan. This is useful when using CW on mobile, and you want to delete a file from the implementation, without needing to switch back to the timeline view in order to do it.

此外，新的“计划”占位符包含一个删除图标，可以让你快速从计划中删除一个文件。这在移动设备上使用 CW 时很有用，你可以从实现中删除一个文件，而无需切换回时间线视图来执行此操作。

<img src="https://github.com/user-attachments/assets/d1aa515d-2a5e-4802-9279-aa0a8a670a7e" width="600px" />

### Branch switching

分支切换

You can now easily start a CW session against a new branch, by clicking the branch name label in the header bar. This will bring up a dialog with the list of all active branches, and when selected, starts a new task which targets that branch.

你现在可以通过点击标题栏中的分支名称标签，轻松启动一个针对新分支的 CW 会话。这将弹出一个包含所有活动分支列表的对话框，选择后，将启动一个针对该分支的新任务。

<img src="https://github.com/user-attachments/assets/9635f9f1-d860-4279-8f16-03f9c9b7d10d" width="600px" />

### Whitespace changes

空白更改

By default, whitespace changes are now visible within the file diff editors. This makes it easier to spot when Copilot (or you 😄) make any unintended changes to formatting, and can prevent any surprises after creating a PR. And if you'd like to turn this off (e.g. because a file has a lot of "whitespace churn"), you can click the settings icon in the `Files changed` section, and then select `Ignore whitespace changes`.

默认情况下，空白更改现在在文件差异编辑器中可见。这使得在 Copilot（或你 😄）对格式进行任何意外更改时更容易发现，并且可以防止在创建 PR 后出现任何意外。如果你想关闭此功能（例如，因为文件有很多“空白更改”），你可以点击“更改的文件”部分中的设置图标，然后选择“忽略空白更改”。

<img src="https://github.com/user-attachments/assets/10d0d291-c17e-4240-adf6-b04ef552aa24" width="200px" />

## 📅 30 August 2024

### Features / Enhancements

### 功能/增强

* **Multi-file revision** - You can now select multiple files in the `Files changed` section, and perform an NL revision against them all. This makes it easier to make changes against multiple files, but in a very precise way (e.g. updating an implementation + associated tests, modifying a UI component and the places it's consumed).

* **多文件修订** - 你现在可以在“更改的文件”部分中选择多个文件，并对它们进行 NL 修订。这使得对多个文件进行更改变得更容易，但以非常精确的方式（例如，更新实现+相关测试，修改 UI 组件及其使用位置）。

     <img src="https://github.com/user-attachments/assets/cd46d775-fe3a-4c14-9f8a-6e89a0be25b6" width="500px" />

     To use it, simply click the target icon (in the file header) for all of the files you'd lke to revise. You can then type your intent, and when submitted, all selected files will begin updating their code based on your request.

     要使用它，只需点击所有要修订的文件的目标图标（在文件标题中）。然后你可以输入你的意图，提交后，所有选定的文件将根据你的请求开始更新其代码。

* **File tabs** - You can now open a file in a full-screen tab, in order to view its contents more easily. This compliments the existing "stacked diffs" view (which is useful for gaining a high-level overview of the changes), and allows you to simultaneously browse a file, while also reading the spec/plan and/or using the terminal (which wasn't possible using the file explorer modal).

* **文件标签** - 你现在可以在全屏标签中打开一个文件，以便更轻松地查看其内容。这补充了现有的“堆叠差异”视图（这对于获得更改的高级概览很有用），并允许你同时浏览一个文件，同时阅读规范/计划和/或使用终端（这在文件资源管理器模式下是不可能的）。

   <img src="https://github.com/user-attachments/assets/be60dc55-79da-49f4-bda4-7aea2fc5b2b3" width="700px" />

     To use it, simply click the arrow icon in a file diff's header, which will open that file in a new tab. Additionally, if you click a file link in the task/spec/plan panels, or select the `Open file` menu item for a file in the plan, then the selected file will now open in a tab (as opposed to the file explorer modal).

     要使用它，只需点击文件差异标题中的箭头图标，这将打开一个新标签中的文件。此外，如果你点击任务/规范/计划面板中的文件链接，或选择计划中某个文件的“打开文件”菜单项，则选定的文件现在将在标签中打开（而不是文件资源管理器模式）。

     <img src="https://github.com/user-attachments/assets/0ec519b6-3859-46b7-a331-52123f549dae" width="500px" />

     Even cooler: the list of open files, and the currently active tab, are persisted as part of your session. So when you resume a session later, or share a session with others, the workspace will be in exactly the same place that you left it 💙 Check out [this example](https://copilot-workspace.githubnext.com/lostintangent/gitdoc/issues/77?shareId=910861ee-876e-428d-b25a-c388fa8cea84) to see what we mean.

     更酷的是：打开的文件列表和当前活动的标签作为会话的一部分被保留。因此，当你稍后恢复会话或与他人共享会话时，工作区将位于你离开它的确切位置 💙 查看[此示例](https://copilot-workspace.githubnext.com/lostintangent/gitdoc/issues/77?shareId=910861ee-876e-428d-b25a-c388fa8cea84)以了解我们的意思。

* **URLs in repo-wide instructions** - You can now include URLs in a repo-wide instruction file (`.github/copilot-workspace/CONTRIBUTING.md`), and those URLs will be fetched and included in the context of the session. This makes it easy to augment your repo instructions with documentation, or other reference materials, that can help inform all tasks/issues performed against it.

* **仓库范围指令中的 URL** - 你现在可以在仓库范围的指令文件（`.github/copilot-workspace/CONTRIBUTING.md`）中包含 URL，这些 URL 将被获取并包含在会话的上下文中。这使得通过文档或其他参考材料来扩充你的仓库指令变得容易，这些材料可以帮助告知所有针对它执行的任务/问题。

* **Issue comments** - The `Issue` panel now displays how many comments the issue has (if any), and allows you to one-click navigate to them for more details. Copilot Workspace has always included issue comments as context for a session, but this change makes it easier to have visibility into when comments exist (since they may impact CW's understanding of the task).

* **问题评论** - “问题”面板现在显示问题有多少评论（如果有的话），并允许你一键导航到它们以获取更多详细信息。Copilot Workspace 始终将问题评论作为会话的上下文，但此更改使得更容易了解何时存在评论（因为它们可能会影响 CW 对任务的理解）。

   <img src="https://github.com/user-attachments/assets/29b27332-d30b-464f-9506-14af2684933d" width="500px" />

* **PR improvements** - We made a handul of improvements to the flow of creating and updating pull requests from Copilot Workspace. In particular...

* **PR 改进** - 我们对从 Copilot Workspace 创建和更新拉取请求的流程进行了多项改进。特别是...

   * The option to create a draft PR is now properly disabled, when working against repos that don't support them

   * 在处理不支持它们的仓库时，创建草稿 PR 的选项现在已正确禁用

   * When you update a PR, we no longer create a PR comment for the changes. We simply push a new commit with the specified (or generated) message

   * 当你更新 PR 时，我们不再为更改创建 PR 评论。我们只是推送一个带有指定（或生成）消息的新提交

   * If you manually edit a file, we now automatically switch to `Unpushed` changes mode, when your session is continuing an existing PR (that way the diff view focuses on only net-new changes)

   * 如果你手动编辑文件，当你的会话继续现有的 PR 时，我们现在会自动切换到“未推送”更改模式（这样差异视图只关注净新更改）

## 📅 23 August 2024

### Features / Enhancements

### 功能/增强

* **Repo-wide instructions** - You can now define instructions for Copilot Workspace, that will be automatically applied to every issue or task performed against a repository. This allows you to document policies, suggestions, and other important guidelines that may not be evident from the codebase, but should always be considered.

* **仓库范围指令** - 你现在可以为 Copilot Workspace 定义指令，这些指令将自动应用于针对仓库执行的每个问题或任务。这使你可以记录政策、建议和其他可能不明显的代码库的重要指南，但应始终考虑。

   For example, the following screenshot shows a `Proposed` spec that indicates the need to update the `CHANGELOG.md`, despite the issue not mentioning this requirement. This is because the [repo's  instructions](https://github.com/lostintangent/codeswing/blob/main/.github/copilot-workspace/CONTRIBUTING.md) define that all new features should include an entry in the changelog.

   例如，以下截图显示了一个“拟议”规范，表明需要更新 `CHANGELOG.md`，尽管问题没有提到此要求。这是因为[仓库的指令](https://github.com/lostintangent/codeswing/blob/main/.github/copilot-workspace/CONTRIBUTING.md) 定义了所有新功能应在变更日志中包含一个条目。

   <img src="https://github.com/user-attachments/assets/83770b9e-3a3c-4ca3-88a2-04677ad5ed5f" width="600px" />
   
   To start using this feature, simply create the following file in your repository: `.github/copilot-workspace/CONTRIBUTING.md`. As the name suggests, this file acts as contribution guidance for Copilot, and allows you to include any context you think will be helpful 🧠

   要开始使用此功能，只需在你的仓库中创建以下文件：`.github/copilot-workspace/CONTRIBUTING.md`。顾名思义，此文件充当 Copilot 的贡献指南，并允许你包含任何你认为有帮助的上下文 🧠

   By enabling teams to codify common or required guidelines, we hope to reduce mistakes, repetition, and learning barriers for all developers working across a project 🙌

   通过使团队能够将常见或必需的指南编纂成文，我们希望减少在项目中工作的所有开发人员的错误、重复和学习障碍 🙌

* **Terminal assist enhancements** - When you encounter an error in the terminal, and Copilot suggestions a change to the spec or plan, that suggestion will now be displayed as an editable diff of the spec/plan. This allows you to quickly understand what the suggestion is, and to easily tweak it as needed, before commiting the change.

* **终端辅助增强** - 当你在终端中遇到错误，并且 Copilot 建议更改规范或计划时，该建议现在将显示为规范/计划的可编辑差异。这使你可以快速了解建议是什么，并在提交更改之前轻松调整它。

  Additionally, if you encounter an error in the terminal that is trivial in nature, and therefore, doesn't justify an update to the spec/plan (e.g. lint errors, typos), then the terminal assistance will now suggest making direct edits to the neccessary files. For example, the following shows the suggestion after running a build, which failed due to a typo. Note that Copilot accurately recommends simply fixing the typo directly (as opposed to updating the plan):

  此外，如果你在终端中遇到的错误本质上是微不足道的，因此，不需要更新规范/计划（例如，lint 错误，拼写错误），那么终端辅助现在将建议直接编辑必要的文件。例如，以下显示了运行构建后的建议，由于拼写错误而失败。请注意，Copilot 准确地建议直接修复拼写错误（而不是更新计划）：

  <img src="https://github.com/user-attachments/assets/92c89572-987a-44c8-a8e9-10a2ee79ffd3" width="600px" />

* **File explorer navigation** - The file explorer now supports filtering the tree view by a seach query. As you type, the file tree will be automatically filtered to the matching files, as well as the directories they're contained within. Additionally, directories are now annotated with a green or orange diff icon, to indicate when they contain an added or changed file (respectively). Collectively, these two enhancements should make it a lot easier to navigate codebases within CW (along with the existing support for go-to-definition in the editor).

* **文件资源管理器导航** - 文件资源管理器现在支持按搜索查询过滤树视图。当你键入时，文件树将自动过滤到匹配的文件以及它们包含的目录。此外，目录现在用绿色或橙色差异图标注释，以指示它们何时包含添加或更改的文件（分别）。总的来说，这两项增强功能应该使在 CW 中导航代码库变得更加容易（以及编辑器中现有的转到定义支持）。

  <img src="https://github.com/user-attachments/assets/b288601c-d244-4720-a0cf-247a7fcb4257" width="400px" />

* **File search on mobile** - You can now easily search the contents of a file on mobile, by tapping the magnifying glass icon in the file's header bar. This has always been possible on desktop, by pressing `CMD+F` within the editor. But this new button provides the same navigation ability, regardless what device you're currently working from 📱

* **移动设备上的文件搜索** - 你现在可以通过点击文件标题栏中的放大镜图标，轻松搜索移动设备上的文件内容。这在桌面上一直是可能的，通过在编辑器中按 `CMD+F`。但这个新按钮提供了相同的导航能力，无论你当前使用的是什么设备 📱

  <img src="https://github.com/user-attachments/assets/127da4c4-68ba-4301-b440-9f15ef061110" width="300px" />

* **Sticky toolbar** - The `Files changed` toolbar is now "sticky", which means that it stays visible as you scroll through the implemented files. This ensures that you can expand/collapse the timeline, discard the implementation, or toggle between split/unified diff view, without needing to scroll to the top of the files list to do it (which was obviously pretty annoying!).

* **粘性工具栏** - “更改的文件”工具栏现在是“粘性”的，这意味着当你滚动浏览已实现的文件时，它会保持可见。这确保你可以展开/折叠时间线，丢弃实现，或在拆分/统一差异视图之间切换，而无需滚动到文件列表顶部来执行此操作（这显然非常烦人！）。

   <img src="https://github.com/user-attachments/assets/2b753dff-ee56-43c1-a165-89a5fb5e81ca" width="700px" />

## 📅 16 August 2024

### Features / Enhancements

### 功能/增强

* **File regeneration** - The file toolbar now includes a regenerate button, which allows you to ask CW to "try again" with implementing it. This can be useful if you've revised the plan through NL, and noticed that CW may have missed a detail. Or, if you'd like to ask it to get a bit more "creative" with its interpretation of your intent 🎨

* **文件再生** - 文件工具栏现在包括一个再生按钮，允许你要求 CW “再试一次”来实现它。如果你通过 NL 修订了计划，并注意到 CW 可能遗漏了一个细节，这可能很有用。或者，如果你想要求它在解释你的意图时变得更加“有创意” 🎨

  The `Specification` and `Plan` panels already had a regenerate button, and so this change ensures that in addition to editing/revising/undoing, you can regenerate every piece of content within the workspace.

  “规范”和“计划”面板已经有一个再生按钮，因此此更改确保除了编辑/修订/撤消外，你还可以再生工作区内的每一部分内容。

  <img src="https://github.com/user-attachments/assets/c3470d4c-cfe5-4176-b116-12f8a83fdb18" width="500px" />

* **Desktop notification** - You can now opt-into getting a system notification whenever a CW session is finished implementing (and the page isn't currently visible). This is useful if you're implementing a large plan, and want to switch to another task while it's running. But then know as soon as it's ready for your review 🏃

* **桌面通知** - 你现在可以选择在 CW 会话完成实施时（并且页面当前不可见）接收系统通知。如果你正在实施一个大计划，并且希望在其运行时切换到另一个任务，这很有用。但一旦它准备好供你审查，你就会知道 🏃

   <img src="https://github.com/user-attachments/assets/7d285c40-16b0-40fd-a009-dbd72012ee76" width="300px" />
   
   To turn this on, simply click your avatar in the upper-right, select `Settings`, and then check the `Show notification after implementing` option. Your browser will ask for permission for CW to show notifications, and so make sure to approve that 👍

   要打开此功能，只需点击右上角的头像，选择“设置”，然后勾选“实施后显示通知”选项。你的浏览器将请求 CW 显示通知的权限，因此请确保批准 👍

   <img src="https://github.com/user-attachments/assets/898162a8-5f32-426e-8080-8444d558e80f" width="300px" />

* **Improved code search** - As a follow-up to supporting web URLs in the task definition, we've introduced an improvement to the way we perform code search, when analyzing the details of your issues/tasks. Depending on the codebase/scenario, this allows us to better identify the right set of files to edit (across the entire repo). And ultimately, can improve the quality/success-rate of CW.

* **改进的代码搜索** - 作为支持任务定义中的 Web URL 的后续，我们引入了一种改进的方法来执行代码搜索，以分析你的问题/任务的详细信息。根据代码库/场景，这使我们能够更好地识别要编辑的正确文件集（跨整个仓库）。最终，可以提高 CW 的质量/成功率。

   We're still refining this enhancement. And so for now, you need to opt-into it by clicking the beaker icon in the header bar, and checking the `Use code search during task analysis` setting. If you get a chance to turn this on, and use CW for a while, then we'd [love to hear](https://gh.io/next-discord) if you notice any improvements 💙

   我们仍在改进此增强功能。因此，现在，你需要通过点击标题栏中的烧杯图标并勾选“在任务分析期间使用代码搜索”设置来选择加入。如果你有机会打开它，并使用 CW 一段时间，那么我们[很想听听](https://gh.io/next-discord)你是否注意到任何改进 💙
  
   <img src="https://github.com/user-attachments/assets/ee6ddcb8-4f4c-4892-b76b-ae8ccfa783d8" width="400px" />

* **Task authoring** - The `Task`/`Issue` panels now match the authoring experience for other markdown editors across GitHub (e.g. issue descriptions, PR comments, etc.). In particular, instead of requiring you to explicitly put the task into "edit mode", or requiring you to explicitly save it in order to preview the content, the panels now provide two tabs that you can seamlessly switch between: `Write` and `Preview`.

* **任务创作** - “任务”/“问题”面板现在与 GitHub 上其他 markdown 编辑器的创作体验相匹配（例如，问题描述，PR 评论等）。特别是，不再需要你明确地将任务置于“编辑模式”，或明确地保存它以预览内容，现在面板提供了两个选项卡，你可以无缝切换：`编写`和`预览`。

   <img src="https://github.com/user-attachments/assets/03ad1ede-22d7-4358-addf-9198101b8909" width="500px" />

* **Issue/PR status** - The workspace header now indicates the status of the issue and/or PR associated with a session, by coloring the issue and PR icons based on whether they're open (green) or closed/merged (purple). This can make it easier to spot if you accidentally opened an issue/PR that has already been completed. At which point, you can work on something else! 🙌

* **问题/PR 状态** - 工作区标题现在通过根据问题和 PR 图标是否打开（绿色）或关闭/合并（紫色）来指示与会话关联的问题和/或 PR 的状态。这可以使你更容易发现是否意外打开了已完成的问题/PR。此时，你可以处理其他事情！🙌

   <img src="https://github.com/user-attachments/assets/5cbc5939-7ac3-48f8-bd50-ba0fc2d169fc" width="600px" />

## 📅 9 August 2024

### Features / Enhancements

### 功能/增强

* **External context** - When defining a task/issue, you can now include links to external references, and Copilot Workspace will use them as additional context when generating the spec, plan, and code. This makes it a _lot_ easier to express your intent, without having to copy & paste and/or summarize existing content (which can be non-trivial!). In particular, CW supports referencing the following types of assets:

* **外部上下文** - 在定义任务/问题时，你现在可以包含指向外部参考的链接，Copilot Workspace 将在生成规范、计划和代码时将它们用作附加上下文。这使得表达你的意图变得_容易_得多，而无需复制和粘贴和/或总结现有内容（这可能是非平凡的！）。特别是，CW 支持引用以下类型的资产：

   1. *Issues / Pull Requests* - If you reference an issue/PR by number (e.g. `#43`) or URL, then CW will take into account it's description and comments. Additionally, if you link to a specific issue/PR comment, then CW will focus it's attention on just that one. This allows you to use an existing discussion/feedback as context, or work on "umbrella issues" that aggregate a set of sub-tasks together.

   1. *问题/拉取请求* - 如果你通过编号（例如 `#43`）或 URL 引用问题/PR，则 CW 将考虑其描述和评论。此外，如果你链接到特定问题/PR 评论，则 CW 将专注于该评论。这允许你将现有讨论/反馈用作上下文，或处理汇总一组子任务的“伞形问题”。

   1. *Repository files* - If you reference the URL of a file in a GitHub repository (that you have access to), then CW will include that in its set of prioritized references. Additionally, you can include a link to a specific line ([example](https://github.com/lostintangent/codeswing/blob/b40dbeb3dbf5f133121605c751e1fa7c7a6f67ec/src/extension.ts#L16)) or range of lines in a file ([example](https://github.com/lostintangent/codeswing/blob/b40dbeb3dbf5f133121605c751e1fa7c7a6f67ec/src/preview/layoutManager.ts#L53-L62)), in order to focus CW on that exact code. This allows you to use existing code as a source of inspiration (e.g. "Implement an auth provider just like the one in <URL>"), and help steer Copilot in a more precise direction.

   1. *仓库文件* - 如果你引用 GitHub 仓库中的文件 URL（你有访问权限），则 CW 将其包含在优先参考集内。此外，你可以包含指向文件中特定行的链接（[示例](https://github.com/lostintangent/codeswing/blob/b40dbeb3dbf5f133121605c751e1fa7c7a6f67ec/src/extension.ts#L16)）或行范围的链接（[示例](https://github.com/lostintangent/codeswing/blob/b40dbeb3dbf5f133121605c751e1fa7c7a6f67ec/src/preview/layoutManager.ts#L53-L62)），以便 CW 专注于该确切代码。这允许你使用现有代码作为灵感来源（例如“实现一个类似于 <URL> 的身份验证提供程序”），并帮助更精确地引导 Copilot。

   1. *Arbitrary web URLs* - If you reference a public web URL, then CW will fetch and use a summary of its content. Additionally, if you link to a specific fragment of a page (e.g. `#link-to-a-specific-heading`), then CW will extract and focus on just that section. This allows you to reference documentation/blog posts/tweets/etc. that can provide more recent and/or specific instructions of what you're trying to accomplish 💪

   1. *任意 Web URL* - 如果你引用公共 Web URL，则 CW 将获取并使用其内容摘要。此外，如果你链接到页面的特定片段（例如 `#link-to-a-specific-heading`），则 CW 将提取并专注于该部分。这允许你引用文档/博客文章/推文等，可以提供你试图完成的更近期和/或具体的说明 💪

    > Note: This capability isn't enabled by default, and so if you'd like to give it a try, click the `Experiments` link in your avatar menu, and check either `Utilize linked issues, PR, and GitHub file links in analysis` and/or `Utilize referenced generic web content in analysis`.

    > 注意：此功能默认未启用，因此如果你想尝试，请点击头像菜单中的“实验”链接，并勾选“在分析中使用链接的问题、PR 和 GitHub 文件链接”和/或“在分析中使用引用的通用 Web 内容”。

* **NL revision** - After you implement a plan, Copilot Workspace now displays a natural language revision bar at the bottom of the `Files changed` section. This allows you to update the plan in complex and arbitrary ways, while remaining focused on reviewing the changes.

* **NL 修订** - 在你实施计划后，Copilot Workspace 现在在“更改的文件”部分底部显示一个自然语言修订栏。这允许你以复杂和任意的方式更新计划，同时专注于审查更改。

    <img src="https://github.com/user-attachments/assets/1f20f837-548f-4a33-9ec5-e07002c67f65" width="400px" />

    Additionally, if you'd like to revise a specific file, you can click the bullseye icon in the file's header, which will put the NL revision bar into "scoped file" mode.

    此外，如果你想修订特定文件，可以点击文件标题中的靶心图标，这将使 NL 修订栏进入“范围文件”模式。

    <img src="https://github.com/user-attachments/assets/74e393da-8dcf-4c17-809e-4306a3676178" width="400px" />

   Both of these changes are part of a larger theme to elevate/simplify the ability to iterate through natural language. And you can expect to see more improvements in this space in the coming weeks 👍 

   这两项更改都是提升/简化通过自然语言迭代能力的更大主题的一部分。你可以期待在接下来的几周内看到更多改进 👍
  
* **Terminal repair improvements** - CW's terminal assistance can now perform updates to the plan, when you encounter an error that requires a code change. This can be helpful when a build/test/lint action fails, and you want Copilot to suggest a fix. While this capability is still early (and evolving!), we're excited to make steady progress towards a better workflow for automatically addressing errors.

* **终端修复改进** - CW 的终端辅助现在可以在你遇到需要代码更改的错误时对计划进行更新。当构建/测试/lint 操作失败时，这可能会有所帮助，并且你希望 Copilot 建议修复方法。虽然此功能仍处于早期阶段（并且在不断发展！），但我们很高兴在自动解决错误的更好工作流程方面取得稳定进展。

* **Exit path improvements** - When you create a PR/branch/repo, CW no longer generates a commit description by default. That way you can decide if you'd like Copilot to write a message for you, or if you'd prefer to craft your own 💙

* **退出路径改进** - 当你创建 PR/分支/仓库时，CW 不再默认生成提交描述。这样你可以决定是否希望 Copilot 为你编写消息，或者你更喜欢自己编写 💙

  Additionally, when you create a PR for a session that's associated with an issue, the PR dialog now includes a checkbox that allows you to indicate whether the code changes fix the issue or not. When checked, CW will insert a `Fixes #<number` into the issue description. Otherwise, it will insert a `Related to #<number>` (which is what it did previously).

  此外，当你为与问题关联的会话创建 PR 时，PR 对话框现在包含一个复选框，允许你指示代码更改是否解决了问题。选中后，CW 将在问题描述中插入 `Fixes #<number`。否则，它将插入 `Related to #<number>`（这是之前的做法）。

  <img src="https://github.com/user-attachments/assets/a5b9c1e6-6f32-4b87-8de0-16336030f68f" width="400px" />

* **SVG preview** - When you implement or open a `*.svg` file, you can now preview a rendered version of its contents, by clicking the eyeball icon in its header. We previously introduced preview support for Markdown, and plan to continue adding support for other file formats in the coming weeks (HTML? 🤔)

* **SVG 预览** - 当你实现或打开 `*.svg` 文件时，你现在可以通过点击其标题中的眼球图标预览其内容的渲染版本。我们之前引入了对 Markdown 的预览支持，并计划在接下来的几周内继续添加对其他文件格式的支持（HTML？🤔）

    <img src="https://github.com/user-attachments/assets/d8229ba0-c373-4ff6-875a-677b0b5414d1" width="500px" />

* **Sessions + Settings** - The user menu (that you get to by clicking your avatar in the upper-right) now includes two new items:

* **会话+设置** - 用户菜单（通过点击右上角的头像进入）现在包括两个新项目：

   * `Your sessions` - This navigates you to the [CW dashboard](https://copilot-workspace.githubnext.com), so you can see your recent/bookmarked/completed sessions. We got feedback that folks weren't discovering the dashboard, and so we wanted to make this a bit more discoverable (since it's super useful!)

   * `你的会话` - 这将导航到 [CW 仪表板](https://copilot-workspace.githubnext.com)，以便你可以查看最近的/书签的/已完成的会话。我们收到反馈说人们没有发现仪表板，所以我们希望使其更容易发现（因为它非常有用！）

      <img src="https://github.com/user-attachments/assets/28992503-8f08-4fde-bb7c-f840fe0471f7" width="200px" />

   * `Settings` - This opens a dialog with some optional user settings that can be enabled/disabled. To start, this dialog includes the existing options to automatically start a Codespace on session start/implement. But we also introduced a new setting called `Collapse timeline on implement`, which as the name implies, allows you to automatically collapse the left-side panel after implementing.

   * `设置` - 这将打开一个对话框，其中包含一些可选的用户设置，可以启用/禁用。首先，此对话框包括现有选项，以在会话启动/实施时自动启动 Codespace。但我们还引入了一个名为“实施时折叠时间线”的新设置，顾名思义，它允许你在实施后自动折叠左侧面板。
   
     When paired with the new NL revision bar, this setting allows you to enter a sort of "zen mode" for Copilot Workspace, where once you're happy with the plan, you can focus your entire screen on reviewing and revising the code 🚀

     当与新的 NL 修订栏配对时，此设置允许你进入 Copilot Workspace 的一种“禅模式”，一旦你对计划感到满意，你可以将整个屏幕集中在审查和修订代码上 🚀
 
     <img src="https://github.com/user-attachments/assets/2a22900a-2950-4311-a072-7c07ce4fbfbc" width="400px" />

* **Renamed files** - Renamed files are now collapsed by default in the `Files changed` section. This makes it easier to focus your attention on new and changed code, while simply seeing the presence of renamed or deleted files. If a file is both renamed + changed, then it won't be collapsed post-implement, so you can properly review its changes.

* **重命名文件** - 重命名的文件现在在“更改的文件”部分中默认折叠。这使你更容易将注意力集中在新代码和更改的代码上，同时只需查看重命名或删除的文件的存在。如果一个文件既重命名又更改，那么在实施后它不会折叠，因此你可以正确地审查其更改。

    <img src="https://github.com/user-attachments/assets/fd3cd39d-6466-4185-8693-aad8a4b9c1d1" width="400px" />

* **Dark mode editor** - The code editor is now properly themed for users with a dark mode system setting. The editor's background was previously a medium greyish color, and now it's black 🖤  

* **暗模式编辑器** - 代码编辑器现在为具有暗模式系统设置的用户正确设置了主题。编辑器的背景以前是中等灰色，现在是黑色 🖤  

* **Usage quota increase** - Due to popular demand, we've increased the daily usage quota again. That way, the folks that are using CW for many tasks every day, can keep sending us amazing feedback 🙏

* **使用配额增加** - 由于需求量大，我们再次增加了每日使用配额。这样，每天使用 CW 处理许多任务的人们可以继续向我们发送惊人的反馈 🙏

## 📅 2 August 2024

### Features / Enhancements

### 功能/增强

* **Terminal error assistance** - When you run a command in the terminal, and it fails (!), the lightbulb button will now turn red. This indicates that Copilot Workspace is aware of the error, and is ready to help you fix it 💪

* **终端错误辅助** - 当你在终端中运行命令并且失败时（！），灯泡按钮现在会变红。这表明 Copilot Workspace 知道错误，并准备帮助你修复它 💪

   <img src="https://github.com/user-attachments/assets/e7f6b848-689c-42aa-aefa-e22b5c189ddf" width="600px" /><br />
  
   If you click on the lightbulb in this state, the terminal assistance UI will pop-up, and automatically generate a suggestion for how to address the issue. If the suggestion looks right, you can one-click accept it. Otherwise, you can refine the help instructions, or tweak the generated terminal command, to steer Copilot in the right direction.

   如果你在这种状态下点击灯泡，终端辅助 UI 将弹出，并自动生成解决问题的建议。如果建议看起来正确，你可以一键接受它。否则，你可以完善帮助说明，或调整生成的终端命令，以引导 Copilot 朝正确的方向前进。

   <img src="https://github.com/user-attachments/assets/cd439128-b1d7-4288-aa85-d57baedcc341" width="600px" />

   This experience can help you perform project and environment setup, correct your usage of CLI tools (seriously, who can remember all these args?), and even suggest modifications to the spec/plan. Over the coming weeks, we'll continue refining this capability even further, to ensure that debugging and repairing build/test/etc. errors is as simple and delightful as possible 🙌

   这种体验可以帮助你进行项目和环境设置，纠正你对 CLI 工具的使用（说真的，谁能记住所有这些参数？），甚至建议修改规范/计划。在接下来的几周内，我们将继续进一步完善此功能，以确保调试和修复构建/测试等错误尽可能简单和愉快 🙌
  
* **Recent repositories** - When you visit the [Copilot Workspace dashboard](https://copilot.workspace.github.com), the `Recent` tab now displays a section at the top called `Recent repositories`. This provides a list of your five most recently-active repos, and allows you to start a new task for them in a single click. When paired with the CW PWA, this makes it simple to begin/resume work using Copilot Workspace, without needing to create an issue, or search for the desired repo 🚀

* **最近的仓库** - 当你访问 [Copilot Workspace 仪表板](https://copilot.workspace.github.com)时，“最近”选项卡现在在顶部显示一个名为“最近的仓库”的部分。这提供了你最近活动的五个仓库的列表，并允许你一键为它们启动一个新任务。当与 CW PWA 配对时，这使得使用 Copilot Workspace 开始/恢复工作变得简单，而无需创建问题或搜索所需的仓库 🚀

  <img src="https://github.com/user-attachments/assets/2d633362-b6d5-45ab-96d8-a816ec4a6e19" width="700px" />

* **Implementation panel re-design** - The `Implementation` panel has been removed from the timeline, in favor of three UX enhancements, which _dramatically_ improve the usability of CW on mobile and in fullscreen-mode:

* **实施面板重新设计** - “实施”面板已从时间线中移除，取而代之的是三项 UX 增强功能，这些功能_显著_提高了 CW 在移动设备和全屏模式下的可用性：

   1. The "exith path" button has been moved to the upper-right corner of the workspace toolbar. This ensures that it's clear how to complete a task, regardless what state your workspace is in 👍

   1. “退出路径”按钮已移至工作区工具栏的右上角。这确保无论你的工作区处于何种状态，都清楚如何完成任务 👍

      <img src="https://github.com/user-attachments/assets/efe72ff9-b18d-4e5a-a94d-3020e61e395e" width="400px" />

   2. While an implementation is in-progress, the status indicator and stop button are now displayed at the bottom of the `Files changed` section. This ensures you can see/control the implementation at any-time, as opposed to just when you have the timeline opened + scrolled to the bottom.

   2. 在实施进行中时，状态指示器和停止按钮现在显示在“更改的文件”部分的底部。这确保你可以随时查看/控制实施，而不仅仅是在你打开时间线并滚动到底部时。

      <img src="https://github.com/user-attachments/assets/417e1f91-7bb7-43d3-bbdf-f57122d3d5bb" width="400px" />

   3. The "discard all files" button has been moved to the left of the `Split | Unified` toggle in the `Files changed` section. That way, if you're reviewing code, and decide you want to try another approach, you can clear the session directly from there.

   3. “丢弃所有文件”按钮已移至“更改的文件”部分中“拆分|统一”切换的左侧。这样，如果你正在审查代码，并决定尝试另一种方法，你可以直接从那里清除会话。

      <img src="https://github.com/user-attachments/assets/2e69bf1d-dff3-4475-b0d1-d256010e8fe0" width="600px" />

* **List organization** - The spec and plan can now be fully re-organized, by clicking on the `...` menu for any sub-step, and choosing `Move item up` or `Move item down`. This won't impact the code generation in any way, and so you can feel free to order things however feels best/most intuitive to you. In particular, this can be useful when sharing a session with others, and you want to curate the spec/plan a bit for improved readability.

* **列表组织** - 现在可以通过点击任何子步骤的“...”菜单，并选择“上移项目”或“下移项目”来完全重新组织规范和计划。这不会以任何方式影响代码生成，因此你可以随意按你认为最好的/最直观的方式排序。特别是，当与他人共享会话时，这可能很有用，并且你希望为提高可读性而稍微策划规范/计划。

    <img src="https://github.com/user-attachments/assets/71ad72b2-5c1a-482c-800e-d6e4420c2c16" width="400px" />

* **Switching branches** - If you're working on a CW session, and realize you'd like to build upon a different branch, you can now click the `New Session` button, and select `Select a branch`. This will display a dialog with a list of the current repo's branches, and let you start a new ad-hoc task for the specified branch.

* **切换分支** - 如果你正在处理 CW 会话，并意识到你想基于不同的分支构建，现在你可以点击“新会话”按钮，并选择“选择分支”。这将显示一个包含当前仓库分支列表的对话框，并让你为指定的分支启动一个新的临时任务。

   <img src="https://github.com/user-attachments/assets/ec01d52b-526a-400c-a200-1ef4946fff00" width="400px" />

* **Terminal status** - The terminal icon (in the workspace toolbar) now displays a green dot whenever the terminal is connected. Now that CW auto-start's the terminal (for repos that don't include a `devcontainer.json`), this allows you to quickly see when the terminal is ready, so you can jump into it and start building/running code.

* **终端状态** - 终端图标（在工作区工具栏中）现在在终端连接时显示一个绿色点。现在 CW 自动启动终端（对于不包含 `devcontainer.json` 的仓库），这使你可以快速查看终端何时准备就绪，以便你可以进入并开始构建/运行代码。

   <img src="https://github.com/user-attachments/assets/ccffd7a9-ba10-4da7-a025-1df765c334fb" width="400px" />
  
* **Experiments** - We periodically ship new features that are off by-default, since they're not quite ready for prime-time usage. And to make it easier to discover these features, and know when you have them on, the workspace toolbar now displays a beaker icon, that indicates how many experiments you have enabled.

* **实验** - 我们定期发布默认关闭的新功能，因为它们还没有准备好用于黄金时段。为了更容易发现这些功能，并知道你何时启用了它们，工作区工具栏现在显示一个烧杯图标，指示你启用了多少实验。

   <img src="https://github.com/user-attachments/assets/d9fc7b50-d736-4d01-b3e1-5df5ce70b964" width="200px" />

   When clicked, this button brings up the `Experiments` dialog, which let's you try out our cutting-edge features (and then hopefully send us feedback!) 🔥

   点击此按钮时，会弹出“实验”对话框，让你试用我们的前沿功能（然后希望你能向我们发送反馈！）🔥

   <img src="https://github.com/user-attachments/assets/00af1eb1-dddf-4f9a-b82f-2a2097b2e649" width="400px" />

* **Docs/changelog** - To make it easier to access the CW docs and changelog (the thing you're currently reading!), the user menu (in the workspace toolbar) now includes links for the `User manual` and `What's new?`. That way you can keep up with the fun, and see how we're addressing your feedback. But without needing to remember/search for random URLs in our [GitHub Next Discord](https://gh.io/next-discord) 🤗

* **文档/变更日志** - 为了更容易访问 CW 文档和变更日志（你当前正在阅读的内容！），用户菜单（在工作区工具栏中）现在包括“用户手册”和“新功能？”的链接。这样你可以跟上乐趣，看看我们如何解决你的反馈。但无需记住/搜索我们 [GitHub Next Discord](https://gh.io/next-discord) 中的随机 URL 🤗

   <img src="https://github.com/user-attachments/assets/20de5b4e-346e-43a1-b5aa-fc43e7c5ee52" width="200px" />

## 📅 26 July 2024

### Features / Enhancements

### 功能/增强

* [Session continuation](#session-continuation)
* [Proceed to plan (task->plan)](#proceed-to-plan-task-plan)
* [Optimized file viewers](#optimized-file-viewers)
* [Spec/plan/code improvements](#specplancode-improvements)
  
### Session continuation

### 会话继续

When you create a repository/PR/branch from Copilot Workspace, we now provide two options for your next step:

当你从 Copilot Workspace 创建仓库/PR/分支时，我们现在为你的下一步提供两个选项：

   * Starting an entirely new session (for the current repo/PR/branch)

   * 启动一个全新的会话（针对当前仓库/PR/分支）

   * Continuing to iterate on the current session (<ins>this is the new part!</ins> 🙌)   

   * 继续迭代当前会话（<ins>这是新部分！</ins> 🙌）   

   <img width="500px" src="https://github.com/user-attachments/assets/0d12972a-0b1d-4193-a930-535f88191d66"/><br />
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Just created a PR? Let's stay in the flow!_

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_刚创建了一个 PR？让我们保持在流程中！_

This is a _significant_ change to the CW workflow, and has the following key benefits:

这是对 CW 工作流程的_重大_更改，并具有以下主要优点：

   * It allows you to share context across multiple commits, and consolidate logically-related changes within a single session

   * 它允许你在多个提交中共享上下文，并在单个会话中合并逻辑相关的更改

   * It allows you to correct post-commit mistakes or address feedback, without having to create follow-up CW sessions

   * 它允许你纠正提交后的错误或解决反馈，而无需创建后续的 CW 会话
 
In this sense, a CW session has evolved from being associated with a single commit, and is now logically associated with a branch, or chain of commits (for trunk-based development). This not only provides a lot more flexibility, but also, reflects the way that many developers wanted to use it. So we're excited to hear feedback!

从这个意义上说，CW 会话已经从与单个提交相关联演变为逻辑上与分支或提交链（用于基于主干的开发）相关联。这不仅提供了更多的灵活性，还反映了许多开发人员希望使用它的方式。因此，我们很高兴听到反馈！

<img width="400px" src="https://github.com/user-attachments/assets/c525f7e9-5b2b-45dc-a463-c4bc00810837" />

&nbsp;&nbsp;&nbsp;_A single CW session that lead to a PR + follow-up commit_

&nbsp;&nbsp;&nbsp;_一个导致 PR + 后续提交的单个 CW 会话_

To make this multi-commit workflow even more fun...when you implement changes to a CW session (that was already pushed to a repo/PR/branch), you'll see a new `All | Unchanged` toggle button in the toolbar. This allows you to easily see the changes for the most recent iteration, as opposed to the changes for the overall session (which could now include multiple commits).

为了使这个多提交工作流程更加有趣...当你对 CW 会话进行更改（已经推送到仓库/PR/分支）时，你会在工具栏中看到一个新的“全部|未更改”切换按钮。这使你可以轻松查看最近一次迭代的更改，而不是整个会话的更改（现在可能包括多个提交）。

For example, if you have a CW session that you created a PR from, you could address PR feedback in that same session, quickly review those exact changes, and then confidently push an update to the PR (after running/testing it in the terminal!)

例如，如果你有一个从中创建 PR 的 CW 会话，你可以在同一个会话中解决 PR 反馈，快速审查这些确切的更改，然后自信地推送更新到 PR（在终端中运行/测试后！）

<img src="https://github.com/user-attachments/assets/7c89389a-7607-4ecc-ab7c-d140061fac44" width="800px" />

&nbsp;&nbsp;&nbsp;_Reviewing a readme update to an existing PR/CW session_

&nbsp;&nbsp;&nbsp;_审查现有 PR/CW 会话的自述文件更新_

---

### Proceed to plan (task->plan)

### 继续计划（任务->计划）

When you start an ad-hoc task (opening a repo/PR/branch in CW, as opposed to an issue), you can now choose to skip generating a spec, and proceed directly to planning 🏃

当你启动一个临时任务（在 CW 中打开仓库/PR/分支，而不是问题）时，你现在可以选择跳过生成规范，并直接进行计划 🏃

<img src="https://github.com/user-attachments/assets/68ddf82d-26b5-4008-8222-7730b4f0afcc" width="600px" />

This helps CW feel a lot more optimized, for tasks that fall into the following categories:

这有助于 CW 感觉更加优化，适用于以下类别的任务：

* They're simple or precise in nature (e.g. `Rename the readme and translate it into German`)

* 它们本质上是简单或精确的（例如 `重命名自述文件并将其翻译成德语`）

* They're very well-defined/articulated (e.g. you write a paragraph/bullet points for the desired behavior)

* 它们非常明确/清晰（例如，你为所需行为编写一段/要点）

In these cases, you likely don't need a summary of the task (because you just wrote it!), or help fleshing out the success criteria (because it's simple!). And in those instances, CW should now feel a lot faster, more lightweight, and easier to iterate 🚀

在这些情况下，你可能不需要任务的摘要（因为你刚刚写了它！），或帮助充实成功标准（因为它很简单！）。在这些情况下，CW 现在应该感觉更快，更轻量化，更容易迭代 🚀

When you proceed directly to the plan, the `Specification` panel will still be displayed in the timeline, but it will be greyed out. And if you review the plan/code, and realize that you actually do need a bit more help investigating the task, then you can expand the `Task` panel and select `Add Specification`. That way the spec feels helpful if/when needed, but not required 👍

当你直接进行计划时，“规范”面板仍将显示在时间线中，但它将变灰。如果你审查计划/代码，并意识到你实际上确实需要更多帮助来调查任务，那么你可以展开“任务”面板并选择“添加规范”。这样，如果/在需要时，规范会感觉有帮助，但不是必需的 👍

<img src="https://github.com/user-attachments/assets/5460d267-9769-48a3-9d76-5a37f83bed35" width="600px" />

_The CW timeline, with the `Specification` panel skipped, as we went from task->plan_

_CW 时间线，跳过“规范”面板，因为我们从任务->计划_

When you open an issue, CW continues to generate a spec as the first step, and doesn't give you the option to skip it. This is because issues are much more complex and ambiguous in practice, and therefore, they commonly benefit from the summarization/contextualization/thinking that the spec panel offers.

当你打开一个问题时，CW 继续生成规范作为第一步，并且不提供跳过它的选项。这是因为问题在实践中要复杂得多且模糊不清，因此，它们通常受益于规范面板提供的总结/上下文/思考。

---

### Optimized file viewers

### 优化的文件查看器

When you implement a plan, the `Files changed` list now includes two key improvements, to make it easier to review the code:

当你实施计划时，“更改的文件”列表现在包括两个关键改进，以便更轻松地审查代码：

* Added/renamed files are displayed using a code editor (as opposed to a diff editor)

* 添加/重命名的文件使用代码编辑器显示（而不是差异编辑器）

* Deleted files are automatically collapsed, so they don't clutter up the list

* 删除的文件会自动折叠，因此它们不会使列表混乱

These changes also make it easier to edit code post-implement, since it's a lot nicer to write code in a standard editor vs. a diff editor. Especially with the help of CW's integrated language services + Copilot completions 💙

这些更改还使得在实施后更容易编辑代码，因为在标准编辑器中编写代码比在差异编辑器中编写代码要好得多。特别是在 CW 的集成语言服务 + Copilot 补全的帮助下 💙

<img src="https://github.com/user-attachments/assets/7c868d7e-9a93-44d7-830e-63a30dc48490" width="600px" />

&nbsp;&nbsp;&nbsp;_Reviewing added/deleted files in a more natural/distraction-free way_

&nbsp;&nbsp;&nbsp;_以更自然/无干扰的方式审查添加/删除的文件_

---

### Spec/plan/code improvements

### 规范/计划/代码改进

We made numerous improvements to the way we generate the spec and plan, which should increase the quality a bit, for both larger repos and complex tasks. Additionally, we improved our code generation, so that it shouldn't delete unrelated code/comments when implementing a task.

我们对生成规范和计划的方式进行了许多改进，这应该会提高大型仓库和复杂任务的质量。此外，我们改进了代码生成，因此在实施任务时不应删除不相关的代码/注释。

Finally, after enabling speculative decoding a few weeks ago, we've confirmed that it's stable enough to be on by default, and we've removed it from the `Experiments` panel. That said, we really appreciate all the great feedback from preview users, as we've continued to focus on improving the perf and quality of code generation 🙏

最后，在几周前启用推测解码后，我们确认它足够稳定，可以默认启用，并且我们已将其从“实验”面板中移除。也就是说，我们非常感谢预览用户的所有出色反馈，因为我们继续专注于提高代码生成的性能和质量 🙏

## 📅 12 July 2024

### Features / Enhancements

### 功能/增强

* **Markdown preview** - The file explorer and file diffs now include support for previewing Markdown content. This allows you to easily visualize how formatting with look (e.g. tables), when you're adding or editing docs.

* **Markdown 预览** - 文件资源管理器和文件差异现在包括对预览 Markdown 内容的支持。这使你可以在添加或编辑文档时轻松可视化格式的外观（例如表格）。

   To use it, simply click the eye icon in the toolbar above the file. And over time, you can expect to see this icon appear for other file types, as we expand the preview support 🚀

   要使用它，只需点击文件上方工具栏中的眼睛图标。随着时间的推移，你可以期待看到此图标出现在其他文件类型中，因为我们扩展了预览支持 🚀

  ![image](https://github.com/user-attachments/assets/f887fcb6-aaf6-4cba-b103-2c65e8eee839)

* **Codespaces auto-start** - We now automatically spin up a Codespace when you click the `Implement` button, as opposed to waiting until you open the terminal. This has the benefit of providing language services when reviewing code (e.g. hover info, error squiggles, go-to-definition), and making the terminal available as soon as you need it (e.g. to build the code after it's done implementing).

* **Codespaces 自动启动** - 我们现在在你点击“实施”按钮时自动启动一个 Codespace，而不是等到你打开终端。这在审查代码时提供语言服务（例如悬停信息，错误波浪线，转到定义），并在你需要时立即提供终端（例如在实施完成后构建代码）。

   ![image](https://github.com/user-attachments/assets/c3045665-ac26-41cf-9670-41bda8ebf518)

  _The little green dot indicates that you're session is enriched with language services, thanks to the auto-started Codespaces!_

  _小绿点表示你的会话充实了语言服务，感谢自动启动的 Codespaces！_

   > Note: If a repo includes a `devcontainer.json` file, we don't currently auto-start the Codespace. We'll be adding support for that soon, but in the meantime, you can enable this by checking the `Spin up a codespace on start of implement` setting in the `Experiments` panel.

   > 注意：如果仓库包含 `devcontainer.json` 文件，我们目前不会自动启动 Codespace。我们将很快添加对此的支持，但与此同时，你可以通过在“实验”面板中勾选“在实施开始时启动 Codespace”设置来启用此功能。

* **Increased usage quota** - In order to enable power users to get the most out of Copilot Workspace, we've doubled the daily usage quota. We were seeing lots of cases of folks hitting their limit, and so we're excited to unblock that, and let to AI-assisted creativity flow more freely 💙

* **增加使用配额** - 为了使高级用户能够充分利用 Copilot Workspace，我们将每日使用配额增加了一倍。我们看到很多人达到了他们的限制，所以我们很高兴解除这个限制，让 AI 辅助的创造力更自由地流动 💙

### Bug Fixes

### 错误修复

* **Exit path dialogs** - When you attempt to create a PR/branch/commit/repo from a Copilot Workspace session, the modal dialog will no longer automatically close when you click outside of it. That way you don't lose any work (e.g. a PR description) as a result of an accidental click/drag.

* **退出路径对话框** - 当你尝试从 Copilot Workspace 会话创建 PR/分支/提交/仓库时，模态对话框在你点击其外部时将不再自动关闭。这样你不会因为意外点击/拖动而丢失任何工作（例如 PR 描述）。

* **File explorer view toggle** - When you open a file in the file explorer, the `Code / Diff` toggle button now works correctly for added/edited files.

* **文件资源管理器视图切换** - 当你在文件资源管理器中打开文件时，“代码/差异”切换按钮现在可以正确地用于添加/编辑的文件。

* **Invalid markdown in tasks** - If an issue/task includes invalid markdown for image references, Copilot Workspace is now resilient to that, and will simply render it as a broken image.

* **任务中的无效 markdown** - 如果问题/任务包含无效的图像引用 markdown，Copilot Workspace 现在对此具有弹性，并将其简单地呈现为损坏的图像。

* **Resuming interrupted sessions** - If you accidentally close a session while it's in the middle of generating the spec, Copilot Workspace will now automatically resume spec generation once you re-open it.

* **恢复中断的会话** - 如果你在生成规范的过程中意外关闭会话，Copilot Workspace 现在将在你重新打开它后自动恢复规范生成。
## 📅 3 July 2024

This week's release is all about performance and quality. So when you use Copilot Workspace, things should feel **noticeably faster** overall. And also, a little bit smarter 😎 

本周的发布全部关于性能和质量。因此，当你使用 Copilot Workspace 时，整体上应该感觉**明显更快**。而且，也会更聪明一点 😎

| For example... | Before today | After today |
|-|-|-|
| Generating the <ins>code</ins> for [this session](https://copilot-workspace.githubnext.com/lostintangent/gistpad?shareId=3538ee23-b72f-4681-932a-b293e7418f82) | ~9.5 minutes | ~2 minutes (-7.5 minutes 🔥) |
| Generating the <ins>plan</ins> for [this session](https://copilot-workspace-staging.githubnext.com/altryne/openai-cookbook?shareId=7e46d597-7a68-41d2-b95c-66bdd2b8a4bc) |~33 seconds | ~15 seconds (>2x speed-up) |
| Generating the <ins>spec</ins> for [this session](https://copilot-workspace.githubnext.com/lostintangent/github-security-alerts/issues/10?shareId=7a84f35c-a612-4ea3-ae0f-2505786819ee) | ~15 seconds | ~6 seconds (>2x speed-up) |

| 例如... | 今天之前 | 今天之后 |
|-|-|-|
| 为[此会话](https://copilot-workspace.githubnext.com/lostintangent/gistpad?shareId=3538ee23-b72f-4681-932a-b293e7418f82)生成<ins>代码</ins> | ~9.5 分钟 | ~2 分钟（-7.5 分钟 🔥） |
| 为[此会话](https://copilot-workspace-staging.githubnext.com/altryne/openai-cookbook?shareId=7e46d597-7a68-41d2-b95c-66bdd2b8a4bc)生成<ins>计划</ins> |~33 秒 | ~15 秒（>2 倍加速） |
| 为[此会话](https://copilot-workspace.githubnext.com/lostintangent/github-security-alerts/issues/10?shareId=7a84f35c-a612-4ea3-ae0f-2505786819ee)生成<ins>规范</ins> | ~15 秒 | ~6 秒（>2 倍加速） |

What contributed to these gains?

是什么促成了这些收益？

* We migrated to GPT-4o, and made numerous improvements to spec/plan/code generation
* We introduced "speculative decoding" for code generation _(read below for details)_

* 我们迁移到 GPT-4o，并对规范/计划/代码生成进行了许多改进
* 我们为代码生成引入了“推测解码” _(请阅读下面的详细信息)_

### Speculative decoding

### 推测解码

We [previously shipped](https://github.com/githubnext/copilot-workspace-user-manual/blob/main/changes.md#perf-improvements) an experiment called "speculative decoding", which provided a 2x+ speed-up on code generation. That experiment is now on by default, and is a key part of the boost you'll see when implementing a plan.

我们[之前发布](https://github.com/githubnext/copilot-workspace-user-manual/blob/main/changes.md#perf-improvements)了一个名为“推测解码”的实验，它在代码生成方面提供了 2 倍以上的加速。该实验现在默认开启，并且是你在实施计划时看到的提升的关键部分。

With this enabled, Copilot Workspace now predicts the "edit locations" within a file, as opposed to re-generating every line. This allows us to retain the stability of whole-file generation, but with a **dramatic improvement** in performance.

启用此功能后，Copilot Workspace 现在预测文件中的“编辑位置”，而不是重新生成每一行。这使我们能够保持整个文件生成的稳定性，但性能有了**显著提高**。

Additionally, to indicate when Copilot Workspace is predicting the next edit location (vs. editing code), the progress bar will display a "barber pole" overlay. That way, you know when it's thinking hard on your behalf ❤️

此外，为了指示 Copilot Workspace 何时预测下一个编辑位置（与编辑代码相对），进度条将显示一个“理发杆”覆盖层。这样，你就知道它何时在为你努力思考 ❤️

![image](https://github.com/user-attachments/assets/153095d2-8300-4703-8d0a-ae53ba2771fc)

### File copy operations

### 文件复制操作

When a task/issue includes the need to copy a file, this should now work as expected. Previously, Copilot Workspace would incorrectly attempt to rename the existing file. And now, it will translate the copy operation into the creation of a new file, that includes a step for copying the contents of the originating file (along with any subsequent edits).

当任务/问题需要复制文件时，现在应该可以按预期工作。以前，Copilot Workspace 会错误地尝试重命名现有文件。而现在，它会将复制操作转换为创建一个新文件，其中包括复制原始文件内容的步骤（以及任何后续编辑）。

For example, here's a [sample session](https://copilot-workspace-staging.githubnext.com/githubnext/hello-world?shareId=a071696d-32e6-4428-9b0f-e09dbf61e1aa) that copies a file, and translates it's `console.log` messages into Japanese:

例如，这里有一个[示例会话](https://copilot-workspace-staging.githubnext.com/githubnext/hello-world?shareId=a071696d-32e6-4428-9b0f-e09dbf61e1aa)，它复制了一个文件，并将其 `console.log` 消息翻译成日语：

<img src="https://github.com/user-attachments/assets/27d81847-8934-4836-9b8e-95dfb7755f15" width="400px" />

## 📅 28 June 2024

### Features / Enhancements

### 功能/增强

* **Copilot completions and language services in embedded editors** - Support for rich language features (hover info, error squiggles, go-to-definition) and Copilot completions are now enabled by default. This was previously released as an opt-in experiment, and thanks to the amazing feedback from preview users, it's now ready for general usage 🎉 

* **嵌入式编辑器中的 Copilot 补全和语言服务** - 现在默认启用对丰富语言功能（悬停信息、错误波浪线、转到定义）和 Copilot 补全的支持。这之前作为选择加入的实验发布，感谢预览用户的惊人反馈，现在已准备好供一般使用 🎉 

   <img src="https://github.com/user-attachments/assets/077d072d-71fd-4c31-b038-5ac0c1499d22" width="800px" />
   
   A few things to note:
   
   * Copilot completions are supported in all languages, but the other editor features currently only support JS/TS, Python, and Go. We'll be introducing support for other languages soon, and so let us know which ones you'd like to see next 💪

   * Copilot 补全支持所有语言，但其他编辑器功能目前仅支持 JS/TS、Python 和 Go。我们将很快引入对其他语言的支持，因此请告诉我们你希望接下来看到哪些语言 💪

   * The rich editing features are only enabled when a terminal/Codespace is attached to your session. So if you'd like to use them, either manually open the integrated terminal, or enable one of the `Spin up a codespace...` experiments. And in either case, you can tell that rich editing is "activated", because you'll see a cool little green dot in the upper-right of the `Files changed` section.

   * 只有在终端/Codespace 附加到你的会话时，才会启用丰富的编辑功能。因此，如果你想使用它们，可以手动打开集成终端，或启用 `Spin up a codespace...` 实验之一。在任何一种情况下，你都可以知道丰富的编辑已“激活”，因为你会在“更改的文件”部分的右上角看到一个很酷的小绿点。

      <img src="https://github.com/user-attachments/assets/6c5a3d6e-e224-4994-8910-ee7ffcd6f802" width="300px" />
      
   * In addition to stabilizing the existing feature set, we've also expanded the editing experience quite a bit. So read on for details about that!
   
   * 除了稳定现有的功能集外，我们还大大扩展了编辑体验。所以请继续阅读以了解详细信息！

* **Auto-completion / signature help** - When editing code within Copilot Workspace, you'll now see auto-completion everywhere you'd expect. And also, when you call functions, you'll see the editor overlay that describes its signature details. This, along with the existing Copilot completions support, should make it a lot nicer to make any last minute tweaks, before sending out a PR 🚀

* **自动补全/签名帮助** - 在 Copilot Workspace 中编辑代码时，你现在会在你期望的任何地方看到自动补全。此外，当你调用函数时，你会看到描述其签名详细信息的编辑器覆盖层。这与现有的 Copilot 补全支持一起，应该使在发送 PR 之前进行任何最后的调整变得更加愉快 🚀

   <img src="https://github.com/user-attachments/assets/455678c5-b086-4b1b-a1a8-332d4d2ff99c" width="600px" />
   
* **Error squiggles on mobile** - When using Copilot Workspace from your phone, you can now place your cursor over an error squiggle in an editor, and correctly see the details of the issue. With this in place, we now have full parity for rich editing, between desktop and mobile 📱

* **移动设备上的错误波浪线** - 当你从手机上使用 Copilot Workspace 时，你现在可以将光标放在编辑器中的错误波浪线上，并正确查看问题的详细信息。有了这个功能，我们现在在桌面和移动设备之间实现了丰富编辑的完全一致 📱

   <img src="https://github.com/user-attachments/assets/19b8bece-2cb4-48c6-8209-79c56a344a41" width="400px" />

* **Go-to-definition for external dependencies** - When you perform a go-to-definition on a 3rd-party API (e.g. an NPM package), it will now correctly navigate to the corresponding type definition. That way, you can inspect the API surface for any dependencies, without needing to leave the workspace.

* **外部依赖项的转到定义** - 当你对第三方 API（例如 NPM 包）执行转到定义时，它现在会正确导航到相应的类型定义。这样，你可以检查任何依赖项的 API 表面，而无需离开工作区。

   <img src="https://github.com/user-attachments/assets/ebffffc3-acb0-426e-a5eb-ecd438fee658" width="600px" />
   
   _Note: This will only work once you've restored app dependencies from the terminal and/or if your repo includes a `devcontainer.json` file that does this automatically._

   _注意：这只有在你从终端恢复应用程序依赖项和/或你的仓库包含一个自动执行此操作的 `devcontainer.json` 文件时才有效。_

* **Copilot in Codespaces** - When you open a session in a Codespace, the [Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) and [Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) extensions are now automatically installed for you. That way, you can edit along with Copilot in the workspace, and then seamlessly continue doing that in a Codespace, without any additional setup.

* **Codespaces 中的 Copilot** - 当你在 Codespace 中打开会话时，[Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) 和 [Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) 扩展现在会自动为你安装。这样，你可以在工作区中与 Copilot 一起编辑，然后在 Codespace 中无缝继续进行，而无需任何额外设置。

   <img src="https://github.com/user-attachments/assets/8366d834-5249-480c-87e1-0335f66256d0" width="400px" />

* **Renaming files** - Copilot Workspace now understands when a file is being renamed, but doesn't need to be edited. And in those cases, it can perform the rename immediately, as opposed to AI-generating it's contents. This results in a big perf boost for plans that include simple renames, and is a follow-up to the optimizations we made for deleting files.

* **重命名文件** - Copilot Workspace 现在理解何时重命名文件，但不需要编辑。在这些情况下，它可以立即执行重命名，而不是 AI 生成其内容。这为包含简单重命名的计划带来了巨大的性能提升，并且是我们为删除文件所做的优化的后续。

   <img src="https://github.com/user-attachments/assets/6b3aff5a-8f48-49ad-9328-89bb817634b0" width="700px" />

* **Session management** - You can now delete a session from within the workspace, by clicking the `New Session` button and selecting `Delete Session`. This was already possible from [the dashboard](https://copilot-workspace.githubnext.com), but this new entrypoint makes it easier to clean up sessions once you're done with them.

* **会话管理** - 你现在可以通过点击“新会话”按钮并选择“删除会话”从工作区中删除会话。这在[仪表板](https://copilot-workspace.githubnext.com)中已经可以实现，但这个新入口使你完成会话后更容易清理会话。

   <img src="https://github.com/user-attachments/assets/e32e052c-e5e9-4c5a-ab98-20f84cc6c489" width="400px" />

## 📅 14 June 2024

### Features / Enhancements

### 功能/增强

* **Terminal command suggestions** - In order to make it easier to use the terminal (including from your phone!), you can now describe an action you’d like to perform (e.g. `Build the project`, `List all markdown files in the src directory`), and let Copilot suggest the corresponding shell command. And just like everything else in Copilot Workspace, you can edit or regenerate the suggestion, to make sure you get exactly what you’re looking for 🚀

* **终端命令建议** - 为了更容易使用终端（包括从手机上！），你现在可以描述你想要执行的操作（例如 `构建项目`，`列出 src 目录中的所有 markdown 文件`），并让 Copilot 建议相应的 shell 命令。就像 Copilot Workspace 中的其他所有内容一样，你可以编辑或重新生成建议，以确保你得到你想要的 🚀

   <img src="https://github.com/user-attachments/assets/c21f9b37-3671-44a7-996c-3198a628d200" width="800px" />

* **Devcontainer tasks** - To make it simpler to run common/repeated terminal commands, a repository can now define `tasks` in its `devcontainer.json` file, which configure the shell commands needed to perform a build, test, and/or run against it ([example](https://github.com/lostintangent/contributor-gallery/blob/main/.devcontainer/devcontainer.json)).

* **Devcontainer 任务** - 为了简化运行常见/重复的终端命令，现在可以在仓库的 `devcontainer.json` 文件中定义 `tasks`，这些任务配置了执行构建、测试和/或运行所需的 shell 命令（[示例](https://github.com/lostintangent/contributor-gallery/blob/main/.devcontainer/devcontainer.json)）。

   When defined, these tasks will appear as buttons in the integrated terminal, so that validating code changes becomes as simple as a couple clicks. Even cooler, you can edit the `devcontainer.json` file directly within Copilot Workspace, and any new/changed tasks will appear immediately 💪

   定义后，这些任务将作为按钮出现在集成终端中，因此验证代码更改变得像点击几下一样简单。更酷的是，你可以直接在 Copilot Workspace 中编辑 `devcontainer.json` 文件，任何新/更改的任务将立即出现 💪

   <img src="https://github.com/user-attachments/assets/9656109a-3ef5-4b09-a3cc-8b4bb7432c29" width="800px" />

* **Copilot completions on mobile** - When manually editing code from your phone, you can now make use of Copilot completions, thanks to a new `Accept` button which appears anytime a Copilot suggestion is visible in the editor.

* **移动设备上的 Copilot 补全** - 当你从手机上手动编辑代码时，你现在可以利用 Copilot 补全，这要归功于一个新的 `接受` 按钮，只要在编辑器中看到 Copilot 建议时就会出现。

   <img src="https://github.com/user-attachments/assets/8ca206e8-fde5-432f-9105-b0700e427f1a" width="400px" />

   _Note: In order to make use of Copilot completions, you need to check the `Enable Copilot and language services in editors` option in the `Experiments` dialog (which is available when clicking on your avatar in the upper-right)._

   _注意：为了使用 Copilot 补全，你需要在“实验”对话框中勾选“在编辑器中启用 Copilot 和语言服务”选项（点击右上角的头像时可用）。_

* **Simplified branch tasks** - When you start a task from the GitHub repository page, Copilot Workspace will now respect the currently selected branch. That way, you can easily perform any tasks, against any branch 🔥

* **简化的分支任务** - 当你从 GitHub 仓库页面开始任务时，Copilot Workspace 现在会尊重当前选择的分支。这样，你可以轻松地对任何分支执行任何任务 🔥

   <img src="https://github.com/user-attachments/assets/4bdfd1e5-d2b4-412f-a7ef-e417ea08aa7c" width="700px" />

### Perf Improvements

### 性能改进

* **Speculative decoding** - We're working to improve the feedback loop when implementing a plan. And as part of that, we've introduced a new experiment that should speed up code generation by ~2.5x (!!). We'll be turning this on by default soon, but for now, you can try it out by checking the `Use speculative decoding to speed up implement` option in the `Experiments` dialog (which you can access by clicking your avatar in the upper-right).

* **推测解码** - 我们正在努力改进实施计划时的反馈循环。作为其中的一部分，我们引入了一个新的实验，应该可以将代码生成速度提高约 2.5 倍（！！）。我们很快会默认开启此功能，但现在，你可以通过在“实验”对话框中勾选“使用推测解码加速实施”选项来试用它（你可以通过点击右上角的头像访问该对话框）。

* **New Session** - When you click the `New Session` button from the [Copilot Workspace dashboard](https://copilot-workspace.githubnext.com), your MRU list of repositories should show up immediately, since we now pre-fetch/cache them in advance. That way, starting a new session is 2-3 faster 🏎️

* **新会话** - 当你从 [Copilot Workspace 仪表板](https://copilot-workspace.githubnext.com)点击“新会话”按钮时，你的 MRU 仓库列表应该会立即显示，因为我们现在预先获取/缓存它们。这样，启动新会话的速度提高了 2-3 倍 🏎️

## 📅 24 May 2024

### Features / Enhancements

### 功能/增强

* **PWA support** - You can now install Copilot Workspace on your desktop or mobile home screen, and have a more native app-like feel (e.g. no browser chrome, no accidental back navigations when swiping left, better keyboard handling). This also makes it easier to jump back into in-progress tasks, from any of your devices 💙

* **PWA 支持** - 你现在可以将 Copilot Workspace 安装在桌面或移动设备的主屏幕上，并拥有更原生的应用程序感觉（例如，没有浏览器 chrome，向左滑动时不会意外返回导航，更好的键盘处理）。这也使你可以更轻松地从任何设备跳回进行中的任务 💙

   To get started, simply navigate to the [Copilot Workspace dashboard](https://copilot-workspace.githubnext.com), and then either click the `Install Copilot Workspace` button in the navigation bar (on desktop), or click `Add to Home Screen` from the share menu (on mobile).

   要开始使用，只需导航到 [Copilot Workspace 仪表板](https://copilot-workspace.githubnext.com)，然后在导航栏中点击“安装 Copilot Workspace”按钮（在桌面上），或从共享菜单中点击“添加到主屏幕”（在移动设备上）。

   ![image](https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/399ff59d-08b7-464a-9eed-cc5b1b3f2260)<br />
   &nbsp;&nbsp;_Working on a task in a beautiful Copilot Workspace PWA from your desktop_ 😻

   &nbsp;&nbsp;<img src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/ba6673bb-5fcb-4406-9975-e3c6aa7e68ef" width="400px" /><br />
   &nbsp;&nbsp;_Copilot Workspace nestled comfortably on the iOS dock_

* **Organizing the plan** - You can now re-order the plan by moving files up or down in the list. And since the `Files changed` list is also sorted by the plan, this allows you to better organize sessions for both self-review, but also, to better curate them when sharing sessions with others (like [this](https://copilot-workspace.githubnext.com/lostintangent/gitdoc/issues/52?shareId=94b2e8df-15ea-41bd-b5f6-a1d9f5b376dc)!).

* **组织计划** - 你现在可以通过在列表中向上或向下移动文件来重新排序计划。由于“更改的文件”列表也按计划排序，这使你可以更好地组织会话以进行自我审查，但也可以在与他人共享会话时更好地策划它们（如[此示例](https://copilot-workspace.githubnext.com/lostintangent/gitdoc/issues/52?shareId=94b2e8df-15ea-41bd-b5f6-a1d9f5b376dc)！）。

   When you actually implement the plan, Copilot Workspace will determine the most logical order to make edits in (e.g. creating shared functions/components, before editing their consumers). So you can feel free to organize the plan in whichever way feels best to you, and rest assured that Copilot will continue to do the right thing 🙌

   当你实际实施计划时，Copilot Workspace 将确定最合乎逻辑的编辑顺序（例如，在编辑其使用者之前创建共享函数/组件）。因此，你可以随意以你认为最好的方式组织计划，并放心，Copilot 将继续做正确的事情 🙌

   <img src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/a6b92ea0-f1b4-40c3-ac7c-59f4d89a1489" width="400px" /><br />
   &nbsp;&nbsp;_Updating the order of files in a plan_

* **Enhanced social preview image** - When you share a Copilot Workspace session on Slack/Teams/Twitter/SMS/etc. (like [this one](https://copilot-workspace.githubnext.com/lostintangent/gitdoc/issues/52?shareId=94b2e8df-15ea-41bd-b5f6-a1d9f5b376dc)!) the preview now displays a customized image for the repo and task it’s associated with _(for public repos)_. It also now includes a warp speed background, since clicking on the link is sort of like transporting you into another space 🚀 (and of course, it just looks cool...)

* **增强的社交预览图像** - 当你在 Slack/Teams/Twitter/SMS 等上共享 Copilot Workspace 会话时（如[此示例](https://copilot-workspace.githubnext.com/lostintangent/gitdoc/issues/52?shareId=94b2e8df-15ea-41bd-b5f6-a1d9f5b376dc)！），预览现在显示与其关联的仓库和任务的自定义图像 _(对于公共仓库)_. 它现在还包括一个曲速背景，因为点击链接有点像将你传送到另一个空间 🚀（当然，它看起来很酷...）

   <img width="800px" src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/b6bab922-1dd2-40c5-825c-53a2c870cb15" /><br />
   _Sharing a Copilot Workspace session with someone in Slack_

### Bug Fixes

### 错误修复

* **Manually adding files to the plan** - The `Add file to plan` dialog now correctly detects existing file paths in all cases, and makes it easy to add/edit/rename/delete files from the plan.

* **手动将文件添加到计划中** - “将文件添加到计划”对话框现在在所有情况下都能正确检测到现有文件路径，并使从计划中添加/编辑/重命名/删除文件变得容易。

* **File syncing for long-ish running sessions** - The bi-directional file syncer (that syncs changes between the Workspace and the terminal) now properly syncs files for sessions, when the `HEAD` of the branch has since progressed. This makes it easier to work on Workspace sessions throughout the day, or across days, regardless how active the target branch is 💪

* **长时间运行会话的文件同步** - 当分支的 `HEAD` 进展时，双向文件同步器（在工作区和终端之间同步更改）现在正确地为会话同步文件。这使得无论目标分支有多活跃，都可以更轻松地在一天或几天内处理工作区会话 💪

## 📅 17 May 2024

### Features / Enhancements

### 功能/增强

* **Revise the spec, plan, and code with natural language** - In addition to making direct edits to the specification or plan, you can now provide natural language instructions for how you'd like to revise them (e.g. `Add tests for this change`). This same capability is also available on the header for changed files, which allows you to revise code based on a specific instruction (e.g. `Move the logging logic into a separate function`), in addition to editing it manually.

* **用自然语言修订规范、计划和代码** - 除了直接编辑规范或计划外，你现在还可以提供自然语言指令，说明你希望如何修订它们（例如 `为此更改添加测试`）。这种相同的功能也可用于更改文件的标题，这使你可以根据特定指令修订代码（例如 `将日志记录逻辑移到单独的函数中`），除了手动编辑它。

   ![image](https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/883e48a1-265c-4b12-bfaa-4c70e4ec2317)

* **Copilot completions and language services in embedded editors** - We've shipped an initial experience for getting hover info, error squiggles, go-to-definition, and Copilot completions directly from the embedded editors in Copilot Workspace. That way you can quickly spot issues to fix, easily navigate the code changes, or make manual edits, while receiving the Copilot assistance you know and love 💙

* **嵌入式编辑器中的 Copilot 补全和语言服务** - 我们已经发布了一个初始体验，可以直接从 Copilot Workspace 中的嵌入式编辑器获取悬停信息、错误波浪线、转到定义和 Copilot 补全。这样你可以快速发现需要修复的问题，轻松导航代码更改，或进行手动编辑，同时获得你熟悉和喜爱的 Copilot 帮助 💙

   ![image](https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/1fd21aa6-028c-44c7-ac9e-3fa55249c914)

   Here's a few things to note about this enhancement:

   这里有一些关于此增强功能的注意事项：

   * It isn't on by default, and so if you want to try it, you need to click on your avatar in the upper right, select `Experiments` and then check the `Enable Copilot and language services in editors` setting.
   * The language services (hover info, error squiggles, go-to-definition) currently only support JavaScript/TypeScript, Python and Go. But more languages are coming!
   * Support for Copilot completions requires an active Copilot subscription. If you don't have one, then you simply won't see "ghost text" in the editor, but you can still use the language services described above.

   * 它默认未启用，因此如果你想尝试，你需要点击右上角的头像，选择“实验”，然后勾选“在编辑器中启用 Copilot 和语言服务”设置。
   * 语言服务（悬停信息、错误波浪线、转到定���）目前仅支持 JavaScript/TypeScript、Python 和 Go。但更多语言即将推出！
   * 支持 Copilot 补全需要一个有效的 Copilot 订阅。如果你没有，那么你只是在编辑器中看不到“幽灵文本”，但你仍然可以使用上述描述的语言服务。

* **UX layout persistence** - When you collapse changed files and/or minimize the timeline, that UX state is now properly persisted for the session. That way, when you return to a session later, you can pick up exactly where you left off. Or if you share a snapshot with someone else, you can curate the UX to look exactly how you want them to see it 🚀

* **用户体验布局持久化** - 当你折叠更改的文件和/或最小化时间线时，该用户体验状态现在会为会话正确持久化。这样，当你稍后返回会话时，你可以准确地从你离开的地方继续。如果你与其他人共享快照，你可以策划用户体验，使其看起来正是你希望他们看到的样子 🚀

   ![image](https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/529c4aef-19ca-47b1-8d07-47bd6eab799b)

* **Redesigned progress indicator for file implementation** - When a file is currently being implemented, we now display a progress bar underneath it to better visualize the status of the code generation. Additionally, when an existing file is being edited, we now properly display the delta of code changes that were added.

* **重新设计的文件实施进度指示器** - 当一个文件当前正在实施时，我们现在在其下方显示一个进度条，以更好地可视化代码生成的状态。此外，当现有文件正在编辑时，我们现在正确显示添加的代码更改的增量。

   ![image](https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/b58a8c2a-24b7-4cf3-84fb-46a9c4b81daa)

   ![image](https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/f725a6ca-2a31-4603-b602-d88c9736c8f8)

* **Easier code review on mobile** - When viewing a multi-file session on a mobile device, you can now click an implemented file to view the changes in a full-screen editor, and then easily page between the other files that were edited.

* **移动设备上更容易的代码审查** - 在移动设备上查看多文件会话时，你现在可以点击已实现的文件，在全屏编辑器中查看更改，然后轻松在其他已编辑的文件之间分页。

   <img src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/3d04c431-b61c-4e53-86fd-723c2fd9439a" width="400px" />

* **The "topic" now renders markdown** - The question/task that is displayed at the top of the `Specification` panel is now rendered properly when it includes markdown. In particular, it's common for this to include backticks when the task definition refers to a symbol using them.

* **“主题”现在呈现 markdown** - 当问题/任务包含 markdown 时，现在在“规范”面板顶部显示的问题/任务会正确呈现。特别是，当任务定义使用反引号引用符号时，通常会包含反引号。

   <img src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/92ee8afc-1f95-4d5d-8ed5-dfcb6bcff14c" width="500px" />

* **Add manually edited files to the plan** - In addition to generating code changes with AI, Copilot Workspace allows you to manually edit files through its file explorer and/or the integrated terminal. And in order to make it easier to include these manually edited files in the plan (e.g. so you could do further AI-assisted iteration on them), they now include a `+` button in their header bar, which let's you one-click add them to the plan. 

* **将手动编辑的文件添加到计划中** - 除了使用 AI 生成代码更改外，Copilot Workspace 还允许你通过其文件资源管理器和/或集成终端手动编辑文件。为了更容易将这些手动编辑的文件包含在计划中（例如，你可以对它们进行进一步的 AI 辅助迭代），它们现在在其标题栏中包含一个 `+` 按钮，可以让你一键将它们添加到计划中。

   <img src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/baa3c855-6686-4869-8405-372d2251d2fd" width="700px" />

* **Share links now include the repo and title in their preview** - If you share a session link with someone via Twitter, Slack, Teams, SMS, etc. the preview that is displayed to them will now properly include the repository that the session is associated with, and the title of the session. That way, it's a little bit clearer what you're sharing, before they actually click it.

* **共享链接现在在预览中包含仓库和标题** - 如果你通过 Twitter、Slack、Teams、SMS 等与他人共享会话链接，显示给他们的预览现在会正确包含会话关联的仓库和会话的标题。这样，在他们实际点击之前，你共享的内容会更清晰一些。

   <img src="https://github.com/githubnext/copilot-workspace-user-manual/assets/116461/a616f9bf-5220-4301-b633-d3f24fcc787a" width="500px" />

* **Improved status messages for panels** - Whenever you generate/regenerate/revise the spec/plan, or implement files, those steps now display more helpful status messages.

* **改进的面板状态消息** - 每当你生成/重新生成/修订规范/计划或实施文件时，这些步骤现在会显示更有帮助的状态消息。

## 📅 9 May 2024

### Features / Enhancements

### 功能/增强

* **Support for very large repositories** - The first release of Copilot Workspace only worked up to limited repository size. These limitations are now largely lifted.
  
* **支持非常大的仓库** - Copilot Workspace 的第一个版本仅适用于有限的仓库大小。这些限制现在基本上被取消了。

* **Copilot Workspace will now process "delete" operations efficiently** - Copilot Workspace will now process 'delete' operations more promptly, without making any unnecessary model invocations.

* **Copilot Workspace 现在将高效处理“删除”操作** - Copilot Workspace 现在将更及时地处理“删除”操作，而不会进行任何不必要的模型调用。

* **Color the `Issue` and `Pull Request` panel icons based on their state** - When opening an issue or pull request within Copilot Workspace, we'll now indicate the state of the issue/PR, using the same colors as GitHub.com: open (green), completed/merged (purple), closed (red), and closed as not planned (grey). That way, the status of the issue/PR will be immediately clear 👍

* **根据状态为“问题”和“拉取请求”面板图标着色** - 在 Copilot Workspace 中打开问题或拉取请求时，我们现在将使用与 GitHub.com 相同的颜色指示问题/PR 的状态：打开（绿色）、完成/合并（紫色）、关闭（红色）和关闭为未计划（灰色）。这样，问题/PR 的状态将立即清晰 👍

   <img src="https://github.com/user-attachments/assets/116461/1f127b54-a697-4594-8a0f-946dfb47b06b" width="600px" />

   *Opening an issue that's closed as completed*

   *打开一个已关闭为完成的问题*

   <img src="https://github.com/user-attachments/assets/116461/1f9a0ea6-bf6f-4f1e-961c-107f27dbb12c" width="600px" />

   *Opening a pull request that's been closed*

   *打开一个已关闭的拉取请求*

### Bug Fixes

### 错误修复

* **Fix session reload for any session not on default branch of repository**. A user reported that Copilot Workspace could not reload sessions if they were associated with a non-default branch of a repository. This is now fixed.

* **修复非仓库默认分支的会话重新加载问题**。一位用户报告说，如果会话与仓库的非默认分支关联，Copilot Workspace 无法重新加载会话。现在已修复。

* **Fix virtual keyboard overlaying editor**.  A fix was made for mobile where the virtual keyboard was obscuring some of the file editor.

* **修复虚拟键盘覆盖编辑器问题**。修复了移动设备上的虚拟键盘遮挡部分文件编辑器的问题。

* **Fix scroll to implementation**.  "Scroll to implementation" for a step of the plan was not working as expected. This is now fixed.

* **修复滚动到实现问题**。计划步骤的“滚动到实现”未按预期工作。现在已修复。

* **Numerous mobile layout fixes**. Many subtle but important fixes have been made to layout and interaction on mobile devices.

* **许多移动设备布局修复**。对移动设备上的布局和交互进行了许多细微但重要的修复。

## 📅 29 April 2024

Initial release! 🚀

初始发布！🚀
