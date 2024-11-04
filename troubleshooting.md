## Troubleshooting

### Introduction

Welcome to the troubleshooting guide for Copilot Workspace! In this section, we will provide you with helpful tips and solutions to common issues you may encounter while working with organizations and private repositories in Copilot Workspace. Our goal is to ensure that you have a smooth and productive experience. Let's dive in!

欢迎使用 Copilot Workspace 故障排除指南！在本节中，我们将为您提供有用的提示和解决方案，以解决您在使用 Copilot Workspace 处理组织和私有存储库时可能遇到的常见问题。我们的目标是确保您拥有顺畅且高效的体验。让我们开始吧！

### Troubleshooting Organizations

When working with organizations in Copilot Workspace, you may encounter some common issues. Here are some troubleshooting tips to help you resolve them:

在 Copilot Workspace 中处理组织时，您可能会遇到一些常见问题。以下是一些故障排除提示，帮助您解决这些问题：

- **You are accessing an org that must approve OAuth apps**. As part of the login you authorize the OAuth app into various orgs, depending on the org policies with regard to OAuth apps. You can request access and the organization can approve the OAuth app. If you need to re-request access or revoke any access at all you can [control the status of your connection with the OAuth app](https://github.com/settings/connections/applications/903eccd8a9d2ff50288f).

- **您正在访问必须批准 OAuth 应用的组织**。作为登录的一部分，您授权 OAuth 应用进入各种组织，具体取决于组织对 OAuth 应用的政策。您可以请求访问，组织可以批准 OAuth 应用。如果您需要重新请求访问或完全撤销任何访问，您可以[控制与 OAuth 应用的连接状态](https://github.com/settings/connections/applications/903eccd8a9d2ff50288f)。

- **Although you appear to have the correct authorization credentials, the `github` organization has enabled OAuth App access restrictions, meaning that data access to third-parties is limited.** This is because an org restricts OAuth apps. Some of authorization attempts for orgs may fail if the org doesn't allow OAuth apps at all. This can affect even access to public repositories in organizations that deny access to OAuth apps.

- **尽管您似乎拥有正确的授权凭据，但 `github` 组织已启用 OAuth 应用访问限制，这意味着对第三方的数据访问受到限制。** 这是因为组织限制了 OAuth 应用。如果组织完全不允许 OAuth 应用，则某些组织的授权尝试可能会失败。这甚至会影响对拒绝访问 OAuth 应用的组织中的公共存储库的访问。

- **Resource protected by organization SAML enforcement. You must grant your OAuth token access to this organization**.You may be logging in to an organization with SAML control, e.g. Microsoft. They should
  1. Log out of Copilot Workspace.
  2. Go through SAML auth in the browser by looking at, say, a repository of the organization
  3. Then log back into Copilot Workspace.

- **资源受组织 SAML 强制保护。您必须授予您的 OAuth 令牌访问此组织的权限**。您可能正在登录具有 SAML 控制的组织，例如 Microsoft。他们应该
  1. 退出 Copilot Workspace。
  2. 通过在浏览器中查看组织的存储库来进行 SAML 认证
  3. 然后重新登录 Copilot Workspace。

### Troubleshooting Private Repositories

- **You can't access a private repository in your own account**. After login you should be able to access your personal private repositories unless you have removed access for the OAuth app. If you have trouble, it is possible it is because you landed in Copilot Workspace via a sharing link and have only given public repo privileges. You should log out and log back in again and this should restore access. Failing that you should [check the status of their connection with the OAuth app](https://github.com/settings/connections/applications/903eccd8a9d2ff50288f).

- **您无法访问自己帐户中的私有存储库**。登录后，您应该能够访问您的个人私有存储库，除非您已删除对 OAuth 应用的访问权限。如果您遇到问题，可能是因为您通过共享链接进入了 Copilot Workspace，并且只授予了公共存储库权限。您应该退出并重新登录，这应该会恢复访问权限。如果仍然无法解决，您应该[检查与 OAuth 应用的连接状态](https://github.com/settings/connections/applications/903eccd8a9d2ff50288f)。

## Ambiguity Warnings

If Copilot Workspace detects that your task is overly ambiguous/unclear (e.g. it doesn’t seem aligned with the goals/focus of the repo), then it may warn you about that and ask you to clarify the task further, before you can carry on. This is done to prevent hallucination in the specification and help guide you towards the “pit of success”, since subsequent stages of the workflow work best with sufficient detail.

如果 Copilot Workspace 检测到您的任务过于模糊/不清楚（例如，它似乎与存储库的目标/重点不一致），那么它可能会警告您并要求您进一步澄清任务，然后才能继续。这是为了防止规范中的幻觉，并帮助引导您走向“成功之路”，因为工作流程的后续阶段在有足够细节的情况下效果最佳。

<img src="images/further-techniques/ambiguous-spec.png" width=600 alt="Ambiguous specification">

*任务过于模糊，需要澄清意图的警告*

### Troubleshooting Codespaces

- **Billable owner could not be determined for a new codespace, Repository may not be used for a codespace.** The CW OAuth app is not installed in the billable owner's organization.

- **无法确定新代码空间的计费所有者，存储库可能无法用于代码空间。** CW OAuth 应用未安装在计费所有者的组织中。

Please view the [Codespaces Guide](codespaces-guide.md) for more information on Codespaces and troubleshooting common errors.

有关 Codespaces 和故障排除常见错误的更多信息，请查看[Codespaces 指南](codespaces-guide.md)。
