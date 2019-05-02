#
# PySNMP MIB module CISCO-VISM-XGCP-EXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-XGCP-EXT
# Produced by pysmi-0.3.4 at Wed May  1 12:18:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
voice, = mibBuilder.importSymbols("BASIS-MIB", "voice")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Counter64, iso, Integer32, Bits, NotificationType, MibIdentifier, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Counter64", "iso", "Integer32", "Bits", "NotificationType", "MibIdentifier", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismXgcpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 94))
ciscoVismXgcpExtMIB.setRevisions(('2003-07-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismXgcpExtMIB.setRevisionsDescriptions(('Initial version of the MIB. The content of this MIB was originally available in SMIv1 version. The MIB has been converted to SMIv2 version and descriptions of some of the objects have been modified.',))
if mibBuilder.loadTexts: ciscoVismXgcpExtMIB.setLastUpdated('200307110000Z')
if mibBuilder.loadTexts: ciscoVismXgcpExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismXgcpExtMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismXgcpExtMIB.setDescription('The MIB module contain the XGCP MIB feature in VISM')
vismXgcpExtensionGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5))
vismXgcpCoreObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1))
vismXgcpEnhancementsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2))
vismXgcpRequestMaxTimeout = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRequestMaxTimeout.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRequestMaxTimeout.setDescription(' This object specifies the maximum timeout value. This timer value is used along with xgcpRequestTimeout and xgcpRequestRetries (in xgcpGrp.my) to determine the exponential retry interval for retransmitting unacknowledged xgcp messages. The value of this timer has to be greater than or equal to xgcpRequestTimeout. The default value of this object is 500 milliseconds. When the value of this object changes vismXgcpCoreObjects changed trap will be sent. ')
vismXgcpPort = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535)).clone(2427)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpPort.setStatus('current')
if mibBuilder.loadTexts: vismXgcpPort.setDescription('This object is used to configure the local UDP port on VISM used by the SGCP and MGCP protocols to communicate with the call agent. The UDP port is used together with vismIpAddress to identify the local end of a SGCP/MGCP connection. The default value of this object is 2427. In VISM 1.5 this object always defaults to 2427 and is read-only. ')
vismXgcpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3), )
if mibBuilder.loadTexts: vismXgcpPeerTable.setStatus('current')
if mibBuilder.loadTexts: vismXgcpPeerTable.setDescription('This table is used to provision peer-specific XGCP configuration information. Each table entry corresponds to an XGCP peer name / peer XGCP variant combination. ')
vismXgcpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1), ).setIndexNames((0, "CISCO-VISM-XGCP-EXT", "vismXgcpPeerNumber"), (0, "CISCO-VISM-XGCP-EXT", "vismXgcpPeerProtocolNumber"))
if mibBuilder.loadTexts: vismXgcpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: vismXgcpPeerEntry.setDescription('Each row is identified by XGCP peer name and peer XGCP protocol number combination. This means, if an MGC uses more than one variant of XGCP (i.e MGCP, SGCP 1.0, SGCP 1.1 etc), an entry will be maintained for each of the protocols. mgcNumber and mgcProtocolNumber from MGMIB are used as foreign index to this table. Entries in this table are implicitly created by the agent. An entry shall be created when an entry is created in the mgcProtocolTable and when mgcProtocolNumber refers to an XGCP variant (i.e MGCP, SGCP 1.0, SGCP 1.1 etc) as supported protocol. An entry shall be deleted if the corresponding entry in the mgcProtocolTable is deleted. As both mgcProtocolTable and vismXgcpPeerTable have mgcNumber and mgcProtocolNumber as index, referential integrity between the two tables is automatically ensured. ')
vismXgcpPeerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpPeerNumber.setStatus('current')
if mibBuilder.loadTexts: vismXgcpPeerNumber.setDescription('The value of this object is the same as mgcNumber from MGMIB. ')
vismXgcpPeerProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpPeerProtocolNumber.setStatus('current')
if mibBuilder.loadTexts: vismXgcpPeerProtocolNumber.setDescription('The value of this object is the same as mgcProtocolNumber from MGMIB. ')
vismXgcpPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535)).clone(2427)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpPeerPort.setStatus('current')
if mibBuilder.loadTexts: vismXgcpPeerPort.setDescription('This object is used to configure the local UDP port on VISM used by the SGCP and MGCP protocols to communicate with the call agent. The UDP port is used together with vismIpAddress to identify the local end of a SGCP/MGCP connection. If the protocol configured for the call agent is MGCP 1.0, the default port is 2727. In all other cases, the default value of this object is 2427. In VISM 1.5 this object always defaults to 2427 and is read-only. ')
vismXgcpMsgStatTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4), )
if mibBuilder.loadTexts: vismXgcpMsgStatTable.setStatus('current')
if mibBuilder.loadTexts: vismXgcpMsgStatTable.setDescription('This table is an extension to the xgcpMsgStatTable contained in the XGCP MIB. This table provides per-message type based detailed statistics information. ')
vismXgcpMsgStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1), ).setIndexNames((0, "CISCO-VISM-XGCP-EXT", "vismXgcpIpAddress"))
if mibBuilder.loadTexts: vismXgcpMsgStatEntry.setStatus('current')
if mibBuilder.loadTexts: vismXgcpMsgStatEntry.setDescription('The row of the vismXgcpMsgStatTable contains additional information about XGCP message statistics beyond that provided by the XGCP MIB. ')
vismXgcpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpIpAddress.setStatus('current')
if mibBuilder.loadTexts: vismXgcpIpAddress.setDescription(' This object specifies the IP address of the Media Gateway Controller. The value of this object is the same as xgcpIpAddress of XGCP-MIB. ')
vismXgcpCrcxCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpCrcxCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpCrcxCnts.setDescription(' This refers to the count of CRCX (Create Connection) messages received from the call agent since reset. ')
vismXgcpCrcxFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpCrcxFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpCrcxFailCnts.setDescription(' This refers to the count of CRCX (Create Connection) messages received from the call agent that were responded to with a failure return code. ')
vismXgcpMdcxCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpMdcxCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpMdcxCnts.setDescription(' This refers to the count of MDCX (Modify Connection) messages received from the call agent since reset. ')
vismXgcpMdcxFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpMdcxFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpMdcxFailCnts.setDescription(' This refers to the count of MDCX (Modify Connection) messages received from the call agent that were responded to with a failure return code. ')
vismXgcpDlcxRcvCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxRcvCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpDlcxRcvCnts.setDescription(' This refers to the count of DLCX (Delete Connection) messages received from the call agent since reset. ')
vismXgcpDlcxRcvFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxRcvFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpDlcxRcvFailCnts.setDescription(' This refers to the count of DLCX (Delete Connection) messages received from the call agent that were responded to with a failure return code. ')
vismXgcpDlcxSentCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxSentCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpDlcxSentCnts.setDescription(' This refers to the count of DLCX (Delete Connection) messages sent to the call agent since reset. ')
vismXgcpDlcxSentFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxSentFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpDlcxSentFailCnts.setDescription(' This refers to the count of DLCX (Delete Connection) messages sent to the call agent for which a response with failure return code was received or which timed out waiting for an acknowledgement. ')
vismXgcpRqntCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRqntCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRqntCnts.setDescription(' This refers to the count of RQNT (Request Notify) messages received from the call agent since reset. ')
vismXgcpRqntFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRqntFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRqntFailCnts.setDescription(' This refers to the count of RQNT (Request Notify) messages received from the call agent that were responded to with a failure return code. ')
vismXgcpNtfyCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpNtfyCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpNtfyCnts.setDescription(' This refers to the count of NTFY (Notify) messages sent to the call agent since reset. ')
vismXgcpNtfyFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpNtfyFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpNtfyFailCnts.setDescription(' This refers to the count of NTFY (Notify) messages sent to the call agent for which a response with failure return code was received or which timed out waiting for a response. ')
vismXgcpAuepCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAuepCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpAuepCnts.setDescription(' This refers to the count of AUEP (Audit Endpoint) messages received from the call agent since reset. ')
vismXgcpAuepFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAuepFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpAuepFailCnts.setDescription(' This refers to the count of AUEP (Audit Endpoint) messages received from the call agent that were responded to with a failure return code. ')
vismXgcpAucxCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAucxCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpAucxCnts.setDescription(' This refers to the count of AUCX (Audit Connection) messages received from the call agent since reset. ')
vismXgcpAucxFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAucxFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpAucxFailCnts.setDescription(' This refers to the count of AUCX (Audit Connection) messages received from the call agent that were responded to with a failure return code. ')
vismXgcpRsipCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRsipCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRsipCnts.setDescription(' This refers to the count of RSIP (Restart In Progress) messages sent to the call agent since reset. ')
vismXgcpRsipFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRsipFailCnts.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRsipFailCnts.setDescription(' This refers to the count of RSIP (Restart In Progress) messages sent to the call agent for which a response with failure return code was received or which timed out waiting for a response. ')
vismXgcpRestartInProgressTdinit = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdinit.setReference(' Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Section 4.4.7 ')
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdinit.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdinit.setDescription('The endpoint becomes disconnected when it tries to communicate with the call agent and the retransmission procedure times out after retrying. The endpoint in disconnected state starts the disconnected timer initialised to the random value and uniformly distributed between 1 and initial waiting delay (Tdinit) in seconds. The gateway waits for either the end of this timer, or the reception of call agent command or the detection of local user activity for the endpoint. When the disconnected timer elapses, or when a command is received from the call agent or when there is a local user activity, the Media Gateway sends the Restart In Progress command with the restart method as RM:disconnected to the Media Gateway Controller. The initial waiting delay (Tdinit) timeout value is defined by this MIB object. The recommended value of this object is 15 seconds. ')
vismXgcpRestartInProgressTdmin = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmin.setReference(' Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Section 4.4.7 ')
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmin.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmin.setDescription('The endpoint becomes disconnected when it tries to communicate with the call agent and the retransmission procedure times out after retrying. The endpoint in disconnected state starts the disconnected timer initialised to the random value and uniformly distributed between 1 and initial waiting delay (Tdinit) in seconds. The gateway waits for either the end of this timer, or the reception of call agent command or the detection of local user activity for the endpoint. When the disconnected timer elapses, or when a command is received from the call agent or when there is a local user activity, the Media Gateway sends the Restart In Progress command with the restart method as RM:disconnected to the Media Gateway Controller. In case of local user activity, a provisionable disconnected minimum waiting delay (Tdmin) must have been elapsed since the gateway became disconnected. The minimum waiting delay (Tdmin) timeout value used by the Media Gateway to send the Restart In Progress with the restart method as RM:disconnected to the Media Gateway Controller if there is any local user activity is defined by this object. Media Gateway initiated delete connection (DLCX) or restart in progress (RSIP) commands are not considered as local user activity. The events observed on the TDM interface or on the network constitute the local user activity. The recommended value of this object is 15 seconds. ')
vismXgcpRestartInProgressTdmax = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5000)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmax.setReference(' Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Section 4.4.7 ')
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmax.setStatus('current')
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmax.setDescription('The maximum waiting delay (Tdmax) timeout value used by the Media Gateway to send the Restart In Progress with the restart method as RM:disconnected to the Media Gateway Controller when the endpoint has become disconnected is defined by this object. The endpoint becomes disconnected when it tries to communicate with the call agent and the retransmission procedure times out after retrying. The endpoint in disconnected state starts the disconnected timer initialised to the random value and uniformly distributed between 1 and initial waiting delay (Tdinit) in seconds. The gateway waits for either the end of this timer, or the reception of call agent command or the detection of local user activity for the endpoint. When the disconnected timer elapses, or when a command is received from the call agent or when there is a local user activity, the Media Gateway sends the Restart In Progress command with the restart method as RM:disconnected to the Media Gateway Controller. If the disconnected procedure still left the endpoint disconnected, the disconnected timer is doubled subject to a provisionable disconnected maximum waiting delay (Tdmax) in seconds and the gateway starts the new disconnected procedure again. Once the maximum value is reached, the subsequent disconnected Restart In Progress commands use the maximum waiting delay (Tdmax). The recommended value of this object is 600 seconds. ')
ciscoVismXgcpExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 94, 2))
ciscoVismXgcpExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1))
ciscoVismXgcpExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 2))
ciscoVismXgcpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 2, 1)).setObjects(("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpExtensionGroup"), ("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpCoreGroup"), ("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpStatsGroup"), ("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpEnhancementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismXgcpExtCompliance = ciscoVismXgcpExtCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVismXgcpExtCompliance.setDescription('The compliance statement for objects related to VISM-XGCP-MIB.')
ciscoVismXgcpExtensionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 1)).setObjects(("CISCO-VISM-XGCP-EXT", "vismXgcpRequestMaxTimeout"), ("CISCO-VISM-XGCP-EXT", "vismXgcpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismXgcpExtensionGroup = ciscoVismXgcpExtensionGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVismXgcpExtensionGroup.setDescription('The collection of objects which are used to represent VISM XGCP MIB.')
ciscoVismXgcpCoreGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 2)).setObjects(("CISCO-VISM-XGCP-EXT", "vismXgcpPeerNumber"), ("CISCO-VISM-XGCP-EXT", "vismXgcpPeerProtocolNumber"), ("CISCO-VISM-XGCP-EXT", "vismXgcpPeerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismXgcpCoreGroup = ciscoVismXgcpCoreGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVismXgcpCoreGroup.setDescription('The collection of objects which are used to represent VISM peer XGCP MIB configuration.')
ciscoVismXgcpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 3)).setObjects(("CISCO-VISM-XGCP-EXT", "vismXgcpIpAddress"), ("CISCO-VISM-XGCP-EXT", "vismXgcpCrcxCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpCrcxFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpMdcxCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpMdcxFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxRcvCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxRcvFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxSentCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxSentFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpRqntCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpRqntFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpNtfyCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpNtfyFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpAuepCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpAuepFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpAucxCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpAucxFailCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpRsipCnts"), ("CISCO-VISM-XGCP-EXT", "vismXgcpRsipFailCnts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismXgcpStatsGroup = ciscoVismXgcpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVismXgcpStatsGroup.setDescription('The collection of objects which are used to represent VISM peer XGCP MIB Statistics information.')
ciscoVismXgcpEnhancementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 4)).setObjects(("CISCO-VISM-XGCP-EXT", "vismXgcpRestartInProgressTdinit"), ("CISCO-VISM-XGCP-EXT", "vismXgcpRestartInProgressTdmin"), ("CISCO-VISM-XGCP-EXT", "vismXgcpRestartInProgressTdmax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismXgcpEnhancementGroup = ciscoVismXgcpEnhancementGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVismXgcpEnhancementGroup.setDescription('The collection of objects which are used to represent VISM XGCP Enhancement.')
mibBuilder.exportSymbols("CISCO-VISM-XGCP-EXT", vismXgcpMdcxFailCnts=vismXgcpMdcxFailCnts, vismXgcpPeerEntry=vismXgcpPeerEntry, ciscoVismXgcpExtMIBGroups=ciscoVismXgcpExtMIBGroups, vismXgcpAuepCnts=vismXgcpAuepCnts, ciscoVismXgcpExtMIB=ciscoVismXgcpExtMIB, vismXgcpAucxFailCnts=vismXgcpAucxFailCnts, vismXgcpNtfyCnts=vismXgcpNtfyCnts, vismXgcpExtensionGrp=vismXgcpExtensionGrp, ciscoVismXgcpEnhancementGroup=ciscoVismXgcpEnhancementGroup, vismXgcpMsgStatTable=vismXgcpMsgStatTable, vismXgcpDlcxRcvCnts=vismXgcpDlcxRcvCnts, vismXgcpCrcxCnts=vismXgcpCrcxCnts, PYSNMP_MODULE_ID=ciscoVismXgcpExtMIB, vismXgcpMsgStatEntry=vismXgcpMsgStatEntry, vismXgcpRsipCnts=vismXgcpRsipCnts, vismXgcpPeerPort=vismXgcpPeerPort, vismXgcpDlcxSentFailCnts=vismXgcpDlcxSentFailCnts, ciscoVismXgcpExtCompliance=ciscoVismXgcpExtCompliance, ciscoVismXgcpExtMIBConformance=ciscoVismXgcpExtMIBConformance, vismXgcpRqntCnts=vismXgcpRqntCnts, ciscoVismXgcpCoreGroup=ciscoVismXgcpCoreGroup, vismXgcpPeerProtocolNumber=vismXgcpPeerProtocolNumber, vismXgcpDlcxSentCnts=vismXgcpDlcxSentCnts, vismXgcpRequestMaxTimeout=vismXgcpRequestMaxTimeout, vismXgcpRsipFailCnts=vismXgcpRsipFailCnts, ciscoVismXgcpExtensionGroup=ciscoVismXgcpExtensionGroup, ciscoVismXgcpStatsGroup=ciscoVismXgcpStatsGroup, vismXgcpMdcxCnts=vismXgcpMdcxCnts, vismXgcpDlcxRcvFailCnts=vismXgcpDlcxRcvFailCnts, vismXgcpAucxCnts=vismXgcpAucxCnts, vismXgcpIpAddress=vismXgcpIpAddress, vismXgcpAuepFailCnts=vismXgcpAuepFailCnts, vismXgcpPeerTable=vismXgcpPeerTable, ciscoVismXgcpExtMIBCompliances=ciscoVismXgcpExtMIBCompliances, vismXgcpCrcxFailCnts=vismXgcpCrcxFailCnts, vismXgcpRestartInProgressTdinit=vismXgcpRestartInProgressTdinit, vismXgcpCoreObjects=vismXgcpCoreObjects, vismXgcpRqntFailCnts=vismXgcpRqntFailCnts, vismXgcpEnhancementsObjects=vismXgcpEnhancementsObjects, vismXgcpRestartInProgressTdmin=vismXgcpRestartInProgressTdmin, vismXgcpRestartInProgressTdmax=vismXgcpRestartInProgressTdmax, vismXgcpPeerNumber=vismXgcpPeerNumber, vismXgcpNtfyFailCnts=vismXgcpNtfyFailCnts, vismXgcpPort=vismXgcpPort)
