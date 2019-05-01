#
# PySNMP MIB module CISCO-AAA-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-SESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, MibIdentifier, IpAddress, Counter32, Integer32, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibIdentifier", "IpAddress", "Counter32", "Integer32", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Bits", "Gauge32")
TextualConvention, TruthValue, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowPointer", "DisplayString")
ciscoAAASessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 150))
ciscoAAASessionMIB.setRevisions(('2006-03-21 00:00', '2002-04-11 00:00', '1999-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAAASessionMIB.setRevisionsDescriptions(('Added the casnNasPort and casnVaiIfIndex objects to the casnActiveTable. ', 'Imported Unsigned32 from SNMPv2-SMI instead of CISCO-TC ', 'Initial version ',))
if mibBuilder.loadTexts: ciscoAAASessionMIB.setLastUpdated('200603210000Z')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setDescription('This MIB module provides data for accounting sessions based on Authentication, Authorization, Accounting (AAA) protocols. References: RFC 2139 RADIUS Accounting The TACACS+ Protocol Version 1.78, Internet Draft ')
class CctCallId(TextualConvention, Unsigned32):
    description = 'Represents a Call Identifier. The call identifier is used as an unique identifier for an call within the system. A zero value indicates no call ID. '
    status = 'current'

class CasnSessionId(TextualConvention, Unsigned32):
    description = 'Represents an Accounting Session Identifier. The session identifier is used as an unique identifier for a session within the system. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

casnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1))
casnActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1))
casnGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2))
casnActiveTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableEntries.setStatus('current')
if mibBuilder.loadTexts: casnActiveTableEntries.setDescription('Number of entries currently in casnActiveTable ')
casnActiveTableHighWaterMark = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableHighWaterMark.setStatus('current')
if mibBuilder.loadTexts: casnActiveTableHighWaterMark.setDescription('Maximum number of entries present in casnActiveTable since last system re-initialization. This corresponds to the maximum value reported by casnActiveTableEntries. ')
casnActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3), )
if mibBuilder.loadTexts: casnActiveTable.setStatus('current')
if mibBuilder.loadTexts: casnActiveTable.setDescription('This table contains entries for active AAA accounting sessions in the system. ')
casnActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-AAA-SESSION-MIB", "casnSessionId"))
if mibBuilder.loadTexts: casnActiveEntry.setStatus('current')
if mibBuilder.loadTexts: casnActiveEntry.setDescription('The information regarding a single accounting session. Entries are created when a new accounting session is begun. Entries are removed when the accounting session is ended. Initiating termination of a session with the object casnDisconnect will cause removal of the entry when the session completes termination. ')
casnSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 1), CasnSessionId())
if mibBuilder.loadTexts: casnSessionId.setStatus('current')
if mibBuilder.loadTexts: casnSessionId.setDescription("This is the session identification used by the accounting protocol. This value is unique to a session within the system, even if multiple accounting protocols are in use. The value of this object corresponds to these accounting protocol attributes. RADIUS: attribute 44, Acct-Session-Id TACACS+: attribute 'task_id' ")
casnUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnUserId.setStatus('current')
if mibBuilder.loadTexts: casnUserId.setDescription("The User login ID or zero length string if unavailable. The value of this object corresponds to these accounting protocol attributes. RADIUS: attribute 1, User-Name TACACS+: attribute 'user' ")
casnIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIpAddr.setStatus('current')
if mibBuilder.loadTexts: casnIpAddr.setDescription("The IP address of the session or 0.0.0.0 if not applicable or unavailable. RADIUS: attribute 8, Framed-IP-Address TACACS+: attribute 'addr' ")
casnIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 4), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIdleTime.setStatus('current')
if mibBuilder.loadTexts: casnIdleTime.setDescription('The elapsed time that this session has been idle. This is the time since the last user-level data has been received or transmitted. Protocol level handshaking associated with the call is considered to be idle for this object. ')
casnDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: casnDisconnect.setStatus('current')
if mibBuilder.loadTexts: casnDisconnect.setDescription('This object is used to terminate this session. Setting the value to true(1) will initiate termination of this session. The entry will be removed once the session has completed termination. Once this object has been set to true(1), the session termination process can not be cancelled by setting the value false(2). ')
casnCallTrackerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 6), CctCallId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnCallTrackerId.setStatus('current')
if mibBuilder.loadTexts: casnCallTrackerId.setDescription('The value of this object is the entry index in the CISCO-CALL-TRACKER-MIB cctActiveTable of the call corresponding to this accounting session. Using the value of this object to query the cctActiveTable will provide more detailed data regarding the session represented by this casnActiveEntry. ')
casnNasPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnNasPort.setStatus('current')
if mibBuilder.loadTexts: casnNasPort.setDescription('The value of this object identifies a particular conceptual row associated with the session identified by casnSessionId. The conceptual row that this object points to represents a port that is used to transport a session. If the port transporting the session cannot be determined, the value of this object will be zeroDotZero. For example, suppose a session is established using an ATM PVC. If the ifIndex of the ATM interface is 7, and the VPI/VCI values of the PVC are 1, 100 respectively, then the value of this object might be as follows: casnNasPort.15 = atmVclAdminStatus.7.1.100 ^ ^ ^ ^ | | | | casnSessionId --+ | | | ifIndex -------------------------+ | | atmVclVpi ---------------------------+ | atmVclVci ------------------------------+ where atmVclAdminStatus is the first accessible object of the atmVclTable of the ATM-MIB. ')
casnVaiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnVaiIfIndex.setStatus('current')
if mibBuilder.loadTexts: casnVaiIfIndex.setDescription('The ifIndex of the Virtual Access Interface (VAI) that is associated with the PPP session. This interface may not be represented in the IF-MIB in which case the value of this object will be zero. ')
casnTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnTotalSessions.setStatus('current')
if mibBuilder.loadTexts: casnTotalSessions.setDescription('Total number of sessions since last system re-initialization. This value includes all sessions currently in the casnActiveTable and all previous sessions whether terminated via casnDisconnect or via other mechanisms. ')
casnDisconnectedSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnDisconnectedSessions.setStatus('current')
if mibBuilder.loadTexts: casnDisconnectedSessions.setDescription('Total number of sessions which have been disconnected using casnDisconnect since last system re-initialization. This value includes any sessions still in the casnActiveTable with a casnDisconnect value of true(1) and all previous sessions which terminated as a result of setting casnDisconnect. ')
casnMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2))
casnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2, 1))
casnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3))
casnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1))
casnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2))
casnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBCompliance = casnMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: casnMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO AAA Session MIB')
casnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"), ("CISCO-AAA-SESSION-MIB", "casnActiveGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBComplianceRev1 = casnMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: casnMIBComplianceRev1.setDescription('The compliance statement for entities which implement the CISCO AAA Session MIB')
casnActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveTableEntries"), ("CISCO-AAA-SESSION-MIB", "casnActiveTableHighWaterMark"), ("CISCO-AAA-SESSION-MIB", "casnUserId"), ("CISCO-AAA-SESSION-MIB", "casnIpAddr"), ("CISCO-AAA-SESSION-MIB", "casnIdleTime"), ("CISCO-AAA-SESSION-MIB", "casnDisconnect"), ("CISCO-AAA-SESSION-MIB", "casnCallTrackerId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroup = casnActiveGroup.setStatus('current')
if mibBuilder.loadTexts: casnActiveGroup.setDescription('A collection of objects providing the AAA session information. ')
casnGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnTotalSessions"), ("CISCO-AAA-SESSION-MIB", "casnDisconnectedSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnGeneralGroup = casnGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: casnGeneralGroup.setDescription('A collection of objects providing the AAA session information. ')
casnActiveGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 3)).setObjects(("CISCO-AAA-SESSION-MIB", "casnNasPort"), ("CISCO-AAA-SESSION-MIB", "casnVaiIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroupSup1 = casnActiveGroupSup1.setStatus('current')
if mibBuilder.loadTexts: casnActiveGroupSup1.setDescription('A collection of objects that supplements the casnActiveGroup. ')
mibBuilder.exportSymbols("CISCO-AAA-SESSION-MIB", casnActiveTableHighWaterMark=casnActiveTableHighWaterMark, casnDisconnect=casnDisconnect, casnActiveGroup=casnActiveGroup, casnActiveTable=casnActiveTable, casnUserId=casnUserId, casnNasPort=casnNasPort, PYSNMP_MODULE_ID=ciscoAAASessionMIB, casnCallTrackerId=casnCallTrackerId, casnSessionId=casnSessionId, casnIpAddr=casnIpAddr, casnGeneralGroup=casnGeneralGroup, CctCallId=CctCallId, casnVaiIfIndex=casnVaiIfIndex, casnMIBNotificationPrefix=casnMIBNotificationPrefix, casnMIBCompliance=casnMIBCompliance, ciscoAAASessionMIB=ciscoAAASessionMIB, casnActive=casnActive, casnActiveEntry=casnActiveEntry, casnIdleTime=casnIdleTime, casnDisconnectedSessions=casnDisconnectedSessions, casnMIBComplianceRev1=casnMIBComplianceRev1, casnMIBNotifications=casnMIBNotifications, casnGeneral=casnGeneral, CasnSessionId=CasnSessionId, casnMIBGroups=casnMIBGroups, casnActiveGroupSup1=casnActiveGroupSup1, casnMIBObjects=casnMIBObjects, casnTotalSessions=casnTotalSessions, casnMIBConformance=casnMIBConformance, casnActiveTableEntries=casnActiveTableEntries, casnMIBCompliances=casnMIBCompliances)
