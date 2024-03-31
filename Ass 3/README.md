# Web Application Deployment to Azure Using Terraform and GitHub Actions

This repository showcases the deployment of a simple Node.js biography web application to Azure, utilizing Terraform for infrastructure provisioning and GitHub Actions for continuous delivery.

## Deployed Application URL

Access the deployed web application here: [Omer's Biography Page](https://omerullahs-biography-page.azurewebsites.net/)

## Workflow

The CI/CD pipeline is automated with GitHub Actions, detailed in the [azure-cd workflow file](.github/workflows/azure-cd.yml). This workflow triggers on pushes to the 'main' and 'HW' branches, encompassing the following steps:

1. Repository checkout.
2. Azure CLI installation.
3. Azure authentication using service principal credentials via GitHub Secrets.
4. Terraform setup and initialization.
5. Application of Terraform configurations to update the Azure infrastructure.
6. Deployment of the web application to Azure App Service.

## Terraform Configuration

Infrastructure provisioning is handled via Terraform, targeting these main Azure resources:

- **Resource Group**
- **App Service Plan**
- **App Service**

View the Terraform configuration in the [terraform directory](terraform/).

## Challenges Encountered

### Azure Service Limit Exceeded
Encountered a `429 error` indicating a service limit was exceeded due to frequent deployments.

**Solution**: Switching to a different Azure account circumvented the limit. Lessons learned include the significance of managing resource requests and understanding Azure's request limitations.

### Secrets Management
The initial setup of GitHub Secrets and their references in the workflow required careful attention to ensure security and correctness.

### Deployment Package Configuration
Determining the correct file set for the Azure App Service deployment needed several attempts, particularly in configuring the deployment action correctly.

## Conclusion

This project demonstrates an efficient methodology for deploying web applications to Azure using Terraform and GitHub Actions, highlighting the importance of automation in modern cloud infrastructure management.

## License

This project is licensed under the [ISC License](LICENSE).
