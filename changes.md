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

<img src="https://github.com/user-attachments/assets/41b2864a-3b9f-45
