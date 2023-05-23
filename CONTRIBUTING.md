# How to Contribute 

Thank you for your interest in contributing to the LOOBins project! We appreciate and welcome contributions that help bolster the project. You can contribute by adding or updating YAML files that represent LOOBins. **Important Note:** LOOBins does not intend to cover Unix-based binaries that are detailed in [GTFOBins](https://gtfobins.github.io) unless the binary has a very specific use case targeting macOS.

Additionally, you can help us develop the [pyloobins Python SDK](https://pypi.org/project/pyloobins/) contained in the src folder of the repository.


## Add a new LOOBin

1. **Check Existing Issues**: To prevent duplicative work efforts, please first check the active and closed [Issues](https://github.com/infosecB/LOOBins/issues) to ensure that the binary you would like to add isn't already in development. Issues tagged with "Help Wanted" are available for assignment. 

2. **Create an Issue**: Once you have validated that an issue does not exist for the binary you would like to author, create a new issue using the "New LOOBin" template. If you are interesting in claiming a LOOBin that is tagged as "Help Wanted", add a comment. A maintainer will review the issue and assign it to you.

3. **Fork the Repository**: Navigate to the [LOOBins GitHub repository](https://github.com/infosecB/LOOBins) and click the "Fork" button in the top-right corner to create your own copy of the repository.

4. **Clone the Forked Repository**: Open your terminal and run the following command to clone the forked repository to your local machine:

    `git clone https://github.com/your-username/project-name.git`

5. **Create a New Branch**: Navigate to the cloned repository and create a new branch for your changes using the following command:

    `git checkout -b your-branch-name`

6. **Create Your YAML File**: Create a new YAML file in the LOOBins directory located in the root folder the project. Ensure that the YAML file adheres to the [LOOBin schema](https://github.com/infosecB/LOOBins/blob/main/docs/schema.md). 

    The LOOBins json schema is included in [SchemaStore](https://github.com/SchemaStore/schemastore/pull/2893). VS Code will now perform YAML schema validation and linting for LOOBins out of the box. Make sure to install the [YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml). Schema validation will automatically apply to the YAML files within the /LOOBins subfolder.

    You can use the "pyloobins" Python command-line utility to generate a template file:

    `pip install pyloobins`
    `pyloobins create --name "Test"`

    You can validate a new schema by running:

    `pyloobins validate --path "test.yml"`

7. **Commit Your Changes**: Add the new YAML file to the staging area and commit the changes with a descriptive commit message:

    `git add path/to/your-file.yaml`

    `git commit -m "Add YAML file for binary xyz"`

8. **Push Your Changes**: Push the changes to your forked repository on GitHub:

    `git push origin your-branch-name`

9. **Submit a Pull Request**: Navigate to the "Pull requests" tab on the original LOOBins GitHub repository and click the "New pull request" button. Select your forked repository and the branch containing your changes, then click "Create pull request." Provide a detailed description of the changes and any additional information that may be helpful for the maintainers to review.

    Once your pull request is submitted, the maintainers will review your changes and provide feedback. If your changes are approved, they will be merged into the main repository.

    Note: Please replace `LOOBins`, `your-username`, `project-name`, `your-branch-name`, and `path/to/your-file.yaml` with the appropriate values for your specific project.

## Update an existing LOOBin

1. **Fork the Repository**: Navigate to the [LOOBins GitHub repository](https://github.com/infosecB/LOOBins) and click the "Fork" button in the top-right corner to create your own copy of the repository.

2. **Clone the Forked Repository**: Open your terminal and run the following command to clone the forked repository to your local machine:

    `git clone https://github.com/your-username/project-name.git`

3. **Create a New Branch**: Navigate to the cloned repository and create a new branch for your changes using the following command:

    `git checkout -b your-branch-name`

4. **Update the YAML File**: Make your additions/changes in the exiting LOOBin's YAML file.

5. **Commit Your Changes**: Add the new YAML file to the staging area and commit the changes with a descriptive commit message:

    `git add path/to/your-file.yaml`

    `git commit -m "Add YAML file for binary xyz"`

6. **Push Your Changes**: Push the changes to your forked repository on GitHub:

    `git push origin your-branch-name`

7. **Submit a Pull Request**: Navigate to the "Pull requests" tab on the original LOOBins GitHub repository and click the "New pull request" button. Select your forked repository and the branch containing your changes, then click "Create pull request." Provide a detailed description of the changes and any additional information that may be helpful for the maintainers to review.

    Once your pull request is submitted, the maintainers will review your changes and provide feedback. If your changes are approved, they will be merged into the main repository.

    Note: Please replace `LOOBins`, `your-username`, `project-name`, `your-branch-name`, and `path/to/your-file.yaml` with the appropriate values for your specific project.
