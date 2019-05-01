#
# PySNMP MIB module PTOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PTOPO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, TimeTicks, Counter64, Unsigned32, Integer32, mib_2, MibIdentifier, Bits, Gauge32, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter64", "Unsigned32", "Integer32", "mib-2", "MibIdentifier", "Bits", "Gauge32", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, TextualConvention, TimeStamp, RowStatus, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "TimeStamp", "RowStatus", "AutonomousType")
ptopoMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 79))
ptopoMIB.setRevisions(('2000-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ptopoMIB.setRevisionsDescriptions(('Initial Version of the Physical Topology MIB. This version published as RFC 2922.',))
if mibBuilder.loadTexts: ptopoMIB.setLastUpdated('200009210000Z')
if mibBuilder.loadTexts: ptopoMIB.setOrganization('IETF; PTOPOMIB Working Group')
if mibBuilder.loadTexts: ptopoMIB.setContactInfo('PTOPOMIB WG Discussion: ptopo@3com.com Subscription: majordomo@3com.com msg body: [un]subscribe ptopomib Andy Bierman Cisco Systems Inc. 170 West Tasman Drive San Jose, CA 95134 408-527-3711 abierman@cisco.com Kendall S. Jones Nortel Networks 4401 Great America Parkway Santa Clara, CA 95054 408-495-7356 kejones@nortelnetworks.com')
if mibBuilder.loadTexts: ptopoMIB.setDescription('The MIB module for physical topology information.')
ptopoMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1))
ptopoData = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1, 1))
ptopoGeneral = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1, 2))
ptopoConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1, 3))
class PtopoGenAddr(TextualConvention, OctetString):
    description = 'The value of an address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class PtopoChassisIdType(TextualConvention, Integer32):
    description = "This TC describes the source of a chassis identifier. The enumeration 'chasIdEntPhysicalAlias(1)' represents a chassis identifier based on the value of entPhysicalAlias for a chassis component (i.e., an entPhysicalClass value of 'chassis(3)'). The enumeration 'chasIdIfAlias(2)' represents a chassis identifier based on the value of ifAlias for an interface on the containing chassis. The enumeration 'chasIdPortEntPhysicalAlias(3)' represents a chassis identifier based on the value of entPhysicalAlias for a port or backplane component (i.e., entPhysicalClass value of 'port(10)' or 'backplane(4)'), within the containing chassis. The enumeration 'chasIdMacAddress(4)' represents a chassis identifier based on the value of a unicast source MAC address (encoded in network byte order and IEEE 802.3 canonical bit order), of a port on the containing chassis. The enumeration 'chasIdPtopoGenAddr(5)' represents a chassis identifier based on a network address, associated with a particular chassis. The encoded address is actually composed of two fields. The first field is a single octet, representing the IANA AddressFamilyNumbers value for the specific address type, and the second field is the PtopoGenAddr address value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("chasIdEntPhysicalAlias", 1), ("chasIdIfAlias", 2), ("chasIdPortEntPhysicalAlias", 3), ("chasIdMacAddress", 4), ("chasIdPtopoGenAddr", 5))

class PtopoChassisId(TextualConvention, OctetString):
    description = "This TC describes the format of a chassis identifier string. Objects of this type are always used with an associated PtopoChassisIdType object, which identifies the format of the particular PtopoChassisId object instance. If the associated PtopoChassisIdType object has a value of 'chasIdEntPhysicalAlias(1)', then the octet string identifies a particular instance of the entPhysicalAlias object for a chassis component (i.e., an entPhysicalClass value of 'chassis(3)'). If the associated PtopoChassisIdType object has a value of 'chasIdIfAlias(2)', then the octet string identifies a particular instance of the ifAlias object for an interface on the containing chassis. If the associated PtopoChassisIdType object has a value of 'chasIdPortEntPhysicalAlias(3)', then the octet string identifies a particular instance of the entPhysicalAlias object for a port or backplane component within the containing chassis. If the associated PtopoChassisIdType object has a value of 'chasIdMacAddress(4)', then this string identifies a particular unicast source MAC address (encoded in network byte order and IEEE 802.3 canonical bit order), of a port on the containing chassis. If the associated PtopoChassisIdType object has a value of 'chasIdPtopoGenAddr(5)', then this string identifies a particular network address, encoded in network byte order, associated with one or more ports on the containing chassis. The first octet contains the IANA Address Family Numbers enumeration value for the specific address type, and octets 2 through N contain the PtopoGenAddr address value in network byte order."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class PtopoPortIdType(TextualConvention, Integer32):
    description = "This TC describes the source of a particular type of port identifier used in the PTOPO MIB. The enumeration 'portIdIfAlias(1)' represents a port identifier based on the ifAlias MIB object. The enumeration 'portIdPortEntPhysicalAlias(2)' represents a port identifier based on the value of entPhysicalAlias for a port or backplane component (i.e., entPhysicalClass value of 'port(10)' or 'backplane(4)'), within the containing chassis. The enumeration 'portIdMacAddr(3)' represents a port identifier based on a unicast source MAC address, which has been detected by the agent and associated with a particular port. The enumeration 'portIdPtopoGenAddr(4)' represents a port identifier based on a network address, detected by the agent and associated with a particular port."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("portIdIfAlias", 1), ("portIdEntPhysicalAlias", 2), ("portIdMacAddr", 3), ("portIdPtopoGenAddr", 4))

