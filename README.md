VMSS Template Generator
=======================

# Short-Term Goal

Auto-generate most of the VMSS templates in the Azure Quickstart Templates repo for easy update.

















# Eventual Requirements


> flag for getting location from parameter or resource group
> flag for getting pip name/label from parameter or auto-generated based on vmssName
> flag for separate osType or just parse image (might not actually be necessary though; could just ignore osType)
> flag for instance count being int or string
> flag for authType split or just password
> flag for autoscale option or not
> flag for setting default to min or allow user to specify
> flag for autoscale min/max/default/intervalse as strings or ints (might not actually be necessary though; why should they be strings?)
> flag for windows/linx split or just one
> flag for logic to determine if can use premium storage or only allow premium/non-premium
> flag for managed disk or regular storage
> flag for os disks
> flag for load balancer, jumpbox, or nothing
> flag for custom script extension
> flag for diagnostics/wad/lad
> flag for _artifactsLocation and sasToken