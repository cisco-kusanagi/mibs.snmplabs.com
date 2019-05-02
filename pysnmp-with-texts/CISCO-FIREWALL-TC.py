#
# PySNMP MIB module CISCO-FIREWALL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FIREWALL-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:58:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, ModuleIdentity, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter64, Bits, Counter32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ModuleIdentity", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFirewallTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 488))
ciscoFirewallTc.setRevisions(('2006-03-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFirewallTc.setRevisionsDescriptions(('Initial version of this module.',))
if mibBuilder.loadTexts: ciscoFirewallTc.setLastUpdated('200603030000Z')
if mibBuilder.loadTexts: ciscoFirewallTc.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoFirewallTc.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-firewalls@cisco.com')
if mibBuilder.loadTexts: ciscoFirewallTc.setDescription('This MIB module defines textual conventions that are commonly used in modeling management information pertaining to configuration, status and activity of firewalls.')
class CFWNetworkProtocol(TextualConvention, Integer32):
    description = "This type denotes protocols operating at layers 3 or 4 of Open System Interconnection (OSI) model. The following values are defined: 'none' Denotes the semantics of 'not applicable'. 'other' Denotes any protocol not listed. 'ip' Denotes Internet Protocol (IP). 'icmp' Denotes Internet Control Message Protocol. 'gre' Denotes Generic Route Encapsulation protocol. 'udp' Denotes User Datagram Protocol. 'tcp' Denotes Transmission Control Protocol. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("other", 2), ("ip", 3), ("icmp", 4), ("gre", 5), ("udp", 6), ("tcp", 7))

class CFWApplicationProtocol(TextualConvention, Integer32):
    reference = 'The protocols enumerated in this textual convention may be correlated with the information on protocols/ services defined by Internet Assigned Numbers Authority (IANA) found at http://www.iana.com/assignments/port-numbers'
    description = "This type denotes the application (OSI Layer 7) protocol/service corresponding to a firewall session or a connection. Description of constants of this type 'none' Denotes the semantics of 'not applicable'. 'other' Denotes any protocol not listed. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170))
    namedValues = NamedValues(("none", 1), ("other", 2), ("ftp", 3), ("telnet", 4), ("smtp", 5), ("http", 6), ("tacacs", 7), ("dns", 8), ("sqlnet", 9), ("https", 10), ("tftp", 11), ("gopher", 12), ("finger", 13), ("kerberos", 14), ("pop2", 15), ("pop3", 16), ("sunRpc", 17), ("msRpc", 18), ("nntp", 19), ("snmp", 20), ("imap", 21), ("ldap", 22), ("exec", 23), ("login", 24), ("shell", 25), ("msSql", 26), ("sybaseSql", 27), ("nfs", 28), ("lotusnote", 29), ("h323", 30), ("cuseeme", 31), ("realmedia", 32), ("netshow", 33), ("streamworks", 34), ("vdolive", 35), ("sap", 36), ("sip", 37), ("mgcp", 38), ("rtsp", 39), ("skinny", 40), ("gtpV0", 41), ("gtpV1", 42), ("echo", 43), ("discard", 44), ("daytime", 45), ("netstat", 46), ("ssh", 47), ("time", 48), ("tacacsDs", 49), ("bootps", 50), ("bootpc", 51), ("dnsix", 52), ("rtelnet", 53), ("ident", 54), ("sqlServ", 55), ("ntp", 56), ("pwdgen", 57), ("ciscoFna", 58), ("ciscoTna", 59), ("ciscoSys", 60), ("netbiosNs", 61), ("netbiosDgm", 62), ("netbiosSsn", 63), ("sqlSrv", 64), ("snmpTrap", 65), ("rsvd", 66), ("send", 67), ("xdmcp", 68), ("bgp", 69), ("irc", 70), ("qmtp", 71), ("ipx", 72), ("dbase", 73), ("imap3", 74), ("rsvpTunnel", 75), ("hpCollector", 76), ("hpManagedNode", 77), ("hpAlarmMgr", 78), ("microsoftDs", 79), ("creativeServer", 80), ("creativePartnr", 81), ("appleQtc", 82), ("igmpV3Lite", 83), ("isakmp", 84), ("biff", 85), ("who", 86), ("syslog", 87), ("router", 88), ("ncp", 89), ("timed", 90), ("ircServ", 91), ("uucp", 92), ("syslogConn", 93), ("sshell", 94), ("ldaps", 95), ("dhcpFailover", 96), ("msexchRouting", 97), ("entrustSvcs", 98), ("entrustSvcHandler", 99), ("ciscoTdp", 100), ("webster", 101), ("gdoi", 102), ("iscsi", 103), ("cddbp", 104), ("ftps", 105), ("telnets", 106), ("imaps", 107), ("ircs", 108), ("pop3s", 109), ("socks", 110), ("kazaa", 111), ("msSqlM", 112), ("msSna", 113), ("wins", 114), ("ica", 115), ("orasrv", 116), ("rdbDbsDisp", 117), ("vqp", 118), ("icabrowser", 119), ("kermit", 120), ("rsvpEncap", 121), ("l2tp", 122), ("pptp", 123), ("h323Gatestat", 124), ("rWinsock", 125), ("radius", 126), ("hsrp", 127), ("net8Cman", 128), ("oracleEmVp", 129), ("oracleNames", 130), ("oracle", 131), ("ciscoSvcs", 132), ("ciscoNetMgmt", 133), ("stun", 134), ("trRsrb", 135), ("ddnsV3", 136), ("aceSvr", 137), ("giop", 138), ("ttc", 139), ("ipass", 140), ("clp", 141), ("citrixImaClient", 142), ("sms", 143), ("citrix", 144), ("realSecure", 145), ("lotusMtap", 146), ("cifs", 147), ("msDotnetster", 148), ("tarantella", 149), ("fcipPort", 150), ("ssp", 151), ("iscsiTarget", 152), ("mySql", 153), ("msClusterNet", 154), ("ldapAdmin", 155), ("ieee80211Iapp", 156), ("oemAgent", 157), ("rtcPmPort", 158), ("dbControlAgent", 159), ("ipsecMsft", 160), ("sipTls", 161), ("aim", 162), ("pcAnyWhereData", 163), ("pcAnyWhereStat", 164), ("x11", 165), ("ircu", 166), ("n2h2Server", 167), ("h323CallSigAlt", 168), ("yahooMsgr", 169), ("msnMsgr", 170))

class CFWPolicy(TextualConvention, OctetString):
    description = "This type denotes the identity of a policy enforced by the firewall. In the context of firewalls, only security policies are relevant. Objects of this type must comprise printable, human readable ASCII characters. A zero length string is used to denote a 'null' policy. An example of a policy is the 'policy-map' entity configured using the Modular Policy Command framework."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CFWPolicyTarget(TextualConvention, OctetString):
    description = "In the context of policy management, the term target refers to an entity on the managed device to which the policy is applied thereby enforcing the policy on the traffic stream(s) associated with the entity. The type 'CFWPolicyTarget' denotes the identity of a policy target. Examples of policy targets include interfaces, security zones, users, user groups and virtual contexts. Objects of this type must comprise printable, human readable ASCII characters. A zero length string is used to denote a 'null' target."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CFWPolicyTargetType(TextualConvention, Integer32):
    description = "This type is used to represent the type of a policy target. The following values are defined: 'all' Certain firewall implementations allow policies to be applied on all applicable targets. (Such policies are termed 'global'). The target type 'all' denotes the set of all applicable targets. 'other' Denotes an entity type that has yet not been classified in one of the other types. This value is useful in accomodating new target types before the textual convention is revised to include them. 'interface' The policy target is an interface of the managed device. 'zone' The policy target is a zone, where a zone is is a collection of interfaces of the managed device. 'zonepair' The policy target is a pair of zones. 'user' Denotes the identity of a user who is authorized to access the firewall itself or the resources protected by the firewall. 'usergroup' Denotes the identity of a user group. User group denotes a collection of user identities, as defined above. 'context' Denotes a logical device defined in the managed device with a distinct management context. Examples of such logical devices include virtual contexts defined by Firewall Service Module, virtual sensors defined by Intrusion Detection Service Module and Virtual Routing and Forwarding (VRFs) defined by IOS. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("all", 1), ("other", 2), ("interface", 3), ("zone", 4), ("zonepair", 5), ("user", 6), ("usergroup", 7), ("context", 8))

class CFWUrlfVendorId(TextualConvention, Integer32):
    description = "This type denotes the vendor of a URL filtering server which the firewall uses to implement URL filtering. A URL filtering server provides a database of URLs with appropriate access restrictions (e.g., deny or permit). Various security devices can make use of these filtering servers to provide URL filtering functionality to the users. The following values are defined: 'other' Other type of URL filtering servers than those specified below. 'websense' Websense URL filtering server. One of the products provided by Websense is a Web Filtering Server. More information about Websense Web Filtering product can be found at http://www.websense.com 'n2h2' N2H2 URL filtering server. More information about N2H2 Filtering product can be found at http://www.n2h2.com "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("websense", 2), ("n2h2", 3))

class CFWUrlServerStatus(TextualConvention, Integer32):
    description = "This type denotes the status of the URL filtering server which the firewall uses to implement URL filtering. The following values are defined: 'online' Indicates that the Server is online 'offline' Indicates that the Server is offline 'indeterminate' Indicates that the Server status cannot be determined "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("online", 1), ("offline", 2), ("indeterminate", 3))

mibBuilder.exportSymbols("CISCO-FIREWALL-TC", CFWPolicyTarget=CFWPolicyTarget, CFWPolicy=CFWPolicy, CFWUrlfVendorId=CFWUrlfVendorId, CFWNetworkProtocol=CFWNetworkProtocol, CFWPolicyTargetType=CFWPolicyTargetType, CFWUrlServerStatus=CFWUrlServerStatus, PYSNMP_MODULE_ID=ciscoFirewallTc, ciscoFirewallTc=ciscoFirewallTc, CFWApplicationProtocol=CFWApplicationProtocol)
