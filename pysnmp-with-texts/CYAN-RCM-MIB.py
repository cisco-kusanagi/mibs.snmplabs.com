#
# PySNMP MIB module CYAN-RCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-RCM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
cyanEntityModules, CyanTypeTc = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules", "CyanTypeTc")
CyanOpStateQualTc, CyanAdminStateTc, CyanSecServiceStateTc, CyanOpStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanOpStateQualTc", "CyanAdminStateTc", "CyanSecServiceStateTc", "CyanOpStateTc")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, MibIdentifier, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, IpAddress, Gauge32, Counter64, Unsigned32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "IpAddress", "Gauge32", "Counter64", "Unsigned32", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyanRcmModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70))
cyanRcmModule.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanRcmModule.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanRcmModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanRcmModule.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanRcmModule.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanRcmModule.setDescription('MIB module for Ring Closure Module')
cyanRcmMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1))
cyanRcmTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1), )
if mibBuilder.loadTexts: cyanRcmTable.setStatus('current')
if mibBuilder.loadTexts: cyanRcmTable.setDescription('A list of Rcm entries.')
cyanRcmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1), ).setIndexNames((0, "CYAN-RCM-MIB", "cyanRcmShelfId"), (0, "CYAN-RCM-MIB", "cyanRcmRcmId"))
if mibBuilder.loadTexts: cyanRcmEntry.setStatus('current')
if mibBuilder.loadTexts: cyanRcmEntry.setDescription('An entry of Rcm.')
cyanRcmShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanRcmShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanRcmShelfId.setDescription('Shelf Id')
cyanRcmRcmId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanRcmRcmId.setStatus('current')
if mibBuilder.loadTexts: cyanRcmRcmId.setDescription('RCM Module Id')
cyanRcmAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 3), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmAdminState.setStatus('current')
if mibBuilder.loadTexts: cyanRcmAdminState.setDescription('Administrative state')
cyanRcmAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 124))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmAssetTag.setStatus('current')
if mibBuilder.loadTexts: cyanRcmAssetTag.setDescription('Asset Tag')
cyanRcmAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmAutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanRcmAutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanRcmBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmBaseMacAddress.setStatus('current')
if mibBuilder.loadTexts: cyanRcmBaseMacAddress.setDescription('Base MAC address of a range of addresses')
cyanRcmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmDescription.setStatus('current')
if mibBuilder.loadTexts: cyanRcmDescription.setDescription('Description')
cyanRcmIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmIdentifier.setStatus('current')
if mibBuilder.loadTexts: cyanRcmIdentifier.setDescription('string OID')
cyanRcmMacBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMacBlockSize.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMacBlockSize.setDescription('Number of MAC addresses allocated from the base MAC address')
cyanRcmMfgCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMfgCleiCode.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMfgCleiCode.setDescription('Common Language Equipment Identifier')
cyanRcmMfgEciCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMfgEciCode.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMfgEciCode.setDescription('Equipment Catalog Item')
cyanRcmMfgModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMfgModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMfgModuleId.setDescription('Module ID')
cyanRcmMfgPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMfgPartNumber.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMfgPartNumber.setDescription('Manufacturing part number')
cyanRcmMfgRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMfgRevision.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMfgRevision.setDescription('Mfg revision number')
cyanRcmMfgSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmMfgSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cyanRcmMfgSerialNumber.setDescription('Mfg serial number')
cyanRcmName = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmName.setStatus('current')
if mibBuilder.loadTexts: cyanRcmName.setDescription('Cyan name')
cyanRcmOidClass = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmOidClass.setStatus('current')
if mibBuilder.loadTexts: cyanRcmOidClass.setDescription('OID Class')
cyanRcmOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 18), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmOperState.setStatus('current')
if mibBuilder.loadTexts: cyanRcmOperState.setDescription('Primary Operation State')
cyanRcmOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 19), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmOperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanRcmOperStateQual.setDescription('Operation state qualifier')
cyanRcmOssLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmOssLabel.setStatus('current')
if mibBuilder.loadTexts: cyanRcmOssLabel.setDescription('CyMS label')
cyanRcmOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmOwner.setStatus('current')
if mibBuilder.loadTexts: cyanRcmOwner.setDescription('Owner')
cyanRcmPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmPartNumber.setStatus('current')
if mibBuilder.loadTexts: cyanRcmPartNumber.setDescription('Cyan part number')
cyanRcmSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 23), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmSecServState.setStatus('current')
if mibBuilder.loadTexts: cyanRcmSecServState.setDescription('Secondary service state')
cyanRcmType = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 24), CyanTypeTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRcmType.setStatus('current')
if mibBuilder.loadTexts: cyanRcmType.setDescription('Equipment type')
cyanRcmObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 20)).setObjects(("CYAN-RCM-MIB", "cyanRcmAdminState"), ("CYAN-RCM-MIB", "cyanRcmAssetTag"), ("CYAN-RCM-MIB", "cyanRcmAutoinserviceSoakTimeSec"), ("CYAN-RCM-MIB", "cyanRcmBaseMacAddress"), ("CYAN-RCM-MIB", "cyanRcmDescription"), ("CYAN-RCM-MIB", "cyanRcmIdentifier"), ("CYAN-RCM-MIB", "cyanRcmMacBlockSize"), ("CYAN-RCM-MIB", "cyanRcmMfgCleiCode"), ("CYAN-RCM-MIB", "cyanRcmMfgEciCode"), ("CYAN-RCM-MIB", "cyanRcmMfgModuleId"), ("CYAN-RCM-MIB", "cyanRcmMfgPartNumber"), ("CYAN-RCM-MIB", "cyanRcmMfgRevision"), ("CYAN-RCM-MIB", "cyanRcmMfgSerialNumber"), ("CYAN-RCM-MIB", "cyanRcmName"), ("CYAN-RCM-MIB", "cyanRcmOidClass"), ("CYAN-RCM-MIB", "cyanRcmOperState"), ("CYAN-RCM-MIB", "cyanRcmOperStateQual"), ("CYAN-RCM-MIB", "cyanRcmOssLabel"), ("CYAN-RCM-MIB", "cyanRcmOwner"), ("CYAN-RCM-MIB", "cyanRcmPartNumber"), ("CYAN-RCM-MIB", "cyanRcmSecServState"), ("CYAN-RCM-MIB", "cyanRcmType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanRcmObjectGroup = cyanRcmObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanRcmObjectGroup.setDescription('Group of objects that comes with Rcm module')
cyanRcmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 30)).setObjects(("CYAN-RCM-MIB", "cyanRcmObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanRcmCompliance = cyanRcmCompliance.setStatus('current')
if mibBuilder.loadTexts: cyanRcmCompliance.setDescription('The basic info needed to be a cyan Rcm')
mibBuilder.exportSymbols("CYAN-RCM-MIB", cyanRcmMfgSerialNumber=cyanRcmMfgSerialNumber, cyanRcmEntry=cyanRcmEntry, cyanRcmBaseMacAddress=cyanRcmBaseMacAddress, cyanRcmMfgRevision=cyanRcmMfgRevision, cyanRcmPartNumber=cyanRcmPartNumber, cyanRcmShelfId=cyanRcmShelfId, cyanRcmMfgModuleId=cyanRcmMfgModuleId, cyanRcmName=cyanRcmName, cyanRcmOssLabel=cyanRcmOssLabel, cyanRcmMibObjects=cyanRcmMibObjects, PYSNMP_MODULE_ID=cyanRcmModule, cyanRcmMfgEciCode=cyanRcmMfgEciCode, cyanRcmModule=cyanRcmModule, cyanRcmOidClass=cyanRcmOidClass, cyanRcmMfgCleiCode=cyanRcmMfgCleiCode, cyanRcmObjectGroup=cyanRcmObjectGroup, cyanRcmOperState=cyanRcmOperState, cyanRcmType=cyanRcmType, cyanRcmMfgPartNumber=cyanRcmMfgPartNumber, cyanRcmOperStateQual=cyanRcmOperStateQual, cyanRcmTable=cyanRcmTable, cyanRcmAssetTag=cyanRcmAssetTag, cyanRcmIdentifier=cyanRcmIdentifier, cyanRcmSecServState=cyanRcmSecServState, cyanRcmOwner=cyanRcmOwner, cyanRcmCompliance=cyanRcmCompliance, cyanRcmAdminState=cyanRcmAdminState, cyanRcmRcmId=cyanRcmRcmId, cyanRcmMacBlockSize=cyanRcmMacBlockSize, cyanRcmAutoinserviceSoakTimeSec=cyanRcmAutoinserviceSoakTimeSec, cyanRcmDescription=cyanRcmDescription)
