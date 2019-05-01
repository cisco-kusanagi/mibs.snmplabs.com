#
# PySNMP MIB module CISCO-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, TimeTicks, Bits, ObjectIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, ModuleIdentity, Counter32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter32", "Gauge32", "Unsigned32")
DisplayString, DateAndTime, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "RowPointer", "TextualConvention")
ciscoFirewallMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 147))
ciscoFirewallMIB.setRevisions(('2005-12-06 00:00', '1999-04-29 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFirewallMIB.setRevisionsDescriptions(('Added the copyright statement and updated the imports such that Unsigned32 is imported from SNMPv2-SMI instead of CISCO-TC. Added a new NOTIFICATION-GROUP ciscoFirewallMIBNotificationGroupRev1 to include all the notifications defined in the MIB. Obsoleted the OBJECT-GROUP ciscoFirewallMIBNotificationGroup. Deprecated the MODULE-COMPLIANCE ciscoFirewallMIBCompliance and added a new MODULE-COMPLIANCE ciscoFirewallMIBComplianceRev1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFirewallMIB.setLastUpdated('200512060000Z')
if mibBuilder.loadTexts: ciscoFirewallMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFirewallMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-pix@cisco.com cs-iosfw@cisco.com')
if mibBuilder.loadTexts: ciscoFirewallMIB.setDescription('MIB module for monitoring Cisco Firewalls.')
ciscoFirewallMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1))
cfwEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1))
cfwBasicEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1))
cfwNetEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2))
cfwSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2))
cfwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1))
cfwStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2))
class ResourceStatistics(TextualConvention, Integer32):
    description = 'This textual convention is used to identify various statistics that are related to the resources on a firewall. highUse : The highest load the resource has had for a time period. The time period will be implementation dependent. highLoad : The highest load the resource has had since startup. maximum : The maximum amount of the resource that is available. minimum : The minimum amount of the resource that is available. low : The lowest amount of the resource that has been available since startup. high : The highest amount of the resource that has been available since startup. average : The average amount of the resource that has been available since startup. free : The amount of the resource that is currently available since startup. inUse : The amount of the resource that is currently in use, eg. CPU usage, memory usage.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("highUse", 1), ("highLoad", 2), ("maximum", 3), ("minimum", 4), ("low", 5), ("high", 6), ("average", 7), ("free", 8), ("inUse", 9))

class Hardware(TextualConvention, Integer32):
    description = 'This textual convention is used to describe various hardware resouces that can be monitored by the firewall. memory - identifies memory. disk - identifies disk. power - identifies power. netInterface - identifies a network interface. tape - identifies a tape drive. controller - identifies hardware controller. cpu - identifies CPU. primaryUnit - identifies the primary unit of the two identical firewalls configured redundancy. secondaryUnit - identifies the secondary unit of the two identical firewalls configured redundancy. other - identifies other hardware.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("memory", 1), ("disk", 2), ("power", 3), ("netInterface", 4), ("cpu", 5), ("primaryUnit", 6), ("secondaryUnit", 7), ("other", 8))

