# Configure Azure Providerr
provider "azurerm" {
  features {}
}

# Resource Group (assuming it already exists)
resource "azurerm_resource_group" "rg" {
  name = "Homework3ResourcesV2" 
  location = "East US"
}

resource "azurerm_app_service_plan" "asp" {
  name                = "omerullah"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Free"
    size = "F1"
  }
}

# App Service (using the newly created plan)
resource "azurerm_app_service" "app" {
  name                = "omerullahs-biography-page"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
}
