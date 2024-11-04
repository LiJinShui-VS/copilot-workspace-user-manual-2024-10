# Tips and Tricks

# 提示和技巧

This document contains assorted tips and tricks for using Copilot Workspace effectively. We'd love to hear your tips and tricks, too! Please share them with us in [feedback channels](README.md#feedback).

本文档包含有效使用 Copilot Workspace 的各种提示和技巧。我们也很想听到您的提示和技巧！请在[反馈渠道](README.md#feedback)中与我们分享。

## Edit the Issue or Task

## 编辑问题或任务

✨ TIP: You can edit the issue or task to guide Copilot Workspace.

✨ 提示：您可以编辑问题或任务以指导 Copilot Workspace。

The Issue/Task panel may be prepopulated with content depending on how you entered Copilot Workspace. For example, if you started from an Issue, the Issue panel will be prepopulated with the content of the issue. This content is ephemeral -- edits aren't synced back to the issue -- and so feel free to edit it to provide more context or to steer Copilot Workspace towards better results.

问题/任务面板可能会根据您进入 Copilot Workspace 的方式预先填充内容。例如，如果您从问题开始，问题面板将预先填充问题的内容。此内容是临时的——编辑不会同步回问题——因此请随意编辑它以提供更多上下文或引导 Copilot Workspace 获得更好的结果。

## Tasks can be short!

## 任务可以很短！

✨ TIP: You might be surprised at the effectiveness of simple tasks like "Add unit tests"

✨ 提示：您可能会对“添加单元测试”之类的简单任务的有效性感到惊讶

Tasks don't have to be long. Simple, clear statements of intent like "Switch to use Python numpy" or "Add more unit tests for the server code" can get you a long way. You can easily add more clarification and iterate.

任务不必很长。像“切换到使用 Python numpy”或“为服务器代码添加更多单元测试”这样的简单、清晰的意图声明可以让您走很长的路。您可以轻松添加更多说明并进行迭代。

## Clarify the Issue or Task

## 澄清问题或任务

✨ TIP: A few words clarifications can make a huge difference!

✨ 提示：几句话的澄清可以产生巨大的影响！

Just a few words of clarification can make a big difference in the quality of the results you get. For example,

几句话的澄清可以对您获得的结果质量产生很大影响。例如，

* _add corresponding unit tests in `test/server`_ or

* _在 `test/server` 中添加相应的单元测试_ 或

* _the problem is in the convolution code_ or

* _问题出在卷积代码中_ 或

* _don't change any existing code just add unit tests_

* _不要更改任何现有代码，只需添加单元测试_

are examples of useful clarifications. Use as many of these as you like!

这些都是有用的澄清示例。根据需要使用其中的任意数量！

## Consider using Examples

## 考虑使用示例

✨ TIP: Giving examples of what you want can be a great way to clarify a task

✨ 提示：给出您想要的示例可以是澄清任务的好方法

For example, you can say: _Here are some examples of command line invocations that should work after the change..._ and give a few examples. Or you can say: _Here are some examples of the expected output..._ and give a few examples.

例如，您可以说：_以下是更改后应能正常工作的命令行调用示例..._ 并给出一些示例。或者您可以说：_以下是预期输出的示例..._ 并给出一些示例。

## Check the Topic and Specification

## 检查主题和规范

✨ TIP: Check the topic and specification - if they're accurate, then Copilot Workspace is on the right track

✨ 提示：检查主题和规范——如果它们是准确的，那么 Copilot Workspace 就在正确的轨道上

The Topic is your first quick glimpse of Copilot Workspace's analysis of your task in the context of your repository, and the Current Specification follows soon after, then the Updated Specification. If these are accurate, then Copilot Workspace is on the right track. If they're not, then you may need to provide more context, clarifications and hints in the Issue/Task panel, or you may be performing something beyond Copilot Workspace's current capabilities.

主题是您第一次快速了解 Copilot Workspace 在您的存储库上下文中对您的任务的分析，紧随其后的是当前规范，然后是更新的规范。如果这些是准确的，那么 Copilot Workspace 就在正确的轨道上。如果它们不准确，那么您可能需要在问题/任务面板中提供更多上下文、澄清和提示，或者您可能正在执行超出 Copilot Workspace 当前能力的操作。

You can edit all of these to correct them, and checking them quickly can save you a lot of time. You can also go back and clarify the issue or task and try again.

您可以编辑所有这些以纠正它们，并且快速检查它们可以为您节省大量时间。您还可以返回并澄清问题或任务，然后重试。

## Check the Content Selection

## 检查内容选择

✨ TIP: Check the content selection and use short notes in the issue or task to say where to look

✨ 提示：检查内容选择并在问题或任务中使用简短的注释说明查看位置

You can [check the content selection used](overview.md#content-selection). Often the content selection can be improved, and right now you do this through natural language and notes on the issue/task. If you know where the code that needs to be changed is, you can say so in the issue/task panel. For example, you can say: _Look in `src/server.js`_ or many other variations.

您可以[检查使用的内容选择](overview.md#content-selection)。通常可以改进内容选择，而现在您可以通过自然语言和问题/任务上的注释来完成此操作。如果您知道需要更改的代码在哪里，您可以在问题/任务面板中说明。例如，您可以说：_查看 `src/server.js`_ 或许多其他变体。

To determine how to address a task, Copilot Workspace must determine which files in a repo are relevant to the task. This is hard, and Copilot Workspace may not always select the right files. If that happens, you may see low-quality results.

为了确定如何解决任务，Copilot Workspace 必须确定存储库中的哪些文件与任务相关。这很难，Copilot Workspace 可能并不总是选择正确的文件。如果发生这种情况，您可能会看到低质量的结果。

To review the files that were selected, in the Specification panel, click the "View references" button:

要查看选择的文件，请在规范面板中点击“查看参考”按钮：

<img src="images/overview/references.png" width=600 alt="Show references dialog">

*模型用于生成原始和修改规范的参考*

To steer Copilot Workspace towards better file selection, you can mention file names, directory names, etc. in the issue/task panel. Just write it naturally, as if you were writing a normal issue.

要引导 Copilot Workspace 进行更好的文件选择，您可以在问题/任务面板中提及文件名、目录名等。只需自然地写出来，就像您在写一个普通问题一样。

## If at First You Don't Succeed...

## 如果一开始你没有成功...

✨ TIP: Try regenerating the spec or plan

✨ 提示：尝试重新生成规范或计划

If you're not happy with the results you're getting, you can try regenerating the spec and/or plan. To do this, click the "Regenerate" button in the Spec or Plan panels:

如果您对获得的结果不满意，可以尝试重新生成规范和/或计划。为此，请点击规范或计划面板中的“重新生成”按钮：

<img src="images/tips-and-tricks/regen.png" width=600 alt="Regenerate button">

*重新生成按钮*

## Iterating on the Implementation

## 迭代实施

✨ TIP: Add short notes to files in the plan, then iterate

✨ 提示：在计划中的文件中添加简短的注释，然后迭代

Often Copilot Workspace will get a task *mostly right*, but may have trouble with some parts. In this case, you can reimplement specific files with new or additional instructions. After implementing and reviewing the code, you can select file(s) in the Plan panel and add bullet points, then click "Update selected files" to reimplement those file(s) with the new instructions that you've provided.

通常 Copilot Workspace 会*大部分正确*地完成任务，但某些部分可能会有问题。在这种情况下，您可以使用新的或附加的指令重新实现特定文件。在实施和审查代码后，您可以在计划面板中选择文件并添加项目符号，然后点击“更新选定文件”以使用您提供的新指令重新实现这些文件。

<img src="images/overview/file-iteration.png" width=600 alt="Update selected files flow">

*计划面板使用户可以逐个文件地迭代实现*

## Add New Files and Iterate

## 添加新文件并迭代

✨ TIP: You can add new files and iterate on the implementation

✨ 提示：您可以添加新文件并迭代实施

If you need to add new files to the implementation, you can do so by clicking the "Add file" button in the Plan panel. This will add a new file to the plan, which you can then implement and iterate on.

如果您需要向实施中添加新文件，可以通过点击计划面板中的“添加文件”按钮来实现。这将向计划中添加一个新文件，然后您可以实施并迭代。

## Consider Generating New Files

## 考虑生成新文件

✨ TIP: Generating new files can be better than appending to existing files

✨ 提示：生成新文件可能比附加到现有文件更好

This technical preview of Copilot Workspace uses "whole file rewriting". This means that when you ask Copilot Workspace to add code to a file, it will replace the entire file with the new code. When performing tasks like writing unit tests or generating documentation or new implementation code, it can be easier and quicker to generate new files, then rename them.

Copilot Workspace 的这个技术预览版使用“整个文件重写”。这意味着当您要求 Copilot Workspace 向文件添加代码时，它将用新代码替换整个文件。在执行编写单元测试或生成文档或新实现代码等任务时，生成新文件然后重命名它们可能更容易和更快。

## Share Early, Share Often

## 早分享，多分享

✨ TIP: You can share your session at any time, including with people who are not part of the Copilot Workspace preview.

✨ 提示：您可以随时分享您的会话，包括与不属于 Copilot Workspace 预览版的人分享。

You can share your Copilot Workspace session with others by clicking the "Share" button in the top right corner of the screen. This will generate a link that you can share with others. These links can be shared with guests, even if they are not part of the Copilot Workspace preview. They will need to log in with their GitHub account to view the session.

您可以通过点击屏幕右上角的“分享”按钮与他人分享您的 Copilot Workspace 会话。这将生成一个您可以与他人分享的链接。这些链接可以与访客共享，即使他们不是 Copilot Workspace 预览版的一部分。他们需要使用他们的 GitHub 帐户登录才能查看会话。

Shared sessions are copies of the original session. Non-guest users can use them as a starting point to continue the task or explore alternative solutions without interfering with the original session. Guest users can view the session but cannot use the workspace to make changes.

共享会话是原始会话的副本。非访客用户可以使用它们作为继续任务或探索替代解决方案的起点，而不会干扰原始会话。访客用户可以查看会话，但不能使用工作区进行更改。

<img src="images/overview/share-link.png" width=200 alt="Share button">

*从标题栏生成共享链接*

## Use the Sessions

## 使用会话

✨ TIP: Return to your work at any time

✨ 提示：随时返回您的工作

Your sessions are automatically saved, so you won't lose work if you close the browser or navigate away from the page. You can return to your session by going to [your Copilot Workspace dashboard](https://copilot-workspace.githubnext.com).

您的会话会自动保存，因此如果您关闭浏览器或离开页面，您不会丢失工作。您可以通过访问[您的 Copilot Workspace 仪表板](https://copilot-workspace.githubnext.com)返回您的会话。

## Configure the Terminal for Your Repository

## 为您的存储库配置终端

✨ TIP: Set up a `devcontainer.json` file in your repository to configure the terminal

✨ 提示：在您的存储库中设置一个 `devcontainer.json` 文件以配置终端

We provide a built-in terminal so that you can validate the code changes that Copilot Workspace suggests. We use GitHub Codespaces to provide this terminal, and we use the `devcontainer.json` file in your repository to configure the container that powers the terminal. If you need to make changes to the default container to e.g. install necessary software, etc., you can do so by creating a `devcontainer.json` file in your repository. Learn more about Development Containers at https://containers.dev/.

我们提供了一个内置终端，以便您可以验证 Copilot Workspace 建议的代码更改。我们使用 GitHub Codespaces 提供此终端，并使用您存储库中的 `devcontainer.json` 文件配置支持终端的容器。如果您需要对默认容器进行更改，例如安装必要的软件等，您可以通过在存储库中创建一个 `devcontainer.json` 文件来实现。了解有关开发容器的更多信息，请访问 https://containers.dev/。

## Use the Codespace

## 使用 Codespace

✨ TIP: Full editing in the Codespace is simple and quick

✨ 提示：在 Codespace 中进行完整编辑既简单又快捷

Modified files are two-way-synced between Copilot Workspace and the terminal/Codespace. Feel free to edit in either place, and your changes will be reflected in the other.

修改后的文件在 Copilot Workspace 和终端/Codespace 之间进行双向同步。随时在任一位置进行编辑，您的更改将反映在另一个位置。

Check out [Codespaces Guide](./codespaces-guide.md) for more information.

有关更多信息，请查看[Codespaces 指南](./codespaces-guide.md)。

## Explore the Experiments!

## 探索实验！

✨ TIP: Explore our experiments and send us feedback!

✨ 提示：探索我们的实验并向我们发送反馈！

We're always trying new things in Copilot Workspace. You can opt into our current experiments by clicking on your avatar in the top right corner of the screen and selecting "Experiments":

我们一直在 Copilot Workspace 中尝试新事物。您可以通过点击屏幕右上角的头像并选择“实验”来选择加入我们当前的实验：

<img src="images/tips-and-tricks/experiments.png" width=200 alt="Experiments selector">

*实验选择器*

## Work Around Model "Laziness"

## 解决模型“懒惰”问题

✨ TIP: If the model is "lazy" and elides chunks of edited files, copy and paste the missing parts from the diff

✨ 提示：如果模型“懒惰”并省略编辑文件的块，请从差异中复制并粘贴缺失的部分

Sometimes the model will be "lazy" and elide chunks of edited files. If you see this happening, you can copy the missing parts from the left-hand side of the diff and paste them into the right-hand side.  We know that's not ideal, and we're working hard on this issue.

有时模型会“懒惰”并省略编辑文件的块。如果您看到这种情况发生，您可以从差异的左侧复制缺失的部分并将其粘贴到右侧。我们知道这并不理想，我们正在努力解决这个问题。

## Edit code in Copilot Workspace

## 在 Copilot Workspace 中编辑代码

✨ TIP: Make edits directly in the code editors per file

✨ 提示：在每个文件的代码编辑器中直接进行编辑

When Copilot Workspace has generated a suggestion, it is presented to you in the implementation panel. But those suggestions aren’t just read-only! You can edit them, and make changes as you desire.

当 Copilot Workspace 生成建议时，它会在实施面板中呈现给您。但这些建议不仅仅是只读的！您可以编辑它们，并根据需要进行更改。

<img src="images/tips-and-tricks/code-editor.png" width=300 alt="Edit code in Copilot Workspace">

*在 Copilot Workspace 中编辑代码*

And if you have a GitHub Codespace open, those edits will sync between Copilot Workspace and the GitHub Codespace too!

如果您打开了 GitHub Codespace，这些编辑也会在 Copilot Workspace 和 GitHub Codespace 之间同步！

## Need to go back?

## 需要回去吗？

✨ TIP: You can use the undo and redo buttons to travel between an older and newer state of your workspace.

✨ 提示：您可以使用撤销和重做按钮在工作区的旧状态和新状态之间切换。

You can use the undo and redo buttons to navigate back to a previous state of your workspace. That can include reverting an implementation, or the additions and tweaks that you may have made to your spec or plan. 

您可以使用撤销和重做按钮导航回工作区的先前状态。这可以包括还原实施，或您可能对规范或计划进行的添加和调整。

<img src="images/tips-and-tricks/undo-redo.png" width=300 alt="Use Undo and Redo to change states in Copilot Workspace">

*使用撤销和重做在 Copilot Workspace 中更改状态*

## On the go? Try Copilot Workspace on Mobile

## 在路上？尝试在移动设备上使用 Copilot Workspace

✨ TIP: Copilot Workspace is mobile-friendly, so consider making changes on the go!

✨ 提示：Copilot Workspace 适合移动设备使用，因此请考虑随时进行更改！

Ideas can happen anywhere, whether you’re at your desk, in a coffee shop or on a bus. With that spark of creativity, you can use Copilot Workspace from your mobile to explore ideas! And if you didn’t fully complete your task, you can use the dashboard in Copilot Workspace to pick up where you left off.

创意可以在任何地方发生，无论您是在办公桌前、咖啡店还是在公交车上。凭借这种创造力的火花，您可以使用移动设备上的 Copilot Workspace 来探索想法！如果您没有完全完成任务，您可以使用 Copilot Workspace 中的仪表板从中断的地方继续。

And if you'd like to easily access Copilot Workspace at any time, you can add it to your mobile homescreen by performing the following steps:

如果您想随时轻松访问 Copilot Workspace，可以通过执行以下步骤将其添加到您的移动主屏幕：

1. Open your mobile browser and navigate to the Copilot Workspace dashboard at [https://copilot-workspace.githubnext.com](https://copilot-workspace.githubnext.com).
2. Once the dashboard loads, tap on the browser's menu and select "Add to Home screen" to easily access Copilot Workspace from your home screen.
3. Confirm the action if prompted, and Copilot Workspace will be added to your home screen, providing a native app-like experience thanks to PWA support.

1. 打开您的移动浏览器并导航到 Copilot Workspace 仪表板 [https://copilot-workspace.githubnext.com](https://copilot-workspace.githubnext.com)。
2. 仪表板加载后，点击浏览器的菜单并选择“添加到主屏幕”，即可轻松从主屏幕访问 Copilot Workspace。
3. 如果出现提示，请确认操作，Copilot Workspace 将被添加到您的主屏幕，感谢 PWA 支持提供类似本机应用程序的体验。

## Regaining access if you revoked OAuth

## 如果您撤销了 OAuth 授权，如何重新获得访问权限

Copilot Workspace is implemented as an OAuth application. If you revoked authorization for the application in your GitHub account settings, you'll no longer be able to use Workspace. You can restore your access at https://copilot-workspace.githubnext.com/ by logging out, then logging in and re-authorizing the OAuth app.

Copilot Workspace 作为 OAuth 应用程序实现。如果您在 GitHub 帐户设置中撤销了对该应用程序的授权，您将无法再使用 Workspace。您可以通过注销，然后登录并重新授权 OAuth 应用程序来恢复您的访问权限 https://copilot-workspace.githubnext.com/。

## Incoming Links

## 传入链接

✨ TIP: Copilot Workspace has a capability for the task to be specified by query parameters when the subject is a repository, branch or pull request. 

✨ 提示：当主题是存储库、分支或拉取请求时，Copilot Workspace 具有通过查询参数指定任务的功能。

```
https://copilot-workspace.githubnext.com/githubnext/copilot-workspace/pull/695?task=Add%20more%20unit%20tests%20to%20this%20pull%20request.```
```

The query parameters supported are

支持的查询参数是

- `task` - The description of the task. If not specified, and the subject is an issue, the body of the issue is used, otherwise no task body is used and the user must enter one.
- `task` - 任务的描述。如果未指定，并且主题是问题，则使用问题的正文，否则不使用任务正文，用户必须输入一个。
- `codeOwner` - The organization or individual for the code repository associated with an issue, e.g. `githubnext` for `githubnext/copilot-workspace`
- `codeOwner` - 与问题相关的代码存储库的组织或个人，例如 `githubnext` 对于 `githubnext/copilot-workspace`
- `codeRepo` - The name of the code repository associated with an issue, e.g. `copilot-workspace` for `githubnext/copilot-workspace`
- `codeRepo` - 与问题相关的代码存储库的名称，例如 `copilot-workspace` 对于 `githubnext/copilot-workspace`
- `branch` - The SHA or branch name to analyze the task at, e.g. `main`
- `branch` - 要分析任务的 SHA 或分支名称，例如 `main`
