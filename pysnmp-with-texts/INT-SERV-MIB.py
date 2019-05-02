#
# PySNMP MIB module INT-SERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INT-SERV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, mib_2, iso, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "mib-2", "iso", "Gauge32", "ObjectIdentity")
DisplayString, TruthValue, RowStatus, TestAndIncr, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TestAndIncr", "TextualConvention")
intSrv = ModuleIdentity((1, 3, 6, 1, 2, 1, 52))
if mibBuilder.loadTexts: intSrv.setLastUpdated('9710030642Z')
if mibBuilder.loadTexts: intSrv.setOrganization('IETF Integrated Services Working Group')
if mibBuilder.loadTexts: intSrv.setContactInfo(' Fred Baker Postal: Cisco Systems 519 Lado Drive Santa Barbara, California 93111 Tel: +1 805 681 0115 E-Mail: fred@cisco.com John Krawczyk Postal: ArrowPoint Communications 235 Littleton Road Westford, Massachusetts 01886 Tel: +1 508 692 5875 E-Mail: jjk@tiac.net')
if mibBuilder.loadTexts: intSrv.setDescription('The MIB module to describe the Integrated Services Protocol')
intSrvObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 1))
intSrvGenObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 2))
intSrvNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 3))
intSrvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4))
class SessionNumber(TextualConvention, Integer32):
    description = 'The Session Number convention is used for numbers identifying sessions or saved PATH or RESV information. It is a number in the range returned by a TestAndIncr variable, having no protocol meaning whatsoever but serving instead as simple identifier. The alternative was a very complex instance or instance object that became unwieldy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Protocol(TextualConvention, Integer32):
    description = 'The value of the IP Protocol field of an IP Datagram Header. This identifies the protocol layer above IP. For example, the value 6 is used for TCP and the value 17 is used for UDP. The values of this field are defined in the As- signed Numbers RFC.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class SessionType(TextualConvention, Integer32):
    description = "The value of the C-Type field of a Session ob- ject, as defined in the RSVP specification. This value determines the lengths of octet strings and use of certain objects such as the 'port' variables. If the C-Type calls for an IP6 address, one would expect all source, des- tination, and next/previous hop addresses to be 16 bytes long, and for the ports to be UDP/TCP port numbers, for example."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class Port(TextualConvention, OctetString):
    description = 'The value of the UDP or TCP Source or Destina- tion Port field, a virtual destination port or generalized port identifier used with the IPSEC Authentication Header or Encapsulating Security Payload, or other session discriminator. If it is not used, the value should be of length 0. This pair, when coupled with the IP Addresses of the source and destination system and the IP protocol field, uniquely identifies a data stream.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 4)

class MessageSize(TextualConvention, Integer32):
    description = 'The size of a message in bytes. This is used to specify the minimum and maximum size of a message along an integrated services route.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BitRate(TextualConvention, Integer32):
    description = 'The rate, in bits/second, that data may move in the context. Applicable contexts minimally include the speed of an interface or virtual circuit, the data rate of a (potentially aggre- gated) data flow, or the data rate to be allo- cated for use by a flow.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BurstSize(TextualConvention, Integer32):
    description = 'The number of octets of IP Data, including IP Headers, that a stream may send without concern for policing.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class QosService(TextualConvention, Integer32):
    description = 'The class of service in use by a flow.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 5))
    namedValues = NamedValues(("bestEffort", 1), ("guaranteedDelay", 2), ("controlledLoad", 5))

intSrvIfAttribTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 1), )
if mibBuilder.loadTexts: intSrvIfAttribTable.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribTable.setDescription("The reservable attributes of the system's in- terfaces.")
intSrvIfAttribEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvIfAttribEntry.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribEntry.setDescription('The reservable attributes of a given inter- face.')
intSrvIfAttribAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 1), BitRate()).setUnits('Bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBits.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBits.setDescription('The number of bits/second currently allocated to reserved sessions on the interface.')
intSrvIfAttribMaxAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 2), BitRate()).setUnits('Bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribMaxAllocatedBits.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribMaxAllocatedBits.setDescription('The maximum number of bits/second that may be allocated to reserved sessions on the inter- face.')
intSrvIfAttribAllocatedBuffer = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 3), BurstSize()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBuffer.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBuffer.setDescription('The amount of buffer space required to hold the simultaneous burst of all reserved flows on the interface.')
intSrvIfAttribFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribFlows.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribFlows.setDescription('The number of reserved flows currently active on this interface. A flow can be created ei- ther from a reservation protocol (such as RSVP or ST-II) or via configuration information.')
intSrvIfAttribPropagationDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 5), Integer32()).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribPropagationDelay.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribPropagationDelay.setDescription('The amount of propagation delay that this in- terface introduces in addition to that intro- diced by bit propagation delays.')
intSrvIfAttribStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribStatus.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribStatus.setDescription("'active' on interfaces that are configured for RSVP.")
intSrvFlowTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 2), )
if mibBuilder.loadTexts: intSrvFlowTable.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowTable.setDescription("Information describing the reserved flows us- ing the system's interfaces.")
intSrvFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 2, 1), ).setIndexNames((0, "INT-SERV-MIB", "intSrvFlowNumber"))
if mibBuilder.loadTexts: intSrvFlowEntry.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowEntry.setDescription('Information describing the use of a given in- terface by a given flow. The counter intSrvFlowPoliced starts counting at the in- stallation of the flow.')
intSrvFlowNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 1), SessionNumber())
if mibBuilder.loadTexts: intSrvFlowNumber.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowNumber.setDescription('The number of this flow. This is for SNMP In- dexing purposes only and has no relation to any protocol value.')
intSrvFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 2), SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowType.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowType.setDescription('The type of session (IP4, IP6, IP6 with flow information, etc).')
intSrvFlowOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("rsvp", 2), ("management", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOwner.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowOwner.setDescription('The process that installed this flow in the queue policy database.')
intSrvFlowDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddr.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDestAddr.setDescription("The destination address used by all senders in this session. This object may not be changed when the value of the RowStatus object is 'ac- tive'.")
intSrvFlowSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddr.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowSenderAddr.setDescription("The source address of the sender selected by this reservation. The value of all zeroes in- dicates 'all senders'. This object may not be changed when the value of the RowStatus object is 'active'.")
intSrvFlowDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddrLength.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDestAddrLength.setDescription("The length of the destination address in bits. This is the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits. This object may not be changed when the value of the RowStatus object is 'active'.")
intSrvFlowSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddrLength.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowSenderAddrLength.setDescription("The length of the sender's address in bits. This is the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits. This object may not be changed when the value of the RowStatus object is 'active'.")
intSrvFlowProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 8), Protocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowProtocol.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowProtocol.setDescription("The IP Protocol used by a session. This ob- ject may not be changed when the value of the RowStatus object is 'active'.")
intSrvFlowDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 9), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestPort.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDestPort.setDescription("The UDP or TCP port number used as a destina- tion port for all senders in this session. If the IP protocol in use, specified by intSrvResvFwdProtocol, is 50 (ESP) or 51 (AH), this represents a virtual destination port number. A value of zero indicates that the IP protocol in use does not have ports. This ob- ject may not be changed when the value of the RowStatus object is 'active'.")
intSrvFlowPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 10), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowPort.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowPort.setDescription("The UDP or TCP port number used as a source port for this sender in this session. If the IP protocol in use, specified by intSrvResvFwdProtocol is 50 (ESP) or 51 (AH), this represents a generalized port identifier (GPI). A value of zero indicates that the IP protocol in use does not have ports. This ob- ject may not be changed when the value of the RowStatus object is 'active'.")
intSrvFlowFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowFlowId.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowFlowId.setDescription('The flow ID that this sender is using, if this is an IPv6 session.')
intSrvFlowInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 12), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowInterface.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowInterface.setDescription('The ifIndex value of the interface on which this reservation exists.')
intSrvFlowIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowIfAddr.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowIfAddr.setDescription('The IP Address on the ifEntry on which this reservation exists. This is present primarily to support those interfaces which layer multi- ple IP Addresses on the interface.')
intSrvFlowRate = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 14), BitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowRate.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowRate.setDescription("The Reserved Rate of the sender's data stream. If this is a Controlled Load service flow, this rate is derived from the Tspec rate parameter (r). If this is a Guaranteed service flow, this rate is derived from the Rspec clearing rate parameter (R).")
intSrvFlowBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 15), BurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowBurst.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowBurst.setDescription("The size of the largest burst expected from the sender at a time. If this is less than the sender's advertised burst size, the receiver is asking the network to provide flow pacing beyond what would be provided under normal circumstances. Such pac- ing is at the network's option.")
intSrvFlowWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowWeight.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowWeight.setDescription('The weight used to prioritize the traffic. Note that the interpretation of this object is implementation-specific, as implementations vary in their use of weighting procedures.')
intSrvFlowQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowQueue.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowQueue.setDescription('The number of the queue used by this traffic. Note that the interpretation of this object is implementation-specific, as implementations vary in their use of queue identifiers.')
intSrvFlowMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 18), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMinTU.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowMinTU.setDescription('The minimum message size for this flow. The policing algorithm will treat smaller messages as though they are this size.')
intSrvFlowMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 19), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMaxTU.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowMaxTU.setDescription('The maximum datagram size for this flow that will conform to the traffic specification. This value cannot exceed the MTU of the interface.')
intSrvFlowBestEffort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowBestEffort.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowBestEffort.setDescription('The number of packets that were remanded to best effort service.')
intSrvFlowPoliced = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowPoliced.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowPoliced.setDescription("The number of packets policed since the incep- tion of the flow's service.")
intSrvFlowDiscard = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDiscard.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDiscard.setDescription("If 'true', the flow is to incur loss when traffic is policed. If 'false', policed traff- ic is treated as best effort traffic.")
intSrvFlowService = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 23), QosService()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowService.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowService.setDescription('The QoS service being applied to this flow.')
intSrvFlowOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOrder.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowOrder.setDescription('In the event of ambiguity, the order in which the classifier should make its comparisons. The row with intSrvFlowOrder=0 is tried first, and comparisons proceed in the order of in- creasing value. Non-serial implementations of the classifier should emulate this behavior.')
intSrvFlowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowStatus.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowStatus.setDescription("'active' for all active flows. This object may be used to install static classifier infor- mation, delete classifier information, or au- thorize such.")
intSrvFlowNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 52, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intSrvFlowNewIndex.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowNewIndex.setDescription("This object is used to assign values to intSrvFlowNumber as described in 'Textual Con- ventions for SNMPv2'. The network manager reads the object, and then writes the value back in the SET that creates a new instance of intSrvFlowEntry. If the SET fails with the code 'inconsistentValue', then the process must be repeated; If the SET succeeds, then the ob- ject is incremented, and the new instance is created according to the manager's directions.")
intSrvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 2, 1)).setObjects(("INT-SERV-MIB", "intSrvIfAttribGroup"), ("INT-SERV-MIB", "intSrvFlowsGroup"), ("INT-SERV-MIB", "intSrvGenObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvCompliance = intSrvCompliance.setStatus('current')
if mibBuilder.loadTexts: intSrvCompliance.setDescription('The compliance statement ')
intSrvIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 1)).setObjects(("INT-SERV-MIB", "intSrvIfAttribAllocatedBits"), ("INT-SERV-MIB", "intSrvIfAttribMaxAllocatedBits"), ("INT-SERV-MIB", "intSrvIfAttribAllocatedBuffer"), ("INT-SERV-MIB", "intSrvIfAttribFlows"), ("INT-SERV-MIB", "intSrvIfAttribPropagationDelay"), ("INT-SERV-MIB", "intSrvIfAttribStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvIfAttribGroup = intSrvIfAttribGroup.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribGroup.setDescription('These objects are required for Systems sup- porting the Integrated Services Architecture.')
intSrvFlowsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 2)).setObjects(("INT-SERV-MIB", "intSrvFlowType"), ("INT-SERV-MIB", "intSrvFlowOwner"), ("INT-SERV-MIB", "intSrvFlowDestAddr"), ("INT-SERV-MIB", "intSrvFlowSenderAddr"), ("INT-SERV-MIB", "intSrvFlowDestAddrLength"), ("INT-SERV-MIB", "intSrvFlowSenderAddrLength"), ("INT-SERV-MIB", "intSrvFlowProtocol"), ("INT-SERV-MIB", "intSrvFlowDestPort"), ("INT-SERV-MIB", "intSrvFlowPort"), ("INT-SERV-MIB", "intSrvFlowFlowId"), ("INT-SERV-MIB", "intSrvFlowInterface"), ("INT-SERV-MIB", "intSrvFlowBestEffort"), ("INT-SERV-MIB", "intSrvFlowRate"), ("INT-SERV-MIB", "intSrvFlowBurst"), ("INT-SERV-MIB", "intSrvFlowWeight"), ("INT-SERV-MIB", "intSrvFlowQueue"), ("INT-SERV-MIB", "intSrvFlowMinTU"), ("INT-SERV-MIB", "intSrvFlowMaxTU"), ("INT-SERV-MIB", "intSrvFlowDiscard"), ("INT-SERV-MIB", "intSrvFlowPoliced"), ("INT-SERV-MIB", "intSrvFlowService"), ("INT-SERV-MIB", "intSrvFlowIfAddr"), ("INT-SERV-MIB", "intSrvFlowOrder"), ("INT-SERV-MIB", "intSrvFlowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvFlowsGroup = intSrvFlowsGroup.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowsGroup.setDescription('These objects are required for Systems sup- porting the Integrated Services Architecture.')
intSrvGenObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 3)).setObjects(("INT-SERV-MIB", "intSrvFlowNewIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGenObjectsGroup = intSrvGenObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: intSrvGenObjectsGroup.setDescription('These objects are required for Systems sup- porting the Integrated Services Architecture.')
mibBuilder.exportSymbols("INT-SERV-MIB", BitRate=BitRate, intSrvIfAttribAllocatedBits=intSrvIfAttribAllocatedBits, intSrvFlowMaxTU=intSrvFlowMaxTU, intSrvFlowOrder=intSrvFlowOrder, PYSNMP_MODULE_ID=intSrv, Protocol=Protocol, intSrvIfAttribAllocatedBuffer=intSrvIfAttribAllocatedBuffer, intSrvFlowDestAddr=intSrvFlowDestAddr, intSrvFlowBurst=intSrvFlowBurst, intSrvIfAttribFlows=intSrvIfAttribFlows, intSrvFlowTable=intSrvFlowTable, intSrvFlowEntry=intSrvFlowEntry, intSrvFlowSenderAddrLength=intSrvFlowSenderAddrLength, intSrvIfAttribGroup=intSrvIfAttribGroup, intSrvFlowInterface=intSrvFlowInterface, intSrvFlowDestAddrLength=intSrvFlowDestAddrLength, intSrvFlowDestPort=intSrvFlowDestPort, BurstSize=BurstSize, intSrvFlowStatus=intSrvFlowStatus, intSrvIfAttribMaxAllocatedBits=intSrvIfAttribMaxAllocatedBits, intSrvFlowNewIndex=intSrvFlowNewIndex, intSrvGroups=intSrvGroups, MessageSize=MessageSize, intSrvFlowRate=intSrvFlowRate, intSrvFlowPort=intSrvFlowPort, intSrvFlowIfAddr=intSrvFlowIfAddr, SessionType=SessionType, intSrvIfAttribTable=intSrvIfAttribTable, intSrvIfAttribPropagationDelay=intSrvIfAttribPropagationDelay, intSrvFlowService=intSrvFlowService, intSrvFlowsGroup=intSrvFlowsGroup, intSrvFlowWeight=intSrvFlowWeight, intSrvFlowMinTU=intSrvFlowMinTU, intSrvFlowProtocol=intSrvFlowProtocol, intSrvFlowOwner=intSrvFlowOwner, intSrvIfAttribEntry=intSrvIfAttribEntry, intSrvFlowSenderAddr=intSrvFlowSenderAddr, QosService=QosService, SessionNumber=SessionNumber, intSrvObjects=intSrvObjects, intSrvGenObjects=intSrvGenObjects, intSrvFlowFlowId=intSrvFlowFlowId, intSrvCompliances=intSrvCompliances, intSrv=intSrv, intSrvFlowNumber=intSrvFlowNumber, intSrvNotifications=intSrvNotifications, intSrvFlowQueue=intSrvFlowQueue, intSrvFlowBestEffort=intSrvFlowBestEffort, intSrvFlowType=intSrvFlowType, intSrvCompliance=intSrvCompliance, Port=Port, intSrvIfAttribStatus=intSrvIfAttribStatus, intSrvFlowPoliced=intSrvFlowPoliced, intSrvFlowDiscard=intSrvFlowDiscard, intSrvGenObjectsGroup=intSrvGenObjectsGroup, intSrvConformance=intSrvConformance)
