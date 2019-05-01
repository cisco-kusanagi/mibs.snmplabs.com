#
# PySNMP MIB module FORCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORCES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, IpAddress, MibIdentifier, Integer32, NotificationType, ObjectIdentity, iso, TimeTicks, ModuleIdentity, mib_2, Counter32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "ObjectIdentity", "iso", "TimeTicks", "ModuleIdentity", "mib-2", "Counter32", "Counter64", "Bits")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
forcesMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 187))
forcesMib.setRevisions(('2010-03-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: forcesMib.setRevisionsDescriptions(('Initial version, published as RFC 5813.',))
if mibBuilder.loadTexts: forcesMib.setLastUpdated('201003100000Z')
if mibBuilder.loadTexts: forcesMib.setOrganization('IETF Forwarding and Control Element Separation (ForCES) Working Group')
if mibBuilder.loadTexts: forcesMib.setContactInfo('WG Charter: http://www.ietf.org/html.charters/forces-charter.html Mailing lists: General Discussion: forces@ietf.org To Subscribe: https://www.ietf.org/mailman/listinfo/forces Chairs: Patrick Droz Email: dro@zurich.ibm.com Jamal Hadi Salim Email: hadi@mojatatu.com Editor: Robert Haas IBM Email: rha@zurich.ibm.com')
if mibBuilder.loadTexts: forcesMib.setDescription("This MIB module contains managed object definitions for the ForCES Protocol. Copyright (c) 2010 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This version of this MIB module is part of RFC 5813; see the RFC itself for full legal notices.")
forcesMibNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 0))
forcesMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 1))
forcesMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 2))
class ForcesID(TextualConvention, OctetString):
    description = 'The ForCES identifier is a 4-octet quantity.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class ForcesProtocolVersion(TextualConvention, Integer32):
    description = 'ForCES protocol version number. The version numbers used are defined in the specifications of the respective protocol: 1 - ForCESv1, RFC 5810.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

