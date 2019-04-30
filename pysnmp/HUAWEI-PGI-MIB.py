#
# PySNMP MIB module HUAWEI-PGI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-PGI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Gauge32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, ModuleIdentity, MibIdentifier, Bits, Unsigned32, Counter32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "ModuleIdentity", "MibIdentifier", "Bits", "Unsigned32", "Counter32", "IpAddress", "NotificationType")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hwPortGroupIsolation = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144))
if mibBuilder.loadTexts: hwPortGroupIsolation.setLastUpdated('200701010000Z')
if mibBuilder.loadTexts: hwPortGroupIsolation.setOrganization('Huawei Technologies Co. Ltd.')
hwPortGroupIsolationMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1))
hwPortGroupIsolationConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1, 1), )
if mibBuilder.loadTexts: hwPortGroupIsolationConfigTable.setStatus('current')
hwPortGroupIsolationConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1, 1, 1), ).setIndexNames((0, "HUAWEI-PGI-MIB", "hwPortGroupIsolationIndex"))
if mibBuilder.loadTexts: hwPortGroupIsolationConfigEntry.setStatus('current')
hwPortGroupIsolationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: hwPortGroupIsolationIndex.setStatus('current')
hwPortGroupIsolationIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPortGroupIsolationIfName.setStatus('current')
hwPortGroupIsolationGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPortGroupIsolationGroupID.setStatus('current')
hwPortGroupIsolationConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 1, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPortGroupIsolationConfigRowStatus.setStatus('current')
hwPortGroupIsolationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 3))
hwPortGroupIsolationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 3, 1))
hwPortGroupIsolationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 3, 1, 1)).setObjects(("HUAWEI-PGI-MIB", "hwPortGroupIsolationObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPortGroupIsolationCompliance = hwPortGroupIsolationCompliance.setStatus('current')
hwPortGroupIsolationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 3, 3))
hwPortGroupIsolationObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 144, 3, 3, 1)).setObjects(("HUAWEI-PGI-MIB", "hwPortGroupIsolationIfName"), ("HUAWEI-PGI-MIB", "hwPortGroupIsolationGroupID"), ("HUAWEI-PGI-MIB", "hwPortGroupIsolationConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPortGroupIsolationObjectGroup = hwPortGroupIsolationObjectGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-PGI-MIB", PYSNMP_MODULE_ID=hwPortGroupIsolation, hwPortGroupIsolation=hwPortGroupIsolation, hwPortGroupIsolationIfName=hwPortGroupIsolationIfName, hwPortGroupIsolationCompliance=hwPortGroupIsolationCompliance, hwPortGroupIsolationConformance=hwPortGroupIsolationConformance, hwPortGroupIsolationConfigTable=hwPortGroupIsolationConfigTable, hwPortGroupIsolationIndex=hwPortGroupIsolationIndex, hwPortGroupIsolationGroups=hwPortGroupIsolationGroups, hwPortGroupIsolationConfigEntry=hwPortGroupIsolationConfigEntry, hwPortGroupIsolationMibObjects=hwPortGroupIsolationMibObjects, hwPortGroupIsolationObjectGroup=hwPortGroupIsolationObjectGroup, hwPortGroupIsolationGroupID=hwPortGroupIsolationGroupID, hwPortGroupIsolationCompliances=hwPortGroupIsolationCompliances, hwPortGroupIsolationConfigRowStatus=hwPortGroupIsolationConfigRowStatus)
