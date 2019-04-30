#
# PySNMP MIB module FORCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORCES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter64, IpAddress, Integer32, ObjectIdentity, mib_2, Counter32, MibIdentifier, NotificationType, Bits, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "IpAddress", "Integer32", "ObjectIdentity", "mib-2", "Counter32", "MibIdentifier", "NotificationType", "Bits", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
forcesMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 187))
forcesMib.setRevisions(('2010-03-10 00:00',))
if mibBuilder.loadTexts: forcesMib.setLastUpdated('201003100000Z')
if mibBuilder.loadTexts: forcesMib.setOrganization('IETF Forwarding and Control Element Separation (ForCES) Working Group')
forcesMibNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 0))
forcesMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 1))
forcesMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 2))
class ForcesID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class ForcesProtocolVersion(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

forcesAssociationEntryUp = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 1)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
if mibBuilder.loadTexts: forcesAssociationEntryUp.setStatus('current')
forcesAssociationEntryDown = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 2)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
if mibBuilder.loadTexts: forcesAssociationEntryDown.setStatus('current')
forcesAssociationEntryUpStats = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 3)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"), ("FORCES-MIB", "forcesAssociationTimeUp"))
if mibBuilder.loadTexts: forcesAssociationEntryUpStats.setStatus('current')
forcesAssociationEntryDownStats = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 4)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"), ("FORCES-MIB", "forcesAssociationTimeUp"), ("FORCES-MIB", "forcesAssociationTimeDown"), ("FORCES-MIB", "forcesAssociationHBMsgSent"), ("FORCES-MIB", "forcesAssociationHBMsgReceived"), ("FORCES-MIB", "forcesAssociationOperMsgSent"), ("FORCES-MIB", "forcesAssociationOperMsgReceived"), ("FORCES-MIB", "forcesAssociationCounterDiscontinuityTime"))
if mibBuilder.loadTexts: forcesAssociationEntryDownStats.setStatus('current')
forcesLatestProtocolVersionSupported = MibScalar((1, 3, 6, 1, 2, 1, 187, 1, 1), ForcesProtocolVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesLatestProtocolVersionSupported.setStatus('current')
forcesAssociations = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 1, 2))
forcesAssociationTable = MibTable((1, 3, 6, 1, 2, 1, 187, 1, 2, 1), )
if mibBuilder.loadTexts: forcesAssociationTable.setStatus('current')
forcesAssociationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1), ).setIndexNames((0, "FORCES-MIB", "forcesAssociationCEID"), (0, "FORCES-MIB", "forcesAssociationFEID"))
if mibBuilder.loadTexts: forcesAssociationEntry.setStatus('current')
forcesAssociationCEID = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 1), ForcesID())
if mibBuilder.loadTexts: forcesAssociationCEID.setStatus('current')
forcesAssociationFEID = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 2), ForcesID())
if mibBuilder.loadTexts: forcesAssociationFEID.setStatus('current')
forcesAssociationRunningProtocolVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 3), ForcesProtocolVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationRunningProtocolVersion.setStatus('current')
forcesAssociationTimeUp = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationTimeUp.setStatus('current')
forcesAssociationTimeDown = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 5), TimeStamp()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: forcesAssociationTimeDown.setStatus('current')
forcesAssociationHBMsgSent = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationHBMsgSent.setStatus('current')
forcesAssociationHBMsgReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationHBMsgReceived.setStatus('current')
forcesAssociationOperMsgSent = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationOperMsgSent.setStatus('current')
forcesAssociationOperMsgReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 9), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationOperMsgReceived.setStatus('current')
forcesAssociationCounterDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationCounterDiscontinuityTime.setStatus('current')
forcesMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 2, 1))
forcesMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 2, 2))
forcesMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 187, 2, 1, 1)).setObjects(("FORCES-MIB", "forcesMibGroup"), ("FORCES-MIB", "forcesNotificationGroup"), ("FORCES-MIB", "forcesNotificationStatsGroup"), ("FORCES-MIB", "forcesStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesMibCompliance = forcesMibCompliance.setStatus('current')
forcesNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 1)).setObjects(("FORCES-MIB", "forcesAssociationEntryUp"), ("FORCES-MIB", "forcesAssociationEntryDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesNotificationGroup = forcesNotificationGroup.setStatus('current')
forcesMibGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 2)).setObjects(("FORCES-MIB", "forcesLatestProtocolVersionSupported"), ("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesMibGroup = forcesMibGroup.setStatus('current')
forcesNotificationStatsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 3)).setObjects(("FORCES-MIB", "forcesAssociationEntryUpStats"), ("FORCES-MIB", "forcesAssociationEntryDownStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesNotificationStatsGroup = forcesNotificationStatsGroup.setStatus('current')
forcesStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 4)).setObjects(("FORCES-MIB", "forcesAssociationTimeUp"), ("FORCES-MIB", "forcesAssociationTimeDown"), ("FORCES-MIB", "forcesAssociationHBMsgSent"), ("FORCES-MIB", "forcesAssociationHBMsgReceived"), ("FORCES-MIB", "forcesAssociationOperMsgSent"), ("FORCES-MIB", "forcesAssociationOperMsgReceived"), ("FORCES-MIB", "forcesAssociationCounterDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesStatsGroup = forcesStatsGroup.setStatus('current')
mibBuilder.exportSymbols("FORCES-MIB", forcesAssociationCounterDiscontinuityTime=forcesAssociationCounterDiscontinuityTime, forcesMibCompliances=forcesMibCompliances, forcesAssociationCEID=forcesAssociationCEID, forcesAssociationHBMsgReceived=forcesAssociationHBMsgReceived, forcesAssociationEntryDown=forcesAssociationEntryDown, forcesAssociationOperMsgReceived=forcesAssociationOperMsgReceived, forcesMibCompliance=forcesMibCompliance, forcesAssociationRunningProtocolVersion=forcesAssociationRunningProtocolVersion, forcesAssociationTimeUp=forcesAssociationTimeUp, forcesAssociationEntryDownStats=forcesAssociationEntryDownStats, forcesAssociationEntryUp=forcesAssociationEntryUp, forcesMibGroup=forcesMibGroup, forcesAssociationFEID=forcesAssociationFEID, PYSNMP_MODULE_ID=forcesMib, forcesMibObjects=forcesMibObjects, forcesMib=forcesMib, forcesAssociationHBMsgSent=forcesAssociationHBMsgSent, forcesAssociationOperMsgSent=forcesAssociationOperMsgSent, ForcesID=ForcesID, forcesMibNotifications=forcesMibNotifications, forcesAssociationEntryUpStats=forcesAssociationEntryUpStats, forcesAssociationTable=forcesAssociationTable, forcesNotificationGroup=forcesNotificationGroup, forcesAssociationEntry=forcesAssociationEntry, forcesNotificationStatsGroup=forcesNotificationStatsGroup, forcesAssociations=forcesAssociations, forcesAssociationTimeDown=forcesAssociationTimeDown, ForcesProtocolVersion=ForcesProtocolVersion, forcesMibConformance=forcesMibConformance, forcesLatestProtocolVersionSupported=forcesLatestProtocolVersionSupported, forcesStatsGroup=forcesStatsGroup, forcesMibGroups=forcesMibGroups)
