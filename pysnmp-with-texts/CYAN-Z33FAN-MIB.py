#
# PySNMP MIB module CYAN-Z33FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-Z33FAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cyanEntityModules, CyanTypeTc = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules", "CyanTypeTc")
CyanLEDTc, CyanOpStateTc, CyanOpStateQualTc, CyanAdminStateTc, CyanSecServiceStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanLEDTc", "CyanOpStateTc", "CyanOpStateQualTc", "CyanAdminStateTc", "CyanSecServiceStateTc")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, MibIdentifier, NotificationType, Counter32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "MibIdentifier", "NotificationType", "Counter32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanZ33FanModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80))
cyanZ33FanModule.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanZ33FanModule.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanZ33FanModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanZ33FanModule.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanZ33FanModule.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanZ33FanModule.setDescription('MIB module for Z33 Fan')
cyanZ33FanMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1))
cyanZ33FanTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1), )
if mibBuilder.loadTexts: cyanZ33FanTable.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanTable.setDescription('A list of Z33Fan entries.')
cyanZ33FanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1), ).setIndexNames((0, "CYAN-Z33FAN-MIB", "cyanZ33FanShelfId"), (0, "CYAN-Z33FAN-MIB", "cyanZ33FanZ33FanId"))
if mibBuilder.loadTexts: cyanZ33FanEntry.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanEntry.setDescription('An entry of Z33Fan.')
cyanZ33FanShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanZ33FanShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanShelfId.setDescription('Shelf Id')
cyanZ33FanZ33FanId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanZ33FanZ33FanId.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanZ33FanId.setDescription('Z33Fan Module Id')
cyanZ33FanAcoLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 3), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAcoLed.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanAcoLed.setDescription('ACO LED')
cyanZ33FanAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAdminState.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanAdminState.setDescription('Administrative state')
cyanZ33FanAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 124))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAssetTag.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanAssetTag.setDescription('Asset Tag')
cyanZ33FanAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanAutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanZ33FanBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanBaseMacAddress.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanBaseMacAddress.setDescription('Base MAC address of a range of addresses')
cyanZ33FanCriticalLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 8), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanCriticalLed.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanCriticalLed.setDescription('Critical alarm LED status')
cyanZ33FanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanDescription.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanDescription.setDescription('Description')
cyanZ33FanFanLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 10), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanFanLed.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanFanLed.setDescription('Fan LED status')
cyanZ33FanFilterLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 11), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanFilterLed.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanFilterLed.setDescription('Filter LED status')
cyanZ33FanIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanIdentifier.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanIdentifier.setDescription('string OID')
cyanZ33FanMacBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMacBlockSize.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMacBlockSize.setDescription('Number of MAC addresses allocated from the base MAC address')
cyanZ33FanMajorLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 14), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMajorLed.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMajorLed.setDescription('Major alarm LED status')
cyanZ33FanMfgCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgCleiCode.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMfgCleiCode.setDescription('Common Language Equipment Identifier')
cyanZ33FanMfgEciCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgEciCode.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMfgEciCode.setDescription('Equipment Catalog Item')
cyanZ33FanMfgModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMfgModuleId.setDescription('Module ID')
cyanZ33FanMfgPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgPartNumber.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMfgPartNumber.setDescription('Manufacturing part number')
cyanZ33FanMfgRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgRevision.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMfgRevision.setDescription('Mfg revision number')
cyanZ33FanMfgSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMfgSerialNumber.setDescription('Mfg serial number')
cyanZ33FanMinorLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 21), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMinorLed.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanMinorLed.setDescription('Minor alarm LED status')
cyanZ33FanName = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanName.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanName.setDescription('Cyan name')
cyanZ33FanOidClass = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOidClass.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanOidClass.setDescription('OID Class')
cyanZ33FanOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 24), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOperState.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanOperState.setDescription('Primary Operation State')
cyanZ33FanOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 25), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanOperStateQual.setDescription('Operation state qualifier')
cyanZ33FanOssLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOssLabel.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanOssLabel.setDescription('CyMS label')
cyanZ33FanOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOwner.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanOwner.setDescription('Owner')
cyanZ33FanPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanPartNumber.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanPartNumber.setDescription('Cyan part number')
cyanZ33FanSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 29), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanSecServState.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanSecServState.setDescription('Secondary service state')
cyanZ33FanType = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 30), CyanTypeTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanType.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanType.setDescription('Equipment type')
cyanZ33FanObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 20)).setObjects(("CYAN-Z33FAN-MIB", "cyanZ33FanAcoLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanAdminState"), ("CYAN-Z33FAN-MIB", "cyanZ33FanAssetTag"), ("CYAN-Z33FAN-MIB", "cyanZ33FanAutoinserviceSoakTimeSec"), ("CYAN-Z33FAN-MIB", "cyanZ33FanBaseMacAddress"), ("CYAN-Z33FAN-MIB", "cyanZ33FanCriticalLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanDescription"), ("CYAN-Z33FAN-MIB", "cyanZ33FanFanLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanFilterLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanIdentifier"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMacBlockSize"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMajorLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgCleiCode"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgEciCode"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgModuleId"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgPartNumber"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgRevision"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgSerialNumber"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMinorLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanName"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOidClass"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOperState"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOperStateQual"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOssLabel"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOwner"), ("CYAN-Z33FAN-MIB", "cyanZ33FanPartNumber"), ("CYAN-Z33FAN-MIB", "cyanZ33FanSecServState"), ("CYAN-Z33FAN-MIB", "cyanZ33FanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanZ33FanObjectGroup = cyanZ33FanObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanObjectGroup.setDescription('Group of objects that comes with Z33Fan module')
cyanZ33FanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 30)).setObjects(("CYAN-Z33FAN-MIB", "cyanZ33FanObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanZ33FanCompliance = cyanZ33FanCompliance.setStatus('current')
if mibBuilder.loadTexts: cyanZ33FanCompliance.setDescription('The basic info needed to be a cyan Z33Fan')
mibBuilder.exportSymbols("CYAN-Z33FAN-MIB", cyanZ33FanOperState=cyanZ33FanOperState, cyanZ33FanDescription=cyanZ33FanDescription, cyanZ33FanMfgRevision=cyanZ33FanMfgRevision, cyanZ33FanModule=cyanZ33FanModule, cyanZ33FanMajorLed=cyanZ33FanMajorLed, cyanZ33FanOperStateQual=cyanZ33FanOperStateQual, cyanZ33FanMfgPartNumber=cyanZ33FanMfgPartNumber, cyanZ33FanType=cyanZ33FanType, cyanZ33FanMfgEciCode=cyanZ33FanMfgEciCode, cyanZ33FanBaseMacAddress=cyanZ33FanBaseMacAddress, cyanZ33FanTable=cyanZ33FanTable, cyanZ33FanAcoLed=cyanZ33FanAcoLed, cyanZ33FanOidClass=cyanZ33FanOidClass, cyanZ33FanFanLed=cyanZ33FanFanLed, cyanZ33FanAutoinserviceSoakTimeSec=cyanZ33FanAutoinserviceSoakTimeSec, cyanZ33FanMacBlockSize=cyanZ33FanMacBlockSize, cyanZ33FanOwner=cyanZ33FanOwner, cyanZ33FanMfgModuleId=cyanZ33FanMfgModuleId, cyanZ33FanIdentifier=cyanZ33FanIdentifier, cyanZ33FanEntry=cyanZ33FanEntry, cyanZ33FanMfgSerialNumber=cyanZ33FanMfgSerialNumber, cyanZ33FanZ33FanId=cyanZ33FanZ33FanId, cyanZ33FanCriticalLed=cyanZ33FanCriticalLed, cyanZ33FanAssetTag=cyanZ33FanAssetTag, cyanZ33FanPartNumber=cyanZ33FanPartNumber, cyanZ33FanObjectGroup=cyanZ33FanObjectGroup, cyanZ33FanCompliance=cyanZ33FanCompliance, cyanZ33FanFilterLed=cyanZ33FanFilterLed, cyanZ33FanSecServState=cyanZ33FanSecServState, cyanZ33FanName=cyanZ33FanName, cyanZ33FanMibObjects=cyanZ33FanMibObjects, cyanZ33FanShelfId=cyanZ33FanShelfId, cyanZ33FanMfgCleiCode=cyanZ33FanMfgCleiCode, cyanZ33FanMinorLed=cyanZ33FanMinorLed, cyanZ33FanAdminState=cyanZ33FanAdminState, PYSNMP_MODULE_ID=cyanZ33FanModule, cyanZ33FanOssLabel=cyanZ33FanOssLabel)
