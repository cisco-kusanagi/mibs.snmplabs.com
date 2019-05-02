#
# PySNMP MIB module CISCO-USER-CONNECTION-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-USER-CONNECTION-TAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, MibIdentifier, ModuleIdentity, Counter32, iso, TimeTicks, Integer32, IpAddress, ObjectIdentity, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "Counter32", "iso", "TimeTicks", "Integer32", "IpAddress", "ObjectIdentity", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoUserConnectionTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 400))
ciscoUserConnectionTapMIB.setRevisions(('2007-08-09 00:00', '2004-03-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setRevisionsDescriptions(('Correct the DESCRIPTION clause of cutcTapStreamTable.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setLastUpdated('200708090000Z')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setContactInfo('Cisco Systems Customer Service Postal:170 W. Tasman Drive San Jose, CA 95134 USA Tel:+1 800 553-NETS E-mail:cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setDescription("This module manages Cisco's intercept feature for user connections. This MIB is used along with CISCO-TAP2-MIB to intercept user traffic. CISCO-TAP2-MIB along with specific filter MIBs like this MIB replace CISCO-TAP-MIB. To create an user connection intercept, an entry cuctTapStreamEntry is created which contains the filter details. An entry cTap2StreamEntry of CISCO-TAP2-MIB is created, which is the common stream information for all kinds of intercepts and type of the specific stream is set to userconnection in this entry.")
cUserConnectionTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1))
cUserConnectionTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2))
cuctTapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1))
cuctTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("acctSessionId", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setDescription("This object displays the types of intercepts supported on this device. This may be dependent on hardware capabilities or software capabilities. The value of this object is non zero, if the device supports interception of user connection traffic. A device may support both types of intercepts at the same time. The following fields may be supported: acctSessonId: packets belonging to a user connection identified by RADIUS attribute account-session-ID may be intercepted. tapEnable: set if table entries with cTap2StreamInterceptEnable set to 'false' are used to pre-screen packets for intercept; otherwise these entries are ignored.")
cuctTapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2), )
if mibBuilder.loadTexts: cuctTapStreamTable.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamTable.setDescription("The Intercept Stream Connection Table lists the user connections (sessions) to be intercepted. The same data stream may be required by multiple taps, and one might assume that often the intercepted stream is a small subset of the traffic that could be intercepted. This essentially provides options for packet selection. The only option available is RADIUS attribute 44, account session ID. When a user tries to use a service provided by a Network Access Server(NAS) such as PPP, NAS authenticates the user with RADIUS server. Upon successful authentication of the user, the user is provided with the requested service and NAS creates an accounting record with RADIUS accounting server for the user. The NAS assigns a unique account session id for the user session in the accounting record created with the RADIUS server. The account session ID may be used to intercept traffic belonging to the user session. The value of first index is that of an entry in the cTap2MediationTable, which identifies the application to which intercepted traffic will be sent to. The second index permits connection classifiers to be used to identify traffic to be intercepted. The value of the second index is that of the stream's counter entry in the cTap2StreamTable.")
cuctTapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cuctTapStreamEntry.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamEntry.setDescription('A stream entry indicates a single data stream to be intercepted to a Mediation Device. Many selected data streams may go to the same application interface, and many application interfaces are supported.')
cuctTapStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setReference('RFC 2059, RFC 2865')
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setDescription('This is the RADIUS attribute 44 acct-session-ID. It identifies a user connection. It is used to specify a user connection to intercept.')
cuctTapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamStatus.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamStatus.setDescription("The status of this conceptual row. This object manages creation, modification, and deletion of rows in this table. When any rows must be changed, cuctTapStreamStatus must be first set to 'notInService'.")
cUserConnectionTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1))
cUserConnectionTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2))
cUserConnectionTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cUserConnectionTapMIBCompliance = cUserConnectionTapMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cUserConnectionTapMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Intercept MIB for user connections.')
cuctTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamCapabilities"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamAcctSessID"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cuctTapStreamComplianceGroup = cuctTapStreamComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamComplianceGroup.setDescription('These objects are necessary for a description of user traffic packets to select for interception.')
mibBuilder.exportSymbols("CISCO-USER-CONNECTION-TAP-MIB", cUserConnectionTapMIBConform=cUserConnectionTapMIBConform, cuctTapStreamEncodePacket=cuctTapStreamEncodePacket, cUserConnectionTapMIBGroups=cUserConnectionTapMIBGroups, PYSNMP_MODULE_ID=ciscoUserConnectionTapMIB, ciscoUserConnectionTapMIB=ciscoUserConnectionTapMIB, cuctTapStreamCapabilities=cuctTapStreamCapabilities, cUserConnectionTapMIBObjects=cUserConnectionTapMIBObjects, cuctTapStreamStatus=cuctTapStreamStatus, cUserConnectionTapMIBCompliances=cUserConnectionTapMIBCompliances, cuctTapStreamTable=cuctTapStreamTable, cuctTapStreamAcctSessID=cuctTapStreamAcctSessID, cuctTapStreamComplianceGroup=cuctTapStreamComplianceGroup, cUserConnectionTapMIBCompliance=cUserConnectionTapMIBCompliance, cuctTapStreamEntry=cuctTapStreamEntry)
