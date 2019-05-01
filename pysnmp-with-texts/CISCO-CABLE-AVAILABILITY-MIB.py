#
# PySNMP MIB module CISCO-CABLE-AVAILABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CABLE-AVAILABILITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Counter32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Unsigned32, ObjectIdentity, Integer32, Gauge32, TimeTicks, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Unsigned32", "ObjectIdentity", "Integer32", "Gauge32", "TimeTicks", "NotificationType", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoCableAvailabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 242))
ciscoCableAvailabilityMIB.setRevisions(('2003-02-20 00:00', '2001-11-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableAvailabilityMIB.setRevisionsDescriptions(('Changed range of object ccaHCCPMemChanSwitchPosition and added ciscoCableAvailabilityComplianceRev1 to allow MIN-ACCESS as read-only for the same. ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCableAvailabilityMIB.setLastUpdated('200302200000Z')
if mibBuilder.loadTexts: ciscoCableAvailabilityMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableAvailabilityMIB.setContactInfo(' Cisco Systems Customer Service Postal: Cisco Systems 170 West Tasman Drive San Jose, CA 95134 U.S.A. Phone: +1 800 553-NETS E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableAvailabilityMIB.setDescription("This is the MIB module for management of Hot Standby Connection to Connection Protocol (HCCP) features. HCCP is a Cisco proprietary solution for High System Availability for Cable Modem Termination Systems (CMTS). The HCCP protocol is primarily responsible for failure detection and to initiate switchover from one CMTS to another. The CMTS protection is at the RF mac domain level, where protecting and working CMTS cable interfaces operate on the same downstream and upstream frequency. HCCP Terminology: HCCP group: A set of RF MAC interfaces which communicate using HCCP messaging. HCCP member: Each RF MAC interface configured for HCCP. Protect: A member in a HCCP group which acts as the hot standby and protecting other members. Working: The member in a HCCP group that is being protected. Thus a 'HCCP group' consists of 'HCCP members' which are RF MAC interfaces configured to function as 'Protect' or 'Working'. Some RF mac interfaces are configured to form a 'HCCP group' and members within one 'HCCP group' communicate with each other using HCCP messaging. By HCCP messaging, some member acting as 'Protect' or hot standby can detect a failure on the other members which are designated as 'Working' in the same HCCP group. The 'Protect' can then take over traffic on the failed interface. Protection scenarios can be N+1 or 1+1. In the N+1 protection scenario, there is only one CMTS designated for protection of N CMTS. For example in 1+1 : When one linecard fails, the other automatically takes over its traffic. During normal operation, only one linecard forwards traffic, the other linecard stands by and listens to the messages passed from the active one. While in the standby mode, the linecard does not forward traffic. HCCP will automatically switchover to the standby in cases of software failures (crash), linecard insertion/removal, interface shutdowns and cable wiring failures etc. Both Protect and Working are preconfigured on the CMTS and all HCCP configuration must comply with the actual cable plant deployment for correct operation of the HCCP protocol. This MIB includes objects to support the HCCP feature on the CMTS.")
ciscoCableAvailabilityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 1))
ccaHCCPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1))
ccaHCCPVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("others", 1), ("version1", 2), ("version2", 3), ("version3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPVersion.setReference('Data-Over-Cable Service Interface Specifications (DOCSIS) Radio Frequency Interface Specification')
if mibBuilder.loadTexts: ccaHCCPVersion.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPVersion.setDescription('The current version of HCCP features. others(1) : Any other HCCP Version other than the following list. version1(2) : HCCP Version 1.0 supports for 1+1 Availability. (1 RF MAC protecting 1 RF MAC without load sharing on the same upstream and downstream frequencies with DOCSIS1.0+ features) version2(3) : HCCP Version 2.0 supports for 1+1 Availability. (1 RF MAC protecting 1 RF MAC without load sharing on the same upstream and downstream frequencies with DOCSIS1.1 features) version3(4) : HCCP Version 3.0 supports for N+1 Availability. (1 RF MAC protecting N RF MAC without load sharing on different upstream and downstream frequencies with DOCSIS1.1 features).')
ccaHCCPGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2), )
if mibBuilder.loadTexts: ccaHCCPGroupTable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupTable.setDescription('This table contains information of the HCCP groups on the CMTS. A HCCP group consists of a set of Working along with a Protect and each group is identified by a unique group ID number. Only members within a group are allowed to communicate with each other via HCCP messaging. ')
ccaHCCPGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"))
if mibBuilder.loadTexts: ccaHCCPGroupEntry.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupEntry.setDescription('A set of attributes of a HCCP group on the CMTS. An entry in this table exists for each configured HCCP group on the CMTS.')
ccaHCCPGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ccaHCCPGroupID.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupID.setDescription('Identification of the HCCP protection group. Only members of the same group talk to each other via HCCP messaging.')
ccaHCCPGroupAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("md5", 2), ("text", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupAuthentication.setReference("Rivest, R., 'The MD5 Message-Digest Algorithm', RFC1321, MIT LCS & RSA Data Security, Inc., April 1992.")
if mibBuilder.loadTexts: ccaHCCPGroupAuthentication.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupAuthentication.setDescription('The value of this object specifies the type of authentication method used. none(1) : No authentication is performed on that group. md5(2) : The MD5 Message Digest algorithm. text(3) : Authentication based on a textual string. ')
ccaHCCPGroupAuthKeyChain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupAuthKeyChain.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupAuthKeyChain.setDescription('This object is the name of a globally configured key chain. It is used to enable authentication and determine the set of keys which may be used on a particular group. If ccaHCCPGroupAuthentication is text(3), it is used as the authentication password. If ccaHCCPGroupAuthentication is md5(2), it is used as the message digest for md5. If a key chain has not been configured, no authentication is performed on that group.')
ccaHCCPGroupHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(333, 5000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupHelloTime.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupHelloTime.setDescription('Hello time is the interval(in milliseconds) between consecutive HELLO messages. HELLO is a one-way message in HCCP sent from Protect to all Working in the group. It indicates that Protect is ready to receive data and expects HELLO_ACK. HELLO message indicates the existence and state of Protect. Failing to send this message indicates Protect is not in service.')
ccaHCCPGroupHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 25000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupHoldTime.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupHoldTime.setDescription('Hold time is the interval(in milliseconds) between the time of receiving the last HELLO ACK message and the time to assume that the cable interface is out of service. In the case of Working, it is the interval in milliseconds between the time when the Working receives a HELLO message and the time to assume that Protect has failed. In the case of Protect, it is the interval in milliseconds between the time when the Protect sends last HELLO message without seeing HELLO_ACK and the time to assume that Working has failed. It is carried by HELLO message and is used by Protect and all Working.')
ccaHCCPGroupRevertEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupRevertEnable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupRevertEnable.setDescription('Enable or disable the Protect to revert switchover after Working is restored to operation. It can be disabled (default) if user wants to perform some tests before revert switching.')
ccaHCCPGroupProtectIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupProtectIpAddrType.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupProtectIpAddrType.setDescription('The type of internet address of ccaHCCPGroupProtectIpAddress.')
ccaHCCPGroupProtectIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupProtectIpAddress.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupProtectIpAddress.setDescription('The IP address of the Protect interface for the group that sends the HELLO message. ')
ccaHCCPGroupIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3), )
if mibBuilder.loadTexts: ccaHCCPGroupIfTable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfTable.setDescription('This table provides the mapping of the RF MAC interfaces on the CMTS to its functionality in the HCCP group. It indicates if the RF MAC interface has been configured as Protect or as a Working.It provides interface specific configuration and state information as well as statistics.')
ccaHCCPGroupIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccaHCCPGroupIfEntry.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfEntry.setDescription('A mapping of a RF MAC interface to its configured functionality as Protect or Working. It provides interface specific configuration and state information as well as statistics. Entries in this table exist for each ifEntry with ifType of docsCableUpstream(129).')
ccaHCCPGroupIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("protect", 2), ("working", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfStatus.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfStatus.setDescription('The value of this object identifies if the interface is functioning as Working or Protect in the HCCP group.')
ccaHCCPGroupIfRevertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfRevertTime.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfRevertTime.setDescription('Revert time used by Working specifies the time interval to wait before automatic revert switching. Within that time interval, manual switchover is allowed to happen.')
ccaHCCPGroupIfTrackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfTrackEnable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfTrackEnable.setDescription('Enable or disable failover based on interface state. The interface can be any interface on the router, which is monitored by keep alive timer. If it is set to true, ccaHCCPGroupTrackInterfaceTable contains the list of interfaces that are being tracked. By default the current interface is under tracking.')
ccaHCCPGroupIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("blocking", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfState.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfState.setDescription('The current state of the HCCP group. The members can either be forwarding traffic or blocking all traffic. ')
ccaHCCPGroupIfLastSwitchReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("holdTimeExpire", 2), ("hwIfDown", 3), ("failTest", 4), ("failLinkDown", 5), ("failBundleDown", 6), ("internal", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfLastSwitchReason.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfLastSwitchReason.setDescription('The reason for last switch. none(1) : No switchover has occurred. holdTimeExpire(2) : Occurs when HCCP fails to hear HELLO/HELLO_ACK and the hold time expires. hwIfDown(3) : Occurs when the hardware interface is down. (eg shut/no shut) failTest(3) : Failover was CLI initiated or SNMP initiated through ccaHCCPGroupSwitchNow. failLinkDown(4) : Failure in the cable wiring or a hardware interface. failBundleDown(5) : A bundled interface failure. internal(6) : All other failures . ')
ccaHCCPGroupIfOnTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfOnTransitions.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfOnTransitions.setDescription("Number of times the value of ccaHCCPGroupIfState transitioned from 'blocking' to 'forwarding'.")
ccaHCCPGroupIfOffTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupIfOffTransitions.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupIfOffTransitions.setDescription("Number of times the value of ccaHCCPGroupIfState transitioned from 'forwarding' to 'blocking'. ")
ccaHCCPGroupTrackInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4), )
if mibBuilder.loadTexts: ccaHCCPGroupTrackInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupTrackInterfaceTable.setDescription('This table contains the attributes of all the interfaces that are being tracked by this group. The interface can be any interface on the chassis, which is monitored by a keep alive timer.')
ccaHCCPGroupTrackInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupTrackIfID"))
if mibBuilder.loadTexts: ccaHCCPGroupTrackInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupTrackInterfaceEntry.setDescription('A set of attributes of an interfaces being tracked within a group. ')
ccaHCCPGroupTrackIfID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: ccaHCCPGroupTrackIfID.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupTrackIfID.setDescription('The value of this object uniquely identifies an interface that is being tracked within this group.')
ccaHCCPGroupTrackIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPGroupTrackIfDescr.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroupTrackIfDescr.setDescription('A textual string containing information about the interface that is being tracked. This corresponds to the ifDescr of the tracked interface.')
ccaHCCPMemberTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5), )
if mibBuilder.loadTexts: ccaHCCPMemberTable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberTable.setDescription("This table contains the attributes of HCCP members. Each RF MAC interface configured for HCCP is called a HCCP member. Entries in this table are created for all members. In the case of Protect, it gives information of all the Working members under it's protection group. In the case of Working, it gives information about itself.")
ccaHCCPMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberID"))
if mibBuilder.loadTexts: ccaHCCPMemberEntry.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberEntry.setDescription('A configurable attributes of a HCCP member within a group. ')
ccaHCCPMemberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ccaHCCPMemberID.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberID.setDescription("The value of this object identifies the Working member's ID inside a group. Members within the same group are uniquely identified by this ID. The ID can be reused outside the group.")
ccaHCCPMemberIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemberIpAddrType.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberIpAddrType.setDescription('The type of internet address of ccaHCCPMemberIpAddress.')
ccaHCCPMemberIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemberIpAddress.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberIpAddress.setDescription('The IP address of the member. If the member functions as Working it represents an IP address on its interface. However in case of Protect, it represents IP address of the Working member that are being protected.')
ccaHCCPMemberState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("nonFunctional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemberState.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberState.setDescription('The current status of to this HCCP group member. If the RF MAC interface is Working, this represents the status of the Working member. active(1) : Working member is forwarding traffic. standby(2) : Working member is blocking traffic. If the RF MAC interface is Protect, this represents the Protect status to this member. active(1) : The Protect is taking over and forwarding the traffic from this Working member which is now blocking. standby(2) : The Protect is standby(blocking). This means that Working member is forwarding traffic and thus works fine. nonFunctional(3): This member is disabled.')
ccaHCCPMemberSwitchNow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccaHCCPMemberSwitchNow.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberSwitchNow.setDescription("This object is used to initiate the switchover. When it is set to true(1) and this interface is Protect, it will cause the switchover to specified Working member. When it is set to true(1), and if this interface is Working, it will cause the switchover to the Protect in it's protection group. Switchover can thus be initiated by either the Protect or the Working. Reading this object will always return false(2).")
ccaHCCPMemChanSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6), )
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchTable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchTable.setDescription('This is an adjunct to ccaHCCPMemberTable. It provides information of HCCP member channel switches. It specifies the RF channel switch type, the RF switch over group and the RF switch module. The upconvertor IP addresses can also be retrieved from this table. This table does not exist if no channel switch has been enabled for this member in the group.')
ccaHCCPMemChanSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberID"), (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchID"))
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchEntry.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchEntry.setDescription('A set of attributes of the channel switch specifying the channel switch details per member (ccaHCCPMemberID) on an interface (ifType is docsCableMaclayer(127)) of a HCCP group. ')
ccaHCCPMemChanSwitchID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchID.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchID.setDescription('Uniquely identifies the entry for channel switch for a member. The channel switch is the RF component that allows downstream and upstream channel switching.')
ccaHCCPMemChanSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("others", 1), ("ucWavecom", 2), ("rfSwitchGrp", 3), ("rfSwitchModule", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchType.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchType.setDescription('Type of the channel switch. others(1) : Any other channel switch which is not in the following list. ucWavecom(2) : Represents the Wavecom upconvertor. rfSwitchGrp(3) : Weinschel channel switch. If ccaHCCPMemChanSwitchModule represents the bitmap of selected modules inside a RF switch chassis. rfSwitchModule(4) : Weinschel channel switch. If ccaHCCPMemChanSwitchModule represents the switch module number inside RF switch chassis.')
ccaHCCPMemChanSwitchIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchIpAddrType.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchIpAddrType.setDescription('The type of internet address of ccaHCCPMemChanSwitchIpAddress.')
ccaHCCPMemChanSwitchIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchIpAddress.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchIpAddress.setDescription("The Ipv4 Address of channel switch. It represents the IP address of the upconverter that this Working member connects to if ccaHCCPMemChanSwitchType is ucWavecom(2). It specifies the RF Switch's IP address if ccaHCCPMemChanSwitchType is rfSwitchGrp(3) or rfSwitchModule(4).")
ccaHCCPMemChanSwitchModule = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchModule.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchModule.setDescription('The module number of channel switch for this member . It is the module number on the upconverter that this member connects to if ccaHCCPMemChanSwitchType is ucWavecom(2). It specifies the RF Switch module number inside an RF Switch chassis if ccaHCCPMemChanSwitchType is rfSwitchModule(4). It is the bitmap of selected modules inside a RF Switch chassis if ccaHCCPMemChanSwitchType is rfSwitchGrp(3).')
ccaHCCPMemChanSwitchProtIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchProtIpAddrType.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchProtIpAddrType.setDescription('The type of internet address of ccaHCCPMemChanSwitchProtIpAddr.')
ccaHCCPMemChanSwitchProtIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchProtIpAddr.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchProtIpAddr.setDescription('The IP address of the Wavecom upconvertor that is connected to the corresponding Protect for this Working member. This object is meaningful only if ccaHCCPMemChanSwitchType is ucWavecom(2) and has no meaning for other types of switches and is ignored in this case.')
ccaHCCPMemChanSwitchProtModule = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchProtModule.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchProtModule.setDescription('The module number on the Wavecom upconvertor that is connected to the corresponding Protect for this Working member. This object is meaningful only if ccaHCCPMemChanSwitchType is ucWavecom(2).')
ccaHCCPMemChanSwitchPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchPosition.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchPosition.setDescription('The position within a switch module for this Working member. This object is valid for ccaHCCPMemChanSwitchType rfSwitchGrp(3) and rfSwitchModule(4). ')
ccaHCCPMemChanSwitchSnmpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchSnmpEnable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemChanSwitchSnmpEnable.setDescription('This object is used to enable SNMP remote control on the Wavecom upconvertor. When it is set to true(1), SNMP remote control is enabled on the upconvertor. When it is set to false(2), SNMP remote control is disabled and front panel manual operation is enabled. This object is meaningful only if ccaHCCPMemChanSwitchType is ucWavecom(2).')
ccaHCCPOnOffNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccaHCCPOnOffNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPOnOffNotificationEnable.setDescription('An indication of whether the ccaHCCPOnNotification and ccaHCCPOffNotification are enabled or disabled.')
ciscoCableAvailabilityMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 2))
ciscoCableAvailabilityMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 2, 0))
ccaHCCPOnNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 242, 2, 0, 1)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfStatus"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfLastSwitchReason"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberState"))
if mibBuilder.loadTexts: ccaHCCPOnNotification.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPOnNotification.setDescription("A notification that is sent when failover occurred and this interface is taking over the traffic from the peer. For example if Protect is taking over a Working member from it's protection group,this notification is sent by the Protect. When Working is restored to operation and is now taking over from the Protect, this notification is sent by Working.")
ccaHCCPOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 242, 2, 0, 2)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfStatus"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfLastSwitchReason"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberState"))
if mibBuilder.loadTexts: ccaHCCPOffNotification.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPOffNotification.setDescription("A notification that is sent when failover occurs and this interface is turning over all traffic to it's peer and is now blocking. For example if Protect is taking over a Working member from it's protection group,this notification is sent by the Working. When Working is restored to operation and is now taking over from the Protect, this notification is sent by Protect.")
ciscoCableAvailabilityMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 3))
ciscoCableAvailabilityMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 1))
ciscoCableAvailabilityMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2))
ciscoCableAvailabilityCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 1, 1)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroup"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberGroup"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableAvailabilityCompliance = ciscoCableAvailabilityCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoCableAvailabilityCompliance.setDescription('The compliance statement for CMTS devices that implement the Hot Standby Connection to Connection Protocol. ')
ciscoCableAvailabilityComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 1, 2)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroup"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberGroup"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableAvailabilityComplianceRev1 = ciscoCableAvailabilityComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoCableAvailabilityComplianceRev1.setDescription('The compliance statement for CMTS devices that implement the Hot Standby Connection to Connection Protocol. ')
ccaHCCPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2, 1)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPVersion"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPOnOffNotificationEnable"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupAuthentication"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupAuthKeyChain"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupHelloTime"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupHoldTime"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupRevertEnable"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupProtectIpAddrType"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupProtectIpAddress"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfRevertTime"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfTrackEnable"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfStatus"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfLastSwitchReason"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfOnTransitions"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfOffTransitions"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupTrackIfDescr"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccaHCCPGroup = ccaHCCPGroup.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPGroup.setDescription('Group of objects implemented in CMTS providing HCCP group information. ')
ccaHCCPMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2, 2)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberIpAddrType"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberIpAddress"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberState"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberSwitchNow"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchType"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchIpAddrType"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchIpAddress"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchModule"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchProtIpAddrType"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchProtIpAddr"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchProtModule"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchPosition"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchSnmpEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccaHCCPMemberGroup = ccaHCCPMemberGroup.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPMemberGroup.setDescription('Group of objects implemented in CMTS providing HCCP member and channel switch information.')
ccaHCCPNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2, 3)).setObjects(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPOnNotification"), ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPOffNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccaHCCPNotificationGroup = ccaHCCPNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ccaHCCPNotificationGroup.setDescription('The notification which a CISCO-CABLE-AVAILABILITY-MIB entity is required to implement.')
mibBuilder.exportSymbols("CISCO-CABLE-AVAILABILITY-MIB", ccaHCCPMemberState=ccaHCCPMemberState, ccaHCCPMemChanSwitchSnmpEnable=ccaHCCPMemChanSwitchSnmpEnable, ccaHCCPMemChanSwitchProtIpAddr=ccaHCCPMemChanSwitchProtIpAddr, ccaHCCPOnNotification=ccaHCCPOnNotification, ccaHCCPGroupIfTable=ccaHCCPGroupIfTable, ccaHCCPGroupIfRevertTime=ccaHCCPGroupIfRevertTime, ciscoCableAvailabilityMIBCompliances=ciscoCableAvailabilityMIBCompliances, ciscoCableAvailabilityMIBGroups=ciscoCableAvailabilityMIBGroups, ccaHCCPGroupIfTrackEnable=ccaHCCPGroupIfTrackEnable, ccaHCCPMemberIpAddrType=ccaHCCPMemberIpAddrType, ccaHCCPGroupIfLastSwitchReason=ccaHCCPGroupIfLastSwitchReason, ccaHCCPGroupHelloTime=ccaHCCPGroupHelloTime, ccaHCCPNotificationGroup=ccaHCCPNotificationGroup, ccaHCCPObjects=ccaHCCPObjects, ccaHCCPMemberGroup=ccaHCCPMemberGroup, ccaHCCPGroupIfOffTransitions=ccaHCCPGroupIfOffTransitions, ccaHCCPMemberTable=ccaHCCPMemberTable, ciscoCableAvailabilityCompliance=ciscoCableAvailabilityCompliance, ccaHCCPGroupProtectIpAddrType=ccaHCCPGroupProtectIpAddrType, ccaHCCPGroupTrackIfID=ccaHCCPGroupTrackIfID, ccaHCCPMemberIpAddress=ccaHCCPMemberIpAddress, ccaHCCPMemChanSwitchIpAddrType=ccaHCCPMemChanSwitchIpAddrType, ccaHCCPGroupAuthKeyChain=ccaHCCPGroupAuthKeyChain, ccaHCCPGroupTable=ccaHCCPGroupTable, ccaHCCPMemChanSwitchType=ccaHCCPMemChanSwitchType, ccaHCCPOffNotification=ccaHCCPOffNotification, ccaHCCPMemChanSwitchPosition=ccaHCCPMemChanSwitchPosition, ciscoCableAvailabilityMIBNotifications=ciscoCableAvailabilityMIBNotifications, ccaHCCPVersion=ccaHCCPVersion, ccaHCCPMemberSwitchNow=ccaHCCPMemberSwitchNow, ccaHCCPMemChanSwitchProtIpAddrType=ccaHCCPMemChanSwitchProtIpAddrType, ccaHCCPGroupProtectIpAddress=ccaHCCPGroupProtectIpAddress, ccaHCCPGroupIfStatus=ccaHCCPGroupIfStatus, ccaHCCPGroupRevertEnable=ccaHCCPGroupRevertEnable, ccaHCCPMemChanSwitchModule=ccaHCCPMemChanSwitchModule, ciscoCableAvailabilityMIBConformance=ciscoCableAvailabilityMIBConformance, ccaHCCPMemChanSwitchID=ccaHCCPMemChanSwitchID, ccaHCCPGroupIfState=ccaHCCPGroupIfState, ccaHCCPMemberID=ccaHCCPMemberID, ccaHCCPGroupIfOnTransitions=ccaHCCPGroupIfOnTransitions, ccaHCCPGroupTrackInterfaceTable=ccaHCCPGroupTrackInterfaceTable, ccaHCCPMemChanSwitchTable=ccaHCCPMemChanSwitchTable, ccaHCCPGroupID=ccaHCCPGroupID, ccaHCCPGroupTrackInterfaceEntry=ccaHCCPGroupTrackInterfaceEntry, ccaHCCPMemChanSwitchProtModule=ccaHCCPMemChanSwitchProtModule, ciscoCableAvailabilityMIB=ciscoCableAvailabilityMIB, ccaHCCPGroupTrackIfDescr=ccaHCCPGroupTrackIfDescr, ccaHCCPMemChanSwitchIpAddress=ccaHCCPMemChanSwitchIpAddress, ccaHCCPOnOffNotificationEnable=ccaHCCPOnOffNotificationEnable, ciscoCableAvailabilityComplianceRev1=ciscoCableAvailabilityComplianceRev1, ciscoCableAvailabilityMIBNotificationsPrefix=ciscoCableAvailabilityMIBNotificationsPrefix, ccaHCCPGroupAuthentication=ccaHCCPGroupAuthentication, ccaHCCPMemChanSwitchEntry=ccaHCCPMemChanSwitchEntry, PYSNMP_MODULE_ID=ciscoCableAvailabilityMIB, ccaHCCPGroupEntry=ccaHCCPGroupEntry, ccaHCCPGroupIfEntry=ccaHCCPGroupIfEntry, ccaHCCPGroupHoldTime=ccaHCCPGroupHoldTime, ciscoCableAvailabilityMIBObjects=ciscoCableAvailabilityMIBObjects, ccaHCCPMemberEntry=ccaHCCPMemberEntry, ccaHCCPGroup=ccaHCCPGroup)