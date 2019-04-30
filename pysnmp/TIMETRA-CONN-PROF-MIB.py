#
# PySNMP MIB module TIMETRA-CONN-PROF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-CONN-PROF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Unsigned32, Integer32, Counter64, ModuleIdentity, ObjectIdentity, Gauge32, IpAddress, NotificationType, iso, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Unsigned32", "Integer32", "Counter64", "ModuleIdentity", "ObjectIdentity", "Gauge32", "IpAddress", "NotificationType", "iso", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TimeStamp")
timetraSRMIBModules, tmnxSRObjs, tmnxSRNotifyPrefix, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraSRMIBModules", "tmnxSRObjs", "tmnxSRNotifyPrefix", "tmnxSRConfs")
TmnxEncapVal, TItemDescription = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxEncapVal", "TItemDescription")
timetraConnProfMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 75))
timetraConnProfMIBModule.setRevisions(('2011-02-01 00:00',))
if mibBuilder.loadTexts: timetraConnProfMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraConnProfMIBModule.setOrganization('Alcatel-Lucent')
tmnxConnProfObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75))
tmnxConnProfNtfyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 75))
tmnxConnProfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75))
tmnxConnProfConfigTimeStamps = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1))
tmnxConnProfConfigObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2))
tmnxConnProfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 75, 0))
tmnxConnProfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1))
tmnxConnProfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2))
class TmnxConnProfId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1000), )
class TmnxConnProfVlanRanges(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 200)

tmnxConnProfTblLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxConnProfTblLastChanged.setStatus('current')
tmnxConnProfTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1), )
if mibBuilder.loadTexts: tmnxConnProfTable.setStatus('current')
tmnxConnProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1), ).setIndexNames((0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"))
if mibBuilder.loadTexts: tmnxConnProfEntry.setStatus('current')
tmnxConnProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 1), TmnxConnProfId())
if mibBuilder.loadTexts: tmnxConnProfId.setStatus('current')
tmnxConnProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfRowStatus.setStatus('current')
tmnxConnProfLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxConnProfLastChanged.setStatus('current')
tmnxConnProfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 4), TItemDescription()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfDescription.setStatus('current')
tmnxConnProfVlanRange = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 5), TmnxConnProfVlanRanges()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfVlanRange.setStatus('current')
tmnxConnProfAtmMemberTblLastChgd = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxConnProfAtmMemberTblLastChgd.setStatus('current')
tmnxConnProfAtmMemberTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2), )
if mibBuilder.loadTexts: tmnxConnProfAtmMemberTable.setStatus('current')
tmnxConnProfAtmMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1), ).setIndexNames((0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"), (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberEncapValue"))
if mibBuilder.loadTexts: tmnxConnProfAtmMemberEntry.setStatus('current')
tmnxConnProfAtmMemberEncapValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1, 1), TmnxEncapVal())
if mibBuilder.loadTexts: tmnxConnProfAtmMemberEncapValue.setStatus('current')
tmnxConnProfAtmMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxConnProfAtmMemberRowStatus.setStatus('current')
tmnxConnProfV9v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1, 1)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfTimeStampGroup"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfGroup"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfV9v0Compliance = tmnxConnProfV9v0Compliance.setStatus('current')
tmnxConnV9v0Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1))
tmnxConnProfTimeStampGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 1)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfTblLastChanged"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberTblLastChgd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfTimeStampGroup = tmnxConnProfTimeStampGroup.setStatus('current')
tmnxConnProfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 2)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfRowStatus"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfLastChanged"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfDescription"), ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanRange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfGroup = tmnxConnProfGroup.setStatus('current')
tmnxConnProfAtmMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 3)).setObjects(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxConnProfAtmMemberGroup = tmnxConnProfAtmMemberGroup.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-CONN-PROF-MIB", tmnxConnProfAtmMemberGroup=tmnxConnProfAtmMemberGroup, tmnxConnProfAtmMemberRowStatus=tmnxConnProfAtmMemberRowStatus, tmnxConnProfTblLastChanged=tmnxConnProfTblLastChanged, tmnxConnProfTimeStampGroup=tmnxConnProfTimeStampGroup, PYSNMP_MODULE_ID=timetraConnProfMIBModule, tmnxConnProfNtfyPrefix=tmnxConnProfNtfyPrefix, tmnxConnProfCompliances=tmnxConnProfCompliances, tmnxConnProfGroups=tmnxConnProfGroups, tmnxConnProfTable=tmnxConnProfTable, tmnxConnProfConfigTimeStamps=tmnxConnProfConfigTimeStamps, TmnxConnProfVlanRanges=TmnxConnProfVlanRanges, tmnxConnProfLastChanged=tmnxConnProfLastChanged, TmnxConnProfId=TmnxConnProfId, tmnxConnProfNotifications=tmnxConnProfNotifications, tmnxConnProfId=tmnxConnProfId, tmnxConnProfAtmMemberEncapValue=tmnxConnProfAtmMemberEncapValue, tmnxConnProfConformance=tmnxConnProfConformance, tmnxConnProfAtmMemberTable=tmnxConnProfAtmMemberTable, tmnxConnV9v0Groups=tmnxConnV9v0Groups, tmnxConnProfObjs=tmnxConnProfObjs, tmnxConnProfGroup=tmnxConnProfGroup, tmnxConnProfConfigObjs=tmnxConnProfConfigObjs, tmnxConnProfEntry=tmnxConnProfEntry, tmnxConnProfAtmMemberTblLastChgd=tmnxConnProfAtmMemberTblLastChgd, tmnxConnProfRowStatus=tmnxConnProfRowStatus, tmnxConnProfV9v0Compliance=tmnxConnProfV9v0Compliance, tmnxConnProfDescription=tmnxConnProfDescription, tmnxConnProfAtmMemberEntry=tmnxConnProfAtmMemberEntry, tmnxConnProfVlanRange=tmnxConnProfVlanRange, timetraConnProfMIBModule=timetraConnProfMIBModule)
