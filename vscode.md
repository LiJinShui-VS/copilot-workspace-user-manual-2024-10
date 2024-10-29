# GitHub Copilot Workspace VS Code extension

# GitHub Copilot Workspace VS Code 扩展

This Copilot Workspace VS Code extension allows you to use GitHub Copilot Workspace from the comfort of VS Code. Continue an existing session and edit and debug the proposed changes before creating a PR. Whether you use natural language to revise the plan or implementation, or edit files directly, you can use the full power of VS Code and its extension ecosystem all while syncing your edits to GitHub Copilot Workspace on the web.

此 Copilot Workspace VS Code 扩展允许您在 VS Code 的舒适环境中使用 GitHub Copilot Workspace。继续现有会话并在创建 PR 之前编辑和调试建议的更改。无论您是使用自然语言来修改计划或实施，还是直接编辑文件，您都可以使用 VS Code 及其扩展生态系统的全部功能，同时将您的编辑同步到 Web 上的 GitHub Copilot Workspace。

This is currently an alpha extension and we will be rolling out enhancements to the extension in multiple phases.

这目前是一个 alpha 扩展，我们将分多个阶段推出扩展的增强功能。

1. **Continue on:** Browse your Copilot Workspace sessions and sync changes so you can edit and debug your application in VS Code locally, using one of the other [VS Code Remote extensions](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), or in your own [Codespace](https://github.com/features/codespaces).

1. **继续：** 浏览您的 Copilot Workspace 会话并同步更改，以便您可以在本地的 VS Code 中编辑和调试您的应用程序，使用其他 [VS Code 远程扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)之一，或在您自己的 [Codespace](https://github.com/features/codespaces) 中。

2. **[IN-PROGRESS] Update your workspace using AI**:

2. **[进行中] 使用 AI 更新您的工作区**：

    - **Available:** Create, edit, and make natural language revisions to the plan and files in the plan.
    - **可用：** 创建、编辑并对计划和计划中的文件进行自然语言修订。
    - **Planned**: Support for editing / adding information to the task, specification, and brainstorming, plus integration into chat.
    - **计划：** 支持编辑/添加任务、规范和头脑风暴的信息，并集成到聊天中。

3. **[FUTURE] Create new:** While not available now, you'll be able to create a new Copilot Workspace session in VS Code.

3. **[未来] 创建新：** 虽然现在不可用，但您将能够在 VS Code 中创建一个新的 Copilot Workspace 会话。

## Getting started

## 入门

* [Quick Start](#quick-start)
* [快速入门](#quick-start)
* [Browsing Sessions](#browsing-sessions)
* [浏览会话](#browsing-sessions)
* [Managing Sessions](#managing-sessions)
* [管理会话](#managing-sessions)
* [Planing and Implementing](#plan-and-implement)
* [计划和实施](#plan-and-implement)
* [Natural Language Revisions](#natural-language-revisions)
* [自然语言修订](#natural-language-revisions)
* [Known Limitations](#known-limitations)
* [已知限制](#known-limitations)

### Quick Start

### 快速入门

1. If you haven't already, install [Visual Studio Code](https://code.visualstudio.com/).

1. 如果您还没有安装，请安装 [Visual Studio Code](https://code.visualstudio.com/)。

1. Next, open a session [on the web](https://copilot-workspace.githubnext.com) that you'd like to continue working on in VS Code.

1. 接下来，打开一个您想在 VS Code 中继续工作的 [Web 会话](https://copilot-workspace.githubnext.com)。

1. Click on the `VS Code` button in the session screen.

1. 在会话屏幕中点击 `VS Code` 按钮。

    ![VS Code icon in web UX](./images/vscode/upper-right.png)

1. Allow your browser to open the link in VS Code when prompted.

1. 当提示时，允许您的浏览器在 VS Code 中打开链接。

Follow the directions that appear in VS Code and make any selections when prompted, and you'll be guided towards syncing the session to your local machine. That's it! 😎

按照 VS Code 中出现的指示进行操作，并在提示时进行选择，您将被引导将会话同步到本地计算机。就是这样！😎

Here is generally what you can expect to see:

以下是您通常可以看到的内容：

1. VS Code will open (if it isn't already running), and you'll be prompted to install the Copilot Workspace extension and then open the URI. If the extension is already installed, you'll just be asked about the URI. Either way, open the URI.

1. VS Code 将打开（如果尚未运行），并提示您安装 Copilot Workspace 扩展，然后打开 URI。如果扩展已安装，您只需询问 URI。无论哪种方式，打开 URI。

    <img src="./images/vscode/ghcw-extn-install.png" title="Image of install VS Code extension and open URI notification" width="200px">

1. **[One time]** If you haven't signed in already, you'll be prompted to do so. Click the `Sign in` and complete the sign in process in the browser that opens.

1. **[一次性]** 如果您尚未登录，系统会提示您登录。点击 `登录` 并在打开的浏览器中完成登录过程。

    <img src="./images/vscode/ghcw-sign-in-notification.png" title="Image of sign-in notification" width="400px">

1. If the VS Code instance already has a folder with the related repository in it open, the extension will immediately start syncing the session locally. Otherwise you may be prompted to clone the repository or pick an existing folder with it in it.

1. 如果 VS Code 实例已经打开了包含相关存储库的文件夹，扩展将立即开始在本地同步会话。否则，系统可能会提示您克隆存储库或选择其中包含的现有文件夹。

    <img src="./images/vscode/ghcw-clone-or-open-folder.png" title="Image of clone or open folder notification" width="200px">

Once syncing has begun, your local repository will switch to GitHub Copilot Workspace tracking branch with a `ghcw-session` prefix as you can see in the status bar.

一旦同步开始，您的本地存储库将切换到带有 `ghcw-session` 前缀的 GitHub Copilot Workspace 跟踪分支，如状态栏中所示。

<img src="./images/vscode/ghcw-branch-example.png" title="Image of branch in status bar" width="250px">

Any edits make to the local files will be synced back to the web session. This allows you to use the full power of VS Code with GitHub Copilot Workspace.

对本地文件所做的任何编辑都将同步回 Web 会话。这使您可以使用 VS Code 的全部功能与 GitHub Copilot Workspace 一起使用。

However, if you picked a session that doesn't yet have an implementation with updated files to start syncing, you'll be notified that you can start syncing once you [have an implementation](#planning-and-implementing).

但是，如果您选择了一个尚未实现更新文件的会话以开始同步，系统会通知您一旦[有实现](#planning-and-implementing)后即可开始同步。

<img src="./images/vscode/ghcw-uri-sync-not-enabled.png" title="Image of notification that sync was not enabled" width="400px">

## Browsing Sessions

## 浏览会话

Even if you are not syncing a session locally, you can still browse through your sessions and view their details. To browse and manage your sessions, first click on the `GitHub Copilot Workspace` icon in the activity bar on the left side of the VS Code window.

即使您没有在本地同步会话，您仍然可以浏览您的会话并查看其详细信息。要浏览和管理您的会话，首先点击 VS Code 窗口左侧活动栏中的 `GitHub Copilot Workspace` 图标。

<img src="./images/vscode/ghcw-activity-bar-icon.png" title="Image of status bar with GitHub Copilot Workspace icon" width="50px">

After you've clicked the activity bar icon, you'll either see list of your sessions, or details about a specific session you've already selected.

点击活动栏图标后，您将看到会话列表或您已选择的特定会话的详细信息。

The session list is sorted by repository. Any repository that applies to currently opened VS Code folders will be on top. You can always get back to the session list when viewing session details by clicking on the `Back to Session List` arrow in the `Task` view or using the **GitHub Copilot Workspace: Back to Session List** command from the Command Pallette (F1 or Ctrl/Cmd+Shift+P).

会话列表按存储库排序。任何适用于当前打开的 VS Code 文件夹的存储库都将位于顶部。您可以在查看会话详细信息时通过点击 `任务` 视图中的 `返回会话列表` 箭头或使用命令面板中的 **GitHub Copilot Workspace: 返回会话列表** 命令（F1 或 Ctrl/Cmd+Shift+P）随时返回会话列表。

Selecting a session in the session list will hide the list and show the related session details instead. A `Task` (or Issue or Pull Request) view and `Plan` view will be visible.  Each view can be expanded into a larger panel by clicking on the "full screen" icon.

在会话列表中选择一个会话将隐藏列表并显示相关的会话详细信息。将显示 `任务`（或问题或拉取请求）视图和 `计划` 视图。每个视图都可以通过点击“全屏”图标扩展为更大的面板。

The `Task` view includes a description of the task along with links to additional information. The `Plan` view will include details about the related plan for your session (if one exists yet) any files currently in the plan.

`任务` 视图包括任务的描述以及指向其他信息的链接。`计划` 视图将包括有关您的会话的相关计划的详细信息（如果存在）以及计划中当前的任何文件。

If the [plan has already been implemented](#planning-and-implementing), you'll be able to view any changed files by clicking on file in the plan.

如果[计划已经实施](#planning-and-implementing)，您可以通过点击计划中的文件查看任何更改的文件。

<img src="./images/vscode/ghcw-overview.png" width="700px" />

When syncing is active, clicking on the file will open a local changes view of the synced contents. This view is editable and the changes will be synced back to the web session. If the session is not syncing, you will see the changes currently stored in the web session in a read-only mode.

当同步处于活动状态时，点击文件将打开同步内容的本地更改视图。此视图是可编辑的，更改将同步回 Web 会话。如果会话未同步，您将以只读模式看到当前存储在 Web 会话中的更改。

You can also click on the `Open File` icon when hovering on an file in the plan to open the file (instead of the changes view) in a new tab in VS Code. You may be prompted to start syncing the session if you are not already.

您还可以在计划中的文件上悬停时点击 `打开文件` 图标，在 VS Code 的新选项卡中打开文件（而不是更改视图）。如果您尚未开始同步会话，系统可能会提示您开始同步。

## Managing Sessions

## 管理会话

You can sync session file changes locally for any session that has a plan and an initial implementation.

您可以为任何有计划和初始实施的会话在本地同步会话文件更改。

If the session you opened does not yet have an implementation, see [Planning and Implementing](#planning-and-implementing) for information on creating one from VS Code. You can then sync its contents locally once done.

如果您打开的会话尚未实施，请参阅[计划和实施](#planning-and-implementing)以获取有关从 VS Code 创建会话的信息。完成后，您可以在本地同步其内容。

### Stopping Syncing Changes

### 停止同步更改

The quick start highlighted a fast way to start syncing your session's changes locally, so let's cover how to stop syncing changes next.

快速入门强调了一种快速开始在本地同步会话更改的方法，因此让我们接下来介绍如何停止同步更改。

If the session list is visible, you will see a green checkbox next to any session that is currently being synced. When hovering over this session, you will see a `Stop Syncing Changes` button. Otherwise, if the session details are visible for a session that is currently syncing, you will find this same button in the `Plan` view. Simply click this button in either location to stop syncing.

如果会话列表可见，您将看到当前正在同步的任何会话旁边有一个绿色复选框。当悬停在此会话上时，您将看到一个 `停止同步更改` 按钮。否则，如果当前正在同步的会话的会话详细信息可见，您将在 `计划` 视图中找到相同的按钮。只需在任一位置点击此按钮即可停止同步。

| Session List | Session Details |
| 会话列表 | 会话详细信息 |
| :--- | :--- |
| <img src="./images/vscode/ghcw-session-list-button.png" title="Image of session list" width="300px"> | <img src="./images/vscode/ghcw-session-details-button.png" title="Image of session detail" width="300px"> |

Alternatively, you can use the Command Palette (F1 or Ctrl/Cmd+Shift+P) and select the **GitHub Copilot Workspace: Stop Syncing Changes** command when you have the session details open.

或者，您可以使用命令面板（F1 或 Ctrl/Cmd+Shift+P）并在打开会话详细信息时选择 **GitHub Copilot Workspace: 停止同步更改** 命令。

You'll be switched back to the branch you where on when you started syncing changes, or **main** (or master) if nothing else. Since the changes you made locally are kept in sync automatically when syncing is active, the working tree is also cleaned out so you can easily jump in and out of sessions.

您将切换回开始同步更改时所在的分支，或者 **main**（或 master）如果没有其他分支。由于在同步处于活动状态时，您在本地所做的更改会自动保持同步，因此工��树也会被清理，以便您可以轻松地进出会话。

The next time you sync this same session, the session will go back to this tracking branch and the latest changes in GitHub Copilot Workspace - including your edits - will appear again.

下次您同步同一会话时，会话将返回到此跟踪分支，并且 GitHub Copilot Workspace 中的最新更改 - 包括您的编辑 - 将再次出现。

Note that if you manually change the branch away from the one set when syncing began, syncing will also automatically stop. However, in this case, any changes you made will be kept in the working tree to make sure you don't lose something you intended to keep. Stopping syncing as described above will ensure you've got a clean working tree to continue making other changes.

请注意，如果您手动更改分支而不是同步开始时设置的分支，同步也会自动停止。但是，在这种情况下，您所做的任何更改都将保留在工作树中，以确保您不会丢失您打算保留的内容。按照上述步骤停止同步将确保您有一个干净的工作树，以继续进行其他更改。

### Syncing Changes Locally

### 本地同步更改

As outlined in the quick start, you can always click on the VS Code icon in the GitHub Copilot Workspace web UI to start syncing changes locally. But you can also start syncing a session directly from within VS Code.

如快速入门中所述，您可以随时点击 GitHub Copilot Workspace Web UI 中的 VS Code 图标以开始在本地同步更改。但您也可以直接从 VS Code 内部开始同步会话。

However, as described in these previous sections, note that only sessions with a [plan and an initial implementation](#planning-and-implementing) can be synced locally.

但是，如前几节所述，请注意，只有具有[计划和初始实施](#planning-and-implementing)的会话才能在本地同步。

If session list is visible, hovering over a session that is not currently being synced (no green checkbox), will show a `Stop Syncing Changes` button. Otherwise, if the session details are visible instead, you will see this same button the `Plan` view (assuming syncing is inactive for this session). Click this button to start syncing changes for the session locally.

如果会话列表可见，悬停在当前未同步的会话上（没有绿色复选框），将显示一个 `停止同步更改` 按钮。否则，如果会话详细信息可见，您将在 `计划` 视图中看到相同的按钮（假设此会话的同步处于非活动状态）。点击此按钮以在本地开始同步会话的更改。

Note that any other existing session that is already syncing for the same repository will automatically stop syncing first, so you don't have to worry about conflicts.

请注意，任何其他已为同一存储库同步的现有会话将首先自动停止同步，因此您无需担心冲突。

| Session List | Session Details |
| 会话列表 | 会话详细信息 |
| :--- | :--- |
| <img src="./images/vscode/ghcw-session-list-no-sync.png" title="Image of session list" width="300px"> | <img src="./images/vscode/ghcw-session-details-no-sync.png" title="Image of session detail" width="300px"> |

Similarly, you can use the Command Palette (F1 or Ctrl/Cmd+Shift+P) and select the **GitHub Copilot Workspace: Sync Changes Locally** command when you are in the detail view for a session to start syncing.

同样，您可以使用命令面板（F1 或 Ctrl/Cmd+Shift+P）并在会话的详细视图中选择 **GitHub Copilot Workspace: 本地同步更改** 命令以开始同步。

Next you may be prompted as follows:
1. If you do not currently have the repository for the session open in VS Code, you will be prompted to open a folder with the repository or to clone the repository in a fresh location.
1. 如果您当前没有在 VS Code 中打开会话的存储库，系统会提示您打开包含存储库的文件夹或在新位置克隆存储库。
1. If you do have the correct repository open, but the current working tree has uncommitted changes, you'll be asked what you want to do with them.
1. 如果您确实打开了正确的存储库，但当前工作树有未提交的更改，系统会询问您要如何处理它们。

Either way, once this is done, your local repository will be on a GitHub Copilot Workspace tracking branch with a `ghcw-session` prefix as you can see in the status bar.

无论哪种方式，一旦完成，您的本地存储库将位于带有 `ghcw-session` 前缀的 GitHub Copilot Workspace 跟踪分支上，如状态栏中所示。

<img src="./images/vscode/ghcw-branch-example.png" title="Image of branch in status bar" width="250px">

Any edits make to the local files will be synced back to the web session, so you do not need to worry about committing or loosing your changes.

对本地文件所做的任何编辑都将同步回 Web 会话，因此您无需担心提交或丢失更改。

### Deleting a Session

### 删除会话

To delete a session, you click on the trash can icon next to the item in the session list. If you are currently viewing a session's details, select **Delete Session** from the context menu that appears when clicking on the `...` button on the `Task` or `Plan` views.

要删除会话，请点击会话列表中项目旁边的垃圾桶图标。如果您当前正在查看会话的详细信息，请从 `任务` 或 `计划` 视图中的 `...` 按钮出现的上下文菜单中选择 **删除会话**。

Alternatively, you can use thee Command Palette (F1 or Ctrl/Cmd+Shift+P) and select the **GitHub Copilot Workspace: Delete Session** command when you are viewing a session's details.

或者，您可以使用命令面板（F1 或 Ctrl/Cmd+Shift+P）并在查看会话详细信息时选择 **GitHub Copilot Workspace: 删除会话** 命令。

## Planning and implementing

## 计划和实施

When the session details are visible (and you see the `Task` and `Plan` views), you can make changes to the plan and its related implementation for the session right from VS Code.

当会话详细信息可见时（并且您看到 `任务` 和 `计划` 视图），您可以直接从 VS Code 对会话的计划及其相关实施进行更改。

In fact, can also generate and implement an initial plan if your session doesn't have one yet.

事实上，如果您的会话尚未有计划，您还可以生成和实施初始计划。

You will find a number of different options for interacting with the plan by clicking on the `...` button in the `Plan` view. However, the most common actions will appear as icons. Let's go through what each of these does.

您可以通过点击 `计划` 视图中的 `...` 按钮找到与计划交互的多种不同选项。然而，最常见的操作将以图标形式出现。让我们逐一了解这些操作的功能。

| Button | Command | Description | Location(s) |
| 按钮 | 命令 | 描述 | 位置 |
| :--- | :--- | :--- | :--- |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/project.svg"  width="24px" style="background-color:white;"> | Generate Plan | Generates a plan for the session and creates an inital implementation. | Plan view when no plan exists. Regenerate plan is available in the  `...` context menu afterwards. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/project.svg"  width="24px" style="background-color:white;"> | 生成计划 | 为会话生成计划并创建初始实施。 | 当没有计划时的计划视图。之后可以在 `...` 上下文菜单中重新生成计划。 |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/sparkle.svg"  width="24px" style="background-color:white;"> | Implement Plan | Implement (or re-implement) the selected items in the plan view. | Plan view when plan exists, `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/sparkle.svg"  width="24px" style="background-color:white;"> | 实施计划 | 实施（或重新实施）计划视图中的选定项目。 | 当计划存在时的计划视图，`...` 上下文菜单。 |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/comment.svg" width="24px" style="background-color:white;"> | Revise Plan | Make revisions to the entire plan using natural language. Will automatically implement the requested changes. | Plan view when plan exists, `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/comment.svg" width="24px" style="background-color:white;"> | 修订计划 | 使用自然语言对整个计划进行修订。将自动实施请求的更改。 | 当计划存在时的计划视图，`...` 上下文菜单。 |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/sync.svg"  width="24px" style="background-color:white;"> | Sync Changes Locally | See Managing Sessions. Start syncing session changes locally. | Plan view if there is an implementation, and the session is not already syncing, `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/sync.svg"  width="24px" style="background-color:white;"> | 本地同步更改 | 参见管理会话。开始在本地同步会话更改。 | 如果有实施的计划视图，并且会话尚未同步，`...` 上下文菜单。 |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/sync-ignored.svg"  width="24px" style="background-color:white;"> | Stop Syncing Changes | See Managing Sessions.  Stops syncing session changes locally. | Plan view if the visible session is already syncing, `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/sync-ignored.svg"  width="24px" style="background-color:white;"> | 停止同步更改 | 参见管理会话。停止在本地同步会话更改。 | 如果可见会话已在同步的计划视图，`...` 上下文菜单。 |

Generally these same commands are available in the Command Palette (F1 or Ctrl/Cmd+Shift+P) as well.

通常，这些相同的命令也可以在命令面板（F1 或 Ctrl/Cmd+Shift+P）中使用。

The `...` context menu is also available for files and items in the plan when you hover over them. This context menu will allow you to view the files, their changes, or edit, move, delete, or the list items as needed.

当您悬停在计划中的文件和项目上时，`...` 上下文菜单也可用。此上下文菜单将允许您查看文件、其更改，或根据需要编辑、移动、删除或列出项目。

### Natural Language Revisions

### 自然语言修订

You can also make revisions to the plan and implementation using natural language. This can be done for the entire plan as highlighted previously, or you can make targeted revisions to a file in the plan. You can even add another file to the plan and revise it in one shot.

您还可以使用自然语言对计划和实施进行修订。这可以对整个计划进行，如前所述，或者您可以对计划中的文件进行有针对性的修订。您甚至可以将另一个文件添加到计划中并一次性修订。

To make file-level revisions easy, there are buttons in the upper-right of any open editor window for a file that can be part of the plan.

为了简化文件级别的修订，任何打开的编辑器窗口的右上角都有按钮，可以成为计划的一部分。

<img src="./images/vscode/ghcw-editor-actions.png" title="Image of editor actions" width="700px">

Here's a summary of where you can trigger these kinds of revisions:

以下是您可以触发这些修订的地方的摘要：

| Button | Command | Description | Location(s) |
| 按钮 | 命令 | 描述 | 位置 |
| :--- | :--- | :--- | :--- |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/comment.svg" width="24px" style="background-color:white;"> | Revise Plan | Make revisions to the entire plan using natural language. Will automatically implement the requested changes. | Plan view when plan exists, `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/comment.svg" width="24px" style="background-color:white;"> | 修订计划 | 使用自然语言对整个计划进行修订。将自动实施请求的更改。 | 当计划存在时的计划视图，`...` 上下文菜单。 |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/target.svg"  width="24px" style="background-color:white;"> | Revise File | Make targeted revisions to a file using natural language. Will automatically either add the file to the plan or add a step to an existing entry, and then implement the requested changes. | Plan file items (hover), Editor actions (upper-right), `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/target.svg"  width="24px" style="background-color:white;"> | 修订文件 | 使用自然语言对文件进行有针对性的修订。将自动将文件添加到计划中或添加到现有条目的步骤，然后实施请求的更改。 | 计划文件项目（悬停）、编辑器操作（右上角）、`...` 上下文菜单。 |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/add.svg"  width="24px" style="background-color:white;"> | Add File to Plan | Adds the file to the plan, but makes no revisions to it. | Editor actions (upper-right), `...` context menu. |
| <img src="https://raw.githubusercontent.com/microsoft/vscode-codicons/refs/heads/main/src/icons/add.svg"  width="24px" style="background-color:white;"> | 将文件添加到计划 | 将文件添加到计划中，但不对其进行修订。 | 编辑器操作（右上角）、`...` 上下文菜单。 |

## Known Limitations

## 已知限制

1. As outlined above, you need to use the web UI for the following as they are not yet available in VS Code:
1. 如上所述，您需要使用 Web UI 进行以下操作，因为它们尚未在 VS Code 中可用：
    1. Starting a new session
    1. 开始一个新会话
    1. Edits to the task/specification/brainstorming
    1. 编辑任务/规范/头脑风暴
    1. Creating a PR from a session
    1. 从会话创建 PR
1. File syncing status does not cross open windows. So if you have multiple windows for the same folder (and repository) open, and each are syncing, you can end up transmitting or applying same file contents multiple times and fail to apply updates. To avoid this, either use a single window for a given repository, or do not start file syncing for more than one.
1. 文件同步状态不会跨打开的窗口。因此，如果您为同一文件夹（和存储库）打开多个窗口，并且每个窗口都在同步，您可能会多次传输或应用相同的文件内容，并且无法应用更新。为避免这种情况，请为给定的存储库使用单个窗口，或不要启动多个文件同步。
1. The sessions list will only show sessions that would also show up in the web's session list. For example, it excludes archived sessions or sessions that include a task but nothing else. However, as long as the session is in the web UI, you'll be able to click on the "Open in VS Code" button to open it in VS Code.
1. 会话列表将仅显示也会出现在 Web 会话列表中的会话。例如，它排除了已存档的会话或仅包含任务但没有其他内容的会话。但是，只要会话在 Web UI 中，您就可以点击“在 VS Code 中打开”按钮在 VS Code 中打开它。
