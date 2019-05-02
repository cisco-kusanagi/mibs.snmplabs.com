#
# PySNMP MIB module COSINE-InVision-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COSINE-InVision-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
csOrionMIB, csInVisionMIB, csModules = mibBuilder.importSymbols("COSINE-GLOBAL-REG", "csOrionMIB", "csInVisionMIB", "csModules")
csOrionSystemIpAddress, csOrionRestoreNumVRs, csOrionRestoreSlotIndex, csOrionBladeType = mibBuilder.importSymbols("COSINE-ORION-MIB", "csOrionSystemIpAddress", "csOrionRestoreNumVRs", "csOrionRestoreSlotIndex", "csOrionBladeType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Counter32, Counter64, Integer32, enterprises, mib_2, ObjectIdentity, Gauge32, iso, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Bits, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Integer32", "enterprises", "mib-2", "ObjectIdentity", "Gauge32", "iso", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Bits", "NotificationType", "IpAddress")
PhysAddress, DateAndTime, DisplayString, RowStatus, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DateAndTime", "DisplayString", "RowStatus", "TimeStamp", "TextualConvention")
cosineInVisionMod = ModuleIdentity((1, 3, 6, 1, 4, 1, 3085, 1, 1, 3))
cosineInVisionMod.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cosineInVisionMod.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: cosineInVisionMod.setLastUpdated('9911231355Z')
if mibBuilder.loadTexts: cosineInVisionMod.setOrganization('Cosine Communication Co.')
if mibBuilder.loadTexts: cosineInVisionMod.setContactInfo(' Lianghwa Jou Cosine Communications Co. 1200 Bridge Parkway Redwood City, CA 94065 US 650-637-4777 ljou@cosinecom.com')
if mibBuilder.loadTexts: cosineInVisionMod.setDescription('The MIB module to describe generic objects for InVision system. ')
csInVisionEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1))
csInVisionBladeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2))
csInVisionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3085, 3, 2, 3))
csInVisionServerName = MibScalar((1, 3, 6, 1, 4, 1, 3085, 3, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csInVisionServerName.setStatus('current')
if mibBuilder.loadTexts: csInVisionServerName.setDescription('A it is passed as argument to the trap csInVisionServerDown signifies that SMS Server is Down.')
csInVisionBladeTable = MibTable((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1), )
if mibBuilder.loadTexts: csInVisionBladeTable.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeTable.setDescription('A list of Blades which belongs to InVision database.')
csInVisionBladeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1), ).setIndexNames((0, "COSINE-InVision-MIB", "csInVisionBladeSlotLocation"))
if mibBuilder.loadTexts: csInVisionBladeEntry.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeEntry.setDescription('An entry containing management information applicable to a particular Blade.')
csInVisionBladeSlotLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 26)))
if mibBuilder.loadTexts: csInVisionBladeSlotLocation.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeSlotLocation.setDescription('Slot Location of the Blade in the InVision database.')
csInVisionBladeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeDescr.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeDescr.setDescription('A textual string containing information about the blade. This string should include the name of the manufacturer and the product name.')
csInVisionBladeType = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("process", 1), ("control", 2), ("ethernet", 3), ("ds3Unchannelized", 4), ("ds3channelized", 5), ("oc3Atm", 6), ("oc3Pos", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeType.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeType.setDescription('The type of blade inserted in this slot.')
csInVisionBladeState = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("notPresent", 1), ("inactive", 2), ("active", 3), ("softwareLoading", 4), ("operational", 5), ("nonOperational", 6), ("failedWithBackup", 7), ("failedWithOutBackup", 8), ("backup", 9), ("standby", 10), ("reboot", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeState.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeState.setDescription('The current state of this blade.')
csInVisionBladeEnginesNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeEnginesNumb.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeEnginesNumb.setDescription('The number of engines on the blade.')
csInVisionBladePortNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladePortNumb.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladePortNumb.setDescription('The number of ports on this blade (note, process blades have no ports).')
csInVisionBladeSerialNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeSerialNumb.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeSerialNumb.setDescription('The serial number of the blade. This is a series of alphanumeric characters which uniquely identifies this blade.')
csInVisionBladeHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeHwVer.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeHwVer.setDescription('A textual string containing information about the hardware revision version.')
csInVisionBladeSwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csInVisionBladeSwVer.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeSwVer.setDescription('A textual string containing information about the software revision version.')
csInVisionBladeReset = MibTableColumn((1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csInVisionBladeReset.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeReset.setDescription("The software reset for this blade. It is an action object such that when set to 'reset' will reset this blade. Setting it to 'none' has no effect, and when it is retrieved the value will always be 'none' . ")
csInVisionEventsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1))
csInVisionBladeResyncedInInVision = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 1)).setObjects(("COSINE-ORION-MIB", "csOrionRestoreSlotIndex"), ("COSINE-ORION-MIB", "csOrionBladeType"))
if mibBuilder.loadTexts: csInVisionBladeResyncedInInVision.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeResyncedInInVision.setDescription('A csInVisionBladeResyncedInInVision Inform PDU signifies that a blade had been resynced successfully.')
csInVisionBladeInconsistentInInVision = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 2)).setObjects(("COSINE-ORION-MIB", "csOrionRestoreSlotIndex"), ("COSINE-InVision-MIB", "csInVisionBladeType"), ("COSINE-ORION-MIB", "csOrionBladeType"))
if mibBuilder.loadTexts: csInVisionBladeInconsistentInInVision.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeInconsistentInInVision.setDescription('A csgBladeInconsistent Inform PDU signifies that type of blade in InVision is different from type of blade type in device in same slot.')
csInVisionBladeRestoreOnDevice = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 3)).setObjects(("COSINE-ORION-MIB", "csOrionRestoreSlotIndex"), ("COSINE-ORION-MIB", "csOrionBladeType"))
if mibBuilder.loadTexts: csInVisionBladeRestoreOnDevice.setStatus('current')
if mibBuilder.loadTexts: csInVisionBladeRestoreOnDevice.setDescription('A csInVisionBladeResyncedInInVision Inform PDU signifies that a blade had been resynced successfully.')
csInVisionVRRestoreSuccess = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 4)).setObjects(("COSINE-ORION-MIB", "csOrionRestoreNumVRs"))
if mibBuilder.loadTexts: csInVisionVRRestoreSuccess.setStatus('current')
if mibBuilder.loadTexts: csInVisionVRRestoreSuccess.setDescription('A csgVRRestoreSuccess Inform PDU signifies that InVision is succedded in restoring affecred VRs to device.')
csInVisionVRRestoreFail = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 5)).setObjects(("COSINE-ORION-MIB", "csOrionRestoreNumVRs"))
if mibBuilder.loadTexts: csInVisionVRRestoreFail.setStatus('current')
if mibBuilder.loadTexts: csInVisionVRRestoreFail.setDescription('A csgVRRestoreFail Inform PDU signifies that InVision is failed in restoring affecred VRs to device.')
csInVisionDeviceVRRestoreFail = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 6)).setObjects(("COSINE-ORION-MIB", "csOrionRestoreNumVRs"))
if mibBuilder.loadTexts: csInVisionDeviceVRRestoreFail.setStatus('current')
if mibBuilder.loadTexts: csInVisionDeviceVRRestoreFail.setDescription('A csInVisionDeviceVRRestoreFail Inform PDU signifies that Device is failed in restoring affecred VRs.')
csInVisionFailToRegisterForTrap = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 7)).setObjects(("COSINE-ORION-MIB", "csOrionSystemIpAddress"))
if mibBuilder.loadTexts: csInVisionFailToRegisterForTrap.setStatus('current')
if mibBuilder.loadTexts: csInVisionFailToRegisterForTrap.setDescription('A csInVisionFailToRegisterForTrap Inform PDU signifies that SMS Trap Server failed to register for trap with device.')
csInVisionServerDown = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 8)).setObjects(("COSINE-InVision-MIB", "csInVisionServerName"))
if mibBuilder.loadTexts: csInVisionServerDown.setStatus('current')
if mibBuilder.loadTexts: csInVisionServerDown.setDescription('A csInVisionServerDown Inform PDU signifies that SMS Server is Down. This trap is generated from launcher to any third party alarm display system.')
csInVisionFailToUnRegisterForTrap = NotificationType((1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 9)).setObjects(("COSINE-ORION-MIB", "csOrionSystemIpAddress"))
if mibBuilder.loadTexts: csInVisionFailToUnRegisterForTrap.setStatus('current')
if mibBuilder.loadTexts: csInVisionFailToUnRegisterForTrap.setDescription('A csInVisionFailToUnRegisterForTrap Inform PDU signifies that SMS Trap Server failed to unregister for trap with device.')
mibBuilder.exportSymbols("COSINE-InVision-MIB", csInVisionBladeSlotLocation=csInVisionBladeSlotLocation, csInVisionBladeSwVer=csInVisionBladeSwVer, csInVisionDeviceVRRestoreFail=csInVisionDeviceVRRestoreFail, csInVisionEventsInfo=csInVisionEventsInfo, csInVisionFailToUnRegisterForTrap=csInVisionFailToUnRegisterForTrap, csInVisionVRRestoreSuccess=csInVisionVRRestoreSuccess, csInVisionBladeEntry=csInVisionBladeEntry, csInVisionBladePortNumb=csInVisionBladePortNumb, csInVisionBladeSerialNumb=csInVisionBladeSerialNumb, csInVisionBladeInfo=csInVisionBladeInfo, PYSNMP_MODULE_ID=cosineInVisionMod, csInVisionBladeHwVer=csInVisionBladeHwVer, csInVisionFailToRegisterForTrap=csInVisionFailToRegisterForTrap, csInVisionBladeType=csInVisionBladeType, csInVisionVRRestoreFail=csInVisionVRRestoreFail, csInVisionBladeInconsistentInInVision=csInVisionBladeInconsistentInInVision, csInVisionBladeResyncedInInVision=csInVisionBladeResyncedInInVision, csInVisionServerName=csInVisionServerName, csInVisionBladeDescr=csInVisionBladeDescr, cosineInVisionMod=cosineInVisionMod, csInVisionServerDown=csInVisionServerDown, csInVisionEvents=csInVisionEvents, csInVisionBladeReset=csInVisionBladeReset, csInVisionBladeRestoreOnDevice=csInVisionBladeRestoreOnDevice, csInVisionObjects=csInVisionObjects, csInVisionBladeTable=csInVisionBladeTable, csInVisionBladeState=csInVisionBladeState, csInVisionBladeEnginesNumb=csInVisionBladeEnginesNumb)
