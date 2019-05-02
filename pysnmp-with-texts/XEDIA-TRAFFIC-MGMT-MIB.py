#
# PySNMP MIB module XEDIA-TRAFFIC-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-TRAFFIC-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:43:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier, Counter32, NotificationType, Integer32, ObjectIdentity, Counter64, IpAddress, Gauge32, iso, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter32", "NotificationType", "Integer32", "ObjectIdentity", "Counter64", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Bits")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaTrafficMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 2))
if mibBuilder.loadTexts: xediaTrafficMgmtMIB.setLastUpdated('9705022155Z')
if mibBuilder.loadTexts: xediaTrafficMgmtMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaTrafficMgmtMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaTrafficMgmtMIB.setDescription("This module defines objects for the management of Xedia's proprietary Traffic Management capability. This capability is based on Class-Based Queueing (CBQ). The purpose of the Xedia Traffic Management (xtm) function is to share access to an interface's bandwidth based on policies set up by the administrator.")
xtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 2, 1))
xtmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 2, 2))
xtmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 2, 3))
class XtmIpAddress(TextualConvention, IpAddress):
    description = 'An IPv4 or IPv6 address. The version can be inferred from length.'
    status = 'current'
    displayHint = '1d.'

class XtmProtocol(TextualConvention, Integer32):
    description = 'The value of the IP Protocol field of an IP Datagram Header. This identifies the protocol layer above IP. For example, the value 6 is used for TCP and the value 17 is used for UDP. The values of this field are defined in the Assigned Numbers RFC.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 17))
    namedValues = NamedValues(("any", 0), ("icmp", 1), ("tcp", 6), ("udp", 17))

class XtmPort(TextualConvention, Integer32):
    description = 'A UDP or TCP port value. The values of this field are defined in the Assigned Numbers RFC.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 20, 21, 23, 25, 53, 67, 68, 69, 70, 79, 80, 119, 123, 161, 162, 179))
    namedValues = NamedValues(("any", 0), ("ftpData", 20), ("ftp", 21), ("telnet", 23), ("smtp", 25), ("domain", 53), ("bootps", 67), ("bootpc", 68), ("tftp", 69), ("gopher", 70), ("finger", 79), ("wwwHttp", 80), ("nntp", 119), ("ntp", 123), ("snmp", 161), ("snmpTrap", 162), ("bgp", 179))

class XtmBitRate(TextualConvention, Integer32):
    description = 'A data rate in bits/second.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class XtmTosOctet(TextualConvention, OctetString):
    description = 'A single hexidecimal octet used to specify a type-of-service (TOS) value or mask.'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class XtmRange(DisplayString):
    description = "A range of values. A contiguous range may be specified using a dash (-). Thus a contiguous range of integers may be expressed as 'lowValue-highValue', e.g. 5-10. A discontiguous range may be specified using a comma (,) separated list. For example, '1,12,55'. Contiguous and discontiguous ranges may be combined, as in '1,5-10,12,55'. When set, values are added to the existing XtmRange. For example, setting '100-200' to the existing range of '1,5-10,12,55' yields the value '1,5-10,12,55,100-200'. Values may be deleted from a list using the minus (-) symbol. For example, setting range consisting of '1,5-10,12,55,100-200' to '-55,-150' yields the range string '1,,5-10,12,100-149,151-200'. String values may be completely deleted by setting them to the NULL string. This textual-convention may be used on a variety of data types, including integers, integer enumerations, IpAddresses, and OCTET STRINGs."
    status = 'current'

xtmClassTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2), )
if mibBuilder.loadTexts: xtmClassTable.setStatus('current')
if mibBuilder.loadTexts: xtmClassTable.setDescription("This table is a 'flattened' version of a hierarchical class trees that specify the bandwidth allocation for the CBQ interfaces of the system. Each tree is rooted at an interface. A class may either be a leaf, meaning it has no children, or it may be an interior class which has children. As packets are forwarded out an interface, they are compared to the 'flow definition' of each class down the tree until a matching leaf is found or until all classes are traversed. Once a matching class is found, the packet is transmitted or not based on the constraints configured for the class, most importantly the allocated bandwidth as identified by xtmClassRate. If no matching class is found, the packet is dropped. The 'flow definition' for a class can be defined based on inclusive ranges of the following packet fields: o Source IP Address (or a domain name) o Destination IP Address (or a domain name) o Protocol above layer 3 (e.g., UDP, TCP, ICMP, etc.) o Source Port (which identifies service, e.g., FTP, Telnet, SMTP, etc.) o Destination Port It is important that packets only match zero or one traffic class. In order for this to be true, certain rules must be enforced when classes are defined. Specifically, all 'sibling' classes must be defined using the same criteria. Also, children must use criteria not already specified by one of their ancestors or they must specify a subrange of an already specified criteria. Therefore, this tree would be legal: interface 1 subnet A protocol UDP port SNMP protocol TCP subnet B But this tree would be illegal: interface 2 subnet A subnet B (illegal -- not subrange of parent) protocol TCP (illegal -- different criteria than sibling)")
xtmClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "XEDIA-TRAFFIC-MGMT-MIB", "xtmClassName"))
if mibBuilder.loadTexts: xtmClassEntry.setStatus('current')
if mibBuilder.loadTexts: xtmClassEntry.setDescription("Information about a single traffic class. Traffic classes are identified by their associated interface's ifIndex and their name. (Which means class names must be unique for a particular interface.) Traffic classes can be created and destroyed using this table's xtmClassRowStatus object. A class cannot be used by the run-time system (xtmClassRowStatus = 'active(1)') if it does not follow the rules listed in the DESCRIPTION of the previous object. In this case, the xtmClassRowStatus will remain 'notReady(3)' and the xtmClassOperStatus will be 'downConflict(3)'. Also, in order to become active, the user must have specified a valid value for xtmClassParent and xtmClassRate. All other settable objects may be left at their default values. Finally, the following objects cannot be modified once the row is active: xtmClassParent, and xtmClassQueueElasticityFactor.")
xtmClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: xtmClassName.setStatus('current')
if mibBuilder.loadTexts: xtmClassName.setDescription("A user-defined name for the traffic class. This is the unique identifier for the class within the scope of the interface. For example, the class that defines the IP address range for a particular customer might be 'Customer Fred Co.'")
xtmClassParent = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)).clone('interface')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassParent.setStatus('current')
if mibBuilder.loadTexts: xtmClassParent.setDescription("This object will have one of the following values: - the value of xtmClassName for the parent class in the hierarchy, - the value 'interface' if the class is directly under the interface, which is the root of the tree, or - the value 'orphan' if the class is defined but not yet inserted into the tree. If a parent name is specified, the row cannot become active (have its xtmClassRowStatus set to 'active(1)' unless the parent is valid and is itself active. Note that an interface may have several traffic classes with an xtmClassParent of 'interface'. Note also that an 'orphan' class cannot become 'active(1)' - it must first have a valid parent specified.")
xtmClassRate = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 13), XtmBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassRate.setStatus('current')
if mibBuilder.loadTexts: xtmClassRate.setDescription("A fraction of the bandwidth of the root interface to be allocated to this traffic class. Note that specifying 0 bits/second effectively filters all traffic that matches this class' flow specification. Also note that the sum of bit rates for all classes defined under the same class must be less than or equal to xtmClassRate of the parent.")
xtmClassBounded = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassBounded.setStatus('current')
if mibBuilder.loadTexts: xtmClassBounded.setDescription("The value of this object is 'true(1)' if the class is bounded (can't 'borrow' bandwidth from its parent class) and 'false(2)' otherwise.")
xtmClassPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassPriority.setStatus('current')
if mibBuilder.loadTexts: xtmClassPriority.setDescription('The priority for this class. The smaller the value, the higher the priority. Delay-sensitive flows (such as video or audio) should be given higher priority values.')
xtmClassOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("downConflict", 3), ("autoClassActive", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassOperStatus.setStatus('current')
if mibBuilder.loadTexts: xtmClassOperStatus.setDescription("The actual operational status of the traffic class. The value 'up(1)' means this traffic class is in use, the value 'down(2)' indicates the traffic class is not in use either due to an internal problem or because it (or an ancestor) is administratively disabled, and the value 'downConflict(3)' indicates the class definition conflicts with those of its siblings. The value autoClassActive(4) means that the class is a dynamically created AutoClass, which may not be modified in any way until it is saved to Non-Volatile configuration memory. After an AutoClass is saved to NVRAM, it's operational status will transistion to up(1).")
xtmClassOperMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassOperMsg.setStatus('current')
if mibBuilder.loadTexts: xtmClassOperMsg.setDescription('The operational message associated with the operational status. The message usually provides additional information that may not be obvious through the operational status.')
xtmClassBwUse = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("atLimit", 1), ("underLimit", 2), ("overLimit", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassBwUse.setStatus('current')
if mibBuilder.loadTexts: xtmClassBwUse.setDescription("An indication of whether this traffic class has used its allocated bandwidth (as indicated by xtmClassPercent), has not used its allocated bandwidth or has used more than its allocated bandwidth and is therefore 'atLimit(1)', 'underLimit(2)', or 'overLimit(3)' respectively.")
xtmClassUnsatisfied = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 25), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassUnsatisfied.setStatus('current')
if mibBuilder.loadTexts: xtmClassUnsatisfied.setDescription("An indication of whether this traffic class is 'unsatisfied'. The value of this object is 'true(1)' if it is underLimit and has a persistent backlog, meaning it has packets waiting in its queue. The value is 'false(1)' otherwise. Note that a class can be considered satisfied if it is underLimit and it just hasn't had anything to transmit. The presence of an unsatisfied class indicates that some other class is overLimit and 'hogging' bandwidth. Persistently unsatisfied classes indicate that tuning some of the parameters (such as xtmClassMaxIdle or xtmClassBounded) may be necessary.")
xtmClassQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 26), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmClassQueueSize.setStatus('current')
if mibBuilder.loadTexts: xtmClassQueueSize.setDescription('The size of the queue associated with this traffic class. This is the maximum number of packets that can be in the queue, not the number that are currently queued (see xtmClassStatsQueuedPkts).')
xtmClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassRowStatus.setStatus('current')
if mibBuilder.loadTexts: xtmClassRowStatus.setDescription('Traffic classes are created and delected using this object (using the conventions described in RFC1903).')
xtmClassMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 28), XtmBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassMaxRate.setStatus('current')
if mibBuilder.loadTexts: xtmClassMaxRate.setDescription("The maximum bandwidth the class may achieve, including bandwidth allocated to this class, and any bandwidth that may be borrowed. A value of zero (0) indicates that this feature is not being used. The xtmClassMaxRate must be set to a value higher than the xtmClassRate, but may also exceed the parent class's xtmClassRate.")
xtmClassPeerClassificationOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 44), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassPeerClassificationOrder.setStatus('current')
if mibBuilder.loadTexts: xtmClassPeerClassificationOrder.setDescription("A positive integer representing the classification order of peers within the classification hierarchy. For example, when creating three children under the 'root' class the packet classifier checks incoming packets againts classification parameters from left to right in the order in which the children were created. Each peer (aka 'sibling') is assigned an xtmClass- PeerClassificationOrder of 100 by default, as shown below. +_______+ | root | | class | +_______+ / | \\ / | \\ / | \\ / | \\ / | \\ / | \\ +_______+ +_______+ +_______+ | A | | B | | C | | class | | class | | class | | 100 | | 100 | | 100 | (peer classification order) +_______+ +_______+ +_______+ In the figure above, classification order proceeds from A to B to C. In order to alter this order, this object may be modified. For example, to change the order to C, B A one might assign an xtmClassPeerClassificationOrder of 50 to class C, and an xtmClassPeerClassificationOrder of 150 to class A, resulting in the ordered tree shown below. +_______+ | root | | class | +_______+ / | \\ / | \\ / | \\ / | \\ / | \\ / | \\ +_______+ +_______+ +_______+ | C | | B | | A | | class | | class | | class | | 50 | | 100 | | 150 | (peer classification order) +_______+ +_______+ +_______+ ")
xtmClassSrcIpAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 45), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassSrcIpAddresses.setStatus('current')
if mibBuilder.loadTexts: xtmClassSrcIpAddresses.setDescription("The range of IP source addresses that match this class. An all zeros value means 'any source address'.")
xtmClassDestIpAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 46), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassDestIpAddresses.setStatus('current')
if mibBuilder.loadTexts: xtmClassDestIpAddresses.setDescription("The range of IP destination addresses that match this class. An all zeros value means 'any destination address'.")
xtmClassProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 47), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassProtocols.setStatus('current')
if mibBuilder.loadTexts: xtmClassProtocols.setDescription("The range of IP protocols that match this class. The value '0' 'any protocol'. Numeric strings, character strings, and combinations of the two may be used. Valid strings include: Numeric String Character String ______________ ________________ 1 icmp 6 tcp 17 udp 89 ospf ")
xtmClassSrcPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 48), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassSrcPorts.setStatus('current')
if mibBuilder.loadTexts: xtmClassSrcPorts.setDescription("The range of UDP or TCP source ports that match this class. The value '0' 'any port'. Numeric strings, character strings, and combinations of the two may be used. Valid strings include, but are not limited to the following: Numeric String Character String ______________ ________________ 20 ftpdata 21 ftp 23 telnet 25 smtp 53 domain 67 bootps 68 bootpc 69 tftp 70 gopher 79 finger 80 http 119 nntp 123 ntp 161 snmp 162 snmptrap 179 bgp ")
xtmClassDestPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 49), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassDestPorts.setStatus('current')
if mibBuilder.loadTexts: xtmClassDestPorts.setDescription("The range of UDP or TCP destination ports that match this class. The value '0' 'any port'. Numeric strings, character strings, and combinations of the two may be used. Valid strings include, but are not limited to the following: Numeric String Character String ______________ ________________ 20 ftp_data 21 ftp 23 telnet 25 smtp 53 domain 67 bootps 68 bootpc 69 tftp 70 gopher 79 finger 80 http 119 nntp 123 ntp 161 snmp 162 snmptrap 179 bgp ")
xtmClassApplications = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 50), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassApplications.setStatus('current')
if mibBuilder.loadTexts: xtmClassApplications.setDescription("The application level protocol of the class. Application classification allows you to classify based on the application level protocol. Each application has a corresponding 'Established' enumeration which specifies that communication can not be initiated through this class. For example, 'telnetEstablished' specifies that telnet connections can not pass through this class. 'Established' enumerations provide stateful firewall capabily. For example, in the following configuration, telnet configurations can only be initiated from Host B. Host A can not initiate a telnet connection. +__________________________________+ | | Host A _____| telnet class telnetEstablished|_____ Host B | on cbq.1 class on cbq.2 | +__________________________________+ Numeric strings, character strings, and combinations of the two may be used. Valid strings include the following: Numeric String Character String ______________ ________________ 1 allTcp 2 allTcpEstablished 3 allUdp 4 allUdpEstablished 5 ftp 6 ftpEstablished 7 telnet 8 telnetEstablished 9 http 10 httpEstablished 11 dns 12 dnsEstablished 13 tftp 14 tftpEstablished 15 snmp 16 snmpEstablished 17 httpSSL 18 httpSSLEstablished 19 smtp 20 smtpEstablished 21 bgp 22 bgpEstablished 23 slaProbe 24 slaProbeEstablished ")
xtmClassClassificationTos = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 51), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassClassificationTos.setStatus('current')
if mibBuilder.loadTexts: xtmClassClassificationTos.setDescription('The range of IPv4 Tos Octet values that match this class.')
xtmClassSrcDomainNames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 52), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassSrcDomainNames.setStatus('current')
if mibBuilder.loadTexts: xtmClassSrcDomainNames.setDescription('A list of domain names which are to be dynamically included in the range of source IP addresses.')
xtmClassDestDomainNames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 53), XtmRange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassDestDomainNames.setStatus('current')
if mibBuilder.loadTexts: xtmClassDestDomainNames.setDescription('A list of domain names which are to be dynamically included in the range of destination IP addresses.')
xtmClassOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 2, 1, 2, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("and", 1), ("or", 2))).clone('and')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmClassOperator.setStatus('current')
if mibBuilder.loadTexts: xtmClassOperator.setDescription("An operator applied to all classification parameters of this class. A value of 'and' indicates that packets must match all classification parameters specified by the class in order to be classified within the class. A value of 'or' indicates that packets must match any one of the configured classification parameters specified by the class in order to be classified within the class. For example, consider a class with classification parameters xtmClassSrcIpAddresses of '198.202.232.10' and xtmClassProtocol of 'udp'. When xtmClassOperator is 'and', packets with IP source addresses of 198.202.232.10 and IP protocol of udp are classified within this class. Whe xtmClassOperator is 'or', packets with IP source addresses of 198.202.232.10 or IP protocol or udp are classified within this class.")
mibBuilder.exportSymbols("XEDIA-TRAFFIC-MGMT-MIB", xtmObjects=xtmObjects, xtmClassParent=xtmClassParent, xtmClassOperStatus=xtmClassOperStatus, xtmClassOperMsg=xtmClassOperMsg, xtmClassName=xtmClassName, XtmPort=XtmPort, xtmClassMaxRate=xtmClassMaxRate, xtmConformance=xtmConformance, xtmClassApplications=xtmClassApplications, xtmClassDestIpAddresses=xtmClassDestIpAddresses, xtmClassRate=xtmClassRate, xtmClassBwUse=xtmClassBwUse, xtmClassOperator=xtmClassOperator, xtmClassEntry=xtmClassEntry, xtmClassProtocols=xtmClassProtocols, xtmClassUnsatisfied=xtmClassUnsatisfied, xtmClassQueueSize=xtmClassQueueSize, xediaTrafficMgmtMIB=xediaTrafficMgmtMIB, xtmClassRowStatus=xtmClassRowStatus, xtmClassSrcIpAddresses=xtmClassSrcIpAddresses, PYSNMP_MODULE_ID=xediaTrafficMgmtMIB, XtmRange=XtmRange, XtmProtocol=XtmProtocol, xtmClassBounded=xtmClassBounded, xtmClassPeerClassificationOrder=xtmClassPeerClassificationOrder, xtmClassSrcDomainNames=xtmClassSrcDomainNames, xtmClassTable=xtmClassTable, XtmTosOctet=XtmTosOctet, XtmIpAddress=XtmIpAddress, xtmNotifications=xtmNotifications, xtmClassSrcPorts=xtmClassSrcPorts, xtmClassPriority=xtmClassPriority, xtmClassClassificationTos=xtmClassClassificationTos, XtmBitRate=XtmBitRate, xtmClassDestPorts=xtmClassDestPorts, xtmClassDestDomainNames=xtmClassDestDomainNames)
