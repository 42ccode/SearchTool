SearchTool
项目简介 | Project Introduction
SearchTool 是一个基于 Tkinter 开发的简单文件搜索工具，用户可以通过输入关键字和文件类型来查找指定目录中的文件。该工具适用于快速查找和管理大量文件，提供了直观的图形界面并支持文件的双击打开功能。

SearchTool is a simple file search tool developed with Tkinter. Users can search for files in a specified directory by entering keywords and file types. This tool is ideal for quickly searching and managing a large number of files, providing an intuitive graphical interface and supporting the double-click opening of files.

功能特性 | Features
文件搜索 | File Search: 根据用户输入的关键字和文件类型，在指定目录中搜索匹配的文件。

Search for files in a specified directory based on user-input keywords and file types.

文件类型自动处理 | Auto File Type Handling: 用户输入的文件类型无需包括 .，工具会自动处理。

The tool automatically handles file types, so users don't need to include a ..

文件路径展示 | Display File Paths: 搜索结果以文件路径形式展示在列表框中。

The search results are displayed in the list box as file paths.

文件管理 | File Management: 双击搜索结果中的文件路径，可以使用系统默认的文件管理器打开文件。

Double-clicking on a file path in the search results opens the file with the system's default file manager.

滚动支持 | Scroll Support: 列表框中支持滚动查看大量搜索结果。

Scroll through a large number of search results in the list box.

使用方法 | Usage
克隆仓库到本地：

Clone the repository to your local machine:

bash
复制代码
git clone https://github.com/yourusername/SearchTool.git
进入项目目录：

Navigate to the project directory:

bash
复制代码
cd SearchTool
运行主程序：

Run the main program:

bash
复制代码
python search_tool.py
开发环境 | Development Environment
Python 版本 | Python Version: 3.x
依赖库 | Dependency: Tkinter (Python Standard Library)
项目结构 | Project Structure
bash
复制代码
SearchTool/
├── search_tool.py   # 主程序文件 | Main Program File
├── README.md        # 项目说明文件 | Project README
贡献指南 | Contribution Guidelines
欢迎提交 Pull Request 或报告 Issue。如果你有任何建议或意见，请在仓库中打开一个 Issue。

Contributions are welcome via Pull Requests or by reporting issues. If you have any suggestions or feedback, feel free to open an Issue in the repository.

许可证 | License
该项目使用 MIT 许可证。

This project is licensed under the MIT License.

你可以根据需要调整 README 文件的内容和格式。