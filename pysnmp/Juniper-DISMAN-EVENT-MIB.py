#
# PySNMP MIB module Juniper-DISMAN-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DISMAN-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
mteTriggerEntry, = mibBuilder.importSymbols("DISMAN-EVENT-MIB", "mteTriggerEntry")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Unsigned32, ModuleIdentity, iso, Counter32, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, Counter64, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ModuleIdentity", "iso", "Counter32", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "Counter64", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDismanEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66))
juniDismanEventMIB.setRevisions(('2003-10-30 15:35',))
if mibBuilder.loadTexts: juniDismanEventMIB.setLastUpdated('200310301535Z')
if mibBuilder.loadTexts: juniDismanEventMIB.setOrganization('Juniper Networks, Inc.')
juniDismanEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1))
juniMteTrigger = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1))
juniMteTriggerTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1), )
if mibBuilder.loadTexts: juniMteTriggerTable.setStatus('current')
juniMteTriggerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1), )
mteTriggerEntry.registerAugmentions(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerEntry"))
juniMteTriggerEntry.setIndexNames(*mteTriggerEntry.getIndexNames())
if mibBuilder.loadTexts: juniMteTriggerEntry.setStatus('current')
juniMteTriggerContextNameLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniMteTriggerContextNameLimit.setStatus('current')
juniDismanEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2))
juniDismanEventMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1))
juniMteExistenceTestResult = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("present", 0), ("absent", 1), ("changed", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniMteExistenceTestResult.setStatus('current')
juniDismanEventConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3))
juniDismanEventCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1))
juniDismanEventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2))
juniDismanEventCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1, 1)).setObjects(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDismanEventCompliance = juniDismanEventCompliance.setStatus('current')
juniMteTriggerTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2, 1)).setObjects(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerContextNameLimit"), ("Juniper-DISMAN-EVENT-MIB", "juniMteExistenceTestResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMteTriggerTableGroup = juniMteTriggerTableGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-DISMAN-EVENT-MIB", juniMteTriggerTable=juniMteTriggerTable, juniDismanEventMIBNotificationPrefix=juniDismanEventMIBNotificationPrefix, juniMteTrigger=juniMteTrigger, juniDismanEventGroups=juniDismanEventGroups, juniDismanEventCompliances=juniDismanEventCompliances, juniDismanEventCompliance=juniDismanEventCompliance, juniDismanEventMIBNotificationObjects=juniDismanEventMIBNotificationObjects, juniDismanEventConformance=juniDismanEventConformance, juniMteTriggerEntry=juniMteTriggerEntry, juniDismanEventMIB=juniDismanEventMIB, juniMteTriggerContextNameLimit=juniMteTriggerContextNameLimit, PYSNMP_MODULE_ID=juniDismanEventMIB, juniDismanEventMIBObjects=juniDismanEventMIBObjects, juniMteExistenceTestResult=juniMteExistenceTestResult, juniMteTriggerTableGroup=juniMteTriggerTableGroup)