class PtopoPortId(TextualConvention, OctetString):
    description = "This TC describes the format of a port identifier string. Objects of this type are always used with an associated PtopoPortIdType object, which identifies the format of the particular PtopoPortId object instance. If the associated PtopoPortIdType object has a value of 'portIdIfAlias(1)', then the octet string identifies a particular instance of the ifAlias object. If the associated PtopoPortIdType object has a value of 'portIdEntPhysicalAlias(2)', then the octet string identifies a particular instance of the entPhysicalAlias object for a port component (i.e., entPhysicalClass value of 'port(10)'). If the associated PtopoPortIdType object has a value of 'portIdMacAddr(3)', then this string identifies a particular unicast source MAC address associated with the port. If the associated PtopoPortIdType object has a value of 'portIdPtopoGenAddr(4)', then this string identifies a network address associated with the port. The first octet contains the IANA AddressFamilyNumbers enumeration value for the specific address type, and octets 2 through N contain the PtopoGenAddr address value in network byte order."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class PtopoAddrSeenState(TextualConvention, Integer32):
    description = "This TC describes the state of address detection for a particular type of port identifier used in the PTOPO MIB. The enumeration 'notUsed(1)' represents an entry for which the particular MIB object is not applicable to the remote connection endpoint, The enumeration 'unknown(2)' represents an entry for which the particular address collection state is not known. The enumeration 'oneAddr(3)' represents an entry for which exactly one source address (of the type indicated by the particular MIB object), has been detected. The enumeration 'multiAddr(4)' represents an entry for which more than one source address (of the type indicated by the particular MIB object), has been detected. An agent is expected to set the initial state of the PtopoAddrSeenState to 'notUsed(1)' or 'unknown(2)'. Note that the PTOPO MIB does not restrict or specify the means in which the PtopoAddrSeenState is known to an agent. In particular, an agent may detect this information through configuration data, or some means other than directly monitoring all port traffic."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notUsed", 1), ("unknown", 2), ("oneAddr", 3), ("multiAddr", 4))