class Services(TextualConvention, Integer32):
    description = "This textual convention is used to describe various services that are monitored by the firewall. otherFWService - a service that does not fit into any other category. fileXferFtp - identifies FTP, File Transfer Protocol. fileXferTftp - identifies TFTP, Trivial File Transfer Protocol fileXferFtps - identifies FTP, File Transfer Protocol running over Secure Sockets Layer. loginTelnet - identifies telnet loginRlogin - identifies rlogin. loginTelnets - identifies telnet over Secure Sockets Layer(SSL). remoteExecSunRPC - identifies Sun Remote Procedure Call Protocol. remoteExecMSRPC - identifies Microsoft Remote Procedure Call Protocol. remoteExecRsh - identifies the remote shell. remoteExecXserver - identifies the Xwindows server. webHttp - identifies Hyper Text Transfer Protocol. webHttps - identifies the secure HTTP protocol. mailSmtp - identifies SMTP, Simple Mail Transfer Protocol. mailSmtps - identifies SMTP, Simple Mail Transfer Protocol running over Secure Sockets Layer (SSL). multimediaStreamworks - identifies streamworks. multimediaH323 - identifies H323. multimediaNetShow - identifies NetShow. multimediaVDOLive - identifies vDOLive. multimediaRealAV - identifies RealAV. multimediaRTSP - identifies Real Time Streaming Protocol dbOracle - identifies Oracle's SQL*Net. dbMSsql - identifies MicroSoft SQL. contInspProgLang - identifies a payload as a programming language such as Java or ActiveX. contInspUrl - identifies a payload as a URL. directoryNis - identifies NIS, Network Information Service. directoryDns - identifies DNS, Domain Name Service. directoryNetbiosns - identifies NetBIOSNS - NetBIOS Name Service. directoryNetbiosdgm - identifies NetBIOSNS - NetBIOS datagram Service. directoryNetbiosssn - identifies NetBIOSNS - NetBIOS Session Service. directoryWins - identifies Windows Internet Naming Service (WINS). qryWhois - identifies WhoIs service. qryFinger - identifies finger. qryIdent - identifies Ident. fsNfsStatus - identifies Network File System (NFS) Status. fsNfs - identifies Network File System (NFS). fsCifs - identifies CIFS, Common Internet File Service. protoIcmp - identifies ICMP, Internet Control Message Protocol. protoTcp - identifies TCP, Transmission Control Protocol. protoUdp - identifies UDP, User Datagram Protocol. protoIp - identifies IP, Internet Protocol. protoSnmp - identifies SNMP, Simple Network Management Protocol."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41))
    namedValues = NamedValues(("otherFWService", 1), ("fileXferFtp", 2), ("fileXferTftp", 3), ("fileXferFtps", 4), ("loginTelnet", 5), ("loginRlogin", 6), ("loginTelnets", 7), ("remoteExecSunRPC", 8), ("remoteExecMSRPC", 9), ("remoteExecRsh", 10), ("remoteExecXserver", 11), ("webHttp", 12), ("webHttps", 13), ("mailSmtp", 14), ("multimediaStreamworks", 15), ("multimediaH323", 16), ("multimediaNetShow", 17), ("multimediaVDOLive", 18), ("multimediaRealAV", 19), ("multimediaRTSP", 20), ("dbOracle", 21), ("dbMSsql", 22), ("contInspProgLang", 23), ("contInspUrl", 24), ("directoryNis", 25), ("directoryDns", 26), ("directoryNetbiosns", 27), ("directoryNetbiosdgm", 28), ("directoryNetbiosssn", 29), ("directoryWins", 30), ("qryWhois", 31), ("qryFinger", 32), ("qryIdent", 33), ("fsNfsStatus", 34), ("fsNfs", 35), ("fsCifs", 36), ("protoIcmp", 37), ("protoTcp", 38), ("protoUdp", 39), ("protoIp", 40), ("protoSnmp", 41))

class HardwareStatus(TextualConvention, Integer32):
    description = "This textual convention is used to describe various events that are related to the resources on a firewall. other : Generic resource event. up : The resource is in service. down : The resource is not in service. error : There has been an error for this resource. overTemp : The resource is overheating. busy : The resource is busy. noMedia : A device doesn't have its needed media. backup : Processing has switched to the backup. active : This is the active unit. standby : This is the standby unit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("up", 2), ("down", 3), ("error", 4), ("overTemp", 5), ("busy", 6), ("noMedia", 7), ("backup", 8), ("active", 9), ("standby", 10))

class SecurityEvent(TextualConvention, Integer32):
    description = "This textual convention is used to describe various security-related events and statistics on a firewall. other : Generic attack event. none : No attack is occurring, an informational event. dos : A denial of service attack has been detected. recon : A pattern of reconnaissance activity has been detected. pakFwd : A packet forwarding attack has been detected. addrSpoof : A spoofed address has been detected. svcSpoof : A spoofed service (eg., DNS) has been detected. thirdParty : This site is being used as a third-party for an attack on another network. For example, the 'smurf' attack or email spamming. complete : An attack has terminated invlPak : An invalid packet with attack characteristics has been detected. illegCmd : An illegal command has been found. policy : An attempt has reen made to violate a security policy."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("none", 2), ("dos", 3), ("recon", 4), ("pakFwd", 5), ("addrSpoof", 6), ("svcSpoof", 7), ("thirdParty", 8), ("complete", 9), ("invalPak", 10), ("illegCom", 11), ("policy", 12))

