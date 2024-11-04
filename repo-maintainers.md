# Copilot Workspace for Repository Maintainers

# Copilot Workspace 仓库维护者指南

Copilot Workspace can assist you as a repository maintainer in several ways:

Copilot Workspace 可以通过多种方式帮助您作为仓库维护者：

1. Copilot Workspace can help you explore potential solutions to issues.
2. Copilot Workspace 可以帮助您探索问题的潜在解决方案。
2. Copilot Workspace can help you generate sketches of solutions to issues for potential contributors, lowering the barrier of entry.
2. Copilot Workspace 可以帮助您为潜在贡献者生成问题解决方案的草图，降低入门门槛。
3. Copilot Workspace can help encourage a culture where issue-creators leave additional helpful notes on how to solve issues, for use by both contributors and AI assistants.
3. Copilot Workspace 可以帮助鼓励一种文化，即问题创建者留下有关如何解决问题的额外有用注释，供贡献者和 AI 助手使用。

For example, when a new issue is filed in your repository, you can use Copilot Workspace to generate a sketch of a solution to the issue. You can then use the "Share" button to publish this sketch back to the issue thread, with additional comments about whether you think it is useful or not, and where it might need improvement. This can help potential contributors understand the problem better and provide a starting point for their work.

例如，当在您的仓库中提交新问题时，您可以使用 Copilot Workspace 生成问题解决方案的草图。然后，您可以使用“共享”按钮将此草图发布回问题线程，并附上您认为它是否有用以及可能需要改进的地方的额外评论。这可以帮助潜在贡献者更好地理解问题并为他们的工作提供起点。

Similarly, when a new issue is filed, you can ask the contributor to create a Copilot Workspace session for the issue. This may help the contributor understand the problem better and provide a starting point for their work. You can also include this guidance in the issue template for your repository, assuming your users have access to Copilot Workspace. You can also ask contributors to leave additional notes in the Copilot Workspace session, which can help future contributors and AI assistants understand the problem better.

同样，当提交新问题时，您可以要求贡献者为该问题创建一个 Copilot Workspace 会话。这可能有助于贡献者更好地理解问题并为他们的工作提供起点。假设您的用户可以访问 Copilot Workspace，您还可以在仓库的问题模板中包含此指导。您还可以要求贡献者在 Copilot Workspace 会话中留下额外的注释，这可以帮助未来的贡献者和 AI 助手更好地理解问题。

## Restricting the use of Copilot Workspace in your repository

## 限制在您的仓库中���用 Copilot Workspace

It is possible for undisciplined contributors to over-use AI-assisted code generation. Because of this, we give repository maintainers the option of disabling the direct use of Copilot Workspaces for creating pull requests and/or issue comments in their repositories.

不守纪律的贡献者可能会过度使用 AI 辅助代码生成。因此，我们为仓库维护者提供了禁用 Copilot Workspaces 直接用于在其仓库中创建拉取请求和/或问题评论的选项。

To disable the direct creation of pull requests using Copilot Workspace, create a file `.github/copilot-workspace/policy.json` in the default branch of the repository containing the following content:

要禁用使用 Copilot Workspace 直接创建拉取请求，请在存储库的默认分支中创建一个文件 `.github/copilot-workspace/policy.json`，其中包含以下内容：

```json
{
  "allowPullRequests": false
}
```

To disable the use of Copilot Workspace to directly generate issue comments that contain links to Copilot Workspace sessions, add the following content to the `policy.json` file:

要禁用使用 Copilot Workspace 直接生成包含 Copilot Workspace 会话链接的问题评论，请将以下内容添加到 `policy.json` 文件中：

```json
{
  "allowComments": false
}
```

Users of Copilot Workspace will still be able to:

Copilot Workspace 的用户仍然可以：

- create sharing links to Copilot Workspace sessions and paste them into issue comments
- 创建 Copilot Workspace 会话的共享链接并将其粘贴到问题评论中
- push to new branches in your repository (if they have write access)
- 推送到您的仓库中的新分支（如果他们有写入权限）
- push to new branches in forks of your repository
- 推送到您的仓库分叉中的新分支
- manually create pull requests from branches
- 手动从分支创建拉取请求
- use Copilot Workspace to generate code snippets and files for their own use in their own pull requests and issue comments to your repository
- 使用 Copilot Workspace 生成代码片段和文件，以便在他们自己的拉取请求和问题评论中使用