ptopoConnTable = MibTable((1, 3, 6, 1, 2, 1, 79, 1, 1, 1), )
if mibBuilder.loadTexts: ptopoConnTable.setStatus('current')
if mibBuilder.loadTexts: ptopoConnTable.setDescription('This table contains one or more rows per physical network connection known to this agent. The agent may wish to ensure that only one ptopoConnEntry is present for each local port, or it may choose to maintain multiple ptopoConnEntries for the same local port. Entries based on lower numbered identifier types are preferred over higher numbered identifier types, i.e., lower values of the ptopoConnRemoteChassisType and ptopoConnRemotePortType objects.')
ptopoConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1), ).setIndexNames((0, "PTOPO-MIB", "ptopoConnTimeMark"), (0, "PTOPO-MIB", "ptopoConnLocalChassis"), (0, "PTOPO-MIB", "ptopoConnLocalPort"), (0, "PTOPO-MIB", "ptopoConnIndex"))
if mibBuilder.loadTexts: ptopoConnEntry.setStatus('current')
if mibBuilder.loadTexts: ptopoConnEntry.setDescription('Information about a particular physical network connection. Entries may be created and deleted in this table, either manually or by the agent, if a physical topology discovery process is active.')
ptopoConnTimeMark = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: ptopoConnTimeMark.setStatus('current')
if mibBuilder.loadTexts: ptopoConnTimeMark.setDescription('A TimeFilter for this entry. See the TimeFilter textual convention in RFC 2021 to see how this works.')
ptopoConnLocalChassis = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: ptopoConnLocalChassis.setStatus('current')
if mibBuilder.loadTexts: ptopoConnLocalChassis.setDescription('The entPhysicalIndex value used to identify the chassis component associated with the local connection endpoint.')
ptopoConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 3), PhysicalIndex())
if mibBuilder.loadTexts: ptopoConnLocalPort.setStatus('current')
if mibBuilder.loadTexts: ptopoConnLocalPort.setDescription('The entPhysicalIndex value used to identify the port component associated with the local connection endpoint.')
ptopoConnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ptopoConnIndex.setStatus('current')
if mibBuilder.loadTexts: ptopoConnIndex.setDescription('This object represents an arbitrary local integer value used by this agent to identify a particular connection instance, unique only for the indicated local connection endpoint. A particular ptopoConnIndex value may be reused in the event an entry is aged out and later re-learned with the same (or different) remote chassis and port identifiers. An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot. It is considered unlikely that the ptopoConnIndex will wrap between reboots.')
ptopoConnRemoteChassisType = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 5), PtopoChassisIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemoteChassisType.setStatus('current')
if mibBuilder.loadTexts: ptopoConnRemoteChassisType.setDescription('The type of encoding used to identify the chassis associated with the remote connection endpoint. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).')
ptopoConnRemoteChassis = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 6), PtopoChassisId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemoteChassis.setStatus('current')
if mibBuilder.loadTexts: ptopoConnRemoteChassis.setDescription('The string value used to identify the chassis component associated with the remote connection endpoint. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).')
ptopoConnRemotePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 7), PtopoPortIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemotePortType.setStatus('current')
if mibBuilder.loadTexts: ptopoConnRemotePortType.setDescription("The type of port identifier encoding used in the associated 'ptopoConnRemotePort' object. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).")
ptopoConnRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 8), PtopoPortId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemotePort.setStatus('current')
if mibBuilder.loadTexts: ptopoConnRemotePort.setDescription('The string value used to identify the port component associated with the remote connection endpoint. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).')
ptopoConnDiscAlgorithm = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 9), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnDiscAlgorithm.setStatus('current')
if mibBuilder.loadTexts: ptopoConnDiscAlgorithm.setDescription('An indication of the algorithm used to discover the information contained in this conceptual row. A value of ptopoDiscoveryLocal indicates this entry was configured by the local agent, without use of a discovery protocol. A value of { 0 0 } indicates this entry was created manually by an NMS via the associated RowStatus object. ')
ptopoConnAgentNetAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 10), AddressFamilyNumbers()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnAgentNetAddrType.setStatus('current')
if mibBuilder.loadTexts: ptopoConnAgentNetAddrType.setDescription('This network address type of the associated ptopoConnNetAddr object, unless that object contains a zero length string. In such a case, an NMS application should ignore any returned value for this object. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).')
ptopoConnAgentNetAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 11), PtopoGenAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnAgentNetAddr.setStatus('current')
if mibBuilder.loadTexts: ptopoConnAgentNetAddr.setDescription("This object identifies a network address which may be used to reach an SNMP agent entity containing information for the chassis and port components represented by the associated 'ptopoConnRemoteChassis' and 'ptopoConnRemotePort' objects. If no such address is known, then this object shall contain an empty string. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).")
ptopoConnMultiMacSASeen = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 12), PtopoAddrSeenState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnMultiMacSASeen.setStatus('current')
if mibBuilder.loadTexts: ptopoConnMultiMacSASeen.setDescription("This object indicates if multiple unicast source MAC addresses have been detected by the agent from the remote connection endpoint, since the creation of this entry. If this entry has an associated ptopoConnRemoteChassisType and/or ptopoConnRemotePortType value other than 'portIdMacAddr(3)', then the value 'notUsed(1)' is returned. Otherwise, one of the following conditions must be true: If the agent has not yet detected any unicast source MAC addresses from the remote port, then the value 'unknown(2)' is returned. If the agent has detected exactly one unicast source MAC address from the remote port, then the value 'oneAddr(3)' is returned. If the agent has detected more than one unicast source MAC address from the remote port, then the value 'multiAddr(4)' is returned.")
ptopoConnMultiNetSASeen = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 13), PtopoAddrSeenState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnMultiNetSASeen.setStatus('current')
if mibBuilder.loadTexts: ptopoConnMultiNetSASeen.setDescription("This object indicates if multiple network layer source addresses have been detected by the agent from the remote connection endpoint, since the creation of this entry. If this entry has an associated ptopoConnRemoteChassisType or ptopoConnRemotePortType value other than 'portIdGenAddr(4)' then the value 'notUsed(1)' is returned. Otherwise, one of the following conditions must be true: If the agent has not yet detected any network source addresses of the appropriate type from the remote port, then the value 'unknown(2)' is returned. If the agent has detected exactly one network source address of the appropriate type from the remote port, then the value 'oneAddr(3)' is returned. If the agent has detected more than one network source address (of the same appropriate type) from the remote port, this the value 'multiAddr(4)' is returned.")
ptopoConnIsStatic = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnIsStatic.setStatus('current')
if mibBuilder.loadTexts: ptopoConnIsStatic.setDescription("This object identifies static ptopoConnEntries. If this object has the value 'true(1)', then this entry is not subject to any age-out mechanisms implemented by the agent. If this object has the value 'false(2)', then this entry is subject to all age-out mechanisms implemented by the agent. This object may not be modified if the associated ptopoConnRowStatus object has a value of active(1).")
ptopoConnLastVerifyTime = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnLastVerifyTime.setStatus('current')
if mibBuilder.loadTexts: ptopoConnLastVerifyTime.setDescription("If the associated value of ptopoConnIsStatic is equal to 'false(2)', then this object contains the value of sysUpTime at the time the conceptual row was last verified by the agent, e.g., via reception of a topology protocol message, pertaining to the associated remote chassis and port. If the associated value of ptopoConnIsStatic is equal to 'true(1)', then this object shall contain the value of sysUpTime at the time this entry was last activated (i.e., ptopoConnRowStatus set to 'active(1)').")
ptopoConnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRowStatus.setStatus('current')
if mibBuilder.loadTexts: ptopoConnRowStatus.setDescription('The status of this conceptual row.')
ptopoLastChangeTime = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoLastChangeTime.setStatus('current')
if mibBuilder.loadTexts: ptopoLastChangeTime.setDescription('The value of sysUpTime at the time a conceptual row is created, modified, or deleted in the ptopoConnTable. An NMS can use this object to reduce polling of the ptopoData group objects.')
ptopoConnTabInserts = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 2), Counter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabInserts.setStatus('current')
if mibBuilder.loadTexts: ptopoConnTabInserts.setDescription('The number of times an entry has been inserted into the ptopoConnTable.')
ptopoConnTabDeletes = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 3), Counter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabDeletes.setStatus('current')
if mibBuilder.loadTexts: ptopoConnTabDeletes.setDescription('The number of times an entry has been deleted from the ptopoConnTable.')
ptopoConnTabDrops = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 4), Counter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabDrops.setStatus('current')
if mibBuilder.loadTexts: ptopoConnTabDrops.setDescription('The number of times an entry would have been added to the ptopoConnTable, (e.g., via information learned from a topology protocol), but was not because of insufficient resources.')
ptopoConnTabAgeouts = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabAgeouts.setStatus('current')
if mibBuilder.loadTexts: ptopoConnTabAgeouts.setDescription('The number of times an entry has been deleted from the ptopoConnTable because the information timeliness interval for that entry has expired.')
ptopoConfigTrapInterval = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 3600), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptopoConfigTrapInterval.setStatus('current')
if mibBuilder.loadTexts: ptopoConfigTrapInterval.setDescription("This object controls the transmission of PTOPO notifications. If this object has a value of zero, then no ptopoConfigChange notifications will be transmitted by the agent. If this object has a non-zero value, then the agent must not generate more than one ptopoConfigChange trap-event in the indicated period, where a 'trap-event' is the transmission of a single notification PDU type to a list of notification destinations. If additional configuration changes occur within the indicated throttling period, then these trap- events must be suppressed by the agent. An NMS should periodically check the value of ptopoLastChangeTime to detect any missed ptopoConfigChange trap-events, e.g. due to throttling or transmission loss. If notification transmission is enabled, the suggested default throttling period is 60 seconds, but transmission should be disabled by default. If the agent is capable of storing non-volatile configuration, then the value of this object must be restored after a re-initialization of the management system.")
ptopoConfigMaxHoldTime = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptopoConfigMaxHoldTime.setStatus('current')
if mibBuilder.loadTexts: ptopoConfigMaxHoldTime.setDescription("This object specifies the desired time interval for which an agent will maintain dynamic ptopoConnEntries. After the specified number of seconds since the last time an entry was verified, in the absence of new verification (e.g., receipt of a topology protocol message), the agent shall remove the entry. Note that entries may not always be removed immediately, but may possibly be removed at periodic garbage collection intervals. This object only affects dynamic ptopoConnEntries, i.e. for which ptopoConnIsStatic equals 'false(2)'. Static entries are not aged out. Note that dynamic ptopoConnEntries may also be removed by the agent due to the expired timeliness of learned topology information (e.g., timeliness interval for a remote port expires). The actual age-out interval for a given entry is defined by the following formula: age-out-time = min(ptopoConfigMaxHoldTime, <entry-specific hold-time>) where <entry-specific hold-time> is determined by the discovery algorithm, and may be different for each entry.")
ptopoMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 2))
ptopoMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 2, 0))
ptopoConfigChange = NotificationType((1, 3, 6, 1, 2, 1, 79, 2, 0, 1)).setObjects(("PTOPO-MIB", "ptopoConnTabInserts"), ("PTOPO-MIB", "ptopoConnTabDeletes"), ("PTOPO-MIB", "ptopoConnTabDrops"), ("PTOPO-MIB", "ptopoConnTabAgeouts"))
if mibBuilder.loadTexts: ptopoConfigChange.setStatus('current')
if mibBuilder.loadTexts: ptopoConfigChange.setDescription("A ptopoConfigChange notification is sent when the value of ptopoLastChangeTime changes. It can be utilized by an NMS to trigger physical topology table maintenance polls. Note that transmission of ptopoConfigChange notifications are throttled by the agent, as specified by the 'ptopoConfigTrapInterval' object.")
ptopoRegistrationPoints = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 3))
ptopoDiscoveryMechanisms = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 3, 1))
ptopoDiscoveryLocal = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 3, 1, 1))
ptopoConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 4))
ptopoCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 4, 1))
ptopoGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 4, 2))
ptopoCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 79, 4, 1, 1)).setObjects(("PTOPO-MIB", "ptopoDataGroup"), ("PTOPO-MIB", "ptopoGeneralGroup"), ("PTOPO-MIB", "ptopoConfigGroup"), ("PTOPO-MIB", "ptopoNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoCompliance = ptopoCompliance.setStatus('current')
if mibBuilder.loadTexts: ptopoCompliance.setDescription('The compliance statement for SNMP entities which implement the PTOPO MIB.')
ptopoDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 1)).setObjects(("PTOPO-MIB", "ptopoConnRemoteChassisType"), ("PTOPO-MIB", "ptopoConnRemoteChassis"), ("PTOPO-MIB", "ptopoConnRemotePortType"), ("PTOPO-MIB", "ptopoConnRemotePort"), ("PTOPO-MIB", "ptopoConnDiscAlgorithm"), ("PTOPO-MIB", "ptopoConnAgentNetAddrType"), ("PTOPO-MIB", "ptopoConnAgentNetAddr"), ("PTOPO-MIB", "ptopoConnMultiMacSASeen"), ("PTOPO-MIB", "ptopoConnMultiNetSASeen"), ("PTOPO-MIB", "ptopoConnIsStatic"), ("PTOPO-MIB", "ptopoConnLastVerifyTime"), ("PTOPO-MIB", "ptopoConnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoDataGroup = ptopoDataGroup.setStatus('current')
if mibBuilder.loadTexts: ptopoDataGroup.setDescription('The collection of objects which are used to represent physical topology information for which a single agent provides management information. This group is mandatory for all implementations of the PTOPO MIB.')
ptopoGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 2)).setObjects(("PTOPO-MIB", "ptopoLastChangeTime"), ("PTOPO-MIB", "ptopoConnTabInserts"), ("PTOPO-MIB", "ptopoConnTabDeletes"), ("PTOPO-MIB", "ptopoConnTabDrops"), ("PTOPO-MIB", "ptopoConnTabAgeouts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoGeneralGroup = ptopoGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: ptopoGeneralGroup.setDescription('The collection of objects which are used to report the general status of the PTOPO MIB implementation. This group is mandatory for all agents which implement the PTOPO MIB.')
ptopoConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 3)).setObjects(("PTOPO-MIB", "ptopoConfigTrapInterval"), ("PTOPO-MIB", "ptopoConfigMaxHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoConfigGroup = ptopoConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ptopoConfigGroup.setDescription('The collection of objects which are used to configure the PTOPO MIB implementation behavior. This group is mandatory for agents which implement the PTOPO MIB.')
ptopoNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 4)).setObjects(("PTOPO-MIB", "ptopoConfigChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoNotificationsGroup = ptopoNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ptopoNotificationsGroup.setDescription('The collection of notifications used to indicate PTOPO MIB data consistency and general status information. This group is mandatory for agents which implement the PTOPO MIB.')
mibBuilder.exportSymbols("PTOPO-MIB", ptopoConnMultiNetSASeen=ptopoConnMultiNetSASeen, ptopoConformance=ptopoConformance, ptopoNotificationsGroup=ptopoNotificationsGroup, ptopoConfigChange=ptopoConfigChange, ptopoLastChangeTime=ptopoLastChangeTime, ptopoConnEntry=ptopoConnEntry, ptopoGeneral=ptopoGeneral, ptopoMIBNotifications=ptopoMIBNotifications, PtopoPortId=PtopoPortId, PYSNMP_MODULE_ID=ptopoMIB, ptopoConnRemoteChassisType=ptopoConnRemoteChassisType, ptopoMIB=ptopoMIB, PtopoChassisIdType=PtopoChassisIdType, ptopoConnAgentNetAddrType=ptopoConnAgentNetAddrType, ptopoConfigTrapInterval=ptopoConfigTrapInterval, ptopoGeneralGroup=ptopoGeneralGroup, ptopoMIBObjects=ptopoMIBObjects, ptopoConnTabDrops=ptopoConnTabDrops, ptopoConnRowStatus=ptopoConnRowStatus, ptopoConfigGroup=ptopoConfigGroup, PtopoGenAddr=PtopoGenAddr, ptopoData=ptopoData, PtopoAddrSeenState=PtopoAddrSeenState, ptopoConnRemotePort=ptopoConnRemotePort, ptopoConnDiscAlgorithm=ptopoConnDiscAlgorithm, ptopoConnMultiMacSASeen=ptopoConnMultiMacSASeen, ptopoConnRemoteChassis=ptopoConnRemoteChassis, PtopoPortIdType=PtopoPortIdType, ptopoMIBTrapPrefix=ptopoMIBTrapPrefix, ptopoConnLocalPort=ptopoConnLocalPort, ptopoConnIsStatic=ptopoConnIsStatic, ptopoConnLocalChassis=ptopoConnLocalChassis, ptopoConnLastVerifyTime=ptopoConnLastVerifyTime, ptopoGroups=ptopoGroups, ptopoRegistrationPoints=ptopoRegistrationPoints, ptopoConnRemotePortType=ptopoConnRemotePortType, ptopoDiscoveryLocal=ptopoDiscoveryLocal, ptopoCompliances=ptopoCompliances, ptopoConnTimeMark=ptopoConnTimeMark, ptopoConnAgentNetAddr=ptopoConnAgentNetAddr, ptopoConnTable=ptopoConnTable, ptopoConfigMaxHoldTime=ptopoConfigMaxHoldTime, ptopoConnTabAgeouts=ptopoConnTabAgeouts, ptopoCompliance=ptopoCompliance, ptopoConfig=ptopoConfig, ptopoConnTabDeletes=ptopoConnTabDeletes, PtopoChassisId=PtopoChassisId, ptopoDiscoveryMechanisms=ptopoDiscoveryMechanisms, ptopoConnIndex=ptopoConnIndex, ptopoConnTabInserts=ptopoConnTabInserts, ptopoDataGroup=ptopoDataGroup)
