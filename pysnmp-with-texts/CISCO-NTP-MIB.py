#
# PySNMP MIB module CISCO-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:08:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Unsigned32, iso, Bits, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Counter32, ModuleIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "iso", "Bits", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "ModuleIdentity", "Gauge32", "TimeTicks")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
ciscoNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 168))
ciscoNtpMIB.setRevisions(('2006-07-31 00:00', '2004-07-23 00:00', '2003-07-29 00:00', '2003-07-07 00:00', '2002-02-20 00:00', '2000-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNtpMIB.setRevisionsDescriptions(('Added ciscoNtpSysExtGroup and ciscoNtpSrvNotifGroup groups to support monitoring of NTP server status. ciscoNtpMIBComplianceRev3 is deprecated and replaced by ciscoNtpMIBComplianceRev4.', 'Added cntpPeersPeerName and cntpPeersPeerType objects to cntpPeerVarTable.', 'Added cntpPeersPrefPeer object to cntpPeersVarTable.', 'ciscoNtpPeersGroup is deprecated by ciscoNtpPeersGroupRev1. ciscoNtpMIBCompliance is deprecated by ciscoNtpMIBComplianceRev1.', 'cntpPeersUpdateTime is deprecated by cntpPeersUpdateTimeRev1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNtpMIB.setLastUpdated('200607310000Z')
if mibBuilder.loadTexts: ciscoNtpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNtpMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNtpMIB.setDescription('This MIB module defines a MIB which provides mechanisms to monitor an NTP server. The MIB is derived from the Technical Report #Management of the NTP with SNMP# TR No. 98-09 authored by A.S. Sethi and Dave Mills in the University of Delaware. Below is a brief overview of NTP system architecture and implementation model. This will help understand the objects defined below and their relationships. NTP Intro: The Network Time Protocol (NTP) Version 3, is used to synchronize timekeeping among a set of distributed time servers and clients. The service model is based on a returnable-time design which depends only on measured clock offsets, but does not require reliable message delivery. The synchronization subnet uses a self-organizing, hierarchical master-slave configuration, with synchronization paths determined by a minimum-weight spanning tree. While multiple masters (primary servers) may exist, there is no requirement for an election protocol. System Archiecture: In the NTP model a number of primary reference sources, synchronized by wire or radio to national standards, are connected to widely accessible resources, such as backbone gateways, and operated as primary time servers. The purpose of NTP is to convey timekeeping information from these servers to other time servers via the Internet and also to cross-check clocks and mitigate errors due to equipment or propagation failures. Some number of local-net hosts or gateways, acting as secondary time servers, run NTP with one or more of the primary servers. In order to reduce the protocol overhead, the secondary servers distribute time via NTP to the remaining local-net hosts. In the interest of reliability, selected hosts can be equipped with less accurate but less expensive radio clocks and used for backup in case of failure of the primary and/or secondary servers or communication paths between them. NTP is designed to produce three products: clock offset, round-trip delay and dispersion, all of which are relative to a selected reference clock. Clock offset represents the amount to adjust the local clock to bring it into correspondence with the reference clock. Roundtrip delay provides the capability to launch a message to arrive at the reference clock at a specified time. Dispersion represents the maximum error of the local clock relative to the reference clock. Since most host time servers will synchronize via another peer time server, there are two components in each of these three products, those determined by the peer relative to the primary reference source of standard time and those measured by the host relative to the peer. Each of these components are maintained separately in the protocol in order to facilitate error control and management of the subnet itself. They provide not only precision measurements of offset and delay, but also definitive maximum error bounds, so that the user interface can determine not only the time, but the quality of the time as well. Implementation Model: In what may be the most common client/server model a client sends an NTP message to one or more servers and processes the replies as received. The server interchanges addresses and ports, overwrites certain fields in the message, recalculates the checksum and returns the message immediately. Information included in the NTP message allows the client to determine the server time with respect to local time and adjust the local clock accordingly. In addition, the message includes information to calculate the expected timekeeping accuracy and reliability, as well as select the best from possibly several servers. While the client/server model may suffice for use on local nets involving a public server and perhaps many workstation clients, the full generality of NTP requires distributed participation of a number of client/servers or peers arranged in a dynamically reconfigurable, hierarchically distributed configuration. It also requires sophisticated algorithms for association management, data manipulation and local-clock control. Glossary: 1. Host: Refers to an instantiation of the NTP protocol on a local processor. 2. Peer: Refers to an instantiation of the NTP protocol on a remote processor connected by a network path from the local host.')
ciscoNtpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 0))
ciscoNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1))
ciscoNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2))
cntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1))
cntpPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2))
cntpFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.1"
    description = 'NTP timestamps are represented as a 64-bit unsigned fixed-point number, in seconds relative to 00:00 on 1 January 1900. The integer part is in the first 32 bits and the fraction part is in the last 32 bits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol(Version 3)', RFC-1305, March 1992, Section 3.2.1"
    description = 'This is a two-bit code warning of an impending leap second to be inserted in the NTP timescale. The bits are set before 23:59 on the day of insertion and reset after 00:00 on the following day. This causes the number of seconds (rollover interval) in the day of insertion to be increased or decreased by one. The two bits are coded as below, 00, no warning 01, last minute has 61 seconds 10, last minute has 59 seconds 11, alarm condition (clock not synchronized)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 3.2.1"
    description = 'The time in seconds that could represent signed quantities like time delay with respect to some source. This textual-convention is specific to Cisco implementation of NTP where 32-bit integers are used for such quantities. The signed integer part is in the first 16 bits and the fraction part is in the last 16 bits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 3.2.1"
    description = 'The time in seconds that could represent unsigned quantities like maximum error of the local clock with respect to some source. This textual-convention is specific to Cisco implementation of NTP where 32-bit integers are used for such quantities. The unsigned integer part is in the first 16 bits and the fraction part is in the last 16 bits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 2.2"
    description = 'Indicates the stratum of the clock. The stratum defines the accuracy of a time server. Higher the stratum, lower the accuracy. 0, unspecified 1, primary reference (e.g., calibrated atomic clock, radio clock) 2-255, secondary reference (via NTP)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(TextualConvention, OctetString):
    reference = "D.L. Mills, Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.1"
    description = 'The reference clock identifier. In the case of stratum 0 (unspecified) or stratum 1 (primary reference source), this is a four-octet, left-justified, zero-padded ASCII string as defined in RFC-1305. In the case of stratum 2 and greater (secondary reference) this is the four-octet Internet address of the peer selected for synchronization. Some examples of stratum 0 identifiers are, DCN, DCN routing protocol NIST, NIST public modem TSP, TSP time protocol DTS, Digital Time Service Some examples of stratum 1 identifiers are, ATOM, Atomic clock (calibrated) VLF, VLF radio (OMEGA,, etc.) LORC, LORAN-C radionavigation GOES, GOES UHF environment satellite GPS, GPS UHF satellite positioning'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPPollInterval(TextualConvention, Integer32):
    description = 'The minimum interval between transmitted NTP messages, in seconds as a power of two. For instance, a value of six indicates a minimum interval of 64 seconds.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-20, 20)

