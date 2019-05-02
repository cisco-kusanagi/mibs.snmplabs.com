#
# PySNMP MIB module CISCO-VOICE-CONNECTIVITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-CONNECTIVITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, ModuleIdentity, ObjectIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter64, TimeTicks, Unsigned32, Gauge32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter64", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "Integer32")
TruthValue, DateAndTime, MacAddress, DisplayString, TextualConvention, RowPointer, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "MacAddress", "DisplayString", "TextualConvention", "RowPointer", "AutonomousType")
ciscoVoiceConnectivityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 393))
ciscoVoiceConnectivityMIB.setRevisions(('2005-09-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setLastUpdated('200509130000Z')
if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-itm@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setDescription("This MIB module provides connectivity related information for devices (e.g., 'connectivity between voice gateway, phones, gatekeepers and call processing agent'). The MIB can be used by network management applications to collect the information regarding voice connectivity among the devices in the network. The MIB can also be used to retrieve the status of voice connectivity between the devices. *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS *** SCCP - Skinny Client Control Protocol SGCP - Simple Gateway Control Protocol MGCP - Media Gateway Control Protocol H323 - H.323 protocol SIP - Session Initiation Protocol *** DEFINITIONS *** CALL AGENT A call processing agent component of a device in IP telephony and VoIP network. PORT A port on the device that is associated with call processing agent. REGISTRATION In an IP telephony network, there are typically keep- alive messages or expected registration refresh timers that are used to formulate the registration status of devices and/or users. Possible values of the registration status are as follows: registered: The port has successfully registered with the call agent unregistered: The port is no longer registered with the call agent rejected: Registration request from the port was rejected by the call agent.")
ciscoVoiceConnectivityMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 0))
ciscoVoiceConnectivityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1))
ciscoVoiceConnectivityMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 2))
cvcCallAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1))
cvcPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2))
cvcCallAgentConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3))
cvcNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 4))
cvcCallAgentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1), )
if mibBuilder.loadTexts: cvcCallAgentTable.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentTable.setDescription('This table contains information about call agents. When the network management subsystem implements this MIB, this table lists the call agents that exist in this system. This table will contain one entry per call agent. When systems other than those hosting call agents implement this MIB, this table will contain the list of call agents to which ports of this system are associated. The entries would be representative of remote call agents. For example, if a device is a voice gateway having a T1 port associated with three call processing agents, then this table will have three entries representing each of the three call processing agents. The network management subsystem adds conceptual rows to this table for every call agent.')
cvcCallAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentIndex"))
if mibBuilder.loadTexts: cvcCallAgentEntry.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentEntry.setDescription("An entry (conceptual row) in the cvcCallAgent table, providing associated call agent information such as call agent's IP address and its type.")
cvcCallAgentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cvcCallAgentIndex.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentIndex.setDescription('An arbitrary integer, a unique value for each call agent associated with the device.')
cvcCallAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentName.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentName.setDescription('This object indicates name of the call agent given by call agent administrator.')
cvcCallAgentInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentInetAddressType.setReference('RFC 3291, section 3')
if mibBuilder.loadTexts: cvcCallAgentInetAddressType.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentInetAddressType.setDescription('This object reflects a particular type of internet address and provides the context for interpreting one or more address objects elsewhere in this MIB module.')
cvcCallAgentInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentInetAddress.setReference('RFC 3291, section 3')
if mibBuilder.loadTexts: cvcCallAgentInetAddress.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentInetAddress.setDescription('This object indicates the IP address of the call agent. The type of internet address is indicated by the value of cvcCallAgentInetAddressType.')
cvcCallAgentType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 5), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentType.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentType.setDescription('This object indicates the type of call agent. A list of call agent types can be found in the CISCO-VOICE-APPLICATIONS-OID-MIB.')
cvcPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1), )
if mibBuilder.loadTexts: cvcPortTable.setStatus('current')
if mibBuilder.loadTexts: cvcPortTable.setDescription('This table contains information about ports. When the network management subsystem implements this MIB, this table lists all the ports associated with the call agents listed in cvcCallAgentTable. When systems other than those hosting call agents implement this MIB, this table will contain information of all the ports of the system,associated with the call agents listed in cvcCallAgentTable. The network management subsystem adds conceptual rows to this table for every port associated to call agent.')
cvcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortIndex"))
if mibBuilder.loadTexts: cvcPortEntry.setStatus('current')
if mibBuilder.loadTexts: cvcPortEntry.setDescription('An entry (conceptual row) in the port table, providing the port or interface information such as name, IP address, type, MAC address, type of the device containing this port and protocol used by the port.')
cvcPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cvcPortIndex.setStatus('current')
if mibBuilder.loadTexts: cvcPortIndex.setDescription('An arbitrary integer value uniquely identifying each physical or virtual port of the device associated with call agent.')
cvcPortAssociation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortAssociation.setStatus('current')
if mibBuilder.loadTexts: cvcPortAssociation.setDescription("An association to conceptual row of the port define within another MIB group. This can be used to get more information about the port defined in other MIB group. For example, to get more information about the T1 port defined in this table, this attribute points to a row in ifTable for that T1 port, e.g value for this attribute will be 'ifIndex.5'.")
cvcPortDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortDeviceName.setStatus('current')
if mibBuilder.loadTexts: cvcPortDeviceName.setDescription('The device name under which this port has been registered with call agent. This is a mandatory field that represents the port.')
cvcPortInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortInetAddressType.setReference('RFC 3291, section 3')
if mibBuilder.loadTexts: cvcPortInetAddressType.setStatus('current')
if mibBuilder.loadTexts: cvcPortInetAddressType.setDescription('This object reflects a particular type of internet address and provides the context for interpreting one or more address objects elsewhere in this MIB module.')
cvcPortInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortInetAddress.setReference('RFC 3291, section 3')
if mibBuilder.loadTexts: cvcPortInetAddress.setStatus('current')
if mibBuilder.loadTexts: cvcPortInetAddress.setDescription('This object indicates the IP address of the port. The type of internet address is indicated bythe value of cvcPortInetAddressType.')
cvcPortMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortMACAddress.setStatus('current')
if mibBuilder.loadTexts: cvcPortMACAddress.setDescription('This object indicates the MAC address of the port. For ports which do not have such an address, this object should contain an octet string of zero length.')
cvcPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 7), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortType.setStatus('current')
if mibBuilder.loadTexts: cvcPortType.setDescription('The type of port. Additional values for cvcPortType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention. If the port type is not defined in IANAifType, then value of this object will be other(1). In this case, port type can be identified either by productCategory or by referring to other MIB pointed by cvcPortAssociation.')
cvcProductCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("phone", 1), ("gateway", 2), ("h323Device", 3), ("ctiDevice", 4), ("voiceMailDevice", 5), ("mediaResourceDevice", 6), ("huntListDevice", 7), ("sipDevice", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcProductCategory.setStatus('current')
if mibBuilder.loadTexts: cvcProductCategory.setDescription('This object indicates type of the device that contains the port.')
cvcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sccp", 1), ("sgcp", 2), ("mgcp", 3), ("h323", 4), ("sip", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcProtocol.setReference("RFC 3435 on Media Gateway Control Protocol (MGCP) Version 1.0 RFC 3261 - SIP: Session Initiation Protocol ITU-T Recommendation H.323v.4,'Packet-based multimedia communications systems', November 2000.")
if mibBuilder.loadTexts: cvcProtocol.setStatus('current')
if mibBuilder.loadTexts: cvcProtocol.setDescription(' Protocol the port use for communication to its associated device.')
cvcVirtualInterfaceDN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcVirtualInterfaceDN.setStatus('current')
if mibBuilder.loadTexts: cvcVirtualInterfaceDN.setDescription('This attribute indicates directory number of the port. This attribute is applicable only to virtual or logical interface that is associated with call agent.')
cvcCallAgentConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1), )
if mibBuilder.loadTexts: cvcCallAgentConnectionTable.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentConnectionTable.setDescription('This table contains current registration status information for all the ports, listed in cvcPortTable, that are associated with the call agents listed cvcCallAgentTable. The network management subsystem adds a conceptual row to this table per port and its associated call agent pair. Entries in this table depends on entries in cvcPortTable and cvcCallAgentTable. Deletion of any entry in those other two table will result in deletion of corresponding entry in this table.')
cvcCallAgentConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortIndex"), (0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentIndex"))
if mibBuilder.loadTexts: cvcCallAgentConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentConnectionEntry.setDescription("An entry (conceptual row) in the cvcCallAgentConnectionTable, containing the information about a port or interface's registration status to call agents.")
cvcCallAgentPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentPriority.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentPriority.setDescription("A port can be associated with multiple call agents. In case of failure of the call agent to which the port has been registered, port falls back to the back-up call agent. To achieve this redundancy each call agent is assigned a priority number in context of port. This object indicates the call agent's priority number.")
cvcRegistrationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("notapplicable", 2), ("registered", 3), ("unregistered", 4), ("rejected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcRegistrationStatus.setStatus('current')
if mibBuilder.loadTexts: cvcRegistrationStatus.setDescription('This syntax is used to identify the registration status of the port with call agent. unknown: The registration status of the port is unknown. notapplicable: The registration status of the port is not applicable registered: The port has successfully registered with the call agent unregistered: The port is no longer registered with the call agent rejected: Registration request from the port was rejected by the call agent.')
cvcStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noError", 1), ("unknown", 2), ("configurationError", 3), ("deviceNameUnresolveable", 4), ("maxDevRegReached", 5), ("connectivityError", 6), ("initializationError", 7), ("deviceReset", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcStatusReason.setStatus('current')
if mibBuilder.loadTexts: cvcStatusReason.setDescription('This syntax is used as means of identifying the reasons for a device registration error. Following are possible reason of registration status value. noError: No Error unknown: Unknown error cause configurationError: Device configuration error deviceNameUnresolveable: Unable to resolve the device name to an IP address maxDevRegReached: Maximum number of device registration have been reached connectivityError: Call agent is unable to establish communication with the device during registration initializationError: An error occurred during initialization of the device deviceReset: Indicates that the error was due to device reset.')
cvcLastStatusChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcLastStatusChangeTime.setStatus('current')
if mibBuilder.loadTexts: cvcLastStatusChangeTime.setDescription('The time registration status of the port changed.')
cvcLastRegisteredTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcLastRegisteredTime.setStatus('current')
if mibBuilder.loadTexts: cvcLastRegisteredTime.setDescription('The time the port last registered with the call agent.')
cvcNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvcNotifEnable.setStatus('current')
if mibBuilder.loadTexts: cvcNotifEnable.setDescription('This variable indicates whether the system generates notifications defined in this MIB. A false value will prevent all the notifications from being generated by this system.')
cvcPortRegistrationStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 393, 0, 1)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortDeviceName"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentPriority"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcRegistrationStatus"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcStatusReason"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastStatusChangeTime"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastRegisteredTime"))
if mibBuilder.loadTexts: cvcPortRegistrationStatusChange.setStatus('current')
if mibBuilder.loadTexts: cvcPortRegistrationStatusChange.setDescription('A cvcPortRegistrationStatusChange notification is generated when the value of cvcRegistrationStatus changes. It can be utilized by an NMS to get current registration status change information. cvcPortDeviceName and cvcCallAgentInetAddress can be used by NMS to get information about the port and call agent from cvcPortTable and cvcCallAgentTable respectively. An NMS should periodically check the value of cvcLastStatusChangeTime to detect any missed cvcPortRegistrationStatusChange notification-events due to network problem or any other problem.')
cvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 1))
cvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2))
cvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 1, 1)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentConnectionGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotifGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcMIBCompliance = cvcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvcMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-VOICE-CONNECTIVITY-MIB.')
cvcCallAgentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 1)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentName"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddressType"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcCallAgentGroup = cvcCallAgentGroup.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentGroup.setDescription('A collection of objects which provide info like IP address and HostName about all call agents to which the ports are configured to register. Also it has call agent type.')
cvcPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 2)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortAssociation"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortDeviceName"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortInetAddressType"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortInetAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortMACAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortType"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcProductCategory"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcProtocol"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcVirtualInterfaceDN"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcPortGroup = cvcPortGroup.setStatus('current')
if mibBuilder.loadTexts: cvcPortGroup.setDescription('A collection of objects which provide info about all port/ interface of the device that are configured to register to call agents. Not all objects are applicable to all type of ports or interface. For example some port does not have MACAddress in that case cvcPortMACAddress need not have to be populated. Similarly for some device cvcPortAssociation is not applicable for example phone, in that case cvcPortAssociation object will not be populated but DeviceName, MCAAddress and IPAddress will be populated.')
cvcCallAgentConnectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 3)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentPriority"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcRegistrationStatus"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcStatusReason"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastStatusChangeTime"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastRegisteredTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcCallAgentConnectionGroup = cvcCallAgentConnectionGroup.setStatus('current')
if mibBuilder.loadTexts: cvcCallAgentConnectionGroup.setDescription('A collection of objects which provides registration status information for the port to the call agents defined in cvcPortTable and cvcCallAgentTable. This also provides information about the reason why registration is failed or rejected. It provides last time when status changes and last registered time. In some cases, registration status is not applicable for example H.323 gateway association with call agent, in that case most of these object will not be populated except cvcCallAgentPriority which can be used to find association of port with call agent.')
cvcNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 4)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcNotifGroup = cvcNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cvcNotifGroup.setDescription('A collection of objects which provide info about all the notifications generated by the device that implement this MIB. Implementation of this group is optional.')
cvcNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 5)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortRegistrationStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcNotificationsGroup = cvcNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: cvcNotificationsGroup.setDescription('A collection of notifications that are generated by CISCO-VOICE-CONNECTIVITY-MIB. This is important information when some management application decide not to poll but only rely on notification. Implementation of this group is optional.')
mibBuilder.exportSymbols("CISCO-VOICE-CONNECTIVITY-MIB", cvcPortRegistrationStatusChange=cvcPortRegistrationStatusChange, cvcProductCategory=cvcProductCategory, cvcCallAgentInetAddressType=cvcCallAgentInetAddressType, ciscoVoiceConnectivityMIB=ciscoVoiceConnectivityMIB, ciscoVoiceConnectivityMIBConform=ciscoVoiceConnectivityMIBConform, cvcCallAgentType=cvcCallAgentType, cvcCallAgent=cvcCallAgent, cvcLastRegisteredTime=cvcLastRegisteredTime, cvcPortMACAddress=cvcPortMACAddress, cvcCallAgentConnectionEntry=cvcCallAgentConnectionEntry, cvcNotif=cvcNotif, cvcCallAgentInetAddress=cvcCallAgentInetAddress, cvcRegistrationStatus=cvcRegistrationStatus, cvcPortEntry=cvcPortEntry, cvcMIBCompliances=cvcMIBCompliances, cvcCallAgentConnectionTable=cvcCallAgentConnectionTable, cvcCallAgentPriority=cvcCallAgentPriority, cvcCallAgentConnection=cvcCallAgentConnection, cvcPortAssociation=cvcPortAssociation, cvcPortIndex=cvcPortIndex, ciscoVoiceConnectivityMIBNotifs=ciscoVoiceConnectivityMIBNotifs, cvcPort=cvcPort, cvcCallAgentName=cvcCallAgentName, ciscoVoiceConnectivityMIBObjects=ciscoVoiceConnectivityMIBObjects, cvcNotifEnable=cvcNotifEnable, cvcPortInetAddressType=cvcPortInetAddressType, cvcCallAgentConnectionGroup=cvcCallAgentConnectionGroup, cvcPortType=cvcPortType, cvcCallAgentEntry=cvcCallAgentEntry, cvcNotificationsGroup=cvcNotificationsGroup, PYSNMP_MODULE_ID=ciscoVoiceConnectivityMIB, cvcPortInetAddress=cvcPortInetAddress, cvcCallAgentGroup=cvcCallAgentGroup, cvcMIBGroups=cvcMIBGroups, cvcStatusReason=cvcStatusReason, cvcLastStatusChangeTime=cvcLastStatusChangeTime, cvcPortGroup=cvcPortGroup, cvcVirtualInterfaceDN=cvcVirtualInterfaceDN, cvcNotifGroup=cvcNotifGroup, cvcMIBCompliance=cvcMIBCompliance, cvcCallAgentIndex=cvcCallAgentIndex, cvcProtocol=cvcProtocol, cvcPortDeviceName=cvcPortDeviceName, cvcCallAgentTable=cvcCallAgentTable, cvcPortTable=cvcPortTable)
