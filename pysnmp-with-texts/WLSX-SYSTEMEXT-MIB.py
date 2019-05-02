#
# PySNMP MIB module WLSX-SYSTEMEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WLSX-SYSTEMEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ArubaSwitchRole, ArubaCardType, ArubaActiveState = mibBuilder.importSymbols("ARUBA-TC", "ArubaSwitchRole", "ArubaCardType", "ArubaActiveState")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, Bits, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, NotificationType, TextualConvention, iso, Integer32, snmpModules, ObjectIdentity, Counter64, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "NotificationType", "TextualConvention", "iso", "Integer32", "snmpModules", "ObjectIdentity", "Counter64", "MibIdentifier", "Gauge32")
TAddress, RowStatus, TruthValue, PhysAddress, TDomain, DisplayString, MacAddress, StorageType, TextualConvention, TimeInterval, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "RowStatus", "TruthValue", "PhysAddress", "TDomain", "DisplayString", "MacAddress", "StorageType", "TextualConvention", "TimeInterval", "TestAndIncr")
wlsxSystemExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2))
wlsxSystemExtMIB.setRevisions(('1908-12-11 21:08',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wlsxSystemExtMIB.setRevisionsDescriptions(('The initial revision.',))
if mibBuilder.loadTexts: wlsxSystemExtMIB.setLastUpdated('0812112108Z')
if mibBuilder.loadTexts: wlsxSystemExtMIB.setOrganization('Aruba Wireless Networks')
if mibBuilder.loadTexts: wlsxSystemExtMIB.setContactInfo('Postal: 1322 Crossman Avenue Sunnyvale, CA 94089 E-mail: dl-support@arubanetworks.com Phone: +1 408 227 4500')
if mibBuilder.loadTexts: wlsxSystemExtMIB.setDescription('This MIB module defines MIB objects which provide System level information about the Aruba controller.')
wlsxSystemExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1))
wlsxSystemExtTableGenNumberGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2))
wlsxSysExtSwitchIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchIp.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchIp.setDescription('Controller IP as configured by the user. This IP address uniquely identifies the controller.')
wlsxSysExtHostname = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtHostname.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtHostname.setDescription('Name of the controller.')
wlsxSysExtModelName = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtModelName.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtModelName.setDescription('Model Name of the controller.')
wlsxSysExtSwitchRole = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 4), ArubaSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchRole.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchRole.setDescription('Role of this controller in the Aruba Domain.')
wlsxSysExtSwitchMasterIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchMasterIp.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchMasterIp.setDescription(' Switch IP of the master controller. ')
wlsxSysExtSwitchDate = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxSysExtSwitchDate.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchDate.setDescription(' System notion of the local date and time of day. ')
wlsxSysExtSwitchBaseMacaddress = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchBaseMacaddress.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchBaseMacaddress.setDescription(' The Base MAC address of the controller. ')
wlsxSysExtFanTrayAssemblyNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtFanTrayAssemblyNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtFanTrayAssemblyNumber.setDescription(' Assembly number of the Fan tray. ')
wlsxSysExtFanTraySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtFanTraySerialNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtFanTraySerialNumber.setDescription(' Serial number of the Fan tray ')
wlsxSysExtInternalTemparature = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtInternalTemparature.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtInternalTemparature.setDescription(' Internal temperature in the controller. ')
wlsxSysExtLicenseSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLicenseSerialNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtLicenseSerialNumber.setDescription(' The license serial number of the controller. ')
wlsxSysExtSwitchLicenseCount = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseCount.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseCount.setDescription(' The number of licenses installed on the controller ')
wlsxSysExtProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13), )
if mibBuilder.loadTexts: wlsxSysExtProcessorTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtProcessorTable.setDescription(' The table of processors contained by the controller. ')
wlsxSysExtProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtProcessorID"))
if mibBuilder.loadTexts: wlsxSysExtProcessorEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtProcessorEntry.setDescription(' An entry for one processor contained by the controller. ')
sysExtProcessorID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtProcessorID.setStatus('current')
if mibBuilder.loadTexts: sysExtProcessorID.setDescription(' Processor Index. ')
sysExtProcessorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtProcessorDescr.setStatus('current')
if mibBuilder.loadTexts: sysExtProcessorDescr.setDescription(' Description of the processor. ')
sysExtProcessorLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtProcessorLoad.setStatus('current')
if mibBuilder.loadTexts: sysExtProcessorLoad.setDescription(' The average, over the last minute, of the percentage of time that this processor was not idle. ')
wlsxSysExtStorageTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14), )
if mibBuilder.loadTexts: wlsxSysExtStorageTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtStorageTable.setDescription(' The table of Storage-devices contained by the controller. ')
wlsxSysExtStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtStorageIndex"))
if mibBuilder.loadTexts: wlsxSysExtStorageEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtStorageEntry.setDescription(' An entry for one long-term storage device contained by the controller. ')
sysExtStorageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtStorageIndex.setStatus('current')
if mibBuilder.loadTexts: sysExtStorageIndex.setDescription(' Index into the table. ')
sysExtStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ram", 1), ("flashMemory", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageType.setStatus('current')
if mibBuilder.loadTexts: sysExtStorageType.setDescription(' Type of the storage. ')
sysExtStorageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageSize.setStatus('current')
if mibBuilder.loadTexts: sysExtStorageSize.setDescription(' Total size of the storage filesystem in MB. ')
sysExtStorageUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageUsed.setStatus('current')
if mibBuilder.loadTexts: sysExtStorageUsed.setDescription(' Used Storage in MB. ')
sysExtStorageName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageName.setStatus('current')
if mibBuilder.loadTexts: sysExtStorageName.setDescription(' Name of the storage filesystem. ')
wlsxSysExtMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15), )
if mibBuilder.loadTexts: wlsxSysExtMemoryTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtMemoryTable.setDescription(' The memory status of the controller ')
wlsxSysExtMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtMemoryIndex"))
if mibBuilder.loadTexts: wlsxSysExtMemoryEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtMemoryEntry.setDescription(' An entry for one memory region on the controller. Currently, only the control processor memory is monitored. ')
sysExtMemoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtMemoryIndex.setStatus('current')
if mibBuilder.loadTexts: sysExtMemoryIndex.setDescription(' Index into the table. ')
sysExtMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemorySize.setStatus('current')
if mibBuilder.loadTexts: sysExtMemorySize.setDescription(' Total memory in KB. ')
sysExtMemoryUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemoryUsed.setStatus('current')
if mibBuilder.loadTexts: sysExtMemoryUsed.setDescription(' Used memory in KB. ')
sysExtMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemoryFree.setStatus('current')
if mibBuilder.loadTexts: sysExtMemoryFree.setDescription(' Free memory in KB. ')
wlsxSysExtCardTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16), )
if mibBuilder.loadTexts: wlsxSysExtCardTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtCardTable.setDescription(' The table of Hardware modules in the controller. ')
wlsxSysExtCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtCardSlot"))
if mibBuilder.loadTexts: wlsxSysExtCardEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtCardEntry.setDescription(' An entry for one Hardware Module in the controller. ')
sysExtCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtCardSlot.setStatus('current')
if mibBuilder.loadTexts: sysExtCardSlot.setDescription(' Slot in which this card is located, offset by one. For the user-visible slot number see sysExtCardUserSlot ')
sysExtCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 2), ArubaCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardType.setStatus('current')
if mibBuilder.loadTexts: sysExtCardType.setDescription(' Type of the Card. ')
sysExtCardNumOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfPorts.setStatus('current')
if mibBuilder.loadTexts: sysExtCardNumOfPorts.setDescription(' Number of data ports on the card. ')
sysExtCardNumOfFastethernetPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfFastethernetPorts.setStatus('current')
if mibBuilder.loadTexts: sysExtCardNumOfFastethernetPorts.setDescription(' Number of Fastethernet ports on the card. ')
sysExtCardNumOfGigPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfGigPorts.setStatus('current')
if mibBuilder.loadTexts: sysExtCardNumOfGigPorts.setDescription(' Number of Gigabit ethernet ports on the card. ')
sysExtCardSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardSerialNo.setStatus('current')
if mibBuilder.loadTexts: sysExtCardSerialNo.setDescription(' Serial number of the card. ')
sysExtCardAssemblyNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardAssemblyNo.setStatus('current')
if mibBuilder.loadTexts: sysExtCardAssemblyNo.setDescription(' Assembly Number of the card. ')
sysExtCardManufacturingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardManufacturingDate.setStatus('current')
if mibBuilder.loadTexts: sysExtCardManufacturingDate.setDescription(' Card manufacturing date. ')
sysExtCardHwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardHwRevision.setStatus('current')
if mibBuilder.loadTexts: sysExtCardHwRevision.setDescription(' Hardware revision of the card. ')
sysExtCardFpgaRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardFpgaRevision.setStatus('current')
if mibBuilder.loadTexts: sysExtCardFpgaRevision.setDescription(' Fpga revision number. ')
sysExtCardSwitchChip = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardSwitchChip.setStatus('current')
if mibBuilder.loadTexts: sysExtCardSwitchChip.setDescription(' Switching Chip version. ')
sysExtCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 12), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardStatus.setStatus('current')
if mibBuilder.loadTexts: sysExtCardStatus.setDescription(' Status of the card. ')
sysExtCardUserSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardUserSlot.setStatus('current')
if mibBuilder.loadTexts: sysExtCardUserSlot.setDescription(' User-visible (zero-based) slot number. ')
wlsxSysExtFanTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17), )
if mibBuilder.loadTexts: wlsxSysExtFanTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtFanTable.setDescription(' The table of all supported fans in the controller. Not supported in Aruba 200/800 and 2400 controllers. ')
wlsxSysExtFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtFanIndex"))
if mibBuilder.loadTexts: wlsxSysExtFanEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtFanEntry.setDescription(' An entry for one fan. ')
sysExtFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtFanIndex.setStatus('current')
if mibBuilder.loadTexts: sysExtFanIndex.setDescription(' Index into the table. ')
sysExtFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 2), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtFanStatus.setStatus('current')
if mibBuilder.loadTexts: sysExtFanStatus.setDescription(' Status of the Fan. ')
wlsxSysExtPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18), )
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyTable.setDescription(' The table of all supported Power supplies in the controller. Not supported in Aruba 200, 800 and 2400 controllers. ')
wlsxSysExtPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtPowerSupplyIndex"))
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyEntry.setDescription(' An entry for one power supply. ')
sysExtPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtPowerSupplyIndex.setStatus('current')
if mibBuilder.loadTexts: sysExtPowerSupplyIndex.setDescription(' Index into the table. ')
sysExtPowerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 2), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtPowerSupplyStatus.setStatus('current')
if mibBuilder.loadTexts: sysExtPowerSupplyStatus.setDescription(' Status of the power supply. ')
wlsxSysExtSwitchListTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19), )
if mibBuilder.loadTexts: wlsxSysExtSwitchListTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchListTable.setDescription('This Table will list all the controllers in the Aruba Domain. It will be populated only on the master controller. Local controllers return empty table. ')
wlsxSysExtSwitchListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtSwitchIPAddress"))
if mibBuilder.loadTexts: wlsxSysExtSwitchListEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchListEntry.setDescription('Switch List Entry')
sysExtSwitchIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 1), IpAddress())
if mibBuilder.loadTexts: sysExtSwitchIPAddress.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchIPAddress.setDescription(' IP Address of the controller. ')
sysExtSwitchRole = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 2), ArubaSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchRole.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchRole.setDescription(' Role of the controller. ')
sysExtSwitchLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchLocation.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchLocation.setDescription(' Location of the controller ')
sysExtSwitchSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchSWVersion.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchSWVersion.setDescription(' Software version the controller is running. ')
sysExtSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 5), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchStatus.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchStatus.setDescription(' Status of the controller. ')
sysExtSwitchName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchName.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchName.setDescription(' Host name of the controller. ')
sysExtSwitchSerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchSerNo.setStatus('current')
if mibBuilder.loadTexts: sysExtSwitchSerNo.setDescription(' Serial number of the controller. ')
wlsxSysExtSwitchLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20), )
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseTable.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseTable.setDescription('This table lists all licenses installed on the controller. ')
wlsxSysExtLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtLicenseIndex"))
if mibBuilder.loadTexts: wlsxSysExtLicenseEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtLicenseEntry.setDescription('License Entry')
sysExtLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtLicenseIndex.setStatus('current')
if mibBuilder.loadTexts: sysExtLicenseIndex.setDescription(' License ID number ')
sysExtLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseKey.setStatus('current')
if mibBuilder.loadTexts: sysExtLicenseKey.setDescription(' License Key ')
sysExtLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseInstalled.setStatus('current')
if mibBuilder.loadTexts: sysExtLicenseInstalled.setDescription(' License installation time ')
sysExtLicenseExpires = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseExpires.setStatus('current')
if mibBuilder.loadTexts: sysExtLicenseExpires.setDescription(' License expiry time ')
sysExtLicenseFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseFlags.setStatus('current')
if mibBuilder.loadTexts: sysExtLicenseFlags.setDescription(' License flags; E - enabled; A - auto-generated; R - reboot required to activate ')
sysExtLicenseService = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseService.setStatus('current')
if mibBuilder.loadTexts: sysExtLicenseService.setDescription(' The service enabled by this license. ')
wlsxSysExtMMSCompatLevel = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMMSCompatLevel.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtMMSCompatLevel.setDescription(' Lists the compatibility level of this controller with the MMS ')
wlsxSysExtMMSConfigID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMMSConfigID.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtMMSConfigID.setDescription(' This Object represents the value of the MMS Configuration ID in the controller. ')
wlsxSysExtControllerConfigID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtControllerConfigID.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtControllerConfigID.setDescription(" This Object represents the value of the Controller's Configuration ID. ")
wlsxSysExtIsMMSConfigUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 24), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxSysExtIsMMSConfigUpdateEnabled.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtIsMMSConfigUpdateEnabled.setDescription(' This objects indicates whether the controller is configured to accept configuration snapshots from MMS. ')
wlsxSysExtSwitchLastReload = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchLastReload.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchLastReload.setDescription(' The reason for the last controller reload ')
wlsxSysExtLastStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 26), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLastStatsReset.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtLastStatsReset.setDescription(' Last time switch stats was reset ')
wlsxSysExtUserTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtUserTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtUserTableGenNumber.setDescription(' This objects denotes the number of times the user table was modified since reboot. ')
wlsxSysExtAPBssidTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPBssidTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtAPBssidTableGenNumber.setDescription(' This objects denotes the number of times the AP BSSID table was modified since reboot. ')
wlsxSysExtAPRadioTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPRadioTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtAPRadioTableGenNumber.setDescription(' This objects denotes the number of times the Radio table was modified since reboot. ')
wlsxSysExtAPTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtAPTableGenNumber.setDescription(' This objects denotes the number of times the AP table was modified since reboot. ')
wlsxSysExtSwitchListTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchListTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtSwitchListTableGenNumber.setDescription(' This objects denotes the number of times the Switch list table was modified since reboot. ')
wlsxSysExtPortTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtPortTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtPortTableGenNumber.setDescription(' This objects denotes the number of times the port table was modified since reboot. ')
wlsxSysExtVlanTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtVlanTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtVlanTableGenNumber.setDescription(' This objects denotes the number of times the Vlan table was modified since reboot. ')
wlsxSysExtVlanInterfaceTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtVlanInterfaceTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtVlanInterfaceTableGenNumber.setDescription(' This objects denotes the number of times the Vlan Interface table was modified since reboot. ')
wlsxSysExtLicenseTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLicenseTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtLicenseTableGenNumber.setDescription(' This objects denotes the number of times the license table was modified since reboot. ')
wlsxSysExtMonAPTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMonAPTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtMonAPTableGenNumber.setDescription(' This objects denotes the number of times the monitored AP table was modified since reboot. ')
wlsxSysExtMonStationTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMonStationTableGenNumber.setStatus('current')
if mibBuilder.loadTexts: wlsxSysExtMonStationTableGenNumber.setDescription(' This objects denotes the number of times the monitored station table was modified since reboot. ')
mibBuilder.exportSymbols("WLSX-SYSTEMEXT-MIB", sysExtCardHwRevision=sysExtCardHwRevision, sysExtStorageType=sysExtStorageType, wlsxSysExtIsMMSConfigUpdateEnabled=wlsxSysExtIsMMSConfigUpdateEnabled, wlsxSystemExtTableGenNumberGroup=wlsxSystemExtTableGenNumberGroup, sysExtCardNumOfFastethernetPorts=sysExtCardNumOfFastethernetPorts, wlsxSysExtPowerSupplyTable=wlsxSysExtPowerSupplyTable, wlsxSystemExtGroup=wlsxSystemExtGroup, wlsxSysExtPowerSupplyEntry=wlsxSysExtPowerSupplyEntry, sysExtProcessorLoad=sysExtProcessorLoad, wlsxSysExtMemoryTable=wlsxSysExtMemoryTable, sysExtMemoryUsed=sysExtMemoryUsed, wlsxSysExtStorageTable=wlsxSysExtStorageTable, sysExtStorageIndex=sysExtStorageIndex, sysExtSwitchIPAddress=sysExtSwitchIPAddress, wlsxSysExtSwitchListEntry=wlsxSysExtSwitchListEntry, wlsxSysExtMMSConfigID=wlsxSysExtMMSConfigID, wlsxSysExtAPBssidTableGenNumber=wlsxSysExtAPBssidTableGenNumber, sysExtSwitchLocation=sysExtSwitchLocation, sysExtMemoryFree=sysExtMemoryFree, sysExtProcessorDescr=sysExtProcessorDescr, wlsxSysExtSwitchLastReload=wlsxSysExtSwitchLastReload, wlsxSysExtMonAPTableGenNumber=wlsxSysExtMonAPTableGenNumber, wlsxSysExtSwitchLicenseCount=wlsxSysExtSwitchLicenseCount, wlsxSysExtFanTrayAssemblyNumber=wlsxSysExtFanTrayAssemblyNumber, sysExtStorageSize=sysExtStorageSize, wlsxSysExtLicenseTableGenNumber=wlsxSysExtLicenseTableGenNumber, sysExtSwitchRole=sysExtSwitchRole, sysExtCardManufacturingDate=sysExtCardManufacturingDate, sysExtLicenseFlags=sysExtLicenseFlags, sysExtLicenseIndex=sysExtLicenseIndex, wlsxSysExtMMSCompatLevel=wlsxSysExtMMSCompatLevel, wlsxSysExtCardEntry=wlsxSysExtCardEntry, sysExtCardNumOfPorts=sysExtCardNumOfPorts, wlsxSysExtLicenseEntry=wlsxSysExtLicenseEntry, sysExtCardSerialNo=sysExtCardSerialNo, sysExtStorageName=sysExtStorageName, wlsxSysExtSwitchIp=wlsxSysExtSwitchIp, wlsxSysExtVlanTableGenNumber=wlsxSysExtVlanTableGenNumber, wlsxSysExtProcessorEntry=wlsxSysExtProcessorEntry, wlsxSysExtHostname=wlsxSysExtHostname, wlsxSysExtSwitchListTable=wlsxSysExtSwitchListTable, wlsxSysExtFanEntry=wlsxSysExtFanEntry, sysExtMemoryIndex=sysExtMemoryIndex, wlsxSysExtAPRadioTableGenNumber=wlsxSysExtAPRadioTableGenNumber, wlsxSysExtSwitchDate=wlsxSysExtSwitchDate, wlsxSysExtLastStatsReset=wlsxSysExtLastStatsReset, wlsxSysExtInternalTemparature=wlsxSysExtInternalTemparature, sysExtCardNumOfGigPorts=sysExtCardNumOfGigPorts, wlsxSystemExtMIB=wlsxSystemExtMIB, wlsxSysExtMemoryEntry=wlsxSysExtMemoryEntry, sysExtCardFpgaRevision=sysExtCardFpgaRevision, wlsxSysExtModelName=wlsxSysExtModelName, wlsxSysExtSwitchListTableGenNumber=wlsxSysExtSwitchListTableGenNumber, wlsxSysExtVlanInterfaceTableGenNumber=wlsxSysExtVlanInterfaceTableGenNumber, wlsxSysExtFanTable=wlsxSysExtFanTable, wlsxSysExtSwitchBaseMacaddress=wlsxSysExtSwitchBaseMacaddress, wlsxSysExtControllerConfigID=wlsxSysExtControllerConfigID, wlsxSysExtCardTable=wlsxSysExtCardTable, sysExtCardUserSlot=sysExtCardUserSlot, sysExtCardSwitchChip=sysExtCardSwitchChip, sysExtCardSlot=sysExtCardSlot, wlsxSysExtProcessorTable=wlsxSysExtProcessorTable, sysExtSwitchName=sysExtSwitchName, wlsxSysExtAPTableGenNumber=wlsxSysExtAPTableGenNumber, wlsxSysExtLicenseSerialNumber=wlsxSysExtLicenseSerialNumber, sysExtLicenseKey=sysExtLicenseKey, sysExtMemorySize=sysExtMemorySize, sysExtFanStatus=sysExtFanStatus, sysExtStorageUsed=sysExtStorageUsed, sysExtCardAssemblyNo=sysExtCardAssemblyNo, sysExtPowerSupplyIndex=sysExtPowerSupplyIndex, sysExtLicenseInstalled=sysExtLicenseInstalled, sysExtPowerSupplyStatus=sysExtPowerSupplyStatus, wlsxSysExtUserTableGenNumber=wlsxSysExtUserTableGenNumber, sysExtSwitchSerNo=sysExtSwitchSerNo, PYSNMP_MODULE_ID=wlsxSystemExtMIB, sysExtCardStatus=sysExtCardStatus, wlsxSysExtStorageEntry=wlsxSysExtStorageEntry, sysExtSwitchStatus=sysExtSwitchStatus, wlsxSysExtSwitchRole=wlsxSysExtSwitchRole, wlsxSysExtMonStationTableGenNumber=wlsxSysExtMonStationTableGenNumber, wlsxSysExtSwitchLicenseTable=wlsxSysExtSwitchLicenseTable, sysExtProcessorID=sysExtProcessorID, sysExtLicenseService=sysExtLicenseService, wlsxSysExtFanTraySerialNumber=wlsxSysExtFanTraySerialNumber, sysExtLicenseExpires=sysExtLicenseExpires, sysExtCardType=sysExtCardType, wlsxSysExtPortTableGenNumber=wlsxSysExtPortTableGenNumber, sysExtSwitchSWVersion=sysExtSwitchSWVersion, sysExtFanIndex=sysExtFanIndex, wlsxSysExtSwitchMasterIp=wlsxSysExtSwitchMasterIp)
