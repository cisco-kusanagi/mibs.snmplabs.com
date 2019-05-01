#
# PySNMP MIB module CL-PKTC-EUE-DEV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CL-PKTC-EUE-DEV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
PktcEUETCCredsType, PktcEUETCCreds = mibBuilder.importSymbols("CL-PKTC-EUE-TC-MIB", "PktcEUETCCredsType", "PktcEUETCCreds")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
InetPortNumber, InetAddress, InetAddressType, InetAddressDNS = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType", "InetAddressDNS")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, IpAddress, Counter64, ObjectIdentity, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, TimeTicks, Integer32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "TimeTicks", "Integer32", "MibIdentifier", "Counter32")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
pktcEUEDevMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2))
if mibBuilder.loadTexts: pktcEUEDevMIB.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: pktcEUEDevMIB.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: pktcEUEDevMIB.setContactInfo('Sumanth Channabasappa Cable Television Laboratories, Inc. 858 Coal Creek Circle, Louisville, CO 80027, USA Phone: +1 303-661-9100 Email: sumanth@cablelabs.com Acknowledgements: Thomas Clack, Broadcom - Primary author , and members of the PacketCable PACM Focus Team.')
if mibBuilder.loadTexts: pktcEUEDevMIB.setDescription('This MIB module contains Configuration MIB objects for the Embedded User Equipment (eUE) as required by the PacketCable E-UE Provisioning Framework Specification.')
pktcEUEDevNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 0))
pktcEUEDevObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1))
pktcEUEDevConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2))
pktcEUEDevCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1))
pktcEUEDevGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2))
pktcEUEDevProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1))
pktcEUEDevProfileVersion = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEDevProfileVersion.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevProfileVersion.setDescription(" This MIB Object represents the Device Profile Version for this MIB module. The eUE MUST set this MIB Object to a value of '1.0'.")
pktcEUEDevOpTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2), )
if mibBuilder.loadTexts: pktcEUEDevOpTable.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpTable.setDescription(' This data table contains Operator specific information associated with the eUE.')
pktcEUEDevOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1), ).setIndexNames((0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"))
if mibBuilder.loadTexts: pktcEUEDevOpEntry.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpEntry.setDescription(" Each entry in this data table describes Operator parameters associated with a specific domain name. For each Operator that is associated with a user, the corresponding parameters SHOULD be configured by the Operator. A domain name of '.' indicates any domain name. The eUE MUST use the values provided only for sessions established on behalf of the eUE identifier (e.g. eUE registration, eUE configuration, eUE Identifier based sessions).")
pktcEUEDevOpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: pktcEUEDevOpIndex.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpIndex.setDescription(" A unique value used to identify an instance of a set of values pertaining to a Operator domain identified by 'pktcEUEDevOpDomain'. The indices SHOULD be contiguous. When multiple entries are specified, the eUE MUST give precedence to the values indexed by lower indices.")
pktcEUEDevOpDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 2), InetAddressDNS()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpDomain.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpDomain.setDescription(" This data element contains the Operator's Domain or sub-domain name. A value of '.' indicates any domainName.")
pktcEUEDevOpSTUNAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNAddrType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNAddrType.setDescription(" This data element identifies the data type of the value contained in 'pktcEUEDevOpSTUNAddr'.")
pktcEUEDevOpSTUNAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNAddr.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNAddr.setDescription(" This data element contains the STUN server address associated with the domain name identified in 'pktcEUEDevOpDomain'.")
pktcEUEDevOpSTUNAddrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 5), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNAddrPort.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNAddrPort.setDescription(" This data element contains the STUN server port associated with the server address identified in 'pktcEUEDevOpSTUNAddr'.")
pktcEUEDevOpSTUNRelayAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 6), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayAddrType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayAddrType.setDescription(" This data element identifies the data type of the value contained in 'pktcEUEDevOpSTUNRelayAddr'.")
pktcEUEDevOpSTUNRelayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayAddr.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayAddr.setDescription(" This data element contains the STUNRelay server address associated with the domain name identified in 'pktcEUEDevOpDomain'.")
pktcEUEDevOpSTUNRelayAddrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayAddrPort.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayAddrPort.setDescription(" This data element contains the STUNRelay server port associated with the server address identified in 'pktcEUEDevOpSTUNRelayAddr'.")
pktcEUEDevOpSTUNRelayCredsType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 9), PktcEUETCCredsType().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayCredsType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayCredsType.setDescription(" This data element contains the creds type associated with the STUN Relay creds identified in 'pktcEUEDevOpSTUNRelayCreds'. Valid types include other(1), publicIdentity(2) and username(6).")
pktcEUEDevOpSTUNRelayCreds = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 10), PktcEUETCCreds()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayCreds.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpSTUNRelayCreds.setDescription(' This optional data element MAY contain suitable credentials related to STUN Relay access. If read this data element MUST always return an empty string value.')
pktcEUEDevOpTimerT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 11), Unsigned32().clone(2000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEDevOpTimerT1.setReference('PacketCable IMS Delta Session Initiation Protocol (SIP) and Session Description Protocol (SDP), Stage 3 Specification 3GPP TS 24.229')
if mibBuilder.loadTexts: pktcEUEDevOpTimerT1.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpTimerT1.setDescription(' This is the SIP Timer T1, an estimate for the round trip time in the system (UE to P-CSCF). Please refer to the PacketCable IMS Delta Session Initiation Protocol (SIP) and Session Description Protocol (SDP), Stage 3 Specification 3GPP TS 24.229 for more information.')
pktcEUEDevOpTimerT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 12), Unsigned32().clone(1600)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEDevOpTimerT2.setReference('PacketCable IMS Delta Session Initiation Protocol (SIP) and Session Description Protocol (SDP), Stage 3 Specification 3GPP TS 24.229')
if mibBuilder.loadTexts: pktcEUEDevOpTimerT2.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpTimerT2.setDescription(' This is the SIP Timer T2, an estimate for the maximum retransmit interval for non-INVITE requests and INVITE responses. Please refer to the PacketCable IMS Delta Session Initiation Protocol (SIP) and Session Description Protocol (SDP), Stage 3 Specification 3GPP TS 24.229 for more information.')
pktcEUEDevOpTimerT4 = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 13), Unsigned32().clone(1700)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEDevOpTimerT4.setReference('PacketCable IMS Delta Session Initiation Protocol (SIP) and Session Description Protocol (SDP), Stage 3 Specification 3GPP TS 24.229')
if mibBuilder.loadTexts: pktcEUEDevOpTimerT4.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpTimerT4.setDescription(' This is the SIP Timer T4, an estimate for the maximum duration a message will remain in the network. Please refer to the PacketCable IMS Delta Session Initiation Protocol (SIP) and Session Description Protocol (SDP), Stage 3 Specification 3GPP TS 24.229 for more information.')
pktcEUEDevOpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevOpRowStatus.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpRowStatus.setDescription(' This object defines the row status associated with the particular Operator in the pktcEUEDevOpTable. The value of this object has no effect on whether columnar objects in this row can be modified.')
pktcEUEDevDnsTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3), )
if mibBuilder.loadTexts: pktcEUEDevDnsTable.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsTable.setDescription(" This data table represents the eUE's knowledge of suitable DNS Server information on a per Operator basis. The eUE MUST use the values provided only for sessions established on behalf of the eUE identifier (e.g. eUE P-CSCF Discovery, eUE registration, eUE configuration, eUE Identifier based sessions).")
pktcEUEDevDnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1), ).setIndexNames((0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"), (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsIndex"))
if mibBuilder.loadTexts: pktcEUEDevDnsEntry.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsEntry.setDescription(" Each entry in this data table contains an instance of a DNS Server entry for a given domain name as indicated by 'pktcEUEDevOpDomain'. The information in this table MAY be configured by the Operator.")
pktcEUEDevDnsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: pktcEUEDevDnsIndex.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsIndex.setDescription(' A unique value used to identify an instance in this data table. The indices SHOULD be contiguous. When multiple entries are specified, the eUE MUST give precedence to the values indexed by lower indices.')
pktcEUEDevDnsAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevDnsAddrType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsAddrType.setDescription(" This data element contains the type of the data element contained in 'pktcEUEDevDnsAddr'.")
pktcEUEDevDnsAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevDnsAddr.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsAddr.setDescription(" The IP address of a DNS server associated with the domain name indicated by the primary index 'pktcEUEDevOpIndex', for the instance indicated by the secondary index 'pktcEUEDevDnsIndex'.")
pktcEUEDevDnsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevDnsRowStatus.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsRowStatus.setDescription(" This object defines the row status associated with the particular Operator domanin name in the pktcEUEDevDnsTable. The value of the 'pktcEUEDevDnsAddrType' object MUST not be modified while this object is 'active'. The value of 'pktcEUEDevDnsAddr' MAY be modified while this object is active if the value is consistent with the type specifed by the 'pktcEUEDevDnsAddrType' object.")
pktcEUEDevPCSCFTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4), )
if mibBuilder.loadTexts: pktcEUEDevPCSCFTable.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFTable.setDescription(" This data table represents the eUE's knowledge of suitable P-CSCFs information on a per Operator basis.")
pktcEUEDevPCSCFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1), ).setIndexNames((0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"), (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFIndex"))
if mibBuilder.loadTexts: pktcEUEDevPCSCFEntry.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFEntry.setDescription(' Each entry in this data table contains an instance of a P-CSCF Server entry for a given domain name. The information in this table MAY be configured by the Operator. The eUE MUST use the values provided only for sessions established on behalf of the eUE identifier (e.g. eUE registration, eUE configuration, eUE Identifier based sessions).')
pktcEUEDevPCSCFIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: pktcEUEDevPCSCFIndex.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFIndex.setDescription(' A unique value used to identify an instance in this data table. The indices SHOULD be contiguous.')
pktcEUEDevPCSCFAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevPCSCFAddrType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFAddrType.setDescription(" This data element contains the type of the data element contained in 'pktcEUEDevPCSCFAddr'.")
pktcEUEDevPCSCFAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevPCSCFAddr.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFAddr.setDescription(" The IP address of a DNS server associated with the domain name indicated by the primary index 'pktcEUEDevOpIndex', for the instance indicated by the secondary index 'pktcEUEDevPCSCFIndex'.")
pktcEUEDevPCSCFRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevPCSCFRowStatus.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFRowStatus.setDescription(" This object defines the row status associated with the particular P-CSCF Server entry for the particular domain name. The value of the 'pktcEUEDevPCSCFAddrType' object MUST not be modified while this object is 'active'. The value of 'pktcEUEDevPCSCFAddr' MAY be modified while this object is active if the value is consistent with the type specifed by the 'pktcEUEDevPCSCFAddrType' object.")
pktcEUEDevBSFTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5), )
if mibBuilder.loadTexts: pktcEUEDevBSFTable.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFTable.setDescription(" This data table represents the eUE's knowledge of suitable BSFs to contact.")
pktcEUEDevBSFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1), ).setIndexNames((0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"), (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFASType"), (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFIndex"))
if mibBuilder.loadTexts: pktcEUEDevBSFEntry.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFEntry.setDescription(" Each entry in this data table contains an instance of a BSF, specific to a AS type, for a given Operator's Domain Name. The entries represent the eUE's knowledge of suitable BSFs to contact, as per the IMS GBA architecture to obtain credentials and enabling secure sessions to Application Servers. A list of BSFs for each Operator and application types MAY be configured by the Operator.")
pktcEUEDevBSFASType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: pktcEUEDevBSFASType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFASType.setDescription(" A unique value used to indicate the AS type to which the BSFs correspond. For example: To contact PACM application types, this would be labeled as 'GBA-PACM'. Applications using GBA are required to specify such identifiers explicitly.")
pktcEUEDevBSFIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: pktcEUEDevBSFIndex.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFIndex.setDescription(' A unique value used to identify an instance in this data table. The indices SHOULD be contiguous. When multiple entries are specified, the eUE MUST give precedence to the values indexed by lower indices.')
pktcEUEDevBSFAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEDevBSFAddrType.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFAddrType.setDescription(" This data element contains the type of the data element contained in 'pktcEUEDevBSFAddr'.")
pktcEUEDevBSFAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEDevBSFAddr.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFAddr.setDescription(" The address of a BSF server associated with the domain name indicated by the indices 'pktcEUEDevOpIndex' (Operator Domain), 'pktcEUEDevBSFASType' and 'pktcEUEDevBSFIndex'.")
pktcEUEDevBSFRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcEUEDevBSFRowStatus.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFRowStatus.setDescription(" This object defines the row status associated with this instance of a BSF. The value of the 'pktcEUEDevBSFAddrType' object MUST not be modified while this object is 'active'. The value of 'pktcEUEDevBSFAddr' MAY be modified while this object is active if the value is consistent with the type specifed by the 'pktcEUEDevBSFAddrType' object.")
pktcEUECBSupport = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUECBSupport.setStatus('current')
if mibBuilder.loadTexts: pktcEUECBSupport.setDescription('This MIB Object is used by the eUE to report support for Certificate Bootstrapping. If the MIB Object is set to a value of true(1) it indicates that the device supports Certificate Bootstrapping. If the MIB Object is set to a value of false(1) it indicates that the device does not support Certificate Bootstrapping.')
pktcEUECBEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEUECBEnable.setStatus('current')
if mibBuilder.loadTexts: pktcEUECBEnable.setDescription('This MIB Object is used to initiate the Certificate Bootstrapping procedure in an eUE. If this value is set to a value of true(1) and the MIB Object pktcEUECBData contains a non-zero HTTP/HTTPS URI, then the eUE MUST intiate the Certificate Bootstrapping procedure, if supported. If the eUE does not support the Certificate Bootstrapping procedure, it rejects any attempt to set this MIB Object to a value of true(1). The eUE MUST return a value of false(2) when this MIB Object is read. If the Certificate Bootstrapping procedure was successful, the eUE MUST act on the Certificate Bootstrapping configuration file provided. If the procedure was unsuccessful (e.g., authentication error or inresponsive server), the eUE MUST report the corresponding management event.')
pktcEUECBData = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEUECBData.setStatus('current')
if mibBuilder.loadTexts: pktcEUECBData.setDescription('This MIB Object contains a HTTP/HTTPS URI to be used for Certificate Bootstrapping. Any attempt to set it to anything other than a HTTP/HTTPS URI MUST be rejected by the eUE.')
pktcEUEDevMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1))
pktcEUEDevMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2))
pktcPACM2UEMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1, 1)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevProfileGroup"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpGroup"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsGroup"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFGroup"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcPACM2UEMIBCompliance = pktcPACM2UEMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pktcPACM2UEMIBCompliance.setDescription(' The compliance statement for implementations of the eUE MIB ')
pktcEUEDevProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 1)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevProfileVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEDevProfileGroup = pktcEUEDevProfileGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevProfileGroup.setDescription('The eUE Device Profile Group.')
pktcEUEDevOpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 2)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpDomain"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddrType"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddr"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddrPort"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayAddrType"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayAddr"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayAddrPort"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayCredsType"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayCreds"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTimerT1"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTimerT2"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTimerT4"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEDevOpGroup = pktcEUEDevOpGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevOpGroup.setDescription('The eUE Operator Group.')
pktcEUEDevDnsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 3)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsAddrType"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsAddr"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEDevDnsGroup = pktcEUEDevDnsGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevDnsGroup.setDescription('The eUE DNS Group.')
pktcEUEDevPCSCFGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 4)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFAddrType"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFAddr"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEDevPCSCFGroup = pktcEUEDevPCSCFGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevPCSCFGroup.setDescription('The eUE P-CSCF Group.')
pktcEUEDevBSFGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 5)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFAddrType"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFAddr"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEDevBSFGroup = pktcEUEDevBSFGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevBSFGroup.setDescription('The eUE BSF Group.')
pktcEUEDevCBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 6)).setObjects(("CL-PKTC-EUE-DEV-MIB", "pktcEUECBSupport"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUECBEnable"), ("CL-PKTC-EUE-DEV-MIB", "pktcEUECBData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEDevCBGroup = pktcEUEDevCBGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEDevCBGroup.setDescription('The eUE Certificate Bootstrapping Group.')
mibBuilder.exportSymbols("CL-PKTC-EUE-DEV-MIB", pktcEUEDevProfile=pktcEUEDevProfile, pktcEUEDevBSFIndex=pktcEUEDevBSFIndex, pktcEUEDevConformance=pktcEUEDevConformance, pktcEUEDevPCSCFAddrType=pktcEUEDevPCSCFAddrType, pktcEUEDevOpDomain=pktcEUEDevOpDomain, pktcEUEDevProfileVersion=pktcEUEDevProfileVersion, pktcEUEDevOpTable=pktcEUEDevOpTable, pktcEUEDevDnsRowStatus=pktcEUEDevDnsRowStatus, pktcEUEDevBSFRowStatus=pktcEUEDevBSFRowStatus, pktcEUEDevOpSTUNAddrType=pktcEUEDevOpSTUNAddrType, pktcEUEDevOpTimerT4=pktcEUEDevOpTimerT4, pktcEUEDevCompliances=pktcEUEDevCompliances, pktcEUEDevOpSTUNAddr=pktcEUEDevOpSTUNAddr, pktcEUEDevDnsAddr=pktcEUEDevDnsAddr, pktcEUEDevDnsTable=pktcEUEDevDnsTable, pktcEUECBEnable=pktcEUECBEnable, pktcEUEDevPCSCFTable=pktcEUEDevPCSCFTable, pktcEUEDevProfileGroup=pktcEUEDevProfileGroup, pktcEUEDevDnsGroup=pktcEUEDevDnsGroup, pktcEUEDevDnsEntry=pktcEUEDevDnsEntry, pktcEUEDevBSFAddrType=pktcEUEDevBSFAddrType, pktcEUEDevPCSCFEntry=pktcEUEDevPCSCFEntry, pktcEUEDevObjects=pktcEUEDevObjects, pktcEUEDevPCSCFIndex=pktcEUEDevPCSCFIndex, pktcEUEDevBSFTable=pktcEUEDevBSFTable, pktcEUEDevOpTimerT2=pktcEUEDevOpTimerT2, pktcEUEDevBSFASType=pktcEUEDevBSFASType, pktcEUEDevBSFAddr=pktcEUEDevBSFAddr, pktcEUECBData=pktcEUECBData, pktcEUEDevOpSTUNRelayAddr=pktcEUEDevOpSTUNRelayAddr, pktcEUEDevDnsAddrType=pktcEUEDevDnsAddrType, pktcPACM2UEMIBCompliance=pktcPACM2UEMIBCompliance, pktcEUEDevOpRowStatus=pktcEUEDevOpRowStatus, pktcEUEDevOpSTUNRelayCreds=pktcEUEDevOpSTUNRelayCreds, pktcEUECBSupport=pktcEUECBSupport, pktcEUEDevNotification=pktcEUEDevNotification, pktcEUEDevOpEntry=pktcEUEDevOpEntry, pktcEUEDevMIBCompliances=pktcEUEDevMIBCompliances, pktcEUEDevBSFEntry=pktcEUEDevBSFEntry, pktcEUEDevMIB=pktcEUEDevMIB, pktcEUEDevOpTimerT1=pktcEUEDevOpTimerT1, PYSNMP_MODULE_ID=pktcEUEDevMIB, pktcEUEDevOpIndex=pktcEUEDevOpIndex, pktcEUEDevOpSTUNRelayAddrType=pktcEUEDevOpSTUNRelayAddrType, pktcEUEDevOpSTUNRelayAddrPort=pktcEUEDevOpSTUNRelayAddrPort, pktcEUEDevCBGroup=pktcEUEDevCBGroup, pktcEUEDevDnsIndex=pktcEUEDevDnsIndex, pktcEUEDevOpSTUNAddrPort=pktcEUEDevOpSTUNAddrPort, pktcEUEDevPCSCFGroup=pktcEUEDevPCSCFGroup, pktcEUEDevPCSCFAddr=pktcEUEDevPCSCFAddr, pktcEUEDevBSFGroup=pktcEUEDevBSFGroup, pktcEUEDevOpGroup=pktcEUEDevOpGroup, pktcEUEDevGroups=pktcEUEDevGroups, pktcEUEDevPCSCFRowStatus=pktcEUEDevPCSCFRowStatus, pktcEUEDevMIBGroups=pktcEUEDevMIBGroups, pktcEUEDevOpSTUNRelayCredsType=pktcEUEDevOpSTUNRelayCredsType)