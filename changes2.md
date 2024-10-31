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
