# Codespaces Starter Guide

# Codespaces 入门指南

This document contains useful information for using the terminal/Codespace in your Workspace session.

本文档包含在工作区会话中使用终端/Codespace 的有用信息。

## Codespaces Limits

## Codespaces 限制

### Overall Usage

### 总体使用情况

The technical preview includes limited free Codespaces compute usage that is reset at the start of the calendar month.

技术预览版包括有限的免费 Codespaces 计算使用量，该使用量在日历月初重置。

### Overall Limits

### 总体限制

The technical preview enforces a total Codespaces and total active Codespaces limits that you may encounter. If closing Workspace sessions does not resolve these issues you may reach out to us [here](https://github.com/githubnext/copilot-workspace-user-manual?tab=readme-ov-file#feedback).

技术预览版强制执行你可能遇到的总 Codespaces 和总活跃 Codespaces 限制。如果关闭工作区会话不能解决这些问题，你可以在[这里](https://github.com/githubnext/copilot-workspace-user-manual?tab=readme-ov-file#feedback)联系我们。

### Organization based limits and policies

### 基于组织的限制和政策

If the Organization that owns the repository has set policies for Codespaces usage they will be applied to being able to create Codespaces for Workspace. You should reach out to an administrator of the organization to adjust any policies.

如果拥有仓库的组织为 Codespaces 使用设置了政策，这些政策将应用于能够为工作区创建 Codespaces。你应该联系组织的管理员来调整任何政策。

## Common Errors

## 常见错误

#### You've reached your Copilot Workspace usage limit

#### 你已达到 Copilot Workspace 使用限制

At the start of the next calendar month your free usage limit will reset and you can continue using Workspace. You may reach out to us and give us feedback about the usage limit [here](https://github.com/githubnext/copilot-workspace-user-manual?tab=readme-ov-file#feedback).

在下一个日历月初，你的免费使用限制将重置，你可以继续使用工作区。你可以在[这里](https://github.com/githubnext/copilot-workspace-user-manual?tab=readme-ov-file#feedback)联系我们并提供关于使用限制的反馈。

#### Limit of active Copilot Workspace reached.

#### 达到活跃的 Copilot Workspace 限制。

Remediate this by closing open Workspace sessions and allowing previous sessions to shutdown before creating new ones.

通过关闭打开的工作区会话并允许先前的会话关闭来解决此问题，然后再创建新的会话。

#### Limit of Copilot Workspace reached.

#### 达到 Copilot Workspace 限制。

Remediate this by closing open Workspace sessions and allowing previous sessions to shutdown before creating new ones.

通过关闭打开的工作区会话并允许先前的会话关闭来解决此问题，然后再创建新的会话。

#### Repository may not be used for a Codespace

#### 仓库可能无法用于 Codespace

This may be because of a repository or organization policy restricting Codespaces creation. Please check any settings in the organization or repository that may be preventing Codespaces usage. If you do not find any please reach out to our [technical preview feedback channels](https://github.com/githubnext/copilot-workspace-user-manual?tab=readme-ov-file#feedback) for assistance.

这可能是由于仓库或组织政策限制了 Codespaces 的创建。请检查组织或仓库中的任何设置，这些设置可能会阻止 Codespaces 的使用。如果你没有找到任何问题，请联系我们的[技术预览反馈渠道](https://github.com/githubnext/copilot-workspace-user-manual?tab=readme-ov-file#feedback)寻求帮助。

#### The assigned location is currently unavailable.

#### 分配的位置当前不可用。

You may try again in a few minutes. Additionally, you can change your default Codespaces region in your user settings if you continue to run into this error for a particular region by following these [public docs](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-default-region-for-github-codespaces).

你可以在几分钟后再试一次。此外，如果你在特定区域继续遇到此错误，你可以按照这些[公共文档](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-default-region-for-github-codespaces)在用户设置中更改默认的 Codespaces 区域。

#### Provided `devcontainer.json` cannot be parsed to valid JSON

#### 提供的 `devcontainer.json` 无法解析为有效的 JSON

In the chosen repository you may need to fix the `devcontainer.json` for syntax errors. You can read more about `devcontainer.json` syntax in the following [public docs](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).

在选定的仓库中，你可能需要修复 `devcontainer.json` 的语法错误。你可以在以下[公共文档](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)中了解更多关于 `devcontainer.json` 语法的信息。

#### The organization has enabled OAuth App access restrictions, meaning that access to Copilot Workspace is limited.

#### 组织已启用 OAuth 应用访问限制，这意味着对 Copilot Workspace 的访问受到限制。

Reach out to the organization administrator to give access to the Copilot Workspace OAuth app.

联系组织管理员以授予对 Copilot Workspace OAuth 应用的访问权限。
