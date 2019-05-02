#
# PySNMP MIB module MPLS-TE-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-TE-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
IndexIntegerNextFree, = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexIntegerNextFree")
MplsGlobalId, MplsCcId, MplsIccId, MplsNodeId = mibBuilder.importSymbols("MPLS-TC-EXT-STD-MIB", "MplsGlobalId", "MplsCcId", "MplsIccId", "MplsNodeId")
MplsExtendedTunnelId, MplsTunnelInstanceIndex, mplsStdMIB, MplsTunnelIndex = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsExtendedTunnelId", "MplsTunnelInstanceIndex", "mplsStdMIB", "MplsTunnelIndex")
mplsTunnelInstance, mplsTunnelIndex, mplsTunnelIngressLSRId, mplsTunnelEgressLSRId = mibBuilder.importSymbols("MPLS-TE-STD-MIB", "mplsTunnelInstance", "mplsTunnelIndex", "mplsTunnelIngressLSRId", "mplsTunnelEgressLSRId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, TimeTicks, Integer32, Counter64, NotificationType, Unsigned32, MibIdentifier, ObjectIdentity, Bits, Gauge32, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "TimeTicks", "Integer32", "Counter64", "NotificationType", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Bits", "Gauge32", "IpAddress", "Counter32")
RowPointer, TextualConvention, StorageType, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TextualConvention", "StorageType", "TruthValue", "RowStatus", "DisplayString")
mplsTeExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 20))
mplsTeExtStdMIB.setRevisions(('2015-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTeExtStdMIB.setRevisionsDescriptions(('MPLS TE MIB objects extension',))
if mibBuilder.loadTexts: mplsTeExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsTeExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsTeExtStdMIB.setContactInfo(' Venkatesan Mahalingam Dell Inc, 5450 Great America Parkway, Santa Clara, CA 95054, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Redeem, India Email: kannankvs@gmail.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau Email: tnadeau@lucidvision.com ')
if mibBuilder.loadTexts: mplsTeExtStdMIB.setDescription("This MIB module contains generic object definitions for extending the MPLS Traffic Engineering tunnels in transport networks. Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
mplsTeExtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 20, 0))
mplsTeExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 20, 1))
mplsTunnelExtNodeConfigLocalIdNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 1), IndexIntegerNextFree().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigLocalIdNext.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigLocalIdNext.setDescription('This object contains an unused value for mplsTunnelExtNodeConfigLocalId, or a zero to indicate that none exist. Negative values are not allowed, as they do not correspond to valid values of mplsTunnelExtNodeConfigLocalId.')
mplsTunnelExtNodeConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2), )
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigTable.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigTable.setDescription("This table allows the operator to map a node or LSR identifier (IP-compatible [Global_ID::Node_ID] or ICC-based [ICC_Operator_ID::Node_ID]) with a local identifier. This table is created to reuse the existing mplsTunnelTable for MPLS-based transport network tunnels also. Since the MPLS tunnel's Ingress/Egress LSR identifiers' size (Unsigned32) value is not compatible for MPLS-TP Tunnel, i.e., Global_ID::Node_ID of size 8 bytes and ICC_Operator_ID::Node_ID of size 12 bytes, there exists a need to map the Global_ID::Node_ID or ICC_Operator_ID::Node_ID with the local identifier of size 4 bytes (Unsigned32) value in order to index (Ingress/Egress LSR identifier) the existing mplsTunnelTable.")
mplsTunnelExtNodeConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1), ).setIndexNames((0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigLocalId"))
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigEntry.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigEntry.setDescription('An entry in this table represents a mapping identification for the operator or service provider to a node or an LSR. As per RFC 6370, IP-compatible mapping is represented as Global_ID::Node_ID. As per RFC 6923, the CC and the ICC form the ICC_Operator_ID as CC::ICC, and ICC-compatible mapping is represented as ICC_Operator_ID::Node_ID. Note: Each entry in this table should have a unique [Global_ID and Node_ID] or [CC::ICC and Node_ID] combination.')
mplsTunnelExtNodeConfigLocalId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 1), MplsExtendedTunnelId())
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigLocalId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigLocalId.setDescription("This object is used in accommodating the bigger- size Global_ID::Node_ID and/or the ICC_Operator_ID::Node_ID with the smaller-size LSR identifier in order to index the mplsTunnelTable. The local identifier is configured between 0 and 16777215, as the valid IP address range starts from 16777216(01.00.00.00). This range is chosen to determine whether the mplsTunnelTable's Ingress/Egress LSR ID is an IP address or local identifier. If the configured range is not an IP address, the operator is expected to retrieve the complete information (Global_ID::Node_ID or ICC_Operator_ID::Node_ID) from mplsTunnelExtNodeConfigTable. This way, the existing mplsTunnelTable is reused for bidirectional tunnel extensions for MPLS-based transport networks. The local identifier allows the operator to assign a unique identifier to map Global_ID::Node_ID and/or ICC_Operator_ID::Node_ID. As this local identifier is unique within the node and the same syntax of this object can be used for MPLS-TE tunnel also, it is up to the operator/local management entity to choose a non-conflicting value for indexing the MPLS and MPLS-TP tunnel entries.")
mplsTunnelExtNodeConfigGlobalId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 2), MplsGlobalId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigGlobalId.setReference('MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 3.')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigGlobalId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigGlobalId.setDescription('This object indicates the Global Operator Identifier. This object has no meaning when mplsTunnelExtNodeConfigIccValid is set true.')
mplsTunnelExtNodeConfigCcId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 3), MplsCcId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigCcId.setReference('MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigCcId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigCcId.setDescription('This object allows the operator or service provider to configure a unique MPLS-TP ITU-T Country Code (CC) either for Ingress ID or Egress ID. This object has no meaning when mplsTunnelExtNodeConfigIccValid is set to false.')
mplsTunnelExtNodeConfigIccId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 4), MplsIccId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigIccId.setReference('MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigIccId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigIccId.setDescription('This object allows the operator or service provider to configure a unique MPLS-TP ITU-T Carrier Code (ICC) either for Ingress ID or Egress ID. This object has no meaning when mplsTunnelExtNodeConfigIccValid is set to false.')
mplsTunnelExtNodeConfigNodeId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 5), MplsNodeId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigNodeId.setReference('MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 4.')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigNodeId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigNodeId.setDescription('This object indicates the Node_ID within the scope of a Global_ID or ICC_Operator_ID.')
mplsTunnelExtNodeConfigIccValid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigIccValid.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigIccValid.setDescription('Denotes whether or not this entry uses mplsTunnelExtNodeConfigCcId, mplsTunnelExtNodeConfigIccId, and mplsTunnelExtNodeConfigNodeId for mapping the ICC-based identifiers with the local identifier. Note that if this variable is set to false, then the mplsTunnelExtNodeConfigGlobalId and mplsTunnelExtNodeConfigNodeId objects should have the valid information.')
mplsTunnelExtNodeConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 7), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigStorageType.setDescription("This variable indicates the storage type for this object. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
mplsTunnelExtNodeConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeConfigRowStatus.setDescription('This object allows the operator to create, modify, and/or delete a row in this table.')
mplsTunnelExtNodeIpMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3), )
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapTable.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapTable.setDescription('This read-only table allows the operator to retrieve the local identifier for a given Global_ID::Node_ID in an IP-compatible operator environment. This table MAY be used in on-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (local identifier) from Src-Global_Node_ID or Dst-Global_Node_ID. The Ingress and Egress LSR identifiers are used to retrieve the tunnel entry. This table returns nothing when the associated entry is not defined in mplsTunnelExtNodeConfigTable.')
mplsTunnelExtNodeIpMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1), ).setIndexNames((0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIpMapGlobalId"), (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIpMapNodeId"))
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapEntry.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapEntry.setDescription('An entry in this table represents a mapping of Global_ID::Node_ID with the local identifier. An entry in this table is created automatically when the local identifier is associated with Global_ID and Node_Id in the mplsTunnelExtNodeConfigTable. Note: Each entry in this table should have a unique Global_ID and Node_ID combination.')
mplsTunnelExtNodeIpMapGlobalId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1, 1), MplsGlobalId())
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapGlobalId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapGlobalId.setDescription('This object indicates the Global_ID.')
mplsTunnelExtNodeIpMapNodeId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1, 2), MplsNodeId())
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapNodeId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapNodeId.setDescription('This object indicates the Node_ID within the operator.')
mplsTunnelExtNodeIpMapLocalId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1, 3), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapLocalId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIpMapLocalId.setDescription('This object contains an IP-compatible local identifier that is defined in mplsTunnelExtNodeConfigTable.')
mplsTunnelExtNodeIccMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4), )
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapTable.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapTable.setDescription('This read-only table allows the operator to retrieve the local identifier for a given ICC_Operator_ID::Node_ID in an ICC operator environment. This table MAY be used in on-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (local identifier) from Src-ICC or Dst-ICC. The Ingress and Egress LSR identifiers are used to retrieve the tunnel entry. This table returns nothing when the associated entry is not defined in mplsTunnelExtNodeConfigTable.')
mplsTunnelExtNodeIccMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1), ).setIndexNames((0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapCcId"), (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapIccId"), (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapNodeId"))
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapEntry.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapEntry.setDescription('An entry in this table represents a mapping of ICC_Operator_ID::Node_ID with the local identifier. An entry in this table is created automatically when the local identifier is associated with ICC_Operator_ID::Node_ID in the mplsTunnelExtNodeConfigTable.')
mplsTunnelExtNodeIccMapCcId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 1), MplsCcId())
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapCcId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapCcId.setDescription('This object allows the operator or service provider to configure a unique MPLS-TP ITU-T Country Code (CC) either for Ingress or Egress LSR ID. The CC is a string of two alphabetic characters represented with uppercase letters (i.e., A-Z).')
mplsTunnelExtNodeIccMapIccId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 2), MplsIccId())
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapIccId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapIccId.setDescription('This object allows the operator or service provider to configure a unique MPLS-TP ITU-T Carrier Code (ICC) either for Ingress or Egress LSR ID. The ICC is a string of one to six characters, each character being either alphabetic (i.e., A-Z) or numeric (i.e., 0-9) characters. Alphabetic characters in the ICC should be represented with uppercase letters.')
mplsTunnelExtNodeIccMapNodeId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 3), MplsNodeId())
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapNodeId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapNodeId.setDescription('This object indicates the Node_ID within the ICC-based operator.')
mplsTunnelExtNodeIccMapLocalId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 4), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapLocalId.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtNodeIccMapLocalId.setDescription('This object contains an ICC-based local identifier that is defined in mplsTunnelExtNodeConfigTable.')
mplsTunnelExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5), )
if mibBuilder.loadTexts: mplsTunnelExtTable.setReference('MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370.')
if mibBuilder.loadTexts: mplsTunnelExtTable.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtTable.setDescription('This table represents extensions to mplsTunnelTable in order to support MPLS-TP Tunnels. As per MPLS-TP Identifiers (RFC 6370), LSP_ID for IP-based co-routed bidirectional tunnel: A1-{Global_ID::Node_ID::Tunnel_Num}::Z9-{Global_ID:: Node_ID::Tunnel_Num}::LSP_Num LSP_ID for IP based associated bidirectional tunnel: A1-{Global_ID::Node_ID::Tunnel_Num::LSP_Num}:: Z9-{Global_ID::Node_ID::Tunnel_Num::LSP_Num} mplsTunnelTable is reused for forming the LSP_ID as follows: Source Tunnel_Num is mapped with mplsTunnelIndex, Source Node_ID is mapped with mplsTunnelIngressLSRId, Destination Node_ID is mapped with mplsTunnelEgressLSRId, and LSP_Num is mapped with mplsTunnelInstance. Source Global_ID::Node_ID and/or ICC_Operator_ID::Node_ID and Destination Global_ID::Node_ID and/or ICC_Operator_ID::Node-ID are maintained in the mplsTunnelExtNodeConfigTable. mplsTunnelExtNodeConfigLocalId is used to create an entry in mplsTunnelTable.')
mplsTunnelExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1), ).setIndexNames((0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"), (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"), (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"), (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"))
if mibBuilder.loadTexts: mplsTunnelExtEntry.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtEntry.setDescription('An entry in this table represents additional MPLS-TP- specific tunnel configurations.')
mplsTunnelExtOppositeDirPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 1), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtOppositeDirPtr.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtOppositeDirPtr.setDescription('This object points to the opposite-direction tunnel entry.')
mplsTunnelExtOppositeDirTnlValid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtOppositeDirTnlValid.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtOppositeDirTnlValid.setDescription('Denotes whether or not this tunnel uses mplsTunnelExtOppositeDirPtr for identifying the opposite- direction tunnel information. Note that if this variable is set to true, then the mplsTunnelExtOppositeDirPtr should point to the first accessible row of the valid opposite- direction tunnel.')
mplsTunnelExtDestTnlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 3), MplsTunnelIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtDestTnlIndex.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtDestTnlIndex.setDescription('This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the different tunnel entries. The values of this object and the mplsTunnelExtDestTnlLspIndex object together can be used to identify an opposite-direction LSP, i.e., if the mplsTunnelIndex and mplsTunnelInstance hold the value for forward LSP, this object and mplsTunnelExtDestTnlLspIndex can be used to retrieve the reverse-direction LSP and vice versa. This object and mplsTunnelExtDestTnlLspIndex values provide the first two indices of tunnel entry, and the remaining indices can be derived as follows: the Ingress and Egress Identifiers should be swapped in order to index the other direction tunnel.')
mplsTunnelExtDestTnlLspIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 4), MplsTunnelInstanceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtDestTnlLspIndex.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtDestTnlLspIndex.setDescription('This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the different tunnel entries. This object holds the instance index of the opposite-direction tunnel.')
mplsTunnelExtDestTnlValid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtDestTnlValid.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtDestTnlValid.setDescription('Denotes whether or not this tunnel uses mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex for identifying the opposite-direction tunnel information. Note that if this variable is set to true, then the mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex objects should have the valid opposite-direction tunnel indices.')
mplsTunnelExtIngressLSRLocalIdValid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtIngressLSRLocalIdValid.setReference('MPLS-TE-STD-MIB (RFC 3812), Section 11. mplsTunnelIngressLSRId object in mplsTunnelTable.')
if mibBuilder.loadTexts: mplsTunnelExtIngressLSRLocalIdValid.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtIngressLSRLocalIdValid.setDescription('This object denotes whether the mplsTunnelIngressLSRId contains the local value that is used to reference the complete Ingress Global_ID::Node_ID or ICC_Operator_ID from the mplsTunnelExtNodeConfigTable. If this object is set to FALSE, mplsTunnelExtNodeConfigTable will not contain an entry to reference the local identifier with Global_ID::Node_ID or ICC_Operator_ID::Node_ID value. This object is set to FALSE for legacy implementations like MPLS TE tunnels where mplsTunnelIngressId itself provides the complete Ingress LSR ID.')
mplsTunnelExtEgressLSRLocalIdValid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExtEgressLSRLocalIdValid.setReference('MPLS-TE-STD-MIB (RFC 3812), Section 11. mplsTunnelEgressLSRId object in mplsTunnelTable.')
if mibBuilder.loadTexts: mplsTunnelExtEgressLSRLocalIdValid.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtEgressLSRLocalIdValid.setDescription('This object denotes whether the mplsTunnelEgressLSRId contains the local value, which is used to reference the complete Egress Global_ID::Node_ID or ICC_Operator_ID::Node_ID from the mplsTunnelExtNodeConfigTable. If this object is set to FALSE, mplsTunnelExtNodeConfigTable will not contain an entry to reference the local identifier with Global_ID::Node_ID or ICC_Operator_ID::Node_ID value. This object is set to FALSE for legacy implementations like MPLS TE tunnels where mplsTunnelEgressId itself provides the complete Egress LSR ID.')
mplsTeExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 1))
mplsTeExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2))
mplsTeExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 1, 1)).setObjects(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtGroup"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtIpOperatorGroup"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeExtModuleFullCompliance = mplsTeExtModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsTeExtModuleFullCompliance.setDescription('Compliance statement for agents that provide full support the MPLS-TE-EXT-STD-MIB module.')
mplsTeExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 1, 2)).setObjects(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtGroup"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtIpOperatorGroup"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeExtModuleReadOnlyCompliance = mplsTeExtModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsTeExtModuleReadOnlyCompliance.setDescription('Compliance statement for agents that only provide read-only support for the MPLS-TE-EXT-STD-MIB module.')
mplsTunnelExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2, 1)).setObjects(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtOppositeDirPtr"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtOppositeDirTnlValid"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtDestTnlIndex"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtDestTnlLspIndex"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtDestTnlValid"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtIngressLSRLocalIdValid"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtEgressLSRLocalIdValid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelExtGroup = mplsTunnelExtGroup.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtGroup.setDescription('Necessary, but not sufficient, set of objects to implement tunnels. In addition, depending on the operating environment, the following groups are mandatory.')
mplsTunnelExtIpOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2, 2)).setObjects(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigLocalIdNext"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigGlobalId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigNodeId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIpMapLocalId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigStorageType"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelExtIpOperatorGroup = mplsTunnelExtIpOperatorGroup.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtIpOperatorGroup.setDescription('Object(s) needed to implement IP-compatible tunnels.')
mplsTunnelExtIccOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2, 3)).setObjects(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigLocalIdNext"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigCcId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigIccId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigNodeId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigIccValid"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapLocalId"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigStorageType"), ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelExtIccOperatorGroup = mplsTunnelExtIccOperatorGroup.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelExtIccOperatorGroup.setDescription('Object(s) needed to implement ICC-based tunnels.')
mibBuilder.exportSymbols("MPLS-TE-EXT-STD-MIB", mplsTunnelExtNodeIccMapTable=mplsTunnelExtNodeIccMapTable, mplsTunnelExtNodeConfigLocalId=mplsTunnelExtNodeConfigLocalId, mplsTunnelExtNodeConfigTable=mplsTunnelExtNodeConfigTable, mplsTunnelExtNodeIpMapGlobalId=mplsTunnelExtNodeIpMapGlobalId, mplsTeExtObjects=mplsTeExtObjects, mplsTeExtModuleReadOnlyCompliance=mplsTeExtModuleReadOnlyCompliance, mplsTunnelExtDestTnlLspIndex=mplsTunnelExtDestTnlLspIndex, mplsTunnelExtIngressLSRLocalIdValid=mplsTunnelExtIngressLSRLocalIdValid, mplsTunnelExtNodeIccMapLocalId=mplsTunnelExtNodeIccMapLocalId, mplsTeExtCompliances=mplsTeExtCompliances, mplsTunnelExtNodeConfigLocalIdNext=mplsTunnelExtNodeConfigLocalIdNext, mplsTunnelExtNodeIccMapIccId=mplsTunnelExtNodeIccMapIccId, mplsTeExtStdMIB=mplsTeExtStdMIB, mplsTunnelExtNodeIpMapLocalId=mplsTunnelExtNodeIpMapLocalId, mplsTunnelExtEgressLSRLocalIdValid=mplsTunnelExtEgressLSRLocalIdValid, mplsTunnelExtGroup=mplsTunnelExtGroup, mplsTeExtConformance=mplsTeExtConformance, mplsTunnelExtNodeIpMapNodeId=mplsTunnelExtNodeIpMapNodeId, mplsTunnelExtNodeConfigRowStatus=mplsTunnelExtNodeConfigRowStatus, mplsTeExtModuleFullCompliance=mplsTeExtModuleFullCompliance, mplsTunnelExtEntry=mplsTunnelExtEntry, mplsTunnelExtNodeConfigNodeId=mplsTunnelExtNodeConfigNodeId, mplsTunnelExtDestTnlIndex=mplsTunnelExtDestTnlIndex, mplsTunnelExtNodeIccMapNodeId=mplsTunnelExtNodeIccMapNodeId, mplsTunnelExtIccOperatorGroup=mplsTunnelExtIccOperatorGroup, PYSNMP_MODULE_ID=mplsTeExtStdMIB, mplsTunnelExtOppositeDirPtr=mplsTunnelExtOppositeDirPtr, mplsTunnelExtNodeIpMapTable=mplsTunnelExtNodeIpMapTable, mplsTunnelExtNodeConfigIccId=mplsTunnelExtNodeConfigIccId, mplsTunnelExtNodeConfigCcId=mplsTunnelExtNodeConfigCcId, mplsTunnelExtOppositeDirTnlValid=mplsTunnelExtOppositeDirTnlValid, mplsTunnelExtNodeConfigIccValid=mplsTunnelExtNodeConfigIccValid, mplsTunnelExtNodeIpMapEntry=mplsTunnelExtNodeIpMapEntry, mplsTunnelExtTable=mplsTunnelExtTable, mplsTeExtGroups=mplsTeExtGroups, mplsTunnelExtNodeIccMapCcId=mplsTunnelExtNodeIccMapCcId, mplsTunnelExtDestTnlValid=mplsTunnelExtDestTnlValid, mplsTunnelExtNodeIccMapEntry=mplsTunnelExtNodeIccMapEntry, mplsTunnelExtIpOperatorGroup=mplsTunnelExtIpOperatorGroup, mplsTunnelExtNodeConfigEntry=mplsTunnelExtNodeConfigEntry, mplsTunnelExtNodeConfigGlobalId=mplsTunnelExtNodeConfigGlobalId, mplsTunnelExtNodeConfigStorageType=mplsTunnelExtNodeConfigStorageType)
