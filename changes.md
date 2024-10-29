## 📅 18 October 2024

- [Error repair](#error-repair)
- [Follow ups](#follow-ups)
- [Brainstorm enhancements](#brainstorm-enhancements)
- [Plan command enhancements](#plan-command-enhancements)

### Error repair

When a [build/test/run command](#commands) fails, CW now displays a lightbulb button in the command's toolbar. When you click this, it will trigger a [brainstorming](#brainstorming) action, and then offer a suggestion for how to fix the error.

当[构建/测试/运行命令](#commands)失败时，CW现在会在命令的工具栏中显示一个灯泡按钮。当你点击这个按钮时，它会触发一个[头脑风暴](#brainstorming)操作，然后提供一个修复错误的建议。

<img src="https://github.com/user-attachments/assets/db1cc14e-f3b5-49ea-a9e0-80b8b2b98bba" width="450px" />

当建议返回时，它将包括问题的解释，然后以两种形式之一呈现修复：

1. 一个**终端命令**，可以运行以解决问题（例如，安装缺失的环境依赖项）
2. 一个**计划更新**，可以应用，然后在受影响的文件中实施（例如，缺少的导入，类型错误）

| Terminal fix | Plan fix |
|-|-|
| <img src="https://github.com/user-attachments/assets/f81063fe-deca-455a-9c38-07bbb336b193" width="350px" /> | <img src="https://github.com/user-attachments/assets/029729bd-a50f-4078-b764-a464a35bf4f4" width="350px" /> |

After accepting a suggestion, you can then re-run the failed command, and hopefully see it pass. That said, if you encounter another issue (e.g. a build with multiple errors), then you can just continue to command + repair as much as needed 🚀

接受建议后，你可以重新运行失败的命令，并希望看到它通过。也就是说，如果你遇到另一个问题（例如，一个有多个错误的构建），那么你可以继续命令+修复，直到需要的程度🚀

### Follow ups

We've introduced a new capability into CW, that we're calling `Follow up`. And we're pretty excited about it 😃

我们在CW中引入了一项新功能，我们称之为`跟进`。我们对此感到非常兴奋😃

<img src="https://github.com/user-attachments/assets/bd881a9f-f557-4f9d-8682-25075368ad00" width="400px" />

#### Let's talk about why it's useful!

让我们谈谈为什么它有用！

When you're working against a large repository that has complex/inter-file dependencies, it's possible that a simple change/refactoring can impact many other places across the codebase (e.g. updating a shared method signature). And while the plan can do a great job of identifying the core changes needed for a task (the "primary edits"), it can sometimes miss transitive changes that are needed in response (e.g. updating callers of a changed function).

当你在一个具有复杂/文件间依赖关系的大型代码库中工作时，一个简单的更改/重构可能会影响代码库中的许多其他地方（例如，更新共享方法签名）。虽然计划可以很好地识别任务所需的核心更改（“主要编辑”），但有时它可能会遗漏需要响应的传递更改（例如，更新更改函数的调用者）。

To address this, after you've implemented a plan, you can open up the `Commands` tab and click the new `Follow up` button. This will perform a thorough, fine-grained check on your codebase + edits, to see if any additional changes are required, in order to complete your task. And if any follow-ups are detected, it will edit the neccessary files, and add them to your existing implementation 👍

为了解决这个问题，在你实施了一个计划之后，你可以打开`命令`选项卡并点击新的`跟进`按钮。这将对你的代码库+编辑进行彻底的、细粒度的检查，以查看是否需要任何额外的更改，以完成你的任务。如果检测到任何跟进，它将编辑必要的文件，并将它们添加到你现有的实现中👍

<img src="https://github.com/user-attachments/assets/4c33b6e9-9506-4726-a018-4889b0a2d210" width="400px" />

This workflow is pretty slick, because it allows the initial CW plan to be both fast and focused, which makes it quicker for you to get to code, and easier for you to review the essence of the change. And in cases that a change has repo-wide impact, you can simply trigger a follow up and let Copilot do the rest 😎

这个工作流程非常流畅，因为它允许初始的CW计划既快速又集中，这使你更快地进入代码，并更容易审查更改的本质。而在更改对整个代码库有影响的情况下，你可以简单地触发一个跟进，让Copilot完成剩下的工作😎

#### How can you try it?

你如何尝试它？

At the moment, this experience supports codebases that are written in TypeScript/JavaScript, Python, Java, and C#. So if you're working in one of those languages, we'd love to hear your feedback! And if not, we'd love to hear whether this capability would be useful, in order to help us prioritize new languages in the future 🙏

目前，这种体验支持用TypeScript/JavaScript、Python、Java和C#编写的代码库。所以如果你在这些语言之一中工作，我们很想听到你的反馈！如果不是，我们也很想知道这种功能是否有用，以帮助我们在未来优先考虑新语言🙏

And while we let this capability bake a bit, it's currently disabled by default. So if you'd like to give it a try, simply open the `Experiments` panel (under the avatar menu) and check the `Enable follow up` setting.

虽然我们让这个功能稍微成熟了一点，但它目前默认是禁用的。所以如果你想试一试，只需打开`实验`面板（在头像菜单下）并勾选`启用跟进`设置。

### Brainstorm enhancements

When you open an issue in CW, or click the `Brainstorm` button for ad-hoc tasks, the initially-generated question (`How do I solve this issue?`) is now presented in a "special" structured format. The response includes two sections (`Current behavior` / `Proposed solution`), and has the advantage of allowing you to add/edit/delete/organize any of the steps, in a very granular way.

当你在CW中打开一个问题，或点击`头脑风暴`按钮进行临时任务时，最初生成的问题（`我如何解决这个问题？`）现在以一种“特殊”的结构化格式呈现。响应包括两个部分（`当前行为`/`拟议解决方案`），并且具有允许你以非常细粒度的方式添加/编辑/删除/组织任何步骤的优点。

<img src="https://github.com/user-attachments/assets/d11ad993-6ee7-4899-a3f4-f6c896b0472d" width="700px" />

Additionally, since we're treating this question as "special", it's automatically updated any time you attach an additional brainstorming question/idea to the task. That way, you can continue to brainstorm further, and ensure that CW's understanding of the overall solution remains always up-to-date 👍

此外，由于我们将这个问题视为“特殊”，因此每当你将额外的头脑风暴问题/想法附加到任务时，它会自动更新。这样，你可以继续进一步头脑风暴，并确保CW对整体解决方案的理解始终保持最新👍

### Plan command enhancements

当一个计划包括一个`命令`部分（例如，因为你的任务需要安装第三方依赖项），你现在可以执行单个命令，除了现有的“执行所有”支持。此外，命令的完成状态现在是持久的。因此，当你稍后恢复CW会话时，你可以看到哪些命令已经运行，哪些失败，哪些仍然未完成。

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

作为我们对CW用户体验（例如头脑风暴、操作栏、文件标签/树等）持续改进的一部分，我们引入了一项新功能，称为`命令`，它用一个全高度面板替换了集成终端，并提供了一个简化的体验，用于执行和配置代码的构建/测试/运行。从概念上讲，你可以将其视为工作区中所有需要执行shell命令的任务的集中“枢纽”。

<img src="https://github.com/user-attachments/assets/bb5aa0b5-c0c0-4209-871d-5079a0b28f04" width="1000px" />

And similar to [brainstorming](#brainstorming), this capability is significant enough in scope, that we need to describe it in four distinct parts 😄

- [Running commands](#running-commands) 
- [Command setup / inference](#command-setup--inference)
- [NL command suggestions](#nl-command-suggestions)
- [Plan commands](#plan-commands)  

#### Running commands

To begin using the new `Commands` hub, simply click the existing terminal icon in the header bar. Once opened, it will automatically create and connect to a backing Codespace, so you can start running commands as needed. And if your repository has been configured with a `postAttachCommand` (in your [`devcontainer.json` file](https://containers.dev/implementors/spec/#devcontainerjson)), then you'll see a `Post attach` entry appear, that let's you view the output of its underlying shell commands.

要开始使用新的`命令`中心，只需点击标题栏中的现有终端图标。一旦打开，它将自动创建并连接到一个支持的Codespace，因此你可以根据需要开始运行命令。如果你的仓库已配置了`postAttachCommand`（在你的[`devcontainer.json`文件](https://containers.dev/implementors/spec/#devcontainerjson)中），那么你将看到一个`Post attach`条目出现，让你查看其底层shell命令的输出。

Additionally, if you've configured a `build`, `test`, or `launch` task in your `devcontainer.json`, then you can click to run any of those. This will result in the command being displayed in the list on the `Output` tab, and allow you to view its output, stop it, or re-run it once complete (e.g. to re-trigger a build after editing code).

此外，如果你在`devcontainer.json`中配置了一个`build`、`test`或`launch`任务，那么你可以点击运行其中任何一个。这将导致命令显示在`输出`选项卡的列表中，并允许你查看其输出，停止它，或在完成后重新运行它（例如，在编辑代码后重新触发构建）。

<img src="https://github.com/user-attachments/assets/6a0f0ecc-64f0-4871-b5f3-0840c684b85e" width="450px" />

And just like the existing terminal, if a build/test/run command starts a server, then it will be automatically forwarded, so you can securely view it. 

就像现有的终端一样，如果一个构建/测试/运行命令启动了一个服务器，那么它将被自动转发，因此你可以安全地查看它。

#### Command setup / inference

If you haven't configured any tasks in your `devcontainer.json`, then you can simply click on either the build, test, or run command, and then type the respective shell commands into the task editor. When you do that, the entered commands will be automatically added to a `devcontainer.json` file for you, so you can include them in your subsequent PR.

如果你没有在`devcontainer.json`中配置任何任务，那么你可以简单地点击构建、测试或运行命令，然后将相应的shell命令输入到任务编辑器中。当你这样做时，输入的命令将自动添加到一个`devcontainer.json`文件中，以便你可以将它们包含在后续的PR中。

And if you don't know how to perform a build/test/run on the current repo, then simply click the lightbulb icon next to a task and let CW suggest how to do it for you 🚀

如果你不知道如何在当前仓库上执行构建/测试/运行，那么只需点击任务旁边的灯泡图标，让CW为你建议如何做🚀

<img src="https://github.com/user-attachments/assets/2db837df-33db-4608-8674-54d36ae5e9f7" width="500px" />

#### NL command suggestions

While we've optimized the UX for building, testing, and running your code, there are many other tasks you might need to perform during a session (e.g. linting, formatting, etc.). And to make that simpler, the action bar now enters "command mode" (when you're focused on the `Commands` tab), which lets you describe a shell command you want to run, using only natural language.

虽然我们已经优化了构建、测试和运行代码的用户体验，但在会话期间你可能还需要执行许多其他任务（例如，linting，格式化等）。为了简化这一过程，操作栏现在进入“命令模式”（当你专注于`命令`选项卡时），这让你可以仅使用自然语言描述你想要运行的shell命令。

After typing an NL request, you'll be presented with a command suggestion, which you can edit or regenerate. And if you click the `Run` button, it will open the `Terminal` tab on the `Commands` hub, and execute it on your behalf. 

在输入一个NL请求后，你将看到一个命令建议，你可以编辑或重新生成。如果你点击`运行`按钮，它将打开`命令`中心的`终端`选项卡，并代表你执行它。

<img src="https://github.com/user-attachments/assets/d4dbb27e-3f78-43f7-8e94-d68caa2ae9ce" width="500px" />

#### Plan commands

The "plan commands" feature is now on by default, and when a plan includes shell commands (e.g. running a package manager to include a new dependency), it will execute them via a new `Plan` command entry in the `Commands` tab. 

“计划命令”功能现在默认开启，当一个计划包括shell命令（例如，运行包管理器以包含一个新依赖项）时，它将通过`命令`选项卡中的一个新的`计划`命令条目执行它们。

<img src="https://github.com/user-attachments/assets/60ed8f3d-013f-461f-a143-9d642be5e64e" width="700px" />

### Action bar mode picker

The action bar now allows you to seamlessly switch between its three modes: `Ask`, `Revise`, and `Command`. This ensures that regardless what state your session is in, you can ask a question, revise the plan/implemented files, or execute a terminal command. All using natural language 💙

操作栏现在允许你无缝切换其三种模式：`询问`、`修改`和`命令`。这确保了无论你的会话处于什么状态，你都可以提出问题，修改计划/实施的文件，或执行终端命令。所有这些都使用自然语言💙

<img src="https://github.com/user-attachments/assets/93c6664e-66ad-42a3-96b5-3e9a4cdad099" width="600px" />

Even cooler, you can switch between any of these modes using the following keyboard shortcuts, which make it really easy to navigate a session, while jumping between brainstorming, code iteration, and terminal actions. 

更酷的是，你可以使用以下键盘快捷键在这些模式之间切换，这使得在头脑风暴、代码迭代和终端操作之间跳转时，导航会话变得非常容易。

| Mode | Keyboard shortcut |
|-|-|
| Ask | <kbd>?</kbd> |
| Revise | <kbd>></kbd> |
| Command | <kbd>$</kbd> |

Additionally, each mode retains a history of its previous request. So if you realize you wanted to ask a question a slightly different way, or make a subtly different revision, then simply hit the up arrow, edit, and submit 👍

此外，每种模式都会保留其先前请求的历史记录。因此，如果你意识到你想以稍微不同的方式提出问题，或进行微妙的修改，那么只需按上箭头，编辑并提交👍

> By introducing the new `Commands` tab, and allowing all three of the action bar's modes to be usable at any time, the action bar is now the official "central nervous system" for the entire CW experience. We've really fallen in love with how it feels to start and iterate on tasks now. And we're excited to hear how it feels for everyone else! 👋

> 通过引入新的`命令`选项卡，并允许操作栏的所有三种模式在任何时候都可用，操作栏现在是整个CW体验的官方“中枢神经系统”。我们真的爱上了现在开始和迭代任务的感觉。我们很高兴听到其他人的感受！👋

### Open in VS Code

After a month of _amazing_ feedback from our preview users, we've officially published the [Copilot Workspace extension](https://gh.io/cw-vscode ) to the VS Code marketplace 🥳

在一个月的_惊人_反馈之后，我们的预览用户，我们已经正式发布了[Copilot Workspace扩展](https://gh.io/cw-vscode )到VS Code市场🥳

And in order to make it even easier to use, we've introduced a new `Open in VS Code` button to the CW session header. When you click it, we'll launch VS Code, and open your current session directly from within the editor. That way you can start tasks and brainstorm from the web (or your phone!), and when you want to jump into VS Code to finish it off (e.g. step-debug some code), you can now do that in a single-click 💪

为了使其更容易使用，我们在CW会话标题中引入了一个新的`在VS Code中打开`按钮。当你点击它时，我们将启动VS Code，并直接从编辑器中打开你当前的会话。这样你可以从网络（或手机！）开始任务和头脑风暴，当你想跳到VS Code中完成它时（例如，逐步调试一些代码），你现在可以一键完成💪

<img src="https://github.com/user-attachments/assets/1928f16e-3663-4d6e-becb-8cd409fb4430" width="500px" />

Additionally, the official extension release also includes a ton of new capabilities that make the E2E experience a lot better. In particular, we've enhanced the `Sessions` and `Plan` views in the following ways...

此外，官方扩展发布还包括大量的新功能，使E2E体验更好。特别是，我们通过以下方式增强了`会话`和`计划`视图...

#### `Sessions` view

In order to make it easier to manage _many_ sessions, your sessions list is now grouped by repository, and each session displays an icon based on its respective type: issue, task, or PR. Additionally, when you're done with a session, you can now delete it directly from the editor, by hovering over it and clicking the trash can icon.

为了更容易管理_许多_会话，你的会话列表现在按仓库分组，每个会话根据其各自的类型显示一个图标：问题、任务或PR。此外，当你完成一个会话时，你现在可以通过将鼠标悬停在它上面并点击垃圾桶图标，直接从编辑器中删除它。

<img src="https://github.com/user-attachments/assets/70513fd2-cb7e-416c-9ee6-90c0780d4f21" width="350px" />

#### `Plan` view

The VS Code extension now has full parity with the CW web client, when it comes to iterating on the plan and code in a session. And in particular, you can now perform the following actions on the plan, directly from the `Plan` view:

VS Code扩展现在与CW web客户端完全一致，当涉及到在会话中迭代计划和代码时。特别是，你现在可以直接从`计划`视图对计划执行以下操作：

1. Adding, editing, and deleting files
2. Adding, editing, and deleting steps for a file
3. Re-organizing the plan, by moving/indenting files and steps

1. 添加、编辑和删除文件
2. 添加、编辑和删除文件的步骤
3. 通过移动/缩进文件和步骤重新组织计划

To access these new capabilities, simply click the `...` menu next to a file or step in the plan. We're pretty happy with how this experience "feels", and we're looking forwarding to hearing more feedback 🙌

要访问这些新功能，只需点击计划中文件或步骤旁边的`...`菜单。我们对这种体验的“感觉”非常满意，并期待听到更多反馈🙌

| Plan file actions | Plan step actions |
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

我们引入了一个新设置，允许你在为会话创建PR/分支/仓库后自动将其标记为完成。对于创建许多会话的用户，这可以帮助保持你的`最近会话`列表（在[仪表板](https://copilot-workspace.githubnext.com)上）整洁干净。如果你稍后决定需要继续一个标记为完成的会话，你可以随时从[已完成会话列表](https://copilot-workspace-dev.githubnext.com/?view=completed)中恢复它:thumb:

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

CW现在支持通过`.github/copilot-instructions.md`文件配置整个仓库的自定义指令，除了现有的文件位置（`.github/copilot-workspace/CONTRIBUTING.md`）。如果一个仓库包含一个`.github/copilot-instructions.md`文件，那么它将优先于`.github/copilot-workspace/CONTRIBUTING.md`（如果你定义了两个，我们不会“合并”内容）。否则，这两个文件支持完全相同的一组功能和用户体验（例如，`任务`面板将显示自定义指令作为附加上下文，并且指令中的外部URL将被获取）。