class NTPAssocIdentifier(TextualConvention, Integer32):
    description = 'The association identifier of the peer. Every peer with which an NTP server is associated with is identified by an association identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

cntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cntpSysLeap.setStatus('current')
if mibBuilder.loadTexts: cntpSysLeap.setDescription('Two-bit code warning of an impending leap second to be inserted in the NTP timescale. This object can be set only when the cntpSysStratum has a value of 1.')
cntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cntpSysStratum.setStatus('current')
if mibBuilder.loadTexts: cntpSysStratum.setDescription('The stratum of the local clock. If the value is set to 1, i.e., this is a primary reference, then the Primary-Clock procedure described in Section 3.4.6, in RFC-1305 is invoked.')
cntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPrecision.setStatus('current')
if mibBuilder.loadTexts: cntpSysPrecision.setDescription('Signed integer indicating the precision of the system clock, in seconds to the nearest power of two. The value must be rounded to the next larger power of two; for instance, a 50-Hz (20 ms) or 60-Hz (16.67 ms) power-frequency clock would be assigned the value -5 (31.25 ms), while a 1000-Hz (1 ms) crystal-controlled clock would be assigned the value -9 (1.95 ms).')
cntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 4), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRootDelay.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2.2, 3.2.1")
if mibBuilder.loadTexts: cntpSysRootDelay.setStatus('current')
if mibBuilder.loadTexts: cntpSysRootDelay.setDescription('A signed fixed-point number indicating the total round-trip delay in seconds, to the primary reference source at the root of the synchronization subnet.')
cntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 5), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRootDispersion.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 2.2, 3.2.1")
if mibBuilder.loadTexts: cntpSysRootDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpSysRootDispersion.setDescription('The maximum error in seconds, relative to the primary reference source at the root of the synchronization subnet. Only positive values greater than zero are possible.')
cntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRefId.setStatus('current')
if mibBuilder.loadTexts: cntpSysRefId.setDescription('The reference identifier of the local clock.')
cntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRefTime.setStatus('current')
if mibBuilder.loadTexts: cntpSysRefTime.setDescription('The local time when the local clock was last updated. If the local clock has never been synchronized, the value is zero.')
cntpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 8), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPoll.setStatus('current')
if mibBuilder.loadTexts: cntpSysPoll.setDescription('The interval at which the NTP server polls other NTP servers to synchronize its clock.')
cntpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 9), NTPAssocIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPeer.setStatus('current')
if mibBuilder.loadTexts: cntpSysPeer.setDescription('The current synchronization source. This will contain the unique association identifier cntpPeersAssocId of the corresponding peer entry in the cntpPeersVarTable of the peer acting as the synchronization source. If there is no peer, the value will be 0.')
cntpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 10), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysClock.setStatus('current')
if mibBuilder.loadTexts: cntpSysClock.setDescription('The current local time. Local time is derived from the hardware clock of the particular machine and increments at intervals depending on the design used.')
cntpSysSrvStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("notRunning", 2), ("notSynchronized", 3), ("syncToLocal", 4), ("syncToRefclock", 5), ("syncToRemoteServer", 6))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysSrvStatus.setStatus('current')
if mibBuilder.loadTexts: cntpSysSrvStatus.setDescription('Current state of the NTP server with values coded as follows: 1: server status is unknown 2: server is not running 3: server is not synchronized to any time source 4: server is synchronized to its own local clock 5: server is synchronized to a local hardware refclock (e.g. GPS) 6: server is synchronized to a remote NTP server')
cntpPeersVarTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1), )
if mibBuilder.loadTexts: cntpPeersVarTable.setStatus('current')
if mibBuilder.loadTexts: cntpPeersVarTable.setDescription('This table provides information on the peers with which the local NTP server has associations. The peers are also NTP servers but running on different hosts.')
cntpPeersVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-NTP-MIB", "cntpPeersAssocId"))
if mibBuilder.loadTexts: cntpPeersVarEntry.setStatus('current')
if mibBuilder.loadTexts: cntpPeersVarEntry.setDescription("Each peers' entry provides NTP information retrieved from a particular peer NTP server. Each peer is identified by a unique association identifier. Entries are automatically created when the user configures the NTP server to be associated with remote peers. Similarly entries are deleted when the user removes the peer association from the NTP server. Entries can also be created by the management station by setting values for the following objects: cntpPeersPeerAddress or cntpPeersPeerName, cntpPeersHostAddress and cntpPeersMode and making the cntpPeersEntryStatus as active(1). At the least, the management station has to set a value for cntpPeersPeerAddress or cntpPeersPeerName to make the row active.")
cntpPeersAssocId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 1), NTPAssocIdentifier())
if mibBuilder.loadTexts: cntpPeersAssocId.setStatus('current')
if mibBuilder.loadTexts: cntpPeersAssocId.setDescription('An integer value greater than 0 that uniquely identifies a peer with which the local NTP server is associated.')
cntpPeersConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersConfigured.setStatus('current')
if mibBuilder.loadTexts: cntpPeersConfigured.setDescription('This is a bit indicating that the association was created from configuration information and should not be de-associated even if the peer becomes unreachable.')
cntpPeersPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerAddress.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerAddress.setDescription('The IP address of the peer. When creating a new association, a value should be set either for this object or the corresponding instance of cntpPeersPeerName, before the row is made active.')
cntpPeersPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPeerPort.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerPort.setDescription('The UDP port number on which the peer receives NTP messages.')
cntpPeersHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersHostAddress.setStatus('current')
if mibBuilder.loadTexts: cntpPeersHostAddress.setDescription('The IP address of the local host. Multi-homing can be supported using this object.')
cntpPeersHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersHostPort.setStatus('current')
if mibBuilder.loadTexts: cntpPeersHostPort.setDescription('The UDP port number on which the local host receives NTP messages.')
cntpPeersLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 7), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersLeap.setStatus('current')
if mibBuilder.loadTexts: cntpPeersLeap.setDescription('Two-bit code warning of an impending leap second to be inserted in the NTP timescale of the peer.')
cntpPeersMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersMode.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.3")
if mibBuilder.loadTexts: cntpPeersMode.setStatus('current')
if mibBuilder.loadTexts: cntpPeersMode.setDescription('The association mode of the NTP server, with values coded as follows, 0, unspecified 1, symmetric active - A host operating in this mode sends periodic messages regardless of the reachability state or stratum of its peer. By operating in this mode the host announces its willingness to synchronize and be synchronized by the peer 2, symmetric passive - This type of association is ordinarily created upon arrival of a message from a peer operating in the symmetric active mode and persists only as long as the peer is reachable and operating at a stratum level less than or equal to the host; otherwise, the association is dissolved. However, the association will always persist until at least one message has been sent in reply. By operating in this mode the host announces its willingness to synchronize and be synchronized by the peer 3, client - A host operating in this mode sends periodic messages regardless of the reachability state or stratum of its peer. By operating in this mode the host, usually a LAN workstation, announces its willingness to be synchronized by, but not to synchronize the peer 4, server - This type of association is ordinarily created upon arrival of a client request message and exists only in order to reply to that request, after which the association is dissolved. By operating in this mode the host, usually a LAN time server, announces its willingness to synchronize, but not to be synchronized by the peer 5, broadcast - A host operating in this mode sends periodic messages regardless of the reachability state or stratum of the peers. By operating in this mode the host, usually a LAN time server operating on a high-speed broadcast medium, announces its willingness to synchronize all of the peers, but not to be synchronized by any of them 6, reserved for NTP control messages 7, reserved for private use. When creating a new peer association, if no value is specified for this object, it defaults to symmetricActive(1).')
cntpPeersStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 9), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersStratum.setStatus('current')
if mibBuilder.loadTexts: cntpPeersStratum.setDescription('The stratum of the peer clock.')
cntpPeersPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 10), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPeerPoll.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerPoll.setDescription('The interval at which the peer polls the local host.')
cntpPeersHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 11), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersHostPoll.setStatus('current')
if mibBuilder.loadTexts: cntpPeersHostPoll.setDescription('The interval at which the local host polls the peer.')
cntpPeersPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPrecision.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPrecision.setDescription('Signed integer indicating the precision of the peer clock, in seconds to the nearest power of two. The value must be rounded to the next larger power of two; for instance, a 50-Hz (20 ms) or 60-Hz (16.67 ms) power-frequency clock would be assigned the value -5 (31.25 ms), while a 1000-Hz (1 ms) crystal-controlled clock would be assigned the value -9 (1.95 ms).')
cntpPeersRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 13), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRootDelay.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRootDelay.setDescription('A signed fixed-point number indicating the total round-trip delay in seconds, from the peer to the primary reference source at the root of the synchronization subnet.')
cntpPeersRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 14), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRootDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRootDispersion.setDescription('The maximum error in seconds, of the peer clock relative to the primary reference source at the root of the synchronization subnet. Only positive values greater than zero are possible.')
cntpPeersRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 15), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRefId.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRefId.setDescription('The reference identifier of the peer.')
cntpPeersRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 16), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRefTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRefTime.setDescription('The local time at the peer when its clock was last updated. If the peer clock has never been synchronized, the value is zero.')
cntpPeersOrgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 17), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersOrgTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersOrgTime.setDescription('The local time at the peer, when its latest NTP message was sent. If the peer becomes unreachable the value is set to zero.')
cntpPeersReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 18), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersReceiveTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersReceiveTime.setDescription('The local time, when the latest NTP message from the peer arrived. If the peer becomes unreachable the value is set to zero.')
cntpPeersTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 19), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersTransmitTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersTransmitTime.setDescription('The local time at which the NTP message departed the sender.')
cntpPeersUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersUpdateTime.setStatus('deprecated')
if mibBuilder.loadTexts: cntpPeersUpdateTime.setDescription('The local time, when the most recent NTP message was received from the peer that was used to calculate the skew dispersion. This represents only the 32-bit integer part of the NTPTimestamp.')
cntpPeersReach = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersReach.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.3")
if mibBuilder.loadTexts: cntpPeersReach.setStatus('current')
if mibBuilder.loadTexts: cntpPeersReach.setDescription('A shift register of used to determine the reachability status of the peer, with bits entering from the least significant (rightmost) end. A peer is considered reachable if at least one bit in this register is set to one i.e, if the value of this object is non-zero. The data in the shift register would be populated by the NTP protocol procedures.')
cntpPeersTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersTimer.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.3")
if mibBuilder.loadTexts: cntpPeersTimer.setStatus('current')
if mibBuilder.loadTexts: cntpPeersTimer.setDescription('The interval in seconds, between transmitted NTP messages from the local host to the peer.')
cntpPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 23), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersOffset.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpPeersOffset.setStatus('current')
if mibBuilder.loadTexts: cntpPeersOffset.setDescription('The estimated offset of the peer clock relative to the local clock, in seconds. The host determines the value of this object using the NTP clock-filter algorithm.')
cntpPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 24), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersDelay.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpPeersDelay.setStatus('current')
if mibBuilder.loadTexts: cntpPeersDelay.setDescription('The estimated round-trip delay of the peer clock relative to the local clock over the network path between them, in seconds. The host determines the value of this object using the NTP clock-filter algorithm.')
cntpPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 25), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersDispersion.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpPeersDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpPeersDispersion.setDescription('The estimated maximum error of the peer clock relative to the local clock over the network path between them, in seconds. The host determines the value of this object using the NTP clock-filter algorithm.')
cntpPeersFilterValidEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 26), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersFilterValidEntries.setStatus('current')
if mibBuilder.loadTexts: cntpPeersFilterValidEntries.setDescription('The number of valid entries for a peer in the Filter Register Table. Since, the Filter Register Table is optional, this object will have a value 0 if the Filter Register Table is not implemented.')
cntpPeersEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersEntryStatus.setStatus('current')
if mibBuilder.loadTexts: cntpPeersEntryStatus.setDescription('The status object for this row. When a management station is creating a new row, it should set the value for cntpPeersPeerAddress at least, before the row can be made active(1).')
cntpPeersUpdateTimeRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersUpdateTimeRev1.setStatus('current')
if mibBuilder.loadTexts: cntpPeersUpdateTimeRev1.setDescription('The local time, when the most recent NTP message was received from the peer that was used to calculate the skew dispersion. This represents only the 32-bit integer part of the NTPTimestamp.')
cntpPeersPrefPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPrefPeer.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPrefPeer.setDescription("This object specifies whether this peer is the preferred one over the others. By default, when the value of this object is 'false', NTP chooses the peer with which to synchronize the time on the local system. If this object is set to 'true', NTP will choose the corresponding peer to synchronize the time with. If multiple entries have this object set to 'true', NTP will choose the first one to be set. This object is a means to override the selection of the peer by NTP.")
cntpPeersPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 30), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerType.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerType.setDescription('Represents the type of the corresponding instance of cntpPeersPeerName object.')
cntpPeersPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 31), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerName.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerName.setDescription('The address of the peer. When creating a new association, a value must be set for either this object or the corresponding instance of cntpPeersPeerAddress object, before the row is made active.')
cntpFilterRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2), )
if mibBuilder.loadTexts: cntpFilterRegisterTable.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpFilterRegisterTable.setStatus('current')
if mibBuilder.loadTexts: cntpFilterRegisterTable.setDescription('The following table contains NTP state variables used by the NTP clock filter and selection algorithms. This table depicts a shift register. Each stage in the shift register is a 3-tuple consisting of the measured clock offset, measured clock delay and measured clock dispersion associated with a single observation. An important factor affecting the accuracy and reliability of time distribution is the complex of algorithms used to reduce the effect of statistical errors and falsetickers due to failure of various subnet components, reference sources or propagation media. The NTP clock-filter and selection algorithms are designed to do exactly this. The objects in the filter register table below are used by these algorthims to minimize the error in the calculated time.')
cntpFilterRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-NTP-MIB", "cntpPeersAssocId"), (0, "CISCO-NTP-MIB", "cntpFilterIndex"))
if mibBuilder.loadTexts: cntpFilterRegisterEntry.setStatus('current')
if mibBuilder.loadTexts: cntpFilterRegisterEntry.setDescription('Each entry corresponds to one stage of the shift register, i.e., one reading of the variables clock delay, clock offset and clock dispersion. Entries are automatically created whenever a peer is configured and deleted when the peer is removed.')
cntpFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: cntpFilterIndex.setStatus('current')
if mibBuilder.loadTexts: cntpFilterIndex.setDescription('An integer value in the specified range that is used to index into the table. The size of the table is fixed at 8. Each entry identifies a particular reading of the clock filter variables in the shift register. Entries are added starting at index 1. The index wraps back to 1 when it reaches 8. When the index wraps back, the new entries will overwrite the old entries effectively deleting the old entry.')
cntpFilterPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 2), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersOffset.setStatus('current')
if mibBuilder.loadTexts: cntpFilterPeersOffset.setDescription('The offset of the peer clock relative to the local clock in seconds.')
cntpFilterPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 3), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersDelay.setStatus('current')
if mibBuilder.loadTexts: cntpFilterPeersDelay.setDescription('Round-trip delay of the peer clock relative to the local clock over the network path between them, in seconds. This variable can take on both positive and negative values, depending on clock precision and skew-error accumulation.')
cntpFilterPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 4), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpFilterPeersDispersion.setDescription('The maximum error of the peer clock relative to the local clock over the network path between them, in seconds. Only positive values greater than zero are possible.')
ciscoNtpSrvStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 1)).setObjects(("CISCO-NTP-MIB", "cntpSysSrvStatus"))
if mibBuilder.loadTexts: ciscoNtpSrvStatusChange.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSrvStatusChange.setDescription('This notification is generated whenever the value of cntpSysSrvStatus changes.')
ciscoNtpHighPriorityConnFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 2)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnFailure.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnFailure.setDescription('A failure to connect with an high priority NTP server (e.g. a server at the lowest stratum) is detected.')
ciscoNtpHighPriorityConnRestore = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 3)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnRestore.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnRestore.setDescription('A connection with an high priority NTP server (e.g. a server at the lowest stratum) is restored.')
ciscoNtpGeneralConnFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 4))
if mibBuilder.loadTexts: ciscoNtpGeneralConnFailure.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpGeneralConnFailure.setDescription('This trap is sent when the device loses connectivity to all NTP servers.')
ciscoNtpGeneralConnRestore = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 5)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpGeneralConnRestore.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpGeneralConnRestore.setDescription('This trap is sent when the connection with at least one NTP server has been restored (e.g. after a ciscoNtpGeneralConnFailure).')
ciscoNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1))
ciscoNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2))
ciscoNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 1)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroup"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBCompliance = ciscoNtpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBCompliance.setDescription('The compliance statement for Cisco agents which implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 2)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev1"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev1 = ciscoNtpMIBComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev1.setDescription('The compliance statement for Cisco agents which implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 3)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev1"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev2 = ciscoNtpMIBComplianceRev2.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev2.setDescription('The compliance statement for Cisco agents which implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 4)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev2"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev3 = ciscoNtpMIBComplianceRev3.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev3.setDescription('The compliance statement for Cisco agents which implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 5)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev2"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"), ("CISCO-NTP-MIB", "ciscoNtpSysExtGroup"), ("CISCO-NTP-MIB", "ciscoNtpSrvNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev4 = ciscoNtpMIBComplianceRev4.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev4.setDescription('The compliance statement for Cisco agents which implement the Cisco NTP MIB.')
ciscoNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 1)).setObjects(("CISCO-NTP-MIB", "cntpSysLeap"), ("CISCO-NTP-MIB", "cntpSysStratum"), ("CISCO-NTP-MIB", "cntpSysPrecision"), ("CISCO-NTP-MIB", "cntpSysRootDelay"), ("CISCO-NTP-MIB", "cntpSysRootDispersion"), ("CISCO-NTP-MIB", "cntpSysRefId"), ("CISCO-NTP-MIB", "cntpSysRefTime"), ("CISCO-NTP-MIB", "cntpSysPoll"), ("CISCO-NTP-MIB", "cntpSysPeer"), ("CISCO-NTP-MIB", "cntpSysClock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSysGroup = ciscoNtpSysGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSysGroup.setDescription('The NTP system variables.')
ciscoNtpPeersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 2)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTime"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroup = ciscoNtpPeersGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpPeersGroup.setDescription('The NTP peer variables.')
ciscoNtpFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 3)).setObjects(("CISCO-NTP-MIB", "cntpFilterPeersOffset"), ("CISCO-NTP-MIB", "cntpFilterPeersDelay"), ("CISCO-NTP-MIB", "cntpFilterPeersDispersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpFilterGroup = ciscoNtpFilterGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpFilterGroup.setDescription('The NTP clock-filter variables.')
ciscoNtpPeersGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 4)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroupRev1 = ciscoNtpPeersGroupRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpPeersGroupRev1.setDescription('The NTP peer variables.')
ciscoNtpPeerExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 5)).setObjects(("CISCO-NTP-MIB", "cntpPeersPrefPeer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeerExtGroup = ciscoNtpPeerExtGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpPeerExtGroup.setDescription('The extended set of NTP peer variable(s).')
ciscoNtpPeersGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 6)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"), ("CISCO-NTP-MIB", "cntpPeersPeerName"), ("CISCO-NTP-MIB", "cntpPeersPeerType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroupRev2 = ciscoNtpPeersGroupRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpPeersGroupRev2.setDescription('The NTP peer variables.')
ciscoNtpSysExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 7)).setObjects(("CISCO-NTP-MIB", "cntpSysSrvStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSysExtGroup = ciscoNtpSysExtGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSysExtGroup.setDescription('The extended set of NTP system variable(s).')
ciscoNtpSrvNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 8)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSrvStatusChange"), ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnFailure"), ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnRestore"), ("CISCO-NTP-MIB", "ciscoNtpGeneralConnFailure"), ("CISCO-NTP-MIB", "ciscoNtpGeneralConnRestore"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSrvNotifGroup = ciscoNtpSrvNotifGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSrvNotifGroup.setDescription('The collection of notifications for the NTP Server.')
mibBuilder.exportSymbols("CISCO-NTP-MIB", cntpFilterPeersDispersion=cntpFilterPeersDispersion, cntpPeersUpdateTimeRev1=cntpPeersUpdateTimeRev1, ciscoNtpGeneralConnRestore=ciscoNtpGeneralConnRestore, ciscoNtpMIBComplianceRev2=ciscoNtpMIBComplianceRev2, cntpFilterIndex=cntpFilterIndex, cntpSysRootDelay=cntpSysRootDelay, cntpPeersPeerPoll=cntpPeersPeerPoll, cntpPeersPeerAddress=cntpPeersPeerAddress, ciscoNtpSysGroup=ciscoNtpSysGroup, ciscoNtpMIBCompliance=ciscoNtpMIBCompliance, cntpSysLeap=cntpSysLeap, cntpPeersRefTime=cntpPeersRefTime, ciscoNtpSrvNotifGroup=ciscoNtpSrvNotifGroup, cntpPeersStratum=cntpPeersStratum, cntpFilterPeersOffset=cntpFilterPeersOffset, cntpPeersVarTable=cntpPeersVarTable, cntpPeersReach=cntpPeersReach, cntpSysClock=cntpSysClock, cntpSysPeer=cntpSysPeer, ciscoNtpMIBComplianceRev4=ciscoNtpMIBComplianceRev4, cntpFilterRegisterEntry=cntpFilterRegisterEntry, cntpPeersPeerType=cntpPeersPeerType, cntpPeersRootDispersion=cntpPeersRootDispersion, ciscoNtpMIBGroups=ciscoNtpMIBGroups, cntpPeersHostPort=cntpPeersHostPort, ciscoNtpMIBObjects=ciscoNtpMIBObjects, ciscoNtpMIBConformance=ciscoNtpMIBConformance, ciscoNtpMIBComplianceRev1=ciscoNtpMIBComplianceRev1, cntpFilterRegisterTable=cntpFilterRegisterTable, NTPStratum=NTPStratum, ciscoNtpSrvStatusChange=ciscoNtpSrvStatusChange, ciscoNtpMIBCompliances=ciscoNtpMIBCompliances, cntpFilter=cntpFilter, NTPPollInterval=NTPPollInterval, ciscoNtpPeerExtGroup=ciscoNtpPeerExtGroup, ciscoNtpPeersGroup=ciscoNtpPeersGroup, ciscoNtpMIBNotifs=ciscoNtpMIBNotifs, NTPLeapIndicator=NTPLeapIndicator, cntpSysStratum=cntpSysStratum, cntpPeersAssocId=cntpPeersAssocId, cntpSysRefTime=cntpSysRefTime, cntpPeersEntryStatus=cntpPeersEntryStatus, NTPRefId=NTPRefId, ciscoNtpPeersGroupRev1=ciscoNtpPeersGroupRev1, cntpPeersPeerPort=cntpPeersPeerPort, cntpPeersConfigured=cntpPeersConfigured, cntpSysSrvStatus=cntpSysSrvStatus, cntpPeersPrefPeer=cntpPeersPrefPeer, ciscoNtpGeneralConnFailure=ciscoNtpGeneralConnFailure, cntpSysRefId=cntpSysRefId, NTPTimeStamp=NTPTimeStamp, cntpPeersTransmitTime=cntpPeersTransmitTime, cntpSysPrecision=cntpSysPrecision, cntpPeersHostPoll=cntpPeersHostPoll, cntpPeersUpdateTime=cntpPeersUpdateTime, ciscoNtpHighPriorityConnRestore=ciscoNtpHighPriorityConnRestore, cntpPeersTimer=cntpPeersTimer, cntpPeersRefId=cntpPeersRefId, cntpFilterPeersDelay=cntpFilterPeersDelay, NTPAssocIdentifier=NTPAssocIdentifier, cntpPeersPrecision=cntpPeersPrecision, cntpPeersOffset=cntpPeersOffset, cntpSysRootDispersion=cntpSysRootDispersion, cntpPeersReceiveTime=cntpPeersReceiveTime, NTPUnsignedTimeValue=NTPUnsignedTimeValue, ciscoNtpHighPriorityConnFailure=ciscoNtpHighPriorityConnFailure, ciscoNtpPeersGroupRev2=ciscoNtpPeersGroupRev2, cntpPeersMode=cntpPeersMode, cntpPeersRootDelay=cntpPeersRootDelay, ciscoNtpMIBComplianceRev3=ciscoNtpMIBComplianceRev3, ciscoNtpMIB=ciscoNtpMIB, cntpSystem=cntpSystem, cntpPeersLeap=cntpPeersLeap, cntpPeersPeerName=cntpPeersPeerName, cntpPeersFilterValidEntries=cntpPeersFilterValidEntries, cntpPeersOrgTime=cntpPeersOrgTime, NTPSignedTimeValue=NTPSignedTimeValue, cntpPeers=cntpPeers, PYSNMP_MODULE_ID=ciscoNtpMIB, cntpPeersVarEntry=cntpPeersVarEntry, ciscoNtpFilterGroup=ciscoNtpFilterGroup, ciscoNtpSysExtGroup=ciscoNtpSysExtGroup, cntpPeersDelay=cntpPeersDelay, cntpSysPoll=cntpSysPoll, cntpPeersDispersion=cntpPeersDispersion, cntpPeersHostAddress=cntpPeersHostAddress)
