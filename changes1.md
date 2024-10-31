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
