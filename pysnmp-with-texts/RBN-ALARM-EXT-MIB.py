#
# PySNMP MIB module RBN-ALARM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ALARM-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alarmClearIndex, alarmListName, alarmModelEntry, alarmClearDateAndTime = mibBuilder.importSymbols("ALARM-MIB", "alarmClearIndex", "alarmListName", "alarmModelEntry", "alarmClearDateAndTime")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
rbnModules, = mibBuilder.importSymbols("RBN-SMI", "rbnModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, Unsigned32, TimeTicks, ModuleIdentity, Counter64, Bits, MibIdentifier, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter64", "Bits", "MibIdentifier", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnAlarmExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 5, 53))
rbnAlarmExtMib.setRevisions(('2009-09-18 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnAlarmExtMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: rbnAlarmExtMib.setLastUpdated('200909181800Z')
if mibBuilder.loadTexts: rbnAlarmExtMib.setOrganization('Ericsson, Inc.')
if mibBuilder.loadTexts: rbnAlarmExtMib.setContactInfo(' Ericsson, Inc. 100 Headquarters Drive San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 ')
if mibBuilder.loadTexts: rbnAlarmExtMib.setDescription('This MIB module defines extensions to the alarmModelTable and alarmClearTable defined in ALARM-MIB (RFC 3877).')
rbnAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1))
rbnAlarmModel = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1))
rbnAlarmActive = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 2))
rbnAlarmClear = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3))
rbnAlarmModelTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1, 1), )
if mibBuilder.loadTexts: rbnAlarmModelTable.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmModelTable.setDescription('A table defined to augment the alarmModelTable.')
rbnAlarmModelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1, 1, 1), )
alarmModelEntry.registerAugmentions(("RBN-ALARM-EXT-MIB", "rbnAlarmModelEntry"))
rbnAlarmModelEntry.setIndexNames(*alarmModelEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAlarmModelEntry.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmModelEntry.setDescription('The set of objects which augment a conceptual row in the alarmModelTable.')
rbnAlarmModelResourceIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 512), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAlarmModelResourceIdx.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmModelResourceIdx.setDescription('The index into the varbind list of the notification indicated by alarmModelNotificationId for the object whose value identifies the resource. This object may be used to identify a resource which cannot be identified using alarmModelVarbindSubtree and alarmModelResourcePrefix. The value 0 indicates that rbnAlarmModelResourceIdx is not used. When this object is set to a value other than 0, the value of alarmActiveResourceId shall be set to the RowPointer for the corresponding varbind in the alarmActiveVariableTable. ')
rbnAlarmClearResourceTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1), )
if mibBuilder.loadTexts: rbnAlarmClearResourceTable.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceTable.setDescription('A table containing the resourceId for entries in the alarmClearTable. Each row in this table is associated with the corresponding entry in the alarmClearTable. The value of alarmClearResourceId is the RowPointer for the row in this table.')
rbnAlarmClearResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1), ).setIndexNames((0, "ALARM-MIB", "alarmListName"), (0, "ALARM-MIB", "alarmClearDateAndTime"), (0, "ALARM-MIB", "alarmClearIndex"))
if mibBuilder.loadTexts: rbnAlarmClearResourceEntry.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceEntry.setDescription('The set of object which identifies the resource for an entry in the alarmClearTable. A conceptual row in this table corresponds to the varbind in the varbindlist from a notification')
rbnAlarmClearResourceID = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceID.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceID.setDescription("The alarm variable's object identifier.")
rbnAlarmClearResourceValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceValueType.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceValueType.setDescription('The type of the value. One and only one of the value objects that follow is used for a given row in this table, based on this type.')
rbnAlarmClearResourceCounter32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceCounter32Val.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceCounter32Val.setDescription("The value when rbnAlarmClearResourceType is 'counter32'.")
rbnAlarmClearResourceUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceUnsigned32Val.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceUnsigned32Val.setDescription("The value when rbnAlarmClearResourceType is 'unsigned32'.")
rbnAlarmClearResourceTimeTicksVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceTimeTicksVal.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceTimeTicksVal.setDescription("The value when rbnAlarmClearResourceType is 'timeTicks'.")
rbnAlarmClearResourceInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceInteger32Val.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceInteger32Val.setDescription("The value when rbnAlarmClearResourceType is 'integer32'.")
rbnAlarmClearResourceOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceOctetStringVal.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceOctetStringVal.setDescription("The value when rbnAlarmClearResourceType is 'octetString'.")
rbnAlarmClearResourceIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceIpAddressVal.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceIpAddressVal.setDescription("The value when rbnAlarmClearResourceType is 'ipAddress'.")
rbnAlarmClearResourceOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceOidVal.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceOidVal.setDescription("The value when rbnAlarmClearResourceType is 'objectId'.")
rbnAlarmClearResourceCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAlarmClearResourceCounter64Val.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearResourceCounter64Val.setDescription("The value when rbnAlarmClearResourceType is 'counter64'.")
rbnAlarmExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 2))
rbnAlarmExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 1))
rbnAlarmExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 2))
rbnAlarmExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 1, 1)).setObjects(("RBN-ALARM-EXT-MIB", "rbnAlarmModelGroup"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAlarmExtCompliance = rbnAlarmExtCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmExtCompliance.setDescription('The compliance statement for systems supporting this mib.')
rbnAlarmModelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 2, 1)).setObjects(("RBN-ALARM-EXT-MIB", "rbnAlarmModelResourceIdx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAlarmModelGroup = rbnAlarmModelGroup.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmModelGroup.setDescription('Alarm model extension group')
rbnAlarmClearGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 2, 2)).setObjects(("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceID"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceValueType"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceCounter32Val"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceUnsigned32Val"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceTimeTicksVal"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceInteger32Val"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceOctetStringVal"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceIpAddressVal"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceOidVal"), ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceCounter64Val"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAlarmClearGroup = rbnAlarmClearGroup.setStatus('current')
if mibBuilder.loadTexts: rbnAlarmClearGroup.setDescription('Alarm Clear extension group')
mibBuilder.exportSymbols("RBN-ALARM-EXT-MIB", rbnAlarmClearGroup=rbnAlarmClearGroup, rbnAlarmExtMib=rbnAlarmExtMib, rbnAlarmClearResourceIpAddressVal=rbnAlarmClearResourceIpAddressVal, rbnAlarmExtCompliances=rbnAlarmExtCompliances, rbnAlarmClear=rbnAlarmClear, rbnAlarmClearResourceTimeTicksVal=rbnAlarmClearResourceTimeTicksVal, rbnAlarmExtConformance=rbnAlarmExtConformance, rbnAlarmClearResourceCounter32Val=rbnAlarmClearResourceCounter32Val, rbnAlarmExtGroups=rbnAlarmExtGroups, rbnAlarmModelResourceIdx=rbnAlarmModelResourceIdx, rbnAlarmClearResourceInteger32Val=rbnAlarmClearResourceInteger32Val, rbnAlarmClearResourceCounter64Val=rbnAlarmClearResourceCounter64Val, rbnAlarmModelTable=rbnAlarmModelTable, rbnAlarmExtCompliance=rbnAlarmExtCompliance, rbnAlarmModelEntry=rbnAlarmModelEntry, rbnAlarmClearResourceTable=rbnAlarmClearResourceTable, PYSNMP_MODULE_ID=rbnAlarmExtMib, rbnAlarmClearResourceOidVal=rbnAlarmClearResourceOidVal, rbnAlarmModel=rbnAlarmModel, rbnAlarmObjects=rbnAlarmObjects, rbnAlarmModelGroup=rbnAlarmModelGroup, rbnAlarmClearResourceOctetStringVal=rbnAlarmClearResourceOctetStringVal, rbnAlarmClearResourceID=rbnAlarmClearResourceID, rbnAlarmClearResourceUnsigned32Val=rbnAlarmClearResourceUnsigned32Val, rbnAlarmClearResourceEntry=rbnAlarmClearResourceEntry, rbnAlarmClearResourceValueType=rbnAlarmClearResourceValueType, rbnAlarmActive=rbnAlarmActive)
