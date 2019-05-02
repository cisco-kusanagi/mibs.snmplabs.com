#
# PySNMP MIB module DNOS-SNTP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-SNTP-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Unsigned32, Counter32, Integer32, ModuleIdentity, iso, Counter64, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Unsigned32", "Counter32", "Integer32", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "MibIdentifier")
RowStatus, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "DisplayString")
agentSntpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17))
agentSntpClientMIB.setRevisions(('2011-12-14 00:00', '2011-01-26 00:00', '2007-05-23 00:00', '2003-12-18 16:29',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: agentSntpClientMIB.setRevisionsDescriptions(('sntp source interface object added.', 'Postal address updated.', 'Dell branding related changes.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: agentSntpClientMIB.setLastUpdated('201112140000Z')
if mibBuilder.loadTexts: agentSntpClientMIB.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: agentSntpClientMIB.setContactInfo('')
if mibBuilder.loadTexts: agentSntpClientMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Dell enterprise OID pertaining to SNTP client configuration and statistical collection.')
class SntpClientAdminMode(TextualConvention, Bits):
    reference = 'RFC 2030 - Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI; Section 2.'
    description = 'An SNTP client may operate in any of several modes. At least one mode other than disabled must be supported by a client. disabled - SNTP is not administrative. No SNTP requests are sent from the client nor are any received SNTP messages processed. unicast - SNTP operates in a point-to-point fashion. A unicast client sends a request to a designated server at its unicast address and expects a reply from which it can determine the time and, optionally, the round-trip delay and local clock offset relative to the server. broadcast - SNTP operates using the local broadcast address. The broadcast address has a single subnet scope. The SNTP server uses a broadcast address to send unsolicited SNTP messages to clients. The client listens on this address and sends no requests for updates. The broadcast address is determined by the address and netmask of the service port over which the SNTP client is operating. multicast - SNTP operates in a point-to-multipoint fashion. A multicast client listens on the dedicated broadcast address or multicast group address.'
    status = 'current'
    namedValues = NamedValues(("disabled", 0), ("unicast", 1), ("broadcast", 2), ("multicast", 3))

class SntpClientUpdateStatus(TextualConvention, Integer32):
    reference = 'RFC 2030 - Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI; Section 4.'
    description = "The status of the last received response or broadcast from a configured server. These values are appropriate for all administrative modes. other - None of the following enumeration values. success - The SNTP operation was successful and the system time was updated. requestTimedOut - An SNTP poll request timed out without receiving a response from the SNTP server. badDateEncoded - The time provided by the SNTP server was not valid. versionNotSupported - The SNTP version supported by the server is not compatible with the version supported by the client. This is indicated by the server returning a version later than the version configured for that server or a version of '0'. serverUnsychronized - The SNTP server is not synchronized with its peers. This is indicated via the 'leap indicator' field on the SNTP message. serverKissOfDeath - The SNTP server indicated that no further polls are to be sent to this server. This is indicated by a stratum field field equal to 0 in a message received from a server."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("success", 2), ("requestTimedOut", 3), ("badDateEncoded", 4), ("versionNotSupported", 5), ("serverUnsychronized", 6), ("serverKissOfDeath", 7))

agentSntpClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1))
agentSntpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1))
agentSntpClientUnicast = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2))
agentSntpClientBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 3))
agentSntpClientVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2), ("version3", 3), ("version4", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientVersion.setReference('RFC 2030 - Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI; Section 5.')
if mibBuilder.loadTexts: agentSntpClientVersion.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientVersion.setDescription('The highest SNTP version this client supports. Per RFC 2030, higher versions are required to be backwards compatible with all lower versions with the exception of version 0.')
agentSntpClientSupportedMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 2), SntpClientAdminMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientSupportedMode.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientSupportedMode.setDescription('The SNTP client administrative modes that this device supports. A client may support more than one administrative mode.')
agentSntpClientMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disabled", 0), ("unicast", 1), ("broadcast", 2), ("multicast", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientMode.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientMode.setDescription('The current administrative mode of the SNTP client. A SET of this object will cause the SNTP client to change administrative modes. A SET request MUST have only 1 bit set since is not possible to operate in multiple modes simultaneously. SETs of this object are limited to values supported by the device as specified by agentSntpClientSupportedMode.')
agentSntpClientPort = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 4), InetPortNumber().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(123, 123), ValueRangeConstraint(1025, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientPort.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientPort.setDescription('The local port number used to listen for broadcasts and responses from servers.')
agentSntpClientLastUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 5), DateAndTime().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientLastUpdateTime.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientLastUpdateTime.setDescription("The local date and time that the SNTP client last updated the system time on the device since agent reboot. This time is updated for all non-disabled administrative modes of the SNTP client. If the SNTP client has not updated the time then the client MUST return '00000000'H.")
agentSntpClientLastAttemptTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 6), DateAndTime().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientLastAttemptTime.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientLastAttemptTime.setDescription("The local date and time of the last SNTP request or unsolicited SNTP message for this SNTP client since agent reboot. This value is a timestamp for the agentSntpClientLastAttemptStatus object. When the agentSntpClientLastAttemptStatus has a value of success(2), this object's value should be equal to the value returned by agentSntpClientLastUpdateTime. If no SNTP frames have been processed by the SNTP client then the client MUST return '00000000'H. This object is updated for all non-disabled administrative modes of the SNTP client.")
agentSntpClientLastAttemptStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 7), SntpClientUpdateStatus().clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientLastAttemptStatus.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientLastAttemptStatus.setDescription('The status of the last SNTP request or unsolicited SNTP message for this SNTP client since agent reboot. The status is updated for all non-disabled administrative modes of the SNTP client.')
agentSntpClientServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientServerAddressType.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientServerAddressType.setDescription('The address type of the SNTP server as identified by the last received packet. Support for all address types is NOT REQUIRED.')
agentSntpClientServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 9), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientServerAddress.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientServerAddress.setDescription('The encoded address of the SNTP server as identified by the last received packet.')
agentSntpClientServerMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientServerMode.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientServerMode.setDescription('This is a 3-bit integer identifying the mode of the server as indicated in the last received packet with values defined as follows: Mode Meaning ------------------------------------ 0 reserved 1 symmetric active 2 symmetric passive 3 client 4 server 5 broadcast 6 reserved for NTP control message 7 reserved for private use ')
agentSntpClientServerStratum = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientServerStratum.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientServerStratum.setDescription('This is an 8-bit integer identifying the stratum of the server as indicated in the last received packet with values defined as follows: Stratum Meaning ------------------------------------ 0 unspecified 1 primary reference 2-15 secondary reference 16-255 reserved')
agentSntpClientServerRefClkId = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientServerRefClkId.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientServerRefClkId.setDescription('This is the value of the Reference Identifier in the last received packet defined as follows. Reference Identifier: This is a 32-bit bitstring identifying the particular reference source. In the case of NTP Version 3 or Version 4 stratum-0 (unspecified) or stratum-1 (primary) servers, this is a four-character ASCII string, left justified and zero padded to 32 bits. In NTP Version 3 secondary servers, this is the 32-bit IPv4 address of the reference source. In NTP Version 4 secondary servers, this is the low order 32 bits of the latest transmit timestamp of the reference source.')
agentSntpClientPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(6, 10)).clone(6)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientPollInterval.setStatus('obsolete')
if mibBuilder.loadTexts: agentSntpClientPollInterval.setDescription('The minimum number of seconds between successive SNTP polls of the server in seconds as a power of two. This polling interval is used for SNTP requests in unicast(1) or broadcast(2) administrative mode.')
agentSntpClientSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 1, 14), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientSourceInterface.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface, tunnel interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates the source-interface un-selection.')
agentSntpClientUnicastPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(6, 10)).clone(6)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientUnicastPollInterval.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUnicastPollInterval.setDescription('The minimum number of seconds between successive SNTP polls of the server in seconds as a power of two. This polling interval is used for SNTP requests in unicast(1) administrative mode.')
agentSntpClientUnicastPollTimeout = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientUnicastPollTimeout.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUnicastPollTimeout.setDescription("The number of seconds to wait for a response from a SNTP server before considering the attempt to have 'timed out'. This timeout is used for SNTP requests in unicast(1) administrative mode.")
agentSntpClientUnicastPollRetry = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientUnicastPollRetry.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUnicastPollRetry.setDescription("The number of times to retry a request to the same SNTP server that has 'timed out.'. This retry count is used for directed SNTP requests in unicast(1) administrative mode. For example, assume this object has been SET to a value of 2. When the SNTP client queries a given server it will send 1 SNTP request frame. If that original attempt fails, the client will retry up to a maximum of 2 more times before declaring the unicast poll unsuccessful and attempting the next server.")
agentSntpClientUcastServerMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerMaxEntries.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerMaxEntries.setDescription('The maximum number of server entries that are allowed in the agentSntpClientUcastServerTable.')
agentSntpClientUcastServerCurrEntries = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerCurrEntries.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerCurrEntries.setDescription('The current number of server entries in the agentSntpClientUcastServerTable.')
agentSntpClientUcastServerTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6), )
if mibBuilder.loadTexts: agentSntpClientUcastServerTable.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerTable.setDescription('A table containing configuration and statistical information for unicast SNTP servers. Each server entry is represented by single conceptual row in this table.')
agentSntpClientUcastServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1), ).setIndexNames((0, "DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerIndex"))
if mibBuilder.loadTexts: agentSntpClientUcastServerEntry.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerEntry.setDescription('Information for a particular unicast SNTP server.')
agentSntpClientUcastServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentSntpClientUcastServerIndex.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerIndex.setDescription('This object uniquely identifies the entry in the table.')
agentSntpClientUcastServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentSntpClientUcastServerAddressType.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerAddressType.setDescription('This object specifies how agentSntpClientUcastServerAddr is encoded. Support for all possible enumerations defined by InetAddressType is NOT REQUIRED.')
agentSntpClientUcastServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentSntpClientUcastServerAddress.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerAddress.setDescription('The encoded internet address of an SNTP server. Unicast SNTP requests will be sent to this address. If this address is a DNS hostname, then that hostname SHOULD be resolved into an IP address each time a SNTP request is sent to it.')
agentSntpClientUcastServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(123)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentSntpClientUcastServerPort.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerPort.setDescription('The port number on the server to which poll requests are sent. A set request MUST NOT use a value of 0 for this object.')
agentSntpClientUcastServerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2), ("version3", 3), ("version4", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentSntpClientUcastServerVersion.setReference('RFC 2030 - Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI; Section 5.')
if mibBuilder.loadTexts: agentSntpClientUcastServerVersion.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerVersion.setDescription('The SNTP version this server supports. This is the value that will be encoded in NTP polls when operating in unicast(1) administrative mode.')
agentSntpClientUcastServerPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentSntpClientUcastServerPrecedence.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerPrecedence.setDescription('The precedence that this server has in relation to its peers in the determining the sequence of servers to which SNTP requests will be sent. The client continues sending requests to different servers until a successful response is received or all servers are exhausted. This object indicates the order in which to query the servers. A server entry with a precedence of 1 will be queried before a server with a precedence of 2, and so forth. If more than one server has the same precedence then the request order will follow the lexicographical ordering of the entries in this table.')
agentSntpClientUcastServerLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 7), DateAndTime().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerLastUpdateTime.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerLastUpdateTime.setDescription("The local date and time that the response from this server was used to update the system time on the device since agent reboot. If the SNTP client has not updated the time using a response from this server then this object MUST return '00000000'H.")
agentSntpClientUcastServerLastAttemptTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 8), DateAndTime().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerLastAttemptTime.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerLastAttemptTime.setDescription("The local date and time that this SNTP server was last queried since agent reboot. Essentially, this value is a timestamp for the agentSntpClientUcastServerLastAttemptStatus object. If this server has not been queried then this object MUST return '00000000'H.")
agentSntpClientUcastServerLastAttemptStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 9), SntpClientUpdateStatus().clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerLastAttemptStatus.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerLastAttemptStatus.setDescription("The status of the last SNTP request to this server since agent reboot. If no requests have been made then this object should return 'other'.")
agentSntpClientUcastServerNumRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerNumRequests.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerNumRequests.setDescription('The number of SNTP requests made to this server since the last agent reboot. This includes retry attempts to the server.')
agentSntpClientUcastServerNumFailedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientUcastServerNumFailedRequests.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerNumFailedRequests.setDescription('The number of SNTP requests made to this server that did not result in a successful response since the last agent reboot. This includes retry attempts to the server.')
agentSntpClientUcastServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 2, 6, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentSntpClientUcastServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUcastServerRowStatus.setDescription('The row status of this conceptual row in the table. active - The server is available for use in SNTP client operations. Other writable leaves in this table MAY be modified while the row is in the active state. notInService - The entry is fully configured but is not available for use in SNTP client operations. The agent MAY transition a row from the active to notInService upon receipt of a kiss of death packet from the server. createAndGo - This is the preferred mechanism for creating conceptual rows in this table. This value can never be read as the row will always transition immediately to either active or notInService. destroy - This will remove the conceptual row from the table and make it unavailable for SNTP client operations. ')
agentSntpClientBroadcastCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSntpClientBroadcastCount.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientBroadcastCount.setDescription('The number of unsolicited broadcast SNTP messages that have been received and processed by the SNTP client. Unsolicited SNTP broadcast frames will not be counted unless the SNTP agent is operating in broadcast(3) mode, as specified by agentSntpClientMode.')
agentSntpClientBroadcastInterval = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(6, 10)).clone(6)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSntpClientBroadcastInterval.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientBroadcastInterval.setDescription('The number of seconds the client will wait before processing another broadcast packet expressed as a power of two. Packets received during the wait interval are silently discarded.')
agentSntpClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2))
agentSntpClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2, 1))
agentSntpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2, 2))
agentSntpClientDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2, 1, 1)).setObjects(("DNOS-SNTP-CLIENT-MIB", "agentSntpClientVersion"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientSupportedMode"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientMode"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientLastUpdateTime"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientLastAttemptTime"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientLastAttemptStatus"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientServerAddressType"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientServerAddress"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientServerMode"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientServerStratum"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientServerRefClkId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    agentSntpClientDeviceGroup = agentSntpClientDeviceGroup.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientDeviceGroup.setDescription('A collection of objects providing device level control of an SNTP client on DNOS enabled devices.')
agentSntpClientUnicastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2, 1, 2)).setObjects(("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUnicastPollInterval"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUnicastPollTimeout"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUnicastPollRetry"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerMaxEntries"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerCurrEntries"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerAddress"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerAddressType"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerPrecedence"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerLastUpdateTime"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerLastAttemptTime"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerLastAttemptStatus"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerNumRequests"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerNumFailedRequests"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUcastServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    agentSntpClientUnicastGroup = agentSntpClientUnicastGroup.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientUnicastGroup.setDescription('A collection of objects providing control and statistics for an SNTP client capable of operating in unicast mode.')
agentSntpClientBroadcastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2, 1, 3)).setObjects(("DNOS-SNTP-CLIENT-MIB", "agentSntpClientBroadcastCount"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientBroadcastInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    agentSntpClientBroadcastGroup = agentSntpClientBroadcastGroup.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientBroadcastGroup.setDescription('A collection of objects providing control and statistics for an SNTP client capable of operating in broadcast mode.')
agentSntpClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 17, 2, 2, 1)).setObjects(("DNOS-SNTP-CLIENT-MIB", "agentSntpClientDeviceGroup"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientUnicastGroup"), ("DNOS-SNTP-CLIENT-MIB", "agentSntpClientBroadcastGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    agentSntpClientCompliance = agentSntpClientCompliance.setStatus('current')
if mibBuilder.loadTexts: agentSntpClientCompliance.setDescription('The compliance statement for devices that support agentSntpClient.')
mibBuilder.exportSymbols("DNOS-SNTP-CLIENT-MIB", agentSntpClientBroadcastInterval=agentSntpClientBroadcastInterval, agentSntpClientUcastServerEntry=agentSntpClientUcastServerEntry, agentSntpClientBroadcastGroup=agentSntpClientBroadcastGroup, agentSntpClientBroadcast=agentSntpClientBroadcast, agentSntpClientUcastServerLastAttemptTime=agentSntpClientUcastServerLastAttemptTime, agentSntpClientUcastServerIndex=agentSntpClientUcastServerIndex, agentSntpClientUcastServerMaxEntries=agentSntpClientUcastServerMaxEntries, agentSntpClientUcastServerNumRequests=agentSntpClientUcastServerNumRequests, agentSntpClientUcastServerCurrEntries=agentSntpClientUcastServerCurrEntries, agentSntpClientUcastServerTable=agentSntpClientUcastServerTable, agentSntpClientUcastServerVersion=agentSntpClientUcastServerVersion, SntpClientUpdateStatus=SntpClientUpdateStatus, agentSntpClientLastUpdateTime=agentSntpClientLastUpdateTime, agentSntpClientSourceInterface=agentSntpClientSourceInterface, agentSntpClientMode=agentSntpClientMode, agentSntpClientUcastServerNumFailedRequests=agentSntpClientUcastServerNumFailedRequests, agentSntpClientUnicastPollInterval=agentSntpClientUnicastPollInterval, agentSntpClientUcastServerAddress=agentSntpClientUcastServerAddress, agentSntpClientDeviceGroup=agentSntpClientDeviceGroup, agentSntpClientUcastServerPort=agentSntpClientUcastServerPort, agentSntpClientServerRefClkId=agentSntpClientServerRefClkId, agentSntpClientCompliance=agentSntpClientCompliance, agentSntpClientObjects=agentSntpClientObjects, agentSntpClient=agentSntpClient, agentSntpClientServerAddress=agentSntpClientServerAddress, agentSntpClientCompliances=agentSntpClientCompliances, agentSntpClientLastAttemptStatus=agentSntpClientLastAttemptStatus, agentSntpClientUcastServerLastUpdateTime=agentSntpClientUcastServerLastUpdateTime, agentSntpClientServerAddressType=agentSntpClientServerAddressType, agentSntpClientGroups=agentSntpClientGroups, agentSntpClientLastAttemptTime=agentSntpClientLastAttemptTime, agentSntpClientUnicastGroup=agentSntpClientUnicastGroup, agentSntpClientConformance=agentSntpClientConformance, PYSNMP_MODULE_ID=agentSntpClientMIB, agentSntpClientBroadcastCount=agentSntpClientBroadcastCount, agentSntpClientUnicastPollTimeout=agentSntpClientUnicastPollTimeout, agentSntpClientPort=agentSntpClientPort, agentSntpClientUcastServerRowStatus=agentSntpClientUcastServerRowStatus, agentSntpClientUnicast=agentSntpClientUnicast, agentSntpClientSupportedMode=agentSntpClientSupportedMode, agentSntpClientUcastServerAddressType=agentSntpClientUcastServerAddressType, agentSntpClientUnicastPollRetry=agentSntpClientUnicastPollRetry, agentSntpClientPollInterval=agentSntpClientPollInterval, agentSntpClientServerMode=agentSntpClientServerMode, SntpClientAdminMode=SntpClientAdminMode, agentSntpClientServerStratum=agentSntpClientServerStratum, agentSntpClientUcastServerPrecedence=agentSntpClientUcastServerPrecedence, agentSntpClientMIB=agentSntpClientMIB, agentSntpClientUcastServerLastAttemptStatus=agentSntpClientUcastServerLastAttemptStatus, agentSntpClientVersion=agentSntpClientVersion)
