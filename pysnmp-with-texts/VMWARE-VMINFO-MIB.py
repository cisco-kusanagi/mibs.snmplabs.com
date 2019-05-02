#
# PySNMP MIB module VMWARE-VMINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-VMINFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, Counter64, Unsigned32, ObjectIdentity, Counter32, MibIdentifier, Integer32, NotificationType, iso, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "NotificationType", "iso", "Gauge32", "IpAddress")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
vmwESXNotifications, = mibBuilder.importSymbols("VMWARE-ENV-MIB", "vmwESXNotifications")
vmwVirtMachines, vmwTraps = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwVirtMachines", "vmwTraps")
VmwConnectedState, = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwConnectedState")
vmwVmInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 2, 10))
vmwVmInfoMIB.setRevisions(('2011-09-17 00:00', '2010-06-22 00:00', '2008-10-23 00:00', '2007-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwVmInfoMIB.setRevisionsDescriptions(('Remove vmwVmID as it duplicates vmwVmID.', 'Add managed object vmwVmUUID to vmTable to allow management applications to identify a VM uniquely over a set of ESX systems. This value is useful when VMs may move between systems.', 'Add to comments the Managed Object Browser (MOB) URLs which provide data this MIB module exposes. Handle cases in reporting string for managed objects in this mib where the values depend on additional operator configuration. Instead of returning an empty string, an error message of the form: W|E: error description Add vmNumCpus to vmwVmTable to better report on VSMP virtual machines. Add vmwVmNetConnected and vmwVmMAC to vmwVmNetTable VIM Virtual Devices index range values are documented based on ESX 3/4 implementation, they may change in the future releases. Update comments to note that CDROM also lists DVDROM virtual devices.', 'This is the first revision in SMIv2 format. Prior version was published as SMIv1. Notifications found here were formerly in the VMWARE-TRAPS-MIB module.',))
if mibBuilder.loadTexts: vmwVmInfoMIB.setLastUpdated('201109170000Z')
if mibBuilder.loadTexts: vmwVmInfoMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwVmInfoMIB.setContactInfo('VMware, Inc 3401 Hillview Ave Palo Alto, CA 94304 Tel: 1-877-486-9273 or 650-427-5000 Fax: 650-427-5001 Web: http://communities.vmware.com/community/developer/forums/managementapi ')
if mibBuilder.loadTexts: vmwVmInfoMIB.setDescription('This MIB module provides for monitoring of inventory and state via polling and notifications of state changes for virtual machines residing on this host system. This MIB module also provides a mapping beween SMI managed objects defined here and their corresponding VMware Virtual Infrastructure Management (VIM) API properties.')
vmwVmTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 1), )
if mibBuilder.loadTexts: vmwVmTable.setStatus('current')
if mibBuilder.loadTexts: vmwVmTable.setDescription('A table containing information on virtual machines that have been configured on the system.')
vmwVmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwVmIdx"))
if mibBuilder.loadTexts: vmwVmEntry.setStatus('current')
if mibBuilder.loadTexts: vmwVmEntry.setDescription('Identifies a registered VM on this ESX system.')
vmwVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmIdx.setStatus('current')
if mibBuilder.loadTexts: vmwVmIdx.setDescription('An operational identifier given the VM when registered on this ESX system. The value is not unique across ESX systems and may change upon reboot. VIM property: ha-vm-folder MOB: https://esx.example.com/mob/?moid=ha%2dfolder%2dvm A given Virtual Machine Instance can be queried using this URL: MOB: https://esx.example.com/mob/?moid=vmwVmIdx')
vmwVmDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmDisplayName.setStatus('current')
if mibBuilder.loadTexts: vmwVmDisplayName.setDescription('Name by which this vm is displayed. It is not guaranteed to be unique. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=summary%2eguest')
vmwVmConfigFile = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmConfigFile.setStatus('current')
if mibBuilder.loadTexts: vmwVmConfigFile.setDescription('Path to the configuration file for this vm expressed as a fully qualified path name in POSIX or DOS extended format VM Config file File name: MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2efiles VM Datastore containing the filename: MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2edatastoreUrl')
vmwVmGuestOS = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmGuestOS.setStatus('current')
if mibBuilder.loadTexts: vmwVmGuestOS.setDescription("Operating system running on this vm. This value corresponds to the value specified when creating the VM and unless set correctly may differ from the actual OS running. Will return one of the values if set in order: Vim.Vm.GuestInfo.guestFullName Vim.Vm.GuestInfo.guestId Vim.Vm.GuestInfo.guestFamily MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=guest where moid = vmwVmIdx. If VMware Tools is not running, value will be of form 'E: error message'")
vmwVmMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 5), Integer32()).setUnits('megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmMemSize.setStatus('current')
if mibBuilder.loadTexts: vmwVmMemSize.setDescription('Memory configured for this virtual machine. Memory > MAX Integer32 is reported as max integer32. VIM Property: memoryMB MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware')
vmwVmState = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmState.setStatus('current')
if mibBuilder.loadTexts: vmwVmState.setDescription('Power state of the virtual machine. VIM Property: powerState MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=summary%2eruntime')
vmwVmVMID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmVMID.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVmVMID.setDescription('No longer provided, use vmwVmIdx. See vmwVmUUID for cross system, unique, persistent identifier.')
vmwVmGuestState = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmGuestState.setStatus('current')
if mibBuilder.loadTexts: vmwVmGuestState.setDescription('Operation mode of guest operating system. Values include: running - Guest is running normally. shuttingdown - Guest has a pending shutdown command. resetting - Guest has a pending reset command. standby - Guest has a pending standby command. notrunning - Guest is not running. unknown - Guest information is not available. VIM Property: guestState MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=guest')
vmwVmCpus = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmCpus.setStatus('current')
if mibBuilder.loadTexts: vmwVmCpus.setDescription('Number of virtual CPUs assigned to this virtual machine. VIM Property: numCPU MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware')
vmwVmUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(36, 72))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmUUID.setStatus('current')
if mibBuilder.loadTexts: vmwVmUUID.setDescription('A unique identifier for this VM. Must be unique across a set of ESX systems managed by an instance of vSphere Center. Example value: 564d95d4-bff7-31fd-f20f-db2d808a8b32 VIM Property: uuid MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config')
vmwVmHbaTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 2), )
if mibBuilder.loadTexts: vmwVmHbaTable.setStatus('current')
if mibBuilder.loadTexts: vmwVmHbaTable.setDescription('Table of host bus adapters (hba) for all vms in vmwVmTable.')
vmwVmHbaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwHbaVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwVmHbaIdx"))
if mibBuilder.loadTexts: vmwVmHbaEntry.setStatus('current')
if mibBuilder.loadTexts: vmwVmHbaEntry.setDescription('Uniquely identifies a given virtual machine host bus adapter.')
vmwHbaVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwHbaVmIdx.setStatus('current')
if mibBuilder.loadTexts: vmwHbaVmIdx.setDescription('This number corresponds to the vmwVmIdx in vmwVmTable.')
vmwVmHbaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmHbaIdx.setStatus('current')
if mibBuilder.loadTexts: vmwVmHbaIdx.setDescription('Uniquely identifies a given Host Bus adapter in this VM. May change across system reboots.')
vmwHbaNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaNum.setStatus('current')
if mibBuilder.loadTexts: vmwHbaNum.setDescription('The name of the hba as it appears in the VM Settings. VIM Property: Virtual Device index of 200-299. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware')
vmwHbaVirtDev = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaVirtDev.setStatus('current')
if mibBuilder.loadTexts: vmwHbaVirtDev.setDescription('The oem host bus adapter hardware being emulated to the Guest OS. MOB: Not visible.')
vmwHbaTgtTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 3), )
if mibBuilder.loadTexts: vmwHbaTgtTable.setStatus('current')
if mibBuilder.loadTexts: vmwHbaTgtTable.setDescription('Table of all virtual disks configured for vms in vmwVmTable.')
vmwHbaTgtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwHbaTgtVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwHbaTgtIdx"))
if mibBuilder.loadTexts: vmwHbaTgtEntry.setStatus('current')
if mibBuilder.loadTexts: vmwHbaTgtEntry.setDescription('Identifies a specific storage disk. Index may change across reboots.')
vmwHbaTgtVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwHbaTgtVmIdx.setStatus('current')
if mibBuilder.loadTexts: vmwHbaTgtVmIdx.setDescription('This number corresponds to vmwVmIdx in vmwVmTable.')
vmwHbaTgtIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwHbaTgtIdx.setStatus('current')
if mibBuilder.loadTexts: vmwHbaTgtIdx.setDescription('This value identifies a particular disk.')
vmwHbaTgtNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHbaTgtNum.setStatus('current')
if mibBuilder.loadTexts: vmwHbaTgtNum.setDescription("Identifies the disk as seen from the host bus controller VIM Property: Virtual Device's with index of 2000-2999,3000-3999. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware")
vmwVmNetTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 4), )
if mibBuilder.loadTexts: vmwVmNetTable.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetTable.setDescription('Table of network adapters (nic) for all vms in vmwVmTable.')
vmwVmNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwVmNetVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwVmNetIdx"))
if mibBuilder.loadTexts: vmwVmNetEntry.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetEntry.setDescription('Identifies a particular nic for the specified vmwVmIdx')
vmwVmNetVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmNetVmIdx.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetVmIdx.setDescription('This number corresponds to vmwVmIdx in vmwVmTable.')
vmwVmNetIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwVmNetIdx.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetIdx.setDescription('Identifies a unique network adapter in this table. Not guaranteed to be the same across system reboots.')
vmwVmNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetNum.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetNum.setDescription("The name of the device as it appears in the VM Settings. VIM Property: Virtual Device's with index of 4000-4999. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware")
vmwVmNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetName.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetName.setDescription("What this virutal nic is connected to such as a virtual switch portgroup identifier. VIM Property: Virtual Device's with index of 4000-4999. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware then select property 'backing' to how this nic connects. If no backing was defined by operator, string will start with W: If unavailable, string will start with E:")
vmwVmNetConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetConnType.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVmNetConnType.setDescription('Do not use this value, and should an agent return it discard it.')
vmwVmNetConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 6), VmwConnectedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmNetConnected.setStatus('current')
if mibBuilder.loadTexts: vmwVmNetConnected.setDescription("Reports 'true' if the ethernet virtual device is connected to the virtual machine.")
vmwVmMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwVmMAC.setStatus('current')
if mibBuilder.loadTexts: vmwVmMAC.setDescription("Reports the configured virtual hardware MAC address. If VMware Tools is not running, or VM has not yet been powered on for the first time and mac is to be generated by VM then the value is zero'd out/empty. VIM Property: Virtual Device's with index of 4000-4999. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware")
vmwFloppyTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 5), )
if mibBuilder.loadTexts: vmwFloppyTable.setStatus('current')
if mibBuilder.loadTexts: vmwFloppyTable.setDescription('Table of floppy drives for all vms in vmwVmTable.')
vmwFloppyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwFdVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwFdIdx"))
if mibBuilder.loadTexts: vmwFloppyEntry.setStatus('current')
if mibBuilder.loadTexts: vmwFloppyEntry.setDescription('Identifies one specific floppy device. May change across system reboots.')
vmwFdVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwFdVmIdx.setStatus('current')
if mibBuilder.loadTexts: vmwFdVmIdx.setDescription('This number corresponds to vmwVmIdx in vmwVmTable.')
vmwFdIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwFdIdx.setStatus('current')
if mibBuilder.loadTexts: vmwFdIdx.setDescription('Identifies one specific virtual floppy device.')
vmwFdName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwFdName.setStatus('current')
if mibBuilder.loadTexts: vmwFdName.setDescription("File or Device that this device is connected to, example /dev/fd0. VIM Property: Virtual Device's with index of 8000-8999. MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware If no backing was defined by operator, string will start with W: If unavailable, string will start with E:")
vmwFdConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 4), VmwConnectedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwFdConnected.setStatus('current')
if mibBuilder.loadTexts: vmwFdConnected.setDescription("Reports 'true' if the floppy drive virtual device is connected to the virtual machine.")
vmwCdromTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 2, 6), )
if mibBuilder.loadTexts: vmwCdromTable.setStatus('current')
if mibBuilder.loadTexts: vmwCdromTable.setDescription('Table of DVD or CDROM drives for all vms in vmwVmTable.')
vmwCdromEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1), ).setIndexNames((0, "VMWARE-VMINFO-MIB", "vmwCdVmIdx"), (0, "VMWARE-VMINFO-MIB", "vmwCdromIdx"))
if mibBuilder.loadTexts: vmwCdromEntry.setStatus('current')
if mibBuilder.loadTexts: vmwCdromEntry.setDescription('Identifies a specific DVD or CDROM drive. Value may change across system reboots.')
vmwCdVmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwCdVmIdx.setStatus('current')
if mibBuilder.loadTexts: vmwCdVmIdx.setDescription('This number corresponds to the vmwVmIdx the vmwVmTable.')
vmwCdromIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vmwCdromIdx.setStatus('current')
if mibBuilder.loadTexts: vmwCdromIdx.setDescription('Identifies the specific DVD or CDROM drive.')
vmwCdromName = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwCdromName.setStatus('current')
if mibBuilder.loadTexts: vmwCdromName.setDescription("Reports the iso or device this virtual drive has been configured to use VIM Property: Virtual Device's with index of 3000-3999 (same as disks) MOB: https://esx.example.com/mob/?moid=vmwVmIdx&doPath=config%2ehardware then select property 'backing' to how this cdrom connects. If no backing was defined by operator, string will start with W: If unavailable, string will start with E:")
vmwCdromConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 4), VmwConnectedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwCdromConnected.setStatus('current')
if mibBuilder.loadTexts: vmwCdromConnected.setDescription('Reports true if the dvd/cdrom is connected to the virtual machine.')
vmwVmID = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 101), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVmID.setStatus('current')
if mibBuilder.loadTexts: vmwVmID.setDescription('This holds the same value as vmwVmVMID of the affected vm generating the trap. to allow polling of the affected vm in vmwVmTable.')
vmwVmConfigFilePath = MibScalar((1, 3, 6, 1, 4, 1, 6876, 50, 102), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVmConfigFilePath.setStatus('current')
if mibBuilder.loadTexts: vmwVmConfigFilePath.setDescription('This is the path to the config file of the affected vm generating the trap and is same as vmwVmTable vmwVmConfigFile. It is expressed as POSIX pathname.')
vmwVmPoweredOn = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 1)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmPoweredOn.setStatus('current')
if mibBuilder.loadTexts: vmwVmPoweredOn.setDescription('This trap is sent when a virtual machine is powered on from a suspended or a powered off state. The origin of this event can be several: for instance may be operator initiated, existing vmx process reconnects to control subsystem. NOTE: vms powered up due to VMotion are not reported. Upon receiving this notification client applications should poll the vmwVmTable to obtain current status.')
vmwVmPoweredOff = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmPoweredOff.setStatus('current')
if mibBuilder.loadTexts: vmwVmPoweredOff.setDescription('This trap is sent when a virtual machine is powered off. The origin of this event can be several: for instance may be operator initiated, vmx process terminating abnormally. NOTE: vms powered down due to VMotion are not reported. Upon receiving this notification client applications should poll the vmwVmTable to obtain current status.')
vmwVmHBLost = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 3)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmHBLost.setStatus('current')
if mibBuilder.loadTexts: vmwVmHBLost.setDescription('This trap is sent when a virtual machine detects a loss in guest heartbeat. The Guest heartbeat is only sent if VMware Tools are installed in the Guest OS. Control process will send this event whenever it determines the number of guest heartbeats for a given period of time have not been received. Upon receiving this notification client applications should poll the vmwVmTable to obtain current status.')
vmwVmHBDetected = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 4)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmHBDetected.setStatus('current')
if mibBuilder.loadTexts: vmwVmHBDetected.setDescription('This trap is sent when a virtual machine detects or regains the required number of guest heartbeats for a given period of time. This is only sent if VMware tools are installed in the Guest OS. Upon receiving this notification client applications should poll the vmwVmTable to obtain current status.')
vmwVmSuspended = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 5)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
if mibBuilder.loadTexts: vmwVmSuspended.setStatus('current')
if mibBuilder.loadTexts: vmwVmSuspended.setDescription('This trap is sent when a virtual machine is suspended. The origin of this event may be several: operator initiated, by software api clients, and by other means. Upon receiving this notification client applications should poll the vmwVmTable to obtain current status.')
vmwVmInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2))
vmwVmInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 1))
vmwVmInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2))
vmwResMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 1, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmInfoGroup"), ("VMWARE-VMINFO-MIB", "vmwVmInfoNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwResMIBBasicCompliance = vmwResMIBBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: vmwResMIBBasicCompliance.setDescription('The compliance statement for entities which implement the VMWARE-RESOURCE-MIB.')
vmwVmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 1)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmDisplayName"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFile"), ("VMWARE-VMINFO-MIB", "vmwVmGuestOS"), ("VMWARE-VMINFO-MIB", "vmwVmMemSize"), ("VMWARE-VMINFO-MIB", "vmwVmState"), ("VMWARE-VMINFO-MIB", "vmwVmGuestState"), ("VMWARE-VMINFO-MIB", "vmwHbaNum"), ("VMWARE-VMINFO-MIB", "vmwHbaVirtDev"), ("VMWARE-VMINFO-MIB", "vmwHbaTgtNum"), ("VMWARE-VMINFO-MIB", "vmwVmNetNum"), ("VMWARE-VMINFO-MIB", "vmwVmNetName"), ("VMWARE-VMINFO-MIB", "vmwVmNetConnected"), ("VMWARE-VMINFO-MIB", "vmwVmMAC"), ("VMWARE-VMINFO-MIB", "vmwFdName"), ("VMWARE-VMINFO-MIB", "vmwFdConnected"), ("VMWARE-VMINFO-MIB", "vmwCdromName"), ("VMWARE-VMINFO-MIB", "vmwCdromConnected"), ("VMWARE-VMINFO-MIB", "vmwVmID"), ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"), ("VMWARE-VMINFO-MIB", "vmwVmCpus"), ("VMWARE-VMINFO-MIB", "vmwVmUUID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVmInfoGroup = vmwVmInfoGroup.setStatus('current')
if mibBuilder.loadTexts: vmwVmInfoGroup.setDescription('These objects provide virtual machine details.')
vmwVmInfoNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 2)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmPoweredOn"), ("VMWARE-VMINFO-MIB", "vmwVmPoweredOff"), ("VMWARE-VMINFO-MIB", "vmwVmHBLost"), ("VMWARE-VMINFO-MIB", "vmwVmHBDetected"), ("VMWARE-VMINFO-MIB", "vmwVmSuspended"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVmInfoNotificationGroup = vmwVmInfoNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vmwVmInfoNotificationGroup.setDescription('Group of objects describing notifications (traps).')
vmwVmObsoleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 3)).setObjects(("VMWARE-VMINFO-MIB", "vmwVmVMID"), ("VMWARE-VMINFO-MIB", "vmwVmNetConnType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVmObsoleteGroup = vmwVmObsoleteGroup.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVmObsoleteGroup.setDescription('Managed objects that should not be used.')
mibBuilder.exportSymbols("VMWARE-VMINFO-MIB", vmwCdromEntry=vmwCdromEntry, vmwCdromConnected=vmwCdromConnected, vmwVmSuspended=vmwVmSuspended, vmwVmVMID=vmwVmVMID, vmwVmConfigFilePath=vmwVmConfigFilePath, vmwVmInfoMIBConformance=vmwVmInfoMIBConformance, vmwCdromTable=vmwCdromTable, vmwVmMemSize=vmwVmMemSize, vmwVmNetNum=vmwVmNetNum, vmwHbaTgtVmIdx=vmwHbaTgtVmIdx, vmwHbaNum=vmwHbaNum, vmwVmNetName=vmwVmNetName, vmwVmInfoNotificationGroup=vmwVmInfoNotificationGroup, vmwVmInfoGroup=vmwVmInfoGroup, vmwHbaTgtIdx=vmwHbaTgtIdx, vmwHbaTgtTable=vmwHbaTgtTable, vmwFdName=vmwFdName, vmwVmHbaEntry=vmwVmHbaEntry, vmwVmInfoMIBGroups=vmwVmInfoMIBGroups, vmwVmEntry=vmwVmEntry, PYSNMP_MODULE_ID=vmwVmInfoMIB, vmwVmNetConnType=vmwVmNetConnType, vmwVmNetEntry=vmwVmNetEntry, vmwCdromName=vmwCdromName, vmwVmHBDetected=vmwVmHBDetected, vmwResMIBBasicCompliance=vmwResMIBBasicCompliance, vmwVmInfoMIB=vmwVmInfoMIB, vmwVmUUID=vmwVmUUID, vmwVmHbaTable=vmwVmHbaTable, vmwVmNetIdx=vmwVmNetIdx, vmwVmGuestState=vmwVmGuestState, vmwVmNetConnected=vmwVmNetConnected, vmwVmID=vmwVmID, vmwVmTable=vmwVmTable, vmwVmGuestOS=vmwVmGuestOS, vmwVmMAC=vmwVmMAC, vmwFloppyTable=vmwFloppyTable, vmwFdIdx=vmwFdIdx, vmwHbaVirtDev=vmwHbaVirtDev, vmwVmPoweredOff=vmwVmPoweredOff, vmwHbaTgtNum=vmwHbaTgtNum, vmwHbaTgtEntry=vmwHbaTgtEntry, vmwFloppyEntry=vmwFloppyEntry, vmwVmIdx=vmwVmIdx, vmwVmDisplayName=vmwVmDisplayName, vmwVmHbaIdx=vmwVmHbaIdx, vmwVmState=vmwVmState, vmwCdVmIdx=vmwCdVmIdx, vmwFdConnected=vmwFdConnected, vmwCdromIdx=vmwCdromIdx, vmwHbaVmIdx=vmwHbaVmIdx, vmwVmNetVmIdx=vmwVmNetVmIdx, vmwVmObsoleteGroup=vmwVmObsoleteGroup, vmwFdVmIdx=vmwFdVmIdx, vmwVmHBLost=vmwVmHBLost, vmwVmPoweredOn=vmwVmPoweredOn, vmwVmCpus=vmwVmCpus, vmwVmConfigFile=vmwVmConfigFile, vmwVmInfoMIBCompliances=vmwVmInfoMIBCompliances, vmwVmNetTable=vmwVmNetTable)
