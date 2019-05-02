#
# PySNMP MIB module NETSCREEN-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-POLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
netscreenPolicy, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenPolicy")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenPolicyMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 10, 0))
netscreenPolicyMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-08-13 00:00', '2001-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenPolicyMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'No Comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenPolicyMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenPolicyMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenPolicyMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenPolicyMibModule.setDescription('This module defines NetScreen private MIBs for Policy Monitoring')
nsPlyTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 10, 1), )
if mibBuilder.loadTexts: nsPlyTable.setStatus('current')
if mibBuilder.loadTexts: nsPlyTable.setDescription('A firewall provides a network boundary with a single point of entry and exit-a choke point.You can screen and direct all that traffic through the implementation of a set of access policies. Access policies allow you to permit, deny, encrypt, authenticate, prioritize, schedule, and monitor the traffic attemption to cross your firewall. This table collects all the policy configuration information existing in NetScreen Device.')
nsPlyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1), ).setIndexNames((0, "NETSCREEN-POLICY-MIB", "nsPlyVsys"), (0, "NETSCREEN-POLICY-MIB", "nsPlyId"))
if mibBuilder.loadTexts: nsPlyEntry.setStatus('current')
if mibBuilder.loadTexts: nsPlyEntry.setDescription('Each entry in the nsPlyTable holds a set of configuration parameters associatied with an instance of policy.')
nsPlyId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyId.setStatus('current')
if mibBuilder.loadTexts: nsPlyId.setDescription('Each policy is identified by a unique policy ID.')
nsPlyVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyVsys.setStatus('current')
if mibBuilder.loadTexts: nsPlyVsys.setDescription("Vitural system's name this polic entry belongs to.")
nsPlySrcZone = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlySrcZone.setStatus('current')
if mibBuilder.loadTexts: nsPlySrcZone.setDescription('Traffic through a firewall means that traffic flows from one security zone to another. This object describes the source zone name traffic flow passes.')
nsPlyDstZone = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyDstZone.setStatus('current')
if mibBuilder.loadTexts: nsPlyDstZone.setDescription('Traffic through a firewall means that traffic flows from one security zone to another. This object describes the destination zone name traffic flow passes.')
nsPlySrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlySrcAddr.setStatus('current')
if mibBuilder.loadTexts: nsPlySrcAddr.setDescription('Addresses are objects that identify network devices such as hosts and networks by their location in relation to the firwall on which security zone.To create an access policy for specific addresses, you must first create entries for the relevant hosts and networks in the address book.Source IP address indicates the address in source zone, 0.0.0.0 means any address.')
nsPlyDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyDstAddr.setStatus('current')
if mibBuilder.loadTexts: nsPlyDstAddr.setDescription('Addresses are objects that identify network devices such as hosts and networks by their location in relation to the firwall-on which security zone.To create an access policy for specific addresses, you must first create entries for the relevant hosts and networks in the address book.Source IP address indicates the address in destination zone, 0.0.0.0 means any address.')
nsPlyService = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50))).clone(namedValues=NamedValues(("any", 0), ("aol", 1), ("bgp", 2), ("dpcp-relay", 3), ("dns", 4), ("finger", 5), ("ftp", 6), ("ftp-get", 7), ("ftp-put", 8), ("gopher", 9), ("h323", 10), ("http", 11), ("https", 12), ("icmp-info", 13), ("icmp-timestamp", 14), ("ike", 15), ("imap", 16), ("internet-locator-service", 17), ("irc", 18), ("l2tp", 19), ("ldap", 20), ("mail", 21), ("netmeeting", 22), ("nfs", 23), ("nntp", 24), ("ns-global", 25), ("ns-global-pro", 26), ("ntp", 27), ("ospf", 28), ("pc-anywhere", 29), ("ping", 30), ("pop3", 31), ("pptp", 32), ("real-media", 33), ("rip", 34), ("rlogin", 35), ("snmp", 36), ("ssh", 37), ("syslog", 38), ("talk", 39), ("tcp-any", 40), ("telnet", 41), ("tftp", 42), ("traceroute", 43), ("udp-any", 44), ("uucp", 45), ("vdo-live", 46), ("wais", 47), ("winframe", 48), ("x-windows", 49), ("other", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyService.setStatus('current')
if mibBuilder.loadTexts: nsPlyService.setDescription("Sevices are objects that identify application protocols using layer 4 information such as standard and accepted TCP and UDP port numbers for application services like Telnet, FTP, SMTP and HTTP. This object indicates all the traffic service type this policy allows. 'Any' means all this policy allows all service go through. 'Other' could be a configured service or not in the list. See nsPlyServiceName for service name.")
nsPlyAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("deny", 0), ("permit", 1), ("tunnel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyAction.setStatus('current')
if mibBuilder.loadTexts: nsPlyAction.setDescription('Actions objects that describe what the firewall does to the traffic it receives. Permit allows the packet to pass the firewall. Deny blocks the packet from traversing the firewall. Tunnel encapsulates outgoing IP packets and decapsulates incoming IP packets.')
nsPlyNat = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyNat.setStatus('current')
if mibBuilder.loadTexts: nsPlyNat.setDescription('You can apply NAT at the interface level or at the policy level. With policy-based NAT, you can translate the source address on either incoming or outging network and VPN traffic. This object indicates if this is a policy-based NAT.')
nsPlyFixPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyFixPort.setStatus('current')
if mibBuilder.loadTexts: nsPlyFixPort.setDescription('When in policy-based NAT, the new secure address can come from either a Dynamic IP or from a Mapped IP. This object indicates if poliy-based NAT uses fix port when working on NAT mode.')
nsPlyDipId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyDipId.setStatus('current')
if mibBuilder.loadTexts: nsPlyDipId.setDescription('This object indicates the Dynamic ID chosen for NAT policy.')
nsPlyVpnTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyVpnTunnel.setStatus('current')
if mibBuilder.loadTexts: nsPlyVpnTunnel.setDescription('VPN tunnel this access policy applies to.')
nsPlyL2tpTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyL2tpTunnel.setStatus('current')
if mibBuilder.loadTexts: nsPlyL2tpTunnel.setDescription('L2TP tunnel this access policy applies to.')
nsPlyAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyAuth.setStatus('current')
if mibBuilder.loadTexts: nsPlyAuth.setDescription('This object indicates the selecting this option requires the user at the source address to authenticate his/her identiry by supplying a user name and password before traffic is allowed to graverw the firewall or enter the VPN tunnel.')
nsPlyLogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyLogEnable.setStatus('current')
if mibBuilder.loadTexts: nsPlyLogEnable.setDescription('When you enable logging in an access policy, the NetScreen device logs all connections to which that paticular access policy applies.')
nsPlyCountEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyCountEnable.setStatus('current')
if mibBuilder.loadTexts: nsPlyCountEnable.setDescription('When you enable counting in an access plicy, the NetScreen device counts the total number of bytes of traffic to which this access policy applies and records the informaiton in historical graphs.')
nsPlyAlarmBPS = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyAlarmBPS.setStatus('current')
if mibBuilder.loadTexts: nsPlyAlarmBPS.setDescription('User can set a threshold that triggers an alarm when the traffic permitted by the access policy exceeds a specified number of bytes per second.')
nsPlyAlarmBPM = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyAlarmBPM.setStatus('current')
if mibBuilder.loadTexts: nsPlyAlarmBPM.setDescription('User can set a threshold that triggers an alarm when the traffic permitted by the access policy exceeds a specified number of bytes per Minute.')
nsPlySchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlySchedule.setStatus('current')
if mibBuilder.loadTexts: nsPlySchedule.setDescription('By associating a schedule to an access policy, you can determine when the access policy is in effect.')
nsPlyTrafficShapeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyTrafficShapeEnable.setStatus('current')
if mibBuilder.loadTexts: nsPlyTrafficShapeEnable.setDescription('User can set parameters for the control and shaping of traffic for each access policy.')
nsPlyTrafficPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("high", 0), ("priority2nd", 1), ("priority3rd", 2), ("priority4th", 3), ("priority5th", 4), ("priority6th", 5), ("priority7th", 6), ("priorityLow", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyTrafficPriority.setStatus('current')
if mibBuilder.loadTexts: nsPlyTrafficPriority.setDescription('Traffic priority for this policy.')
nsPlyDSEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyDSEnable.setStatus('current')
if mibBuilder.loadTexts: nsPlyDSEnable.setDescription('Differentiated Services is a system for tagging traffic at a position within a hierarchy of priority.')
nsPlyActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("inuse", 1), ("hidden", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyActiveStatus.setStatus('current')
if mibBuilder.loadTexts: nsPlyActiveStatus.setDescription('Show the status of one policy entry.')
nsPlyName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyName.setStatus('current')
if mibBuilder.loadTexts: nsPlyName.setDescription('policy name (optional)')
nsPlyServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyServiceName.setStatus('current')
if mibBuilder.loadTexts: nsPlyServiceName.setDescription("Sevices name that identify application protocols using layer 4 information such as standard and accepted TCP and UDP port numbers for application services like Telnet, FTP, SMTP and HTTP. This object indicates all the traffic service type this policy allows. 'Any' means all this policy allows all service go through.")
nsPlyMonTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 10, 2), )
if mibBuilder.loadTexts: nsPlyMonTable.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonTable.setDescription('traffic information for the policy-based traffic.')
nsPlyMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1), ).setIndexNames((0, "NETSCREEN-POLICY-MIB", "nsPlyMonId"), (0, "NETSCREEN-POLICY-MIB", "nsPlyMonVsys"))
if mibBuilder.loadTexts: nsPlyMonEntry.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonEntry.setDescription('An entry holds a set of traffic counters of a specific policy.')
nsPlyMonId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonId.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonId.setDescription('Policy Id, also used as index in this table')
nsPlyMonVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonVsys.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonVsys.setDescription('vsys this policy belongs to')
nsPlyMonPackPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonPackPerSec.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonPackPerSec.setDescription('Packets go through this policy per second')
nsPlyMonPackPerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonPackPerMin.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonPackPerMin.setDescription('Packets go through this policy per minute')
nsPlyMonTotalPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonTotalPacket.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonTotalPacket.setDescription('total packets go through this policy')
nsPlyMonBytePerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonBytePerSec.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonBytePerSec.setDescription('Bytes go through this policy per second')
nsPlyMonBytePerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonBytePerMin.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonBytePerMin.setDescription('Bytes go through this policy per minute')
nsPlyMonTotalByte = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonTotalByte.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonTotalByte.setDescription('Total bytes go through this policy')
nsPlyMonSessionPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonSessionPerSec.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonSessionPerSec.setDescription('Sessions go through this policy per second')
nsPlyMonSessionPerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonSessionPerMin.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonSessionPerMin.setDescription('Sessions go through this policy per minute')
nsPlyMonTotalSession = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsPlyMonTotalSession.setStatus('current')
if mibBuilder.loadTexts: nsPlyMonTotalSession.setDescription('Total Sessions go through this policy')
mibBuilder.exportSymbols("NETSCREEN-POLICY-MIB", nsPlyDstZone=nsPlyDstZone, nsPlyMonTotalPacket=nsPlyMonTotalPacket, nsPlyDstAddr=nsPlyDstAddr, nsPlyTrafficPriority=nsPlyTrafficPriority, netscreenPolicyMibModule=netscreenPolicyMibModule, nsPlyAction=nsPlyAction, nsPlyMonPackPerMin=nsPlyMonPackPerMin, nsPlyVpnTunnel=nsPlyVpnTunnel, nsPlyTrafficShapeEnable=nsPlyTrafficShapeEnable, nsPlyId=nsPlyId, nsPlyDSEnable=nsPlyDSEnable, nsPlyMonEntry=nsPlyMonEntry, nsPlyL2tpTunnel=nsPlyL2tpTunnel, nsPlyMonPackPerSec=nsPlyMonPackPerSec, nsPlyCountEnable=nsPlyCountEnable, nsPlyMonBytePerMin=nsPlyMonBytePerMin, nsPlyName=nsPlyName, nsPlyMonSessionPerMin=nsPlyMonSessionPerMin, nsPlyService=nsPlyService, nsPlyAlarmBPM=nsPlyAlarmBPM, nsPlyDipId=nsPlyDipId, nsPlyEntry=nsPlyEntry, nsPlySrcZone=nsPlySrcZone, nsPlyMonVsys=nsPlyMonVsys, nsPlyAlarmBPS=nsPlyAlarmBPS, nsPlyLogEnable=nsPlyLogEnable, nsPlyFixPort=nsPlyFixPort, nsPlyTable=nsPlyTable, nsPlyActiveStatus=nsPlyActiveStatus, nsPlyMonTable=nsPlyMonTable, nsPlySchedule=nsPlySchedule, nsPlyMonTotalSession=nsPlyMonTotalSession, nsPlySrcAddr=nsPlySrcAddr, PYSNMP_MODULE_ID=netscreenPolicyMibModule, nsPlyMonBytePerSec=nsPlyMonBytePerSec, nsPlyServiceName=nsPlyServiceName, nsPlyAuth=nsPlyAuth, nsPlyVsys=nsPlyVsys, nsPlyMonSessionPerSec=nsPlyMonSessionPerSec, nsPlyMonId=nsPlyMonId, nsPlyNat=nsPlyNat, nsPlyMonTotalByte=nsPlyMonTotalByte)
