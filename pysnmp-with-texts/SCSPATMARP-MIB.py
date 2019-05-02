#
# PySNMP MIB module SCSPATMARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCSPATMARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
AtmConnKind, AtmAddr = mibBuilder.importSymbols("ATM-TC-MIB", "AtmConnKind", "AtmAddr")
scspLSID, ScspHFSMStateType, scspServerGroupPID, SCSPVCIInteger, SCSPVPIInteger, scspServerGroupID, scspDCSID = mibBuilder.importSymbols("SCSP-MIB", "scspLSID", "ScspHFSMStateType", "scspServerGroupPID", "SCSPVCIInteger", "SCSPVPIInteger", "scspServerGroupID", "scspDCSID")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, Counter32, Counter64, NotificationType, Unsigned32, experimental, iso, Bits, MibIdentifier, Integer32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "Counter64", "NotificationType", "Unsigned32", "experimental", "iso", "Bits", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
scspAtmarpMIB = ModuleIdentity((1, 3, 6, 1, 3, 2002))
if mibBuilder.loadTexts: scspAtmarpMIB.setLastUpdated('9808020000Z')
if mibBuilder.loadTexts: scspAtmarpMIB.setOrganization('IETF Internetworking Over NBMA Working Group (ion)')
if mibBuilder.loadTexts: scspAtmarpMIB.setContactInfo('Jim Luciani (jliciani@BayNetworks.com Bay Networks Cliff X. Wang (cliff_wang@vnet.ibm.com) Colin Verrilli (verrilli@vnet.ibm.com) IBM Corp.')
if mibBuilder.loadTexts: scspAtmarpMIB.setDescription('This module defines a portion of the management information base (MIB) for managing Server Cache Synchronizatio protocol applied to ATMARP servers.')
scspAtmarpObjects = MibIdentifier((1, 3, 6, 1, 3, 2002, 1))
scspAtmarpNotifications = MibIdentifier((1, 3, 6, 1, 3, 2002, 2))
scspAtmarpConformance = MibIdentifier((1, 3, 6, 1, 3, 2002, 3))
scspAtmarpServerGroupTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 1), )
if mibBuilder.loadTexts: scspAtmarpServerGroupTable.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpServerGroupTable.setDescription('The objects defined in this table are used to for the management of SCSP server groups with application to IP over ATM operation (Classic IP). These objects SHOULD be used along with the protocol independent part objects to support the management of the SCSP protocol applied to synchronizing the atmarp servers in a LIS. There is one entry in this table for each server group. In the case of IP over ATM, each server group corresponds to a Logical IP Subnet.')
scspAtmarpServerGroupEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 1, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"))
if mibBuilder.loadTexts: scspAtmarpServerGroupEntry.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpServerGroupEntry.setDescription('Information about SCSP server group running IP over ATM operation. This table is indexed by scspServerGroupID and scspServerGroupPID. The two indeces point to a corresponding entry in the scspServerGroupTable.')
scspAtmarpServerGroupNetMask = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpServerGroupNetMask.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpServerGroupNetMask.setDescription('The subnet mask associated with this Server Group.')
scspAtmarpServerGroupSubnetAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpServerGroupSubnetAddr.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpServerGroupSubnetAddr.setDescription('The IP subnet address associated with this Server Group.')
scspAtmarpServerGroupRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpServerGroupRowStatus.setReference("RFC 1903, 'Textual Conventions for version 2 of the Simple Network Management Protocol (SNMPv2).'")
if mibBuilder.loadTexts: scspAtmarpServerGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpServerGroupRowStatus.setDescription('This object allows Atmarp Server Group Table entries to be created and deleted from the scspAtmarpServerGroupTable. Note that scspAtmarpServerGroupTable entry creation and deletion is coupled with scspServerGroupTable entry creation and deletion. A scspAtmarpServerGroupTable entry cannot be created until its corresponding scspServerGroupTable entry is created. When a scspServerGroupTable entry is deleted, it also removes the corresponding scspAtmarpServerGroupTable entry.')
scspAtmarpLSTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 2), )
if mibBuilder.loadTexts: scspAtmarpLSTable.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpLSTable.setDescription('The objects defined in this table are used to for the management of the Atmarp Local server in a SCSP server group for IP over ATM operation. These objects SHOULD be used along with the protocol independent part objects to support the management of the SCSP protocol applied to synchronizing the IP over ATM servers.')
scspAtmarpLSEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 2, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"), (0, "SCSP-MIB", "scspLSID"))
if mibBuilder.loadTexts: scspAtmarpLSEntry.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpLSEntry.setDescription('Information about Atmarp Local Server in a SCSP server group. This table is indexed by scspServerGroupID, scspServerGroupPID, and scspLSID. The three indeces point to a corresponding entry in the scspLSTable.')
scspAtmarpLSLSIPAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpLSLSIPAddr.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpLSLSIPAddr.setDescription('The IP address of the Atmarp Local Server. Since an Atmarp server does not have to be assigned an IP address, this object is optional.')
scspAtmarpLSLSAtmAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 2, 1, 2), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpLSLSAtmAddr.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpLSLSAtmAddr.setDescription('The ATM address of the Atmarp Local Server.')
scspAtmarpLSRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpLSRowStatus.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpLSRowStatus.setDescription('This object allows Atmarp Local Server Table entries to be created and deleted from the scspAtmarpLSTable. Note that scspAtmarpLSTable entry creation and deletion is coupled with scspLSTable entry creation and deletion. A scspAtmarpLSTable entry cannot be created until its corresponding scspLSTable entry is created. When a scspLSTable entry is deleted, it also removes the corresponding scspAtmarpLSTable entry.')
scspAtmarpPeerTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 3), )
if mibBuilder.loadTexts: scspAtmarpPeerTable.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerTable.setDescription('The objects defined in this table are used to for the management of the ATMARP sever peers.')
scspAtmarpPeerEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 3, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"), (0, "SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspAtmarpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerEntry.setDescription('Information about each peer ATMARP server participated in the scsp Server group. The table is indexed by scspServerGroupID, scspServerGroupPID, and scspAtmarpPeerIndex.')
scspAtmarpPeerIndex = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerIndex.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerIndex.setDescription('The table index of the peer Atmarp server table.')
scspAtmarpPeerIPAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerIPAddr.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerIPAddr.setDescription('The IP address of the peer Atmarp server. Since an Atmarp server does not have to be assigned an IP address, this object is optional.')
scspAtmarpPeerAtmAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 3), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerAtmAddr.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerAtmAddr.setDescription("The ATM address of the Peer. If SVC is used between LS and Peer, Peer's ATM address should be valid. However, if PVC is used instead SVC, the Peer's ATM address may be a Null OCTET STRING.")
scspAtmarpPeerVCType = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 4), AtmConnKind()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerVCType.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerVCType.setDescription('The type of the virtual circuit between LS and Peer.')
scspAtmarpPeerVPI = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 5), SCSPVPIInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerVPI.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerVPI.setDescription('The VPI value for the virtual circuit between LS and Peer.')
scspAtmarpPeerVCI = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 6), SCSPVCIInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerVCI.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerVCI.setDescription('The VCI value for the virtual circuit between LS and Peer.')
scspAtmarpPeerDCSID = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerDCSID.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerDCSID.setDescription('The DCS ID for this peer. When the peer tabel is created, DCS ID may not have been discovered. Tt is set to a Null string. It will be update when the DCS ID associated with this peer (ATM address) is discovered.')
scspAtmarpPeerRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpPeerRowStatus.setReference("RFC 1903, 'Textual Conventions for version 2 of the Simple Network Management Protocol (SNMPv2).'")
if mibBuilder.loadTexts: scspAtmarpPeerRowStatus.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpPeerRowStatus.setDescription('This object allows Atmarp Peer table entries to be created and deleted from the scspAtmarpPeerTable. Note that scspAtmarpPeerTable entry is created when a peer is configured loaclly or when a peer not previously configured connects to LS.')
scspAtmarpHFSMTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 4), )
if mibBuilder.loadTexts: scspAtmarpHFSMTable.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpHFSMTable.setDescription('The objects defined in this table are used to for the management of the HFSM between the LS and the DCS.')
scspAtmarpHFSMEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 4, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"), (0, "SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspAtmarpHFSMEntry.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpHFSMEntry.setDescription('Information about SCSP HFSM session between the LS and its HFSMs. The table is indexed by scspServerGroupID, scspServerGroupPID, and scspAtmarpPeerIndex.')
scspHFSMHFSMState = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 1), ScspHFSMStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHFSMState.setReference('SCSP draft, Section 2.1')
if mibBuilder.loadTexts: scspHFSMHFSMState.setStatus('current')
if mibBuilder.loadTexts: scspHFSMHFSMState.setDescription('The current state of the Hello Finite State Machine. The allowable states are: down(1), waiting(2), uniConn(3), biConn(4).')
scspHFSMHelloIn = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHelloIn.setStatus('current')
if mibBuilder.loadTexts: scspHFSMHelloIn.setDescription("The number of 'Hello' messages received from this HFSM.")
scspHFSMHelloOut = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHelloOut.setStatus('current')
if mibBuilder.loadTexts: scspHFSMHelloOut.setDescription("The number of 'Hello' messages sent from LS to this HFSM.")
scspHFSMHelloInvalidIn = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHelloInvalidIn.setStatus('current')
if mibBuilder.loadTexts: scspHFSMHelloInvalidIn.setDescription("The number of invalid 'Hello' messages received from this HFSM. Possible message errors include: Hello message when the HFSM is in 'Down' state; Hello message is too short to contain the number of Receiver ID records specified in the header, etc. Other common errors include failed authentication if applicable, errors in the message fields, etc.")
scspHFSMHelloInterval = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspHFSMHelloInterval.setStatus('current')
if mibBuilder.loadTexts: scspHFSMHelloInterval.setDescription('This object contains the value for HelloInterval with the associated HFSM. It is the time (in seconds) between sending of consecutive Hello messages from the HFSM.')
scspHFSMDeadFactor = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspHFSMDeadFactor.setStatus('current')
if mibBuilder.loadTexts: scspHFSMDeadFactor.setDescription("This object contains the value for DeadFactor with this associated server. The DeadFactor along with HelloInterval are contained in 'Hello' messages sent from this HFSM. If 'Hello' messages are not received from this HFSM within the time out interval 'HelloInterval*DeadFactor' (in seconds), then the HFSM MUST be considered to be stalled.")
scspHFSMFamilyID = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMFamilyID.setReference('SCSP draft, Sec.2 and Sec. B.2.5')
if mibBuilder.loadTexts: scspHFSMFamilyID.setStatus('current')
if mibBuilder.loadTexts: scspHFSMFamilyID.setDescription('The family ID is used to refer an aggregate of Protocol ID/SGID pairs. Only a single HFSM is run for all Protocol ID/SGID pairs assigned to a Family ID. When the HFSM is not shared by an aggregate of Protocol ID/SGID pairs, this object should be set to 0.')
scspAtmarpHFSMRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpHFSMRowStatus.setReference("RFC 1903, 'Textual Conventions for version 2 of the Simple Network Management Protocol (SNMPv2).'")
if mibBuilder.loadTexts: scspAtmarpHFSMRowStatus.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpHFSMRowStatus.setDescription('This object allows Atmarp HFSM table entries to be created and deleted from the scspAtmarpHFSMTable. Note that scspAtmarpHFSMTable entry creation and deletion is closely coupled with scspHFSMTable entry creation. A scspAtmarpHFSMTable entry cannot be created until its corresponding scspHFSMTable entry is created. When a scspHFSMTable entry is deleted, it also removes the corresponding scspAtmarpHFSMTable entry.')
scspHFSMDown = NotificationType((1, 3, 6, 1, 3, 2002, 2, 1)).setObjects(("SCSP-MIB", "scspServerGroupID"), ("SCSP-MIB", "scspServerGroupPID"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspHFSMDown.setStatus('current')
if mibBuilder.loadTexts: scspHFSMDown.setDescription("The Hello Finite State Machine associated with this LS/DCS pair enters 'Down' state.")
scspHFSMWaiting = NotificationType((1, 3, 6, 1, 3, 2002, 2, 2)).setObjects(("SCSP-MIB", "scspServerGroupID"), ("SCSP-MIB", "scspServerGroupPID"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspHFSMWaiting.setStatus('current')
if mibBuilder.loadTexts: scspHFSMWaiting.setDescription("The Hello Finite State Machine associated with this LS/DCS pair enters 'Waiting' state.")
scspHFSMBiConn = NotificationType((1, 3, 6, 1, 3, 2002, 2, 3)).setObjects(("SCSP-MIB", "scspServerGroupID"), ("SCSP-MIB", "scspServerGroupPID"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspHFSMBiConn.setStatus('current')
if mibBuilder.loadTexts: scspHFSMBiConn.setDescription("The Hello Finite State Machine associated with this LS/DCS pair enters 'Bidirectional connection' state.")
scspAtmarpCompliances = MibIdentifier((1, 3, 6, 1, 3, 2002, 3, 1))
scspAtmarpGroups = MibIdentifier((1, 3, 6, 1, 3, 2002, 3, 2))
scspAtmarpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 2002, 3, 1, 1)).setObjects(("SCSPATMARP-MIB", "scspAtmarpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scspAtmarpCompliance = scspAtmarpCompliance.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpCompliance.setDescription('The compliance statement for entities that are required for the management of SCSP when applied to ATMARP servers.')
scspAtmarpGroup = ObjectGroup((1, 3, 6, 1, 3, 2002, 3, 2, 1)).setObjects(("SCSPATMARP-MIB", "scspAtmarpServerGroupNetMask"), ("SCSPATMARP-MIB", "scspAtmarpServerGroupSubnetAddr"), ("SCSPATMARP-MIB", "scspAtmarpLSLSIPAddr"), ("SCSPATMARP-MIB", "scspAtmarpLSLSAtmAddr"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"), ("SCSPATMARP-MIB", "scspAtmarpPeerAtmAddr"), ("SCSPATMARP-MIB", "scspAtmarpPeerVCType"), ("SCSPATMARP-MIB", "scspAtmarpPeerVPI"), ("SCSPATMARP-MIB", "scspAtmarpPeerVCI"), ("SCSPATMARP-MIB", "scspAtmarpPeerDCSID"), ("SCSPATMARP-MIB", "scspHFSMHFSMState"), ("SCSPATMARP-MIB", "scspHFSMHelloIn"), ("SCSPATMARP-MIB", "scspHFSMHelloOut"), ("SCSPATMARP-MIB", "scspHFSMHelloInvalidIn"), ("SCSPATMARP-MIB", "scspHFSMHelloInterval"), ("SCSPATMARP-MIB", "scspHFSMDeadFactor"), ("SCSPATMARP-MIB", "scspHFSMFamilyID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scspAtmarpGroup = scspAtmarpGroup.setStatus('current')
if mibBuilder.loadTexts: scspAtmarpGroup.setDescription('This group is mandatory when Atmarp is the client/server protocol running SCSP.')
mibBuilder.exportSymbols("SCSPATMARP-MIB", scspAtmarpObjects=scspAtmarpObjects, scspHFSMHelloOut=scspHFSMHelloOut, scspHFSMWaiting=scspHFSMWaiting, scspAtmarpGroups=scspAtmarpGroups, scspAtmarpPeerVCI=scspAtmarpPeerVCI, scspAtmarpCompliance=scspAtmarpCompliance, scspAtmarpConformance=scspAtmarpConformance, scspAtmarpLSRowStatus=scspAtmarpLSRowStatus, scspAtmarpServerGroupNetMask=scspAtmarpServerGroupNetMask, scspAtmarpPeerRowStatus=scspAtmarpPeerRowStatus, scspAtmarpHFSMTable=scspAtmarpHFSMTable, scspAtmarpPeerDCSID=scspAtmarpPeerDCSID, scspAtmarpServerGroupEntry=scspAtmarpServerGroupEntry, scspAtmarpPeerTable=scspAtmarpPeerTable, scspAtmarpLSLSAtmAddr=scspAtmarpLSLSAtmAddr, scspHFSMFamilyID=scspHFSMFamilyID, scspAtmarpServerGroupTable=scspAtmarpServerGroupTable, scspAtmarpLSTable=scspAtmarpLSTable, scspHFSMDeadFactor=scspHFSMDeadFactor, scspHFSMHelloInterval=scspHFSMHelloInterval, scspAtmarpLSEntry=scspAtmarpLSEntry, scspAtmarpPeerEntry=scspAtmarpPeerEntry, scspHFSMHFSMState=scspHFSMHFSMState, scspAtmarpLSLSIPAddr=scspAtmarpLSLSIPAddr, scspAtmarpPeerAtmAddr=scspAtmarpPeerAtmAddr, scspHFSMHelloIn=scspHFSMHelloIn, scspAtmarpGroup=scspAtmarpGroup, scspAtmarpNotifications=scspAtmarpNotifications, scspAtmarpServerGroupRowStatus=scspAtmarpServerGroupRowStatus, scspAtmarpMIB=scspAtmarpMIB, scspAtmarpHFSMEntry=scspAtmarpHFSMEntry, scspAtmarpPeerIndex=scspAtmarpPeerIndex, PYSNMP_MODULE_ID=scspAtmarpMIB, scspAtmarpServerGroupSubnetAddr=scspAtmarpServerGroupSubnetAddr, scspHFSMHelloInvalidIn=scspHFSMHelloInvalidIn, scspHFSMBiConn=scspHFSMBiConn, scspAtmarpHFSMRowStatus=scspAtmarpHFSMRowStatus, scspAtmarpPeerVCType=scspAtmarpPeerVCType, scspAtmarpPeerIPAddr=scspAtmarpPeerIPAddr, scspAtmarpCompliances=scspAtmarpCompliances, scspHFSMDown=scspHFSMDown, scspAtmarpPeerVPI=scspAtmarpPeerVPI)
