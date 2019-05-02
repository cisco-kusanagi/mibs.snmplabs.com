#
# PySNMP MIB module Juniper-DISMAN-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DISMAN-EVENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:02:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
mteTriggerEntry, = mibBuilder.importSymbols("DISMAN-EVENT-MIB", "mteTriggerEntry")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, IpAddress, Counter64, ModuleIdentity, iso, Unsigned32, Bits, Integer32, Counter32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "IpAddress", "Counter64", "ModuleIdentity", "iso", "Unsigned32", "Bits", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDismanEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66))
juniDismanEventMIB.setRevisions(('2003-10-30 15:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDismanEventMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniDismanEventMIB.setLastUpdated('200310301535Z')
if mibBuilder.loadTexts: juniDismanEventMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDismanEventMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniDismanEventMIB.setDescription('The Distributed Management (Disman) Event MIB extensions for the Juniper Networks enterprise. This MIB module extends event triggers and actions defined in the IETF DISMAN-EVENT-MIB.')
juniDismanEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1))
juniMteTrigger = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1))
juniMteTriggerTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1), )
if mibBuilder.loadTexts: juniMteTriggerTable.setStatus('current')
if mibBuilder.loadTexts: juniMteTriggerTable.setDescription('A table of management event trigger information.')
juniMteTriggerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1), )
mteTriggerEntry.registerAugmentions(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerEntry"))
juniMteTriggerEntry.setIndexNames(*mteTriggerEntry.getIndexNames())
if mibBuilder.loadTexts: juniMteTriggerEntry.setStatus('current')
if mibBuilder.loadTexts: juniMteTriggerEntry.setDescription('Information about a single trigger. Applications create and delete entries using mteTriggerEntryStatus.')
juniMteTriggerContextNameLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniMteTriggerContextNameLimit.setStatus('current')
if mibBuilder.loadTexts: juniMteTriggerContextNameLimit.setDescription('The number of management contexts from which to obtain mteTriggerValueID.')
juniDismanEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2))
juniDismanEventMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1))
juniMteExistenceTestResult = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("present", 0), ("absent", 1), ("changed", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniMteExistenceTestResult.setStatus('current')
if mibBuilder.loadTexts: juniMteExistenceTestResult.setDescription('The type of existence test when an existence trigger fired.')
juniDismanEventConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3))
juniDismanEventCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1))
juniDismanEventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2))
juniDismanEventCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 1, 1)).setObjects(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDismanEventCompliance = juniDismanEventCompliance.setStatus('current')
if mibBuilder.loadTexts: juniDismanEventCompliance.setDescription('The compliance statement for entities that implement the Juniper Disman Event MIB extensions.')
juniMteTriggerTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 66, 3, 2, 1)).setObjects(("Juniper-DISMAN-EVENT-MIB", "juniMteTriggerContextNameLimit"), ("Juniper-DISMAN-EVENT-MIB", "juniMteExistenceTestResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMteTriggerTableGroup = juniMteTriggerTableGroup.setStatus('current')
if mibBuilder.loadTexts: juniMteTriggerTableGroup.setDescription('A collection of objects extending the DISMAN-EVENT-MIB.mteTriggerTable capabilities in a Juniper product.')
mibBuilder.exportSymbols("Juniper-DISMAN-EVENT-MIB", juniMteTrigger=juniMteTrigger, juniDismanEventMIB=juniDismanEventMIB, juniMteTriggerTableGroup=juniMteTriggerTableGroup, juniMteTriggerContextNameLimit=juniMteTriggerContextNameLimit, PYSNMP_MODULE_ID=juniDismanEventMIB, juniDismanEventConformance=juniDismanEventConformance, juniMteTriggerTable=juniMteTriggerTable, juniDismanEventMIBNotificationPrefix=juniDismanEventMIBNotificationPrefix, juniMteTriggerEntry=juniMteTriggerEntry, juniDismanEventMIBNotificationObjects=juniDismanEventMIBNotificationObjects, juniDismanEventGroups=juniDismanEventGroups, juniDismanEventCompliance=juniDismanEventCompliance, juniDismanEventMIBObjects=juniDismanEventMIBObjects, juniMteExistenceTestResult=juniMteExistenceTestResult, juniDismanEventCompliances=juniDismanEventCompliances)
