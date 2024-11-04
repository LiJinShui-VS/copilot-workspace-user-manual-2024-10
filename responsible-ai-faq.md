# Responsible AI FAQ

# 负责任的 AI 常见问题

## What is Copilot Workspace? 

## 什么是 Copilot Workspace？

Copilot Workspace is a reimagined developer inner loop. The focal points of the experience are selecting a task, expressing intent, and then collaborating with AI towards a solution. We believe this can dramatically reduce complexity, improve productivity, and delight developers, without taking away the aspects of software development that they value most, such as decision making, creativity, and ownership. 

Copilot Workspace 是一个重新构想的开发者内部循环。体验的重点是选择任务、表达意图，然后与 AI 合作寻找解决方案。我们相信这可以显著减少复杂性，提高生产力，并让开发人员感到满意，而不会剥夺他们最重视的软件开发方面，例如决策、创造力和所有权。

## What can Copilot Workspace do?  

## Copilot Workspace 能做什么？

Copilot Workspace takes in a development task from a user, for example, a GitHub Issue, and produces a natural-language specification of the current behavior of the code, a plan for how to modify the code to complete the task, and eventually the actual code changes to all relevant files in the repo.  Each step (task, spec, plan, and implementation) is editable by the user, enabling the user to steer the AI to complete the task in the best way.     

Copilot Workspace 接受用户的开发任务，例如 GitHub 问题，并生成代码当前行为的自然语言规范、如何修改代码以完成任务的计划，最终是对仓库中所有相关文件的实际代码更改。每个步骤（任务、规范、计划和实施）都可以由用户编辑，使用户能够引导 AI 以最佳方式完成任务。

## What is/are Copilot Workspace’s intended use(s)? 

## Copilot Workspace 的预期用途是什么？

Copilot Workspace is intended to:

Copilot Workspace 旨在：

1. Accelerate software developers, helping them make small- and medium-scale code changes quickly and correctly.   
2. Reduce the activation energy for developers to start tasks, by giving them an AI-generated starting point. 
3. Help experienced developers work with unfamiliar programming languages and frameworks. 
4. Help developers contribute to unfamiliar codebases, for example, to open source projects. 

1. 加速软件开发人员，帮助他们快速正确地进行小规模和中等规模的代码更改。
2. 通过为开发人员提供 AI 生成的起点，降低他们开始任务的激活能量。
3. 帮助有经验的开发人员使用不熟悉的编程语言和框架。
4. 帮助开发人员为不熟悉的代码库做出贡献，例如开源项目。

## How was Copilot Workspace evaluated? What metrics are used to measure performance? 

## Copilot Workspace 是如何评估的？使用了哪些指标来衡量性能？

Copilot Workspace was evaluated in the following ways: 

Copilot Workspace 通过以下方式进行评估：

* Offline evaluations.  We have a corpus of known tasks and an entrypoint that allows us to run Copilot Workspace over those tasks in a headless mode.  When we make changes to our prompts, switch to a different model, etc., we run those benchmarks and manually validate the changes to Copilot Workspace’s outputs.  If we see regressions, we iterate on the prompts until there are no more regressions.  In addition, we have a larger set of benchmarks that are mined from GitHub, and we use model-driven evaluations to ensure consistent quality. 
* User studies.  In January, we ran a round of user studies with GitHub employees where we gave them a standard task and asked them to complete the task using Copilot Workspace.  We are planning additional user studies as part of the Technical Preview.
* Extensive dogfooding within our team.  We used Copilot Workspace to build Copilot Workspace. 
* Red teaming.  We have prepared a set of malicious prompts and run Copilot Workspace in headless mode over those prompts.  Then we do both human- and model-driven evaluations of the output for harmful responses, and if we see those, we update our prompts and filters so that users do not encounter them. 

* 离线评估。我们有一个已知任务的语料库和一个入口点，允许我们在无头模式下运行 Copilot Workspace。当我们对提示进行更改、切换到不同的模型等时，我们运行这些基准测试并手动验证对 Copilot Workspace 输出的更改。如果我们看到回归，我们会对提示进行迭代，直到没有更多回归。此外，我们还有一组从 GitHub 挖掘出来的更大基准测试，我们使用模型驱动的评估来确保一致的质量。
* 用户研究。1 月份，我们与 GitHub 员工进行了一轮用户研究，我们给他们一个标准任务，并要求他们使用 Copilot Workspace 完成任务。我们计划在技术预览中进行更多的用户研究。
* 我们团队内部广泛的自用测试。我们使用 Copilot Workspace 构建 Copilot Workspace。
* 红队测试。我们准备了一组恶意提示，并在无头模式下运行 Copilot Workspace 处理这些提示。然后我们对输出进行人工和模型驱动的评估，以检测有害响应，如果发现这些响应，我们会更新提示和过滤器，以确保用户不会遇到它们。

## What are the limitations of Copilot Workspace? How can users minimize the impact of Copilot Workspace’s limitations when using the system? 

## Copilot Workspace 的局限性是什么？用户在使用系统时如何最大限度地减少 Copilot Workspace 局限性的影响？

Copilot Workspace is not always correct.  Users should carefully validate its output and should not blindly trust it.  If users detect inaccuracies in Copilot Workspace’s outputs, we have made it easy for them to edit and correct any model-generated outputs. We have also built validation tools, particularly a terminal which allows the user to execute the generated code in a sandboxed environment.  The user should use these tools to validate and correct Copilot Workspace’s outputs. 

Copilot Workspace 并不总是正确的。用户应仔细验证其输出，不应盲目相信它。如果用户发现 Copilot Workspace 输出中的不准确之处，我们已经使他们可以轻松编辑和纠正任何模型生成的输出。我们还构建了验证工具，特别是一个终端，允许用户在沙箱环境中执行生成的代码。用户应使用这些工具来验证和纠正 Copilot Workspace 的输出。

## What operational factors and settings allow for effective and responsible use of Copilot Workspace? 

## 哪些操作因素和设置允许有效和负责任地使用 Copilot Workspace？

Copilot Workspace will perform best on common programming languages and frameworks and when the natural language is English.    

Copilot Workspace 在常见的编程语言和框架以及自然语言为英语时表现最佳。

Code generated by Copilot Workspace should be held to the same standard as human-written code – it should be code reviewed, have automated tests, be analyzed by linters and static analyzers, etc.  Copilot Workspace can help add automated tests to in-progress PRs, helping improve the overall health of a software project. 

Copilot Workspace 生成的代码应达到与人类编写的代码相同的标准——它应经过代码审查、具有自动化测试、由 lint 工具和静态分析工具进行分析等。Copilot Workspace 可以帮助为正在进行的 PR 添加自动化测试，帮助提高软件项目的整体健康状况。

## What should a user do if they encounter offensive content while using Copilot Workspace? 

## 用户在使用 Copilot Workspace 时遇到冒犯性内容应该怎么做？

Please report any examples of offensive content to copilot-safety@github.com.  Please include a share link so that we can investigate. 

请将任何冒犯性内容的示例报告给 copilot-safety@github.com。请包括一个共享链接，以便我们进行调查。
