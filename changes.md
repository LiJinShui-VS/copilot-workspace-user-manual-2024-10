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

When a plan includes a `Commands` section (e.g. because your task required installing 3rd-party dependencies), you can now execute an individual command, in addition to the existing "Execute all" support. Additionally, the completion status of commands are now persisted. So when you resume a CW session later, you can see which commands were already run, which failed, and which are still outstanding.

当一个计划包括一个`命令`部分（例如，因为你的任务需要安装第三方依赖项），你现在可以执行单个命令，除了现有的“执行所有”支持。此外，命令的完成状态现在是持久的。因此，当你稍后恢复CW会话时，你可以看到哪些命令已经运行，哪些失败，哪些仍然未完成。

<img src="https://github.com/user-attachments/assets/ede11071-62a8-4f9c-a8a9-f91a4ddf71c0" width="300px" />