class ContentInspectionEvent(TextualConvention, Integer32):
    description = "Content inspection events, these events report that something was found in the application payload. The details entry in the event can report on what was found (eg., virus, company private info., etc), what it was found in (eg., html, win32 executable, e-mail), and what was done with it (eg., the quarantine location). other : A content inspection event. Used to indicate that some content inspection has occurred that is not covered by the other content inspection enumerations. okay : The check of the content was okay, nothing 'bad' was found. error : There was an error while checking the content. found : Something was found that the content inspection engine has determined merits attention. clean : The content inspection engine has found something that violates the security policy and has neutralized the content in the data flow. reject : The content inspection engine has found something that violates the security policy and has discarded the content. saved : The content inspection engine has found something that violates the security policy and has stored it in a quarentine storage area."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("okay", 2), ("error", 3), ("found", 4), ("clean", 5), ("reject", 6), ("saved", 7))

class ConnectionEvent(TextualConvention, Integer32):
    description = 'This textual convention is used to describe various events and statistics that are related to the connections that occur on a firewall. other : A generic connection event. accept : A connection has been acccepted. error : An error has occurred for a connection. drop : The connection has been dropped. close : A connection has been closed. timeout : A connection has been timed out. refused : A connection has been refused. reset : A connection has been reset. noResp : A connection has received no response.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("other", 1), ("accept", 2), ("error", 3), ("drop", 4), ("close", 5), ("timeout", 6), ("refused", 7), ("reset", 8), ("noResp", 9))

class ConnectionStat(TextualConvention, Integer32):
    description = 'This textual convention is used to describe various connections statistics. other : A generic connection event. totalOpen : Total open connections since reboot. currentOpen : The number of connections currently open. currentClosing : The number of connections currently closing. currentHalfOpen : The number of connections currently half-open. currentInUse : The number of connections currently in use. high : The highest number of connections in use at any one time since system startup.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("totalOpen", 2), ("currentOpen", 3), ("currentClosing", 4), ("currentHalfOpen", 5), ("currentInUse", 6), ("high", 7))

class AccessEvent(TextualConvention, Integer32):
    description = 'This textual convention is used to describe various events and statistics that are related to the access control on a firewall. other : Miscellaneous access event. grant : A service has allowed access based on all of its access checks. deny : a client was denied use of a service. denyMult : A client was denied use of a service multiple times. error : An error has ocurred during the access control process.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("grant", 2), ("deny", 3), ("denyMult", 4), ("error", 5))

class AuthenticationEvent(TextualConvention, Integer32):
    description = 'This textual convention is used to describe various events and statistics that are related to authorization. other : Miscellaneous authentication event. succ : A client successfuly authenticated. error : Error while authenticating. fail : A client failed an authenticating. succPriv : A client accessed a service with special privileges. failPriv : A client failed to access a service with special privileges. failMult : Multiple failed authentication attempts by a client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("succ", 2), ("error", 3), ("fail", 4), ("succPriv", 5), ("failPriv", 6), ("failMult", 7))

class GenericEvent(TextualConvention, Integer32):
    description = "Generic Events - events for which there is no more specific enumeration abnormal : An abnormal event has occurred that is neither 'okay' nor an 'error'. okay : A normal event occurred or the system has changed from an abnormal state to a normal state error : An error event occurred"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("abnormal", 1), ("okay", 2), ("error", 3))

