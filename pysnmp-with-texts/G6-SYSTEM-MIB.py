#
# PySNMP MIB module G6-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/G6-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
g6, = mibBuilder.importSymbols("MICROSENS-G6-MIB", "g6")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, enterprises, Counter64, Unsigned32, IpAddress, Counter32, NotificationType, MibIdentifier, iso, TimeTicks, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "enterprises", "Counter64", "Unsigned32", "IpAddress", "Counter32", "NotificationType", "MibIdentifier", "iso", "TimeTicks", "ObjectIdentity", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
device = ModuleIdentity((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1))
device.setRevisions(('2015-05-22 10:59',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: device.setRevisionsDescriptions(('File creation',))
if mibBuilder.loadTexts: device.setLastUpdated('201505221059Z')
if mibBuilder.loadTexts: device.setOrganization('MICROSENS GmbH & Co. KG')
if mibBuilder.loadTexts: device.setContactInfo('Kueferstrasse 16 D-59067 Hamm Germany support@microsens.de http://www.microsens.de')
if mibBuilder.loadTexts: device.setDescription('Microsens private MIB for Generation 6 Ethernet Switches')
system = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30))
systemShowTimeDate = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemShowTimeDate.setStatus('current')
if mibBuilder.loadTexts: systemShowTimeDate.setDescription('Show system time and date.')
systemSetTime = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSetTime.setStatus('current')
if mibBuilder.loadTexts: systemSetTime.setDescription('Sets the system clock (time only). Syntax: 12:30:00')
systemSetDate = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSetDate.setStatus('current')
if mibBuilder.loadTexts: systemSetDate.setDescription('Sets the system clock (date only). Syntax: 2012-12-24')
systemShowUtilization = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemShowUtilization.setStatus('current')
if mibBuilder.loadTexts: systemShowUtilization.setDescription('Show CPU status information')
systemRebootDevice = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemRebootDevice.setStatus('current')
if mibBuilder.loadTexts: systemRebootDevice.setDescription('This command will restart the device. All communication will be disrupted! Syntax: reboot_device = CONFIRM.')
systemCreateSnapshot = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemCreateSnapshot.setStatus('current')
if mibBuilder.loadTexts: systemCreateSnapshot.setDescription('Creates a snapshot of all relevant configuration and status information packaged as a single tar archieve. This file can be found in service/snapshot.')
systemSendWakeOnLanPacket = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSendWakeOnLanPacket.setStatus('current')
if mibBuilder.loadTexts: systemSendWakeOnLanPacket.setDescription('This command will send a magic packet to wake up a selected sleeping device. The device is identified by its MAC address. Syntax: send_wake_on_lan_packet = 00:11:22:44:55:66.')
systemAlternativeMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 8), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAlternativeMacAddress.setStatus('current')
if mibBuilder.loadTexts: systemAlternativeMacAddress.setDescription('This field is usually empty. This field may be used to override the MAC address fixed in the factory setting. NOTE: This value is read only after a reset!')
systemBootPreference = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sdCardFirst", 0), ("internalFirst", 1), ("sdCardOnly", 2), ("internalOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemBootPreference.setStatus('current')
if mibBuilder.loadTexts: systemBootPreference.setDescription('This feature only applies to devices that feature internal memory plus plugged-in SD cards. It defines which software is used after reboot.')
systemInventory = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemInventory.setStatus('current')
if mibBuilder.loadTexts: systemInventory.setDescription('Inventory string free for customer use. Up to 512 character are accepted. Note this config is linked to the SD card and may change when config or SD card is exchanged. For an inventory that is fixed to the hardware use device.system.set_factory_inventory command.')
systemAutorunCliScript = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAutorunCliScript.setStatus('current')
if mibBuilder.loadTexts: systemAutorunCliScript.setDescription('Optional cli scripts executed after power sequence is completed. Several scripts may be assigned, with comma or blank separation.')
systemLocalConsole = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemLocalConsole.setStatus('current')
if mibBuilder.loadTexts: systemLocalConsole.setDescription('When set to disabled the local serial console port is disabled. Local access via serial cable is blocked. While this enhances local protection it also closes the emergency access should the device become inaccessible over the network due to misconfiguration. The port is also set to disabled, when serial port extension hardware is installed.')
systemPermitDebugAccess = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemPermitDebugAccess.setStatus('current')
if mibBuilder.loadTexts: systemPermitDebugAccess.setDescription('When enabled it is possible to log into the system for debug purposes. This includes telnet/ssh, as well as web and file transfer protocols. To protect the system from unauthorized access it is strongly advised to disable this feature unless instructed by authorized service personnel. NOTE: To ensure that any possibly pending debug access is terminated reboot the device after setting this parameter to disabled.')
systemPermitIncomingAlerts = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemPermitIncomingAlerts.setStatus('current')
if mibBuilder.loadTexts: systemPermitIncomingAlerts.setDescription('When enabled it is possible receive alerts via from external devices via SNMP or HTTP(S). This feature may be used in combination with custom scripting to react to external events. To protect the system from unauthorized spam it is advised to disable this feature unless there is an application for it.')
scriptScheduleTable = MibTable((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15), )
if mibBuilder.loadTexts: scriptScheduleTable.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleTable.setDescription('This dynamic table permits the setup of automated script execution based on precise time scheduling definition. Any number of scripts may be executed at any desired interval or at selected dates. Please ensure the time and date are properly set (via NTP) when using this feature.')
scriptScheduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1), ).setIndexNames((0, "G6-SYSTEM-MIB", "scriptScheduleIndex"))
if mibBuilder.loadTexts: scriptScheduleEntry.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleEntry.setDescription('')
scriptScheduleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)))
if mibBuilder.loadTexts: scriptScheduleIndex.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleIndex.setDescription('Automatically generated')
scriptScheduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleName.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleName.setDescription('Unique name to reference this entry and to remember whose MAC address is entered.')
scriptScheduleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleMode.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleMode.setDescription('When set to disabled this entry is ignored. It is recommended to first set the mode to disabled before the associated time values are modified. When all values are properly set re-enable the entry.')
scriptScheduleCliScript = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleCliScript.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleCliScript.setDescription('Enter the name of the cli script that should be executed when the defined time occurs. Ensure that the script name selects a valid file. Several scripts may be assigned, with comma or blank separation.')
scriptScheduleMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleMinutes.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleMinutes.setDescription('Format: 3,14 select exact minutes hour:03 and hour:14. * is every minute. */5 defines every five minutes.')
scriptScheduleHours = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleHours.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleHours.setDescription('Format: 0-23. Range and comma separation is permitted. * is every hour.')
scriptScheduleDays = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleDays.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleDays.setDescription('Format: 1-31. Range and comma separation is permitted. * is every day.')
scriptScheduleMonths = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleMonths.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleMonths.setDescription('Format: 1-12 or Jan-Dec. Range and comma separation is permitted. * is every month.')
scriptScheduleWeekdays = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scriptScheduleWeekdays.setStatus('current')
if mibBuilder.loadTexts: scriptScheduleWeekdays.setDescription('Format: 0-6 or Sun-Sat. Range and comma separation is permitted. * is every day.')
systemLastBootTime = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 100), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemLastBootTime.setStatus('current')
if mibBuilder.loadTexts: systemLastBootTime.setDescription('The time and date when this device has booted.')
systemUptime = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 101), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUptime.setStatus('current')
if mibBuilder.loadTexts: systemUptime.setDescription('Uptime since last reboot in seconds.')
systemUsedMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 102), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUsedMacAddress.setStatus('current')
if mibBuilder.loadTexts: systemUsedMacAddress.setDescription('Contains the mac address used by this unit. Usually follows to MAC defined in the factory setting, but may be overwritten by the alternative_mac_address.')
systemUsedBootMedia = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 103), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("sdCard", 0), ("internalMemory", 1), ("nfs", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUsedBootMedia.setStatus('current')
if mibBuilder.loadTexts: systemUsedBootMedia.setDescription('')
systemTemperature = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 104), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTemperature.setStatus('current')
if mibBuilder.loadTexts: systemTemperature.setDescription('Temperature value in centigrade.')
systemClimateLevel = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 105), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("criticalLow", 1), ("low", 2), ("normal", 3), ("increased", 4), ("high", 5), ("criticalHigh", 6), ("shutdown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemClimateLevel.setStatus('current')
if mibBuilder.loadTexts: systemClimateLevel.setDescription('Annotated temperature level.')
firmwareTable = MibTable((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106), )
if mibBuilder.loadTexts: firmwareTable.setStatus('current')
if mibBuilder.loadTexts: firmwareTable.setDescription('This section provides details about the running firmware.')
firmwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1), ).setIndexNames((0, "G6-SYSTEM-MIB", "firmwareIndex"))
if mibBuilder.loadTexts: firmwareEntry.setStatus('current')
if mibBuilder.loadTexts: firmwareEntry.setDescription('')
firmwareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0)))
if mibBuilder.loadTexts: firmwareIndex.setStatus('current')
if mibBuilder.loadTexts: firmwareIndex.setDescription('Automatically generated')
firmwareRunningVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareRunningVersion.setStatus('current')
if mibBuilder.loadTexts: firmwareRunningVersion.setDescription('Running firmware version.')
firmwareBuildDate = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareBuildDate.setStatus('current')
if mibBuilder.loadTexts: firmwareBuildDate.setDescription('Build date of the running firmware. Format: 2012-01-18 12:00:22.')
firmwareBuildNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareBuildNumber.setStatus('current')
if mibBuilder.loadTexts: firmwareBuildNumber.setDescription('Build number of the running firmware retrieved from the repository.')
saveInfoTable = MibTable((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107), )
if mibBuilder.loadTexts: saveInfoTable.setStatus('current')
if mibBuilder.loadTexts: saveInfoTable.setDescription('This section provided status information about the internal parameter saving process.')
saveInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1), ).setIndexNames((0, "G6-SYSTEM-MIB", "saveInfoIndex"))
if mibBuilder.loadTexts: saveInfoEntry.setStatus('current')
if mibBuilder.loadTexts: saveInfoEntry.setDescription('')
saveInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0)))
if mibBuilder.loadTexts: saveInfoIndex.setStatus('current')
if mibBuilder.loadTexts: saveInfoIndex.setDescription('Automatically generated')
saveInfoLastSavedParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saveInfoLastSavedParameter.setStatus('current')
if mibBuilder.loadTexts: saveInfoLastSavedParameter.setDescription('Records the last written parameter.')
saveInfoWriteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("nothingToSave", 0), ("processing", 1), ("savedToRam", 2), ("savedToSdcard", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saveInfoWriteStatus.setStatus('current')
if mibBuilder.loadTexts: saveInfoWriteStatus.setDescription('Indicates if writing was succcessful.')
saveInfoTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saveInfoTimeStamp.setStatus('current')
if mibBuilder.loadTexts: saveInfoTimeStamp.setDescription('Records the time the write status was last changed.')
mibBuilder.exportSymbols("G6-SYSTEM-MIB", system=system, scriptScheduleEntry=scriptScheduleEntry, scriptScheduleDays=scriptScheduleDays, systemClimateLevel=systemClimateLevel, device=device, systemShowUtilization=systemShowUtilization, systemCreateSnapshot=systemCreateSnapshot, scriptScheduleWeekdays=scriptScheduleWeekdays, systemLastBootTime=systemLastBootTime, saveInfoEntry=saveInfoEntry, systemInventory=systemInventory, systemLocalConsole=systemLocalConsole, scriptScheduleMinutes=scriptScheduleMinutes, systemPermitIncomingAlerts=systemPermitIncomingAlerts, PYSNMP_MODULE_ID=device, scriptScheduleIndex=scriptScheduleIndex, systemUsedMacAddress=systemUsedMacAddress, systemBootPreference=systemBootPreference, saveInfoWriteStatus=saveInfoWriteStatus, scriptScheduleHours=scriptScheduleHours, scriptScheduleName=scriptScheduleName, firmwareBuildNumber=firmwareBuildNumber, systemShowTimeDate=systemShowTimeDate, firmwareTable=firmwareTable, systemSetDate=systemSetDate, firmwareIndex=firmwareIndex, saveInfoTimeStamp=saveInfoTimeStamp, firmwareEntry=firmwareEntry, systemTemperature=systemTemperature, scriptScheduleTable=scriptScheduleTable, saveInfoTable=saveInfoTable, systemRebootDevice=systemRebootDevice, systemAutorunCliScript=systemAutorunCliScript, scriptScheduleMonths=scriptScheduleMonths, scriptScheduleMode=scriptScheduleMode, scriptScheduleCliScript=scriptScheduleCliScript, systemSendWakeOnLanPacket=systemSendWakeOnLanPacket, systemAlternativeMacAddress=systemAlternativeMacAddress, firmwareBuildDate=firmwareBuildDate, firmwareRunningVersion=firmwareRunningVersion, saveInfoLastSavedParameter=saveInfoLastSavedParameter, systemPermitDebugAccess=systemPermitDebugAccess, systemSetTime=systemSetTime, saveInfoIndex=saveInfoIndex, systemUsedBootMedia=systemUsedBootMedia, systemUptime=systemUptime)
