# Creating Repositories from Templates

# 从模板创建仓库

Copilot Workspace allows you to create repositories from templates using natural language.

Copilot Workspace 允许你使用自然语言从模板创建仓库。

## Using "Use this template" from GitHub.com

## 使用 GitHub.com 的“使用此模板”

To create a repository with Copilot Workspace, you can navigate to a template repository in GitHub.com and choose “Use this template”, like this:

要使用 Copilot Workspace 创建仓库，你可以导航到 GitHub.com 中的模板仓库并选择“使用此模板”，如下所示：

<img src="images/creating-repos/create-repo-from-template.png" width=400 alt="Create repository from template"><br>*Creating a repository from a template via Copilot Workspace*

*通过 Copilot Workspace 从模板创建仓库*

The task is based on the description of the software to create, plus the README of the template repo. You can also start this kind of task by creating a [new session](#using-new-session-on-the-dashboard). Once started a create repository task looks like this:

任务基于要创建的软件描述，加上模板仓库的自述文件。你也可以通过创建[新会话](#using-new-session-on-the-dashboard)来开始这种任务。一旦开始，创建仓库任务看起来像这样：

<img src="images/creating-repos/repo-task-timeline-representation.png" width=600 alt="Repo task timeline representation"><br>*The task is labeled as “Repository”, and the “Template” panel indicates the template repo*

*任务被标记为“仓库”，并且“模板”面板指示模板仓库*

Copilot Workspace will then generate a specification for the repository based on the description you provide, and a plan for creating it, and then the final implementation.

然后，Copilot Workspace 将根据你提供的描述生成仓库的规范，以及创建它的计划，然后是最终的实现。

## Using "New session" on the dashboard

## 在仪表板上使用“新会话”

You can also create a repository from a template by clicking the “New session” button in the [Copilot Workspace dashboard](https://copilot-workspace.githubnext.com), and search for a template. This will open a new task in the workspace where you can describe the software you want to create.

你也可以通过点击 [Copilot Workspace 仪表板](https://copilot-workspace.githubnext.com)中的“新会话”按钮并搜索模板来从模板创建仓库。这将在工作区中打开一个新任务，你可以在其中描述你想要创建的软件。

## Using the URL

## 使用 URL

You can also turn on “Create Repository” mode for any repository URL by adding `?template=true` as a query parameter. For example:

你还可以通过添加 `?template=true` 作为查询参数来为任何仓库 URL 打开“创建仓库”模式。例如：

https://copilot-workspace.githubnext.com/githubnext/hello-world?template=true

For incoming URLs, some repositories are treated as templates by default:

对于传入的 URL，某些仓库默认被视为模板：

- Any GitHub template repository
- Any repository in an organization containing `templates`, upper or lower case, with dash at start or end
- Any repository with `-template`, `-scaffold`, `-starter` or `-boilerplate` in its name, upper or lower case, with dash at start or end

- 任何 GitHub 模板仓库
- 任何组织中包含 `templates` 的仓库，大小写均可，开头或结尾带有破折号
- 任何名称中包含 `-template`、`-scaffold`、`-starter` 或 `-boilerplate` 的仓库，大小写均可，开头或结尾带有破折号