cfwBasicEventsTableLastRow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventsTableLastRow.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventsTableLastRow.setDescription('The index value of the most recently created row in the cfwBasicEventsTable. This number starts at 1 and increase by one with each new log entry. When this number wraps, all events are deleted.')
cfwBasicEventsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2), )
if mibBuilder.loadTexts: cfwBasicEventsTable.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventsTable.setDescription('Table of basic data for firewall events. The agent may choose to delete the instances of cfwBasicEventsEntry as required because of lack of memory. The oldest Events will be selected first for deletion.')
cfwBasicEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwBasicEventIndex"))
if mibBuilder.loadTexts: cfwBasicEventsEntry.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventsEntry.setDescription('An entry in the table, containing general information about an event. This table will always be sparse, i.e., each row will instanciate only a subet of the columnar objects.')
cfwBasicEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfwBasicEventIndex.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventIndex.setDescription('An index that uniquely identifies an entry in the log table. These indices are assigned beginning with 1 and increase by one with each new event logged.')
cfwBasicEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventTime.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventTime.setDescription('The time that the event occurred.')
cfwBasicSecurityEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 3), SecurityEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicSecurityEventType.setStatus('current')
if mibBuilder.loadTexts: cfwBasicSecurityEventType.setDescription('The type of security-related event that this row contains. If the event is not security-related this object will not be instantiated.')
cfwBasicContentInspEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 4), ContentInspectionEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicContentInspEventType.setStatus('current')
if mibBuilder.loadTexts: cfwBasicContentInspEventType.setDescription('The type of content inspection-related event that this row contains. If the event is not content inspection-related this object will not be instantiated.')
cfwBasicConnectionEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 5), ConnectionEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicConnectionEventType.setStatus('current')
if mibBuilder.loadTexts: cfwBasicConnectionEventType.setDescription('The type of connection-related event that this row contains. If the event is not connection-related this object will not be instantiated.')
cfwBasicAccessEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 6), AccessEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicAccessEventType.setStatus('current')
if mibBuilder.loadTexts: cfwBasicAccessEventType.setDescription('The type of access-related event that this row contains. If the event is not access-related this object will not be instantiated.')
cfwBasicAuthenticationEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 7), AuthenticationEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicAuthenticationEventType.setStatus('current')
if mibBuilder.loadTexts: cfwBasicAuthenticationEventType.setDescription('The type of authentication-related event that this row contains. If the event is not authentication-related this object will not be instantiated.')
cfwBasicGenericEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 8), GenericEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicGenericEventType.setStatus('current')
if mibBuilder.loadTexts: cfwBasicGenericEventType.setDescription('The type of generic event that this row contains. If the event does not fall into one of the other categories this object will be populated. Otherwise, this object will not be instantiated.')
cfwBasicEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventDescription.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventDescription.setDescription('A description of the event. The value of the object may be a zero-length string.')
cfwBasicEventDetailsTableRow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 10), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventDetailsTableRow.setStatus('current')
if mibBuilder.loadTexts: cfwBasicEventDetailsTableRow.setDescription('A pointer to a row in the table containing details about this event. Generally, the table will be the cfwNetEventsTable but a Cisco-defined table may also appear here. If there there is no more detailed information for this event the value of this object will have the value {0 0}.')
cfwNetEventsTableLastRow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventsTableLastRow.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventsTableLastRow.setDescription('The index value of the last row in the cfwNetEventsTable. This number starts at 1 and increase by one with each new log entry. When this number wraps, all events are deleted.')
cfwNetEventsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2), )
if mibBuilder.loadTexts: cfwNetEventsTable.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventsTable.setDescription('Table of detailed data for network events. The agent may choose to delete the instances of cfwBasicEventsEntry as required because of lack of memory. It is an implementation-specific matter as to when this deletion may occur. It is recommended that the oldest log instances are deleted first.')
cfwNetEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwNetEventIndex"))
if mibBuilder.loadTexts: cfwNetEventsEntry.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventsEntry.setDescription('An entry in the table, containing detailed information about an event. Note that this table may be sparse. If Network Address Translation is not enabled cfwNetEventInsideSrcIpAddress and cfwNetEventInsideDstIpAddress will not be instantiated in the row. If Port Address Translation is not enabled cfwNetEventInsideSrcIpPort and cfwNetEventInsideDstIpPort will not be instantiated in the row. Entries are added to this table at the same time that events are added to the cfwBasicEventsTable. These two tables may be configured to be different sizes so there may not be a one-to-one correspondence between rows in the two tables.')
cfwNetEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfwNetEventIndex.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventIndex.setDescription('An index that uniquely identifies an entry in the log table. These indices are assigned beginning with one and increase by one with each new log entry. When this number wraps, all events are deleted in order to allow the NMS to differentiate between old and new events.')
cfwNetEventInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInterface.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventInterface.setDescription("The interface most closely associated with this event. For example, for an event that relates to the receipt of a packet, this object identifies the interface on which the packet was received. If there are multiple interfaces associated with an event, the interface most closely associated with the cause of the event will be used. For example, for an event for the setup of a TCP connection, the interface on the initiator's side of the connection would be preferred. If there is no associated interface, then this object has the value zero.")
cfwNetEventSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventSrcIpAddress.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventSrcIpAddress.setDescription('Source IP address in the IP packet that caused the event. If there is no packet associated with the event this object has the value of zero. If the event is the result of multiple packets with different source addresses, this value may be zero or an address taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventInsideSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideSrcIpAddress.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventInsideSrcIpAddress.setDescription('Source IP address after Network Address Translation has been applied. If NAT has not been applied to the source address in this packet this object will not be instantiated, resulting in a sparse table. If the event is the result of multiple packets with different source addresses, this value may be zero or an address taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventDstIpAddress.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventDstIpAddress.setDescription('Destination IP address in the IP packet that caused the event. If there is no packet associated with the event this object has the value of zero. If the event is the result of multiple packets with different destination addresses, this value may be zero or an address taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventInsideDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideDstIpAddress.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventInsideDstIpAddress.setDescription('Destination IP address after Network Address Translation has been applied. If NAT has not been applied to the destination address in this packet this object will not be instantiated, resulting in a sparse table. If the event is the result of multiple packets with different destination addresses, this value may be zero or an address taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventSrcIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventSrcIpPort.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventSrcIpPort.setDescription('Source UDP/TCP port in the IP packet that caused the event. If there is no packet associated with the event this object has the value of zero. If the event is the result of multiple packets with different source ports, this value may be zero or a port taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventInsideSrcIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideSrcIpPort.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventInsideSrcIpPort.setDescription('Source UDP/TCP port after Port Address Translation has been applied. If PAT has not been applied to the source port in this packet this object will not be instantiated, resulting in a sparse table. If the event is the result of multiple packets with different source ports, this value may be zero or a port taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventDstIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventDstIpPort.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventDstIpPort.setDescription('Destination UDP/TCP port in the IP packet that caused the event. If there is no packet associated with the event this object has the value of zero. If the event is the result of multiple packets with different destination ports, this value may be zero or a port taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventInsideDstIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideDstIpPort.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventInsideDstIpPort.setDescription('Destination UDP/TCP port after Port Address Translation has been applied. If PAT has not been applied to the Destination port in this packet this object will not be instantiated, resulting in a sparse table. If the event is the result of multiple packets with different destination ports, this value may be zero or a port taken from an arbitrarily chosen packet in the sequence of packets causing the event.')
cfwNetEventService = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 11), Services()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventService.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventService.setDescription('The identification of the type of service involved with this event.')
cfwNetEventServiceInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventServiceInformation.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventServiceInformation.setDescription("Specific service information. This can be used to describe the particular service indentified by cfwNetEventService and can reflect whether the service is a local service or a gateway service. For example, if the value for cfwNetEventService is loginTelnet then the string provided might be 'local telnet'.")
cfwNetEventIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventIdentity.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventIdentity.setDescription('This object will contain a description of the entity that caused the event. The entity could be a userid, username, processid or other identifier for the entity using the service. If there is no such information then this object will contain a zero-length string.')
cfwNetEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventDescription.setStatus('current')
if mibBuilder.loadTexts: cfwNetEventDescription.setDescription('A detailed description of the event.')
cfwHardwareStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1), )
if mibBuilder.loadTexts: cfwHardwareStatusTable.setStatus('current')
if mibBuilder.loadTexts: cfwHardwareStatusTable.setDescription('Table of firewall cfwHardwareStatusEntry entries.')
cfwHardwareStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwHardwareType"))
if mibBuilder.loadTexts: cfwHardwareStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cfwHardwareStatusEntry.setDescription('An entry in the table, containing status information about a resource.')
cfwHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 1), Hardware())
if mibBuilder.loadTexts: cfwHardwareType.setStatus('current')
if mibBuilder.loadTexts: cfwHardwareType.setDescription('The hardware type for which this row provides status information.')
cfwHardwareInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwHardwareInformation.setStatus('current')
if mibBuilder.loadTexts: cfwHardwareInformation.setDescription('A detailed textual description of the resource identified by cfwHardwareType.')
cfwHardwareStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 3), HardwareStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwHardwareStatusValue.setStatus('current')
if mibBuilder.loadTexts: cfwHardwareStatusValue.setDescription('This object contains the current status of the resource.')
cfwHardwareStatusDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwHardwareStatusDetail.setStatus('current')
if mibBuilder.loadTexts: cfwHardwareStatusDetail.setDescription('A detailed textual description of the current status of the resource which may provide a more specific description than cfwHardwareStatusValue.')
cfwBufferStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1), )
if mibBuilder.loadTexts: cfwBufferStatsTable.setStatus('current')
if mibBuilder.loadTexts: cfwBufferStatsTable.setDescription("A table conatining status information about a firewall's buffers.")
cfwBufferStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwBufferStatSize"), (0, "CISCO-FIREWALL-MIB", "cfwBufferStatType"))
if mibBuilder.loadTexts: cfwBufferStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cfwBufferStatsEntry.setDescription('An entry in the table, containing status information about a particular statistic for the set of buffers of a particular size.')
cfwBufferStatSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfwBufferStatSize.setStatus('current')
if mibBuilder.loadTexts: cfwBufferStatSize.setDescription('This object contains the size of the set of buffers for which this row contains the statistics given by cfwBufferStatType.')
cfwBufferStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 2), ResourceStatistics())
if mibBuilder.loadTexts: cfwBufferStatType.setStatus('current')
if mibBuilder.loadTexts: cfwBufferStatType.setDescription('This object identifies the type of statistic given by this row for the particular set of buffers identified by cfwBufferStatSize.')
cfwBufferStatInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBufferStatInformation.setStatus('current')
if mibBuilder.loadTexts: cfwBufferStatInformation.setDescription('A detailed textual description of the statistic identified by cfwBufferStatType.')
cfwBufferStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBufferStatValue.setStatus('current')
if mibBuilder.loadTexts: cfwBufferStatValue.setDescription('The value of the buffer statistic.')
cfwConnectionStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2), )
if mibBuilder.loadTexts: cfwConnectionStatTable.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatTable.setDescription('Table of firewall statistic instances.')
cfwConnectionStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwConnectionStatService"), (0, "CISCO-FIREWALL-MIB", "cfwConnectionStatType"))
if mibBuilder.loadTexts: cfwConnectionStatEntry.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatEntry.setDescription('An entry in the table, containing information about a firewall statistic.')
cfwConnectionStatService = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 1), Services())
if mibBuilder.loadTexts: cfwConnectionStatService.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatService.setDescription('The identification of the type of connection providing statistics.')
cfwConnectionStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 2), ConnectionStat())
if mibBuilder.loadTexts: cfwConnectionStatType.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatType.setDescription('The state of the connections that this row contains statistics for.')
cfwConnectionStatDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwConnectionStatDescription.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatDescription.setDescription('A detailed textual description of this statistic.')
cfwConnectionStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwConnectionStatCount.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatCount.setDescription("This is an integer that contains the value of the resource statistic. If a type of 'gauge' is more appropriate this object will be omitted resulting in a sparse table.")
cfwConnectionStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwConnectionStatValue.setStatus('current')
if mibBuilder.loadTexts: cfwConnectionStatValue.setDescription("This is an integer that contains the value of the resource statistic. If a type of 'counter' is more appropriate this object will be omitted resulting in a sparse table.")
ciscoFirewallMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 2))
ciscoFirewallMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0))
cfwSecurityNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 2)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwSecurityNotification.setStatus('current')
if mibBuilder.loadTexts: cfwSecurityNotification.setDescription('This notification is used for events involving security events. The included objects provide more detailed information about the event.')
cfwContentInspectNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 3)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwContentInspectNotification.setStatus('current')
if mibBuilder.loadTexts: cfwContentInspectNotification.setDescription('This notification is used to notify the NMS of content inspection events. The included objects provide more detailed information about the event.')
cfwConnNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 4)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwConnNotification.setStatus('current')
if mibBuilder.loadTexts: cfwConnNotification.setDescription('This notification is used to notify the NMS of connection-oriented events. The included objects provide more detailed information about the event.')
cfwAccessNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 5)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwAccessNotification.setStatus('current')
if mibBuilder.loadTexts: cfwAccessNotification.setDescription('This notification is used to notify the NMS of access events. The included objects provide more detailed information about the event.')
cfwAuthNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 6)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwAuthNotification.setStatus('current')
if mibBuilder.loadTexts: cfwAuthNotification.setDescription('This notification is used to notify the NMS of authentication events. The included objects provide more detailed information about the event.')
cfwGenericNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 7)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwGenericNotification.setStatus('current')
if mibBuilder.loadTexts: cfwGenericNotification.setDescription('This notification is used to notify the NMS of events that do not fall into the other categories. The included objects provide more detailed information about the event.')
ciscoFirewallMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 3))
ciscoFirewallMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1))
ciscoFirewallMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2))
ciscoFirewallMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1, 1)).setObjects(("CISCO-FIREWALL-MIB", "ciscoFirewallMIBStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBCompliance = ciscoFirewallMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoFirewallMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco FirewallMIB.')
ciscoFirewallMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1, 2)).setObjects(("CISCO-FIREWALL-MIB", "ciscoFirewallMIBStatisticsGroup"), ("CISCO-FIREWALL-MIB", "ciscoFirewallMIBEventsGroup"), ("CISCO-FIREWALL-MIB", "ciscoFirewallMIBNotificationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBComplianceRev1 = ciscoFirewallMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoFirewallMIBComplianceRev1.setDescription('The compliance statement for entities which implement the Cisco FirewallMIB.')
ciscoFirewallMIBEventsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 1)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventsTableLastRow"), ("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"), ("CISCO-FIREWALL-MIB", "cfwNetEventsTableLastRow"), ("CISCO-FIREWALL-MIB", "cfwNetEventInterface"), ("CISCO-FIREWALL-MIB", "cfwNetEventSrcIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideSrcIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventDstIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideDstIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventSrcIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideSrcIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventDstIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideDstIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventService"), ("CISCO-FIREWALL-MIB", "cfwNetEventServiceInformation"), ("CISCO-FIREWALL-MIB", "cfwNetEventIdentity"), ("CISCO-FIREWALL-MIB", "cfwNetEventDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBEventsGroup = ciscoFirewallMIBEventsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFirewallMIBEventsGroup.setDescription('Firewall events')
ciscoFirewallMIBStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 2)).setObjects(("CISCO-FIREWALL-MIB", "cfwHardwareInformation"), ("CISCO-FIREWALL-MIB", "cfwHardwareStatusValue"), ("CISCO-FIREWALL-MIB", "cfwHardwareStatusDetail"), ("CISCO-FIREWALL-MIB", "cfwBufferStatInformation"), ("CISCO-FIREWALL-MIB", "cfwBufferStatValue"), ("CISCO-FIREWALL-MIB", "cfwConnectionStatDescription"), ("CISCO-FIREWALL-MIB", "cfwConnectionStatCount"), ("CISCO-FIREWALL-MIB", "cfwConnectionStatValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBStatisticsGroup = ciscoFirewallMIBStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFirewallMIBStatisticsGroup.setDescription('Firewall statistics')
ciscoFirewallMIBNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 3)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBNotificationGroup = ciscoFirewallMIBNotificationGroup.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoFirewallMIBNotificationGroup.setDescription('Firewall Notifications')
ciscoFirewallMIBNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 4)).setObjects(("CISCO-FIREWALL-MIB", "cfwSecurityNotification"), ("CISCO-FIREWALL-MIB", "cfwContentInspectNotification"), ("CISCO-FIREWALL-MIB", "cfwConnNotification"), ("CISCO-FIREWALL-MIB", "cfwAccessNotification"), ("CISCO-FIREWALL-MIB", "cfwAuthNotification"), ("CISCO-FIREWALL-MIB", "cfwGenericNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBNotificationGroupRev1 = ciscoFirewallMIBNotificationGroupRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoFirewallMIBNotificationGroupRev1.setDescription('Firewall Notifications')
mibBuilder.exportSymbols("CISCO-FIREWALL-MIB", cfwNetEventsEntry=cfwNetEventsEntry, cfwStatistics=cfwStatistics, cfwBufferStatValue=cfwBufferStatValue, cfwBufferStatSize=cfwBufferStatSize, cfwNetEventInsideDstIpPort=cfwNetEventInsideDstIpPort, cfwBasicConnectionEventType=cfwBasicConnectionEventType, cfwNetEventService=cfwNetEventService, cfwNetEventDescription=cfwNetEventDescription, cfwBasicGenericEventType=cfwBasicGenericEventType, ciscoFirewallMIBNotificationGroup=ciscoFirewallMIBNotificationGroup, cfwGenericNotification=cfwGenericNotification, cfwBufferStatType=cfwBufferStatType, cfwBasicEventIndex=cfwBasicEventIndex, ciscoFirewallMIBNotificationPrefix=ciscoFirewallMIBNotificationPrefix, cfwBasicAccessEventType=cfwBasicAccessEventType, cfwBasicAuthenticationEventType=cfwBasicAuthenticationEventType, cfwNetEvents=cfwNetEvents, cfwNetEventsTable=cfwNetEventsTable, cfwNetEventSrcIpAddress=cfwNetEventSrcIpAddress, ciscoFirewallMIBNotificationGroupRev1=ciscoFirewallMIBNotificationGroupRev1, PYSNMP_MODULE_ID=ciscoFirewallMIB, cfwBasicEventDescription=cfwBasicEventDescription, cfwHardwareStatusValue=cfwHardwareStatusValue, cfwHardwareType=cfwHardwareType, cfwEvents=cfwEvents, HardwareStatus=HardwareStatus, cfwNetEventInsideSrcIpAddress=cfwNetEventInsideSrcIpAddress, cfwStatus=cfwStatus, cfwBasicEventTime=cfwBasicEventTime, cfwHardwareStatusDetail=cfwHardwareStatusDetail, ciscoFirewallMIBEventsGroup=ciscoFirewallMIBEventsGroup, cfwSystem=cfwSystem, ContentInspectionEvent=ContentInspectionEvent, cfwBasicContentInspEventType=cfwBasicContentInspEventType, cfwNetEventDstIpPort=cfwNetEventDstIpPort, cfwAuthNotification=cfwAuthNotification, cfwConnectionStatService=cfwConnectionStatService, Hardware=Hardware, cfwSecurityNotification=cfwSecurityNotification, ciscoFirewallMIBComplianceRev1=ciscoFirewallMIBComplianceRev1, cfwBasicSecurityEventType=cfwBasicSecurityEventType, ConnectionStat=ConnectionStat, cfwHardwareStatusEntry=cfwHardwareStatusEntry, cfwConnectionStatType=cfwConnectionStatType, cfwConnNotification=cfwConnNotification, cfwBasicEventDetailsTableRow=cfwBasicEventDetailsTableRow, SecurityEvent=SecurityEvent, cfwBasicEvents=cfwBasicEvents, cfwNetEventInterface=cfwNetEventInterface, ciscoFirewallMIBConformance=ciscoFirewallMIBConformance, ciscoFirewallMIB=ciscoFirewallMIB, Services=Services, AuthenticationEvent=AuthenticationEvent, cfwHardwareInformation=cfwHardwareInformation, cfwConnectionStatDescription=cfwConnectionStatDescription, cfwHardwareStatusTable=cfwHardwareStatusTable, cfwNetEventIndex=cfwNetEventIndex, cfwConnectionStatValue=cfwConnectionStatValue, cfwNetEventsTableLastRow=cfwNetEventsTableLastRow, GenericEvent=GenericEvent, ciscoFirewallMIBCompliance=ciscoFirewallMIBCompliance, cfwBufferStatsEntry=cfwBufferStatsEntry, cfwBasicEventsTable=cfwBasicEventsTable, cfwConnectionStatCount=cfwConnectionStatCount, ResourceStatistics=ResourceStatistics, cfwNetEventSrcIpPort=cfwNetEventSrcIpPort, cfwConnectionStatEntry=cfwConnectionStatEntry, cfwBufferStatsTable=cfwBufferStatsTable, ciscoFirewallMIBStatisticsGroup=ciscoFirewallMIBStatisticsGroup, AccessEvent=AccessEvent, cfwBufferStatInformation=cfwBufferStatInformation, ConnectionEvent=ConnectionEvent, cfwNetEventInsideSrcIpPort=cfwNetEventInsideSrcIpPort, cfwContentInspectNotification=cfwContentInspectNotification, ciscoFirewallMIBObjects=ciscoFirewallMIBObjects, cfwAccessNotification=cfwAccessNotification, ciscoFirewallMIBCompliances=ciscoFirewallMIBCompliances, cfwNetEventServiceInformation=cfwNetEventServiceInformation, cfwNetEventIdentity=cfwNetEventIdentity, cfwConnectionStatTable=cfwConnectionStatTable, cfwBasicEventsTableLastRow=cfwBasicEventsTableLastRow, cfwNetEventDstIpAddress=cfwNetEventDstIpAddress, cfwNetEventInsideDstIpAddress=cfwNetEventInsideDstIpAddress, cfwBasicEventsEntry=cfwBasicEventsEntry, ciscoFirewallMIBNotifications=ciscoFirewallMIBNotifications, ciscoFirewallMIBGroups=ciscoFirewallMIBGroups)