forcesAssociationEntryUp = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 1)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
if mibBuilder.loadTexts: forcesAssociationEntryUp.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationEntryUp.setDescription('This notification is generated as soon as an association enters the UP state. Note that these notifications are not throttled as the CE itself should throttle the setup of associations.')
forcesAssociationEntryDown = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 2)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
if mibBuilder.loadTexts: forcesAssociationEntryDown.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationEntryDown.setDescription('This notification is generated as soon as an association leaves the UP state. Note that these notifications are not throttled as the CE itself should throttle the setup of associations.')
forcesAssociationEntryUpStats = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 3)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"), ("FORCES-MIB", "forcesAssociationTimeUp"))
if mibBuilder.loadTexts: forcesAssociationEntryUpStats.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationEntryUpStats.setDescription('This notification is generated as soon as an association enters the UP state. Note that these notifications are not throttled as the CE itself should throttle the setup of associations.')
forcesAssociationEntryDownStats = NotificationType((1, 3, 6, 1, 2, 1, 187, 0, 4)).setObjects(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"), ("FORCES-MIB", "forcesAssociationTimeUp"), ("FORCES-MIB", "forcesAssociationTimeDown"), ("FORCES-MIB", "forcesAssociationHBMsgSent"), ("FORCES-MIB", "forcesAssociationHBMsgReceived"), ("FORCES-MIB", "forcesAssociationOperMsgSent"), ("FORCES-MIB", "forcesAssociationOperMsgReceived"), ("FORCES-MIB", "forcesAssociationCounterDiscontinuityTime"))
if mibBuilder.loadTexts: forcesAssociationEntryDownStats.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationEntryDownStats.setDescription('This notification is generated as soon as an association leaves the UP state. Note that these notifications are not throttled as the CE itself should throttle the setup of associations.')
forcesLatestProtocolVersionSupported = MibScalar((1, 3, 6, 1, 2, 1, 187, 1, 1), ForcesProtocolVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesLatestProtocolVersionSupported.setStatus('current')
if mibBuilder.loadTexts: forcesLatestProtocolVersionSupported.setDescription('The ForCES protocol version supported by the CE. The current protocol version is 1. Note that the CE must also allow interaction with FEs supporting earlier versions.')
forcesAssociations = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 1, 2))
forcesAssociationTable = MibTable((1, 3, 6, 1, 2, 1, 187, 1, 2, 1), )
if mibBuilder.loadTexts: forcesAssociationTable.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationTable.setDescription('The (conceptual) table of associations.')
forcesAssociationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1), ).setIndexNames((0, "FORCES-MIB", "forcesAssociationCEID"), (0, "FORCES-MIB", "forcesAssociationFEID"))
if mibBuilder.loadTexts: forcesAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationEntry.setDescription('A (conceptual) entry for one association.')
forcesAssociationCEID = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 1), ForcesID())
if mibBuilder.loadTexts: forcesAssociationCEID.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationCEID.setDescription('The ForCES ID of the CE.')
forcesAssociationFEID = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 2), ForcesID())
if mibBuilder.loadTexts: forcesAssociationFEID.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationFEID.setDescription('The ForCES ID of the FE.')
forcesAssociationRunningProtocolVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 3), ForcesProtocolVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationRunningProtocolVersion.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationRunningProtocolVersion.setDescription('The current ForCES protocol version used in this association. The current protocol version is 1.')
forcesAssociationTimeUp = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationTimeUp.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationTimeUp.setDescription('The value of sysUpTime at the time this association entered the UP state. If this association started prior to the last initialization of the network subsystem, then this object contains a zero value. This object allows to uniquely identify associations with the same CE and FE IDs.')
forcesAssociationTimeDown = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 5), TimeStamp()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: forcesAssociationTimeDown.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationTimeDown.setDescription('The value of sysUpTime at the time this association left the UP state.')
forcesAssociationHBMsgSent = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationHBMsgSent.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationHBMsgSent.setDescription('A counter of how many Heartbeat messages have been sent by the CE on this association since the association entered the UP state. Discontinuities in the value of this counter can occur at reinitialization of the management system, and at other times as indicated by the value of forcesAssociationCounterDiscontinuityTime.')
forcesAssociationHBMsgReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationHBMsgReceived.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationHBMsgReceived.setDescription('A counter of how many Heartbeat messages have been received by the CE on this association since the association entered the UP state. Discontinuities in the value of this counter can occur at reinitialization of the management system, and at other times as indicated by the value of forcesAssociationCounterDiscontinuityTime.')
forcesAssociationOperMsgSent = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationOperMsgSent.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationOperMsgSent.setDescription('A counter of how many messages other than Heartbeat (i.e., Config and Query) have been sent by the CE on this association since the association entered the UP state. Discontinuities in the value of this counter can occur at reinitialization of the management system, and at other times as indicated by the value of forcesAssociationCounterDiscontinuityTime.')
forcesAssociationOperMsgReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 9), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationOperMsgReceived.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationOperMsgReceived.setDescription('A counter of how many messages other than Heartbeat (i.e., Config response, Query response, event notification, and packet redirect) have been received by the CE on this association since the association entered the UP state. Discontinuities in the value of this counter can occur at reinitialization of the management system, and at other times as indicated by the value of forcesAssociationCounterDiscontinuityTime.')
forcesAssociationCounterDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forcesAssociationCounterDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: forcesAssociationCounterDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which any one or more of this association's counters suffered a discontinuity. The relevant counters are the specific instances associated with this association of any ZeroBasedCounter32 object contained in the forcesAssociationTable. If no such discontinuities have occurred since the last reinitialization of the local management subsystem, then this object contains a zero value.")
forcesMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 2, 1))
forcesMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 187, 2, 2))
forcesMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 187, 2, 1, 1)).setObjects(("FORCES-MIB", "forcesMibGroup"), ("FORCES-MIB", "forcesNotificationGroup"), ("FORCES-MIB", "forcesNotificationStatsGroup"), ("FORCES-MIB", "forcesStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesMibCompliance = forcesMibCompliance.setStatus('current')
if mibBuilder.loadTexts: forcesMibCompliance.setDescription('The compliance statement for routers running ForCES and implementing the ForCES MIB.')
forcesNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 1)).setObjects(("FORCES-MIB", "forcesAssociationEntryUp"), ("FORCES-MIB", "forcesAssociationEntryDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesNotificationGroup = forcesNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: forcesNotificationGroup.setDescription('A collection of notifications for signaling important ForCES events.')
forcesMibGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 2)).setObjects(("FORCES-MIB", "forcesLatestProtocolVersionSupported"), ("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesMibGroup = forcesMibGroup.setStatus('current')
if mibBuilder.loadTexts: forcesMibGroup.setDescription('A collection of objects to support management of ForCES routers.')
forcesNotificationStatsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 3)).setObjects(("FORCES-MIB", "forcesAssociationEntryUpStats"), ("FORCES-MIB", "forcesAssociationEntryDownStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesNotificationStatsGroup = forcesNotificationStatsGroup.setStatus('current')
if mibBuilder.loadTexts: forcesNotificationStatsGroup.setDescription('A collection of optional notifications for signaling important ForCES events including statistics.')
forcesStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 187, 2, 2, 4)).setObjects(("FORCES-MIB", "forcesAssociationTimeUp"), ("FORCES-MIB", "forcesAssociationTimeDown"), ("FORCES-MIB", "forcesAssociationHBMsgSent"), ("FORCES-MIB", "forcesAssociationHBMsgReceived"), ("FORCES-MIB", "forcesAssociationOperMsgSent"), ("FORCES-MIB", "forcesAssociationOperMsgReceived"), ("FORCES-MIB", "forcesAssociationCounterDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    forcesStatsGroup = forcesStatsGroup.setStatus('current')
if mibBuilder.loadTexts: forcesStatsGroup.setDescription('A collection of optional objects to provide extra information about the associations. There is no protocol reason to keep such information, but these objects can be very useful in debugging connectivity problems.')
mibBuilder.exportSymbols("FORCES-MIB", forcesAssociationHBMsgSent=forcesAssociationHBMsgSent, forcesAssociationHBMsgReceived=forcesAssociationHBMsgReceived, forcesAssociationOperMsgReceived=forcesAssociationOperMsgReceived, forcesMibCompliances=forcesMibCompliances, forcesAssociationEntry=forcesAssociationEntry, forcesAssociationEntryDown=forcesAssociationEntryDown, forcesMibObjects=forcesMibObjects, forcesMibNotifications=forcesMibNotifications, forcesLatestProtocolVersionSupported=forcesLatestProtocolVersionSupported, forcesAssociationRunningProtocolVersion=forcesAssociationRunningProtocolVersion, forcesAssociationCEID=forcesAssociationCEID, forcesAssociationTimeUp=forcesAssociationTimeUp, forcesAssociations=forcesAssociations, forcesAssociationEntryUp=forcesAssociationEntryUp, ForcesID=ForcesID, forcesAssociationEntryDownStats=forcesAssociationEntryDownStats, forcesMib=forcesMib, forcesNotificationStatsGroup=forcesNotificationStatsGroup, forcesAssociationOperMsgSent=forcesAssociationOperMsgSent, forcesStatsGroup=forcesStatsGroup, forcesMibGroups=forcesMibGroups, forcesMibCompliance=forcesMibCompliance, forcesAssociationTable=forcesAssociationTable, PYSNMP_MODULE_ID=forcesMib, forcesNotificationGroup=forcesNotificationGroup, ForcesProtocolVersion=ForcesProtocolVersion, forcesAssociationTimeDown=forcesAssociationTimeDown, forcesAssociationFEID=forcesAssociationFEID, forcesAssociationEntryUpStats=forcesAssociationEntryUpStats, forcesAssociationCounterDiscontinuityTime=forcesAssociationCounterDiscontinuityTime, forcesMibConformance=forcesMibConformance, forcesMibGroup=forcesMibGroup)
