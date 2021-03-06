#
# PySNMP MIB module CABH-QOS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CABH-QOS2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
clabProjCableHome, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjCableHome")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Gauge32, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, NotificationType, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Gauge32", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Counter64", "Bits")
TruthValue, DisplayString, TimeStamp, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention", "RowStatus")
cabhQos2Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8))
cabhQos2Mib.setRevisions(('2005-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cabhQos2Mib.setRevisionsDescriptions(('Initial revision, published as part of CableHome Specification.',))
if mibBuilder.loadTexts: cabhQos2Mib.setLastUpdated('200504080000Z')
if mibBuilder.loadTexts: cabhQos2Mib.setOrganization('CableLabs Broadband Access Department')
if mibBuilder.loadTexts: cabhQos2Mib.setContactInfo('Kevin Luehrs Postal: Cable Television Laboratories, Inc. 858 Coal Creek Circle Louisville, Colorado 80027 U.S.A. Phone: +1 303-661-9100 Fax: +1 303-661-9199 E-mail: k.luehrs@cablelabs.com; mibs@cablelabs.com')
if mibBuilder.loadTexts: cabhQos2Mib.setDescription('This MIB module supplies parameters for the configuration and monitoring of CableHome QoS capabilities.')
cabhQos2Mib2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 0))
cabhQos2MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1))
cabhQos2Base = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 1))
cabhQos2PsIfAttributes = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2))
cabhQos2PolicyHolderObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3))
cabhQos2DeviceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4))
cabhQos2SetToFactory = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhQos2SetToFactory.setStatus('current')
if mibBuilder.loadTexts: cabhQos2SetToFactory.setDescription('When this object is set to true(1), the PS MUST clear all the entries in cabhQos2PolicyTable and cabhQos2TrafficClassTable. Reading this object always returns false(2).')
cabhQos2LastSetToFactory = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhQos2LastSetToFactory.setStatus('current')
if mibBuilder.loadTexts: cabhQos2LastSetToFactory.setDescription('The value of sysUpTime when cabhQos2SetToFactory was last set to true. Zero if never reset.')
cabhQos2PsIfAttribTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1), )
if mibBuilder.loadTexts: cabhQos2PsIfAttribTable.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PsIfAttribTable.setDescription('This table contains interface attributes. It includes the number of media access priorities and number of queues associated with each PS interface in the Residential Gateway.')
cabhQos2PsIfAttribEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cabhQos2PsIfAttribEntry.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PsIfAttribEntry.setDescription("Number of media access priorities and number of queues for each PS interface in the Residential Gateway. PS does not need to provide support for entries associated with Aggregated LAN interfaces (ifIndex 255 and 254). The PS WAN interfaces are assigned as ifIndex 1 for Wan Management and ifIndex 2 for Wan Data; both interfaces are indicated in this table as 'WAN interface' with ifIndex 1 as the entry identifier.")
cabhQos2PsIfAttribNumPriorities = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhQos2PsIfAttribNumPriorities.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PsIfAttribNumPriorities.setDescription('The number of media access priorities supported by this interface.')
cabhQos2PsIfAttribNumQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhQos2PsIfAttribNumQueues.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PsIfAttribNumQueues.setDescription('The number of queues associated with this interface.')
cabhQos2PolicyHolderEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhQos2PolicyHolderEnabled.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyHolderEnabled.setDescription('The value true indicates that the Policy Holder entity is active and advertised in PS UPnP standard discovery mechanisms; false indicates it is disabled.')
cabhQos2PolicyAdmissionControl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhQos2PolicyAdmissionControl.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyAdmissionControl.setDescription('Indicates if the QoS Policy Admission Control is enabled or disabled for all the traffic requests.')
cabhQos2NumActivePolicyHolder = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhQos2NumActivePolicyHolder.setStatus('current')
if mibBuilder.loadTexts: cabhQos2NumActivePolicyHolder.setDescription('Indicates the number of active policy holders the PS have discovered in the LAN. This object includes the PS Policy Holder if active.')
cabhQos2PolicyTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4), )
if mibBuilder.loadTexts: cabhQos2PolicyTable.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyTable.setDescription("This table contains the operator and user created policies for the management of QoS for applications. PS creates non-persistent entries (of type 'upnp') for the QoS-aware applications and services discovered through UPnP actions in the user part of this table which could be converted to persistent entries by user (of type 'user' or by cable operator of type 'operatorForHomeUserOnly).")
cabhQos2PolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1), ).setIndexNames((0, "CABH-QOS2-MIB", "cabhQos2PolicyOwner"), (0, "CABH-QOS2-MIB", "cabhQos2PolicyOwnerRuleId"))
if mibBuilder.loadTexts: cabhQos2PolicyEntry.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyEntry.setDescription('The indices for these entries.')
cabhQos2PolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("operatorOnly", 1), ("homeUser", 2), ("operatorForHomeUser", 3), ("upnp", 4))))
if mibBuilder.loadTexts: cabhQos2PolicyOwner.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyOwner.setDescription("This Index defines the policy creation owner. The entries of type 'upnp' are dynamically created by the PS for the applications, services and devices that it discovers on the LAN with UPnP QoS actions.")
cabhQos2PolicyOwnerRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cabhQos2PolicyOwnerRuleId.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyOwnerRuleId.setDescription('Index for the set of rules related to an owner index.')
cabhQos2PolicyRuleOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyRuleOrder.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyRuleOrder.setDescription('The order in which the policy rules are processed within An owner.')
cabhQos2PolicyAppDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyAppDomain.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyAppDomain.setDescription('Vendor domain name from the Vendor application name URN.')
cabhQos2PolicyAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyAppName.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyAppName.setDescription('Text description of the application.')
cabhQos2PolicyServiceProvDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyServiceProvDomain.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyServiceProvDomain.setDescription('The service Provider Service Domain Name from the service Provider URN.')
cabhQos2PolicyServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyServiceName.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyServiceName.setDescription('Text description of the Service.')
cabhQos2PolicyPortDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyPortDomain.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyPortDomain.setDescription('Domain name from the Port URN.')
cabhQos2PolicyPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 9), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyPortNumber.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyPortNumber.setDescription('Well known IP transport port of the application.')
cabhQos2PolicyIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 10), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyIpType.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyIpType.setDescription('The type of InetAddress for cabhQos2PolicySrcIp, and cabhQos2PolicyDestIp.')
cabhQos2PolicyIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyIpProtocol.setReference('http://www.iana.org/assignments/protocol-numbers')
if mibBuilder.loadTexts: cabhQos2PolicyIpProtocol.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyIpProtocol.setDescription("The IANA-defined IP protocol number representing the IP protocol to match against the IPv4 protocol number or the IPv6 Next- Header number in the packet. '0' means no protocol is specified as matching criteria for policy determination, i.e., QoS policy is irrespective of IP protocol.")
cabhQos2PolicySrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 12), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicySrcIp.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicySrcIp.setDescription("The IP address to match against the packet's source IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.")
cabhQos2PolicyDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 13), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyDestIp.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyDestIp.setDescription("The IP address to match against the packet's source IP address. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.")
cabhQos2PolicySrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 14), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicySrcPort.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicySrcPort.setDescription('The value that the layer-4 source port number in the packet must have in order to match this policy entry.')
cabhQos2PolicyDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 15), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyDestPort.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyDestPort.setDescription('The value that the layer-4 destination port number in the packet must have in order to match this policy entry.')
cabhQos2PolicyTraffImpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyTraffImpNum.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyTraffImpNum.setDescription("The Traffic priority being assigned to this policy. The final packet tagging is determined by 802.1D rules with the priority hierarchy order (highest to lowest priority) as defined in 802.1D-2004 table G-2: 7, 6, 5, 4, 3, 0, 2, 1. Note that traffic type '1' and '2' has lower priority than '0' (best effort).")
cabhQos2PolicyUserImportance = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyUserImportance.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyUserImportance.setDescription('The UPnP relative value to determine the allocation or reallocation of resources to multiple streams.')
cabhQos2PolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2PolicyRowStatus.setStatus('current')
if mibBuilder.loadTexts: cabhQos2PolicyRowStatus.setDescription("The status of this conceptual row. All writable objects in this row may be modified at any time. The PS MUST NOT allow creation of new entry or modification to an existing active entry such that the resulting entry is a duplicate entry with respect to the following MIBs in an entry: cabhQos2PolicyAppDomain, cabhQos2PolicyAppNameSnmpAdminString, cabhQos2PolicyServiceProvDomainSnmpAdminString, cabhQos2PolicyServiceName SnmpAdminString, cabhQos2PolicyPortDomain SnmpAdminString, cabhQos2PolicyPortNumber InetPortNumber, cabhQos2PolicyIpType InetAddressType, cabhQos2PolicyIpProtocol Unsigned32, cabhQos2PolicySrcIp InetAddress, cabhQos2PolicyDestIp InetAddress, cabhQos2PolicySrcPort InetPortNumber, cabhQos2PolicyDestPort InetPortNumber, The entries of type 'upnp' are not persistent while others are persistent. The user or the operator can change the 'upnp' entries and in that case the PS MUST change the entry to either 'homeUser' or 'operatorForHomeUser', respectively. The PS MUST NOT change the entries of type 'upnp' to 'operatorOnly'.")
cabhQos2TrafficClassTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1), )
if mibBuilder.loadTexts: cabhQos2TrafficClassTable.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassTable.setDescription("This table contains the Classifiers being configured in the PS as an intermediate QOS device. For matching classifiers the PS processes entries in a sorted manner, first entries with cabhQos2TrafficClassMethod 'static' and then 'dynamic' entries.")
cabhQos2TrafficClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1), ).setIndexNames((0, "CABH-QOS2-MIB", "cabhQos2TrafficClassMethod"), (0, "CABH-QOS2-MIB", "cabhQos2TrafficClassIdx"))
if mibBuilder.loadTexts: cabhQos2TrafficClassEntry.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassEntry.setDescription("The conceptual row definition of this table. Only entries with cabhQos2TrafficClassMethod 'static' do persist after PS reboot.")
cabhQos2TrafficClassMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("upnp", 2))))
if mibBuilder.loadTexts: cabhQos2TrafficClassMethod.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassMethod.setDescription("Indicates how this entry have been created. 'static' indicates that the entry has been provisioned via SNMP or related mechanisms like a config file. 'upnp' indicates that the entry was created via UPnP Qos actions.")
cabhQos2TrafficClassIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cabhQos2TrafficClassIdx.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassIdx.setDescription('The index of this conceptual row entry.')
cabhQos2TrafficClassProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassProtocol.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassProtocol.setDescription("The IANA IP transport protocol designated for this classifier. '0' means no protocol is specified as matching criteria.")
cabhQos2TrafficClassIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 4), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassIpType.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassIpType.setDescription('The type of InetAddress for cabhQos2TrafficClassSrcIp, and cabhQos2TrafficClassDestIp.')
cabhQos2TrafficClassSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassSrcIp.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassSrcIp.setDescription("The IP address to match against the packet's source IP address for this classifier. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.")
cabhQos2TrafficClassDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 6), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassDestIp.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassDestIp.setDescription("The IP address to match against the packet's source IP address fro this classifier. This may not be a DNS name, but may be an IPv4 or IPv6 prefix.")
cabhQos2TrafficClassSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 7), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassSrcPort.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassSrcPort.setDescription('The value that the layer-4 source port number in the packet must have in order to match this classifier entry.')
cabhQos2TrafficClassDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassDestPort.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassDestPort.setDescription('The value that the layer-4 destination port number in the packet must have in order to match this classifier entry.')
cabhQos2TrafficClassImpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassImpNum.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassImpNum.setDescription('The traffic priority assigned to this classifier and used for the tagging of the packet streams.')
cabhQos2TrafficClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhQos2TrafficClassRowStatus.setStatus('current')
if mibBuilder.loadTexts: cabhQos2TrafficClassRowStatus.setDescription("The status of this conceptual row. All writable objects in rows with cabhQosTrafficMethod 'static' may be modified at any time. An SNMP Set to Entries with cabhQosTrafficMethod 'upnp' returns an error 'wrongValue'with the exception of the RowStatus object when set to 'destroy'. An attempt to create an entry via SNMP with cabhQosTrafficMethod UPnP returns error 'wrongValue'.")
cabhQos2Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2))
cabhQos2Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 1))
cabhQos2Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 2))
cabhQos2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 1, 1)).setObjects(("CABH-QOS2-MIB", "cabhQos2Group"), ("CABH-QOS2-MIB", "cabhQos2ClassifierGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhQos2Compliance = cabhQos2Compliance.setStatus('current')
if mibBuilder.loadTexts: cabhQos2Compliance.setDescription('The compliance statement for devices that implement CableHome QOS UPnP capabilities.')
cabhQos2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 2, 1)).setObjects(("CABH-QOS2-MIB", "cabhQos2SetToFactory"), ("CABH-QOS2-MIB", "cabhQos2LastSetToFactory"), ("CABH-QOS2-MIB", "cabhQos2PsIfAttribNumPriorities"), ("CABH-QOS2-MIB", "cabhQos2PsIfAttribNumQueues"), ("CABH-QOS2-MIB", "cabhQos2PolicyHolderEnabled"), ("CABH-QOS2-MIB", "cabhQos2PolicyAdmissionControl"), ("CABH-QOS2-MIB", "cabhQos2NumActivePolicyHolder"), ("CABH-QOS2-MIB", "cabhQos2PolicyRuleOrder"), ("CABH-QOS2-MIB", "cabhQos2PolicyAppDomain"), ("CABH-QOS2-MIB", "cabhQos2PolicyAppName"), ("CABH-QOS2-MIB", "cabhQos2PolicyServiceProvDomain"), ("CABH-QOS2-MIB", "cabhQos2PolicyServiceName"), ("CABH-QOS2-MIB", "cabhQos2PolicyPortDomain"), ("CABH-QOS2-MIB", "cabhQos2PolicyPortNumber"), ("CABH-QOS2-MIB", "cabhQos2PolicyIpProtocol"), ("CABH-QOS2-MIB", "cabhQos2PolicyIpType"), ("CABH-QOS2-MIB", "cabhQos2PolicySrcIp"), ("CABH-QOS2-MIB", "cabhQos2PolicyDestIp"), ("CABH-QOS2-MIB", "cabhQos2PolicySrcPort"), ("CABH-QOS2-MIB", "cabhQos2PolicyDestPort"), ("CABH-QOS2-MIB", "cabhQos2PolicyTraffImpNum"), ("CABH-QOS2-MIB", "cabhQos2PolicyUserImportance"), ("CABH-QOS2-MIB", "cabhQos2PolicyRowStatus"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassProtocol"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassIpType"), ("CABH-QOS2-MIB", "cabhQos2PolicySrcIp"), ("CABH-QOS2-MIB", "cabhQos2PolicyDestIp"), ("CABH-QOS2-MIB", "cabhQos2PolicySrcPort"), ("CABH-QOS2-MIB", "cabhQos2PolicyDestPort"), ("CABH-QOS2-MIB", "cabhQos2PolicyTraffImpNum"), ("CABH-QOS2-MIB", "cabhQos2PolicyUserImportance"), ("CABH-QOS2-MIB", "cabhQos2PolicyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhQos2Group = cabhQos2Group.setStatus('current')
if mibBuilder.loadTexts: cabhQos2Group.setDescription('Group of objects for CableHome QOS management.')
cabhQos2ClassifierGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 2, 2)).setObjects(("CABH-QOS2-MIB", "cabhQos2TrafficClassProtocol"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassIpType"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassSrcIp"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassDestIp"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassSrcPort"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassDestPort"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassImpNum"), ("CABH-QOS2-MIB", "cabhQos2TrafficClassRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhQos2ClassifierGroup = cabhQos2ClassifierGroup.setStatus('current')
if mibBuilder.loadTexts: cabhQos2ClassifierGroup.setDescription('Group of objects for cableHome QOS Packet classification.')
mibBuilder.exportSymbols("CABH-QOS2-MIB", cabhQos2PolicyTraffImpNum=cabhQos2PolicyTraffImpNum, cabhQos2PolicyOwnerRuleId=cabhQos2PolicyOwnerRuleId, cabhQos2PolicyHolderEnabled=cabhQos2PolicyHolderEnabled, cabhQos2PolicyDestPort=cabhQos2PolicyDestPort, cabhQos2TrafficClassSrcPort=cabhQos2TrafficClassSrcPort, cabhQos2PolicySrcPort=cabhQos2PolicySrcPort, cabhQos2LastSetToFactory=cabhQos2LastSetToFactory, cabhQos2NumActivePolicyHolder=cabhQos2NumActivePolicyHolder, cabhQos2TrafficClassDestIp=cabhQos2TrafficClassDestIp, cabhQos2TrafficClassTable=cabhQos2TrafficClassTable, cabhQos2Mib=cabhQos2Mib, cabhQos2PolicyEntry=cabhQos2PolicyEntry, cabhQos2Mib2Notifications=cabhQos2Mib2Notifications, cabhQos2PolicyIpProtocol=cabhQos2PolicyIpProtocol, cabhQos2TrafficClassProtocol=cabhQos2TrafficClassProtocol, cabhQos2Compliance=cabhQos2Compliance, cabhQos2TrafficClassIdx=cabhQos2TrafficClassIdx, cabhQos2PsIfAttributes=cabhQos2PsIfAttributes, cabhQos2PsIfAttribTable=cabhQos2PsIfAttribTable, cabhQos2SetToFactory=cabhQos2SetToFactory, cabhQos2TrafficClassRowStatus=cabhQos2TrafficClassRowStatus, cabhQos2MibObjects=cabhQos2MibObjects, cabhQos2PolicyUserImportance=cabhQos2PolicyUserImportance, cabhQos2PolicyRowStatus=cabhQos2PolicyRowStatus, cabhQos2TrafficClassImpNum=cabhQos2TrafficClassImpNum, cabhQos2PolicyRuleOrder=cabhQos2PolicyRuleOrder, cabhQos2PolicyIpType=cabhQos2PolicyIpType, cabhQos2DeviceObjects=cabhQos2DeviceObjects, cabhQos2PolicySrcIp=cabhQos2PolicySrcIp, cabhQos2Groups=cabhQos2Groups, cabhQos2PsIfAttribNumPriorities=cabhQos2PsIfAttribNumPriorities, cabhQos2PolicyAppName=cabhQos2PolicyAppName, cabhQos2TrafficClassIpType=cabhQos2TrafficClassIpType, cabhQos2PolicyServiceProvDomain=cabhQos2PolicyServiceProvDomain, cabhQos2PolicyServiceName=cabhQos2PolicyServiceName, cabhQos2Base=cabhQos2Base, cabhQos2TrafficClassEntry=cabhQos2TrafficClassEntry, cabhQos2PolicyPortDomain=cabhQos2PolicyPortDomain, PYSNMP_MODULE_ID=cabhQos2Mib, cabhQos2TrafficClassMethod=cabhQos2TrafficClassMethod, cabhQos2TrafficClassDestPort=cabhQos2TrafficClassDestPort, cabhQos2PolicyTable=cabhQos2PolicyTable, cabhQos2TrafficClassSrcIp=cabhQos2TrafficClassSrcIp, cabhQos2PsIfAttribEntry=cabhQos2PsIfAttribEntry, cabhQos2Group=cabhQos2Group, cabhQos2PolicyHolderObjects=cabhQos2PolicyHolderObjects, cabhQos2PolicyAdmissionControl=cabhQos2PolicyAdmissionControl, cabhQos2PolicyOwner=cabhQos2PolicyOwner, cabhQos2ClassifierGroup=cabhQos2ClassifierGroup, cabhQos2PolicyDestIp=cabhQos2PolicyDestIp, cabhQos2Conformance=cabhQos2Conformance, cabhQos2Compliances=cabhQos2Compliances, cabhQos2PolicyAppDomain=cabhQos2PolicyAppDomain, cabhQos2PsIfAttribNumQueues=cabhQos2PsIfAttribNumQueues, cabhQos2PolicyPortNumber=cabhQos2PolicyPortNumber)
