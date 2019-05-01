#
# PySNMP MIB module HM2-PWRMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PWRMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:31:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Counter32, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier, ObjectIdentity, Integer32, Unsigned32, iso, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PowerMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 11))
hm2PowerMgmtMib.setRevisions(('2011-03-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2PowerMgmtMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2PowerMgmtMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2PowerMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2PowerMgmtMib.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2PowerMgmtMib.setDescription('Hirschmann Power Management MIB. Copyright (C) 2011. All Rights Reserved.')
hm2PowerMgmtMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 11, 0))
hm2PowerMgmtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 11, 1))
hm2PowerSupplyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1))
hm2PSTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1), )
if mibBuilder.loadTexts: hm2PSTable.setStatus('current')
if mibBuilder.loadTexts: hm2PSTable.setDescription('This table contains all variables related to the power supply units of the chassis/switch. For each power supply slot exists one instance.')
hm2PSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1), ).setIndexNames((0, "HM2-PWRMGMT-MIB", "hm2PSID"))
if mibBuilder.loadTexts: hm2PSEntry.setStatus('current')
if mibBuilder.loadTexts: hm2PSEntry.setDescription('The entry of the hm2PSTable.')
hm2PSID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSID.setStatus('current')
if mibBuilder.loadTexts: hm2PSID.setDescription('This index is used to identify the associated power supply unit.')
hm2PSState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("present", 1), ("defective", 2), ("notInstalled", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSState.setStatus('current')
if mibBuilder.loadTexts: hm2PSState.setDescription('Indicates the operational state of the associated power supply. If the value of this variable changes, a hm2PowerSupply trap is sent.')
hm2PSUSlotInfoTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10), )
if mibBuilder.loadTexts: hm2PSUSlotInfoTable.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotInfoTable.setDescription('This table contains all EEPROM variables related to the power supply slot modules of the chassis/switch. For each power supply slot module exists one instance.')
hm2PSUSlotInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1), ).setIndexNames((0, "HM2-PWRMGMT-MIB", "hm2PSUSlotIndex"))
if mibBuilder.loadTexts: hm2PSUSlotInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotInfoEntry.setDescription('The entry of the hm2PSUSlotInfoTable.')
hm2PSUSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hm2PSUSlotIndex.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotIndex.setDescription('This index is used to identify the associated power supply slot module.')
hm2PSUSlotChassisTypeId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 0), ("mach1020", 1), ("mach4000", 2), ("railswitch", 3), ("grs", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotChassisTypeId.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotChassisTypeId.setDescription('The chassis type id of the associated power supply slot module.')
hm2PSUSlotManufacturerId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("other", 0), ("hirschmann", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotManufacturerId.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotManufacturerId.setDescription('The manufacturer id of the associated power supply slot module.')
hm2PSUSlotManufacturerDate = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotManufacturerDate.setStatus('obsolete')
if mibBuilder.loadTexts: hm2PSUSlotManufacturerDate.setDescription('The manufacturer date of the associated power supply slot module. *** NOTE this is set to OBSOLETE ***')
hm2PSUSlotSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotSerialNumber.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotSerialNumber.setDescription('The serial number of the associated power supply slot module.')
hm2PSUSlotProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotProductCode.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotProductCode.setDescription('The product code of the associated power supply slot module.')
hm2PSUSlotDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotDescription.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotDescription.setDescription('The description of the associated power supply slot module.')
hm2PSUSlotCombinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("only-on-psu1", 0), ("psu1-sys-psu2-poe", 1), ("psu1-poe-psu2-sys", 2), ("two-separate-psus", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotCombinationType.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotCombinationType.setDescription('The combination type of the associated power supply slot module.')
hm2PSUSlotTemperatureRange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("tr-0-60", 0), ("tr-minus40-60", 1), ("tr-minus40-70", 2), ("tr-minus40-70cc", 3), ("tr-minus40-85", 4), ("tr-minus40-85cc", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotTemperatureRange.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotTemperatureRange.setDescription('The temperature range of the associated power supply slot module.')
hm2PSUSlotRevisionId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUSlotRevisionId.setStatus('current')
if mibBuilder.loadTexts: hm2PSUSlotRevisionId.setDescription('Hardware revision of the PSU')
hm2PSUUnitInfoTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20), )
if mibBuilder.loadTexts: hm2PSUUnitInfoTable.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitInfoTable.setDescription('This table contains all EEPROM variables related to the power supply slot module units. For each power supply slot module exists up to two instances.')
hm2PSUUnitInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1), ).setIndexNames((0, "HM2-PWRMGMT-MIB", "hm2PSUSlotIndex"), (0, "HM2-PWRMGMT-MIB", "hm2PSUUnitIndex"))
if mibBuilder.loadTexts: hm2PSUUnitInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitInfoEntry.setDescription('The entry of the hm2PSUUnitInfoTable.')
hm2PSUUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: hm2PSUUnitIndex.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitIndex.setDescription('The number of PSU units on the associated power supply slot module.')
hm2PSUUnitConverterType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ac", 1), ("dc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitConverterType.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitConverterType.setDescription('The converter type of the associated power supply slot module unit.')
hm2PSUUnitNumberOfInputs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitNumberOfInputs.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitNumberOfInputs.setDescription('The number of inputs of the associated power supply slot module unit.')
hm2PSUUnitOutputType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("system", 1), ("both", 2), ("poe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitOutputType.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitOutputType.setDescription('The output type of the associated power supply slot module unit.')
hm2PSUUnitSystemBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitSystemBudget.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitSystemBudget.setDescription('The system budget of the associated power supply slot module unit.')
hm2PSUUnitPoeBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitPoeBudget.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitPoeBudget.setDescription('The Poe budget of the associated power supply slot module unit.')
hm2PSUUnitFanCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitFanCount.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitFanCount.setDescription('The fan count of the associated power supply slot module unit.')
hm2PSUUnitVoltageRange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("vr-18-60vdc", 0), ("vr-24-60vdc", 1), ("vr-24-48vdc", 2), ("vr-60-250vdc-110-240vac", 3), ("vr-48-54vdc-poe", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitVoltageRange.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitVoltageRange.setDescription('The voltage range of the associated power supply slot module unit.')
hm2PSUUnitPowerInterruption = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PSUUnitPowerInterruption.setStatus('current')
if mibBuilder.loadTexts: hm2PSUUnitPowerInterruption.setDescription('The power interruption value of the associated power supply slot module unit.')
hm2PowerSupplyTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 11, 0, 1)).setObjects(("HM2-PWRMGMT-MIB", "hm2PSID"), ("HM2-PWRMGMT-MIB", "hm2PSState"))
if mibBuilder.loadTexts: hm2PowerSupplyTrap.setStatus('current')
if mibBuilder.loadTexts: hm2PowerSupplyTrap.setDescription('This trap is sent when the value of hm2PSState has been changed.')
mibBuilder.exportSymbols("HM2-PWRMGMT-MIB", hm2PSUUnitIndex=hm2PSUUnitIndex, PYSNMP_MODULE_ID=hm2PowerMgmtMib, hm2PowerMgmtMib=hm2PowerMgmtMib, hm2PSUUnitOutputType=hm2PSUUnitOutputType, hm2PSTable=hm2PSTable, hm2PowerSupplyGroup=hm2PowerSupplyGroup, hm2PSUSlotIndex=hm2PSUSlotIndex, hm2PSUSlotManufacturerId=hm2PSUSlotManufacturerId, hm2PSState=hm2PSState, hm2PSEntry=hm2PSEntry, hm2PSUUnitPowerInterruption=hm2PSUUnitPowerInterruption, hm2PowerSupplyTrap=hm2PowerSupplyTrap, hm2PSUSlotSerialNumber=hm2PSUSlotSerialNumber, hm2PSUUnitVoltageRange=hm2PSUUnitVoltageRange, hm2PSUSlotRevisionId=hm2PSUSlotRevisionId, hm2PSUSlotProductCode=hm2PSUSlotProductCode, hm2PSUUnitInfoTable=hm2PSUUnitInfoTable, hm2PSID=hm2PSID, hm2PSUSlotTemperatureRange=hm2PSUSlotTemperatureRange, hm2PSUSlotCombinationType=hm2PSUSlotCombinationType, hm2PSUUnitFanCount=hm2PSUUnitFanCount, hm2PSUSlotManufacturerDate=hm2PSUSlotManufacturerDate, hm2PSUSlotInfoEntry=hm2PSUSlotInfoEntry, hm2PowerMgmtMibNotifications=hm2PowerMgmtMibNotifications, hm2PSUUnitInfoEntry=hm2PSUUnitInfoEntry, hm2PSUSlotInfoTable=hm2PSUSlotInfoTable, hm2PSUSlotChassisTypeId=hm2PSUSlotChassisTypeId, hm2PSUUnitConverterType=hm2PSUUnitConverterType, hm2PSUUnitNumberOfInputs=hm2PSUUnitNumberOfInputs, hm2PSUSlotDescription=hm2PSUSlotDescription, hm2PSUUnitPoeBudget=hm2PSUUnitPoeBudget, hm2PowerMgmtMibObjects=hm2PowerMgmtMibObjects, hm2PSUUnitSystemBudget=hm2PSUUnitSystemBudget)