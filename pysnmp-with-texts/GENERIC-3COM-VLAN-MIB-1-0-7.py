#
# PySNMP MIB module GENERIC-3COM-VLAN-MIB-1-0-7 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GENERIC-3COM-VLAN-MIB-1-0-7
# Produced by pysmi-0.3.4 at Wed May  1 11:09:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Integer32, ObjectIdentity, Counter64, IpAddress, MibIdentifier, iso, ModuleIdentity, Unsigned32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Integer32", "ObjectIdentity", "Counter64", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity", "Unsigned32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
generic = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10))
genExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1))
genVirtual = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14))
a3ComVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1))
a3ComVlanProtocolsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2))
a3ComVirtualGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3))
a3ComEncapsulationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4))
class A3ComVlanType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("vlanLayer2", 1), ("vlanUnspecifiedProtocols", 2), ("vlanIPProtocol", 3), ("vlanIPXProtocol", 4), ("vlanAppleTalkProtocol", 5), ("vlanXNSProtocol", 6), ("vlanISOProtocol", 7), ("vlanDECNetProtocol", 8), ("vlanNetBIOSProtocol", 9), ("vlanSNAProtocol", 10), ("vlanVINESProtocol", 11), ("vlanX25Protocol", 12), ("vlanIGMPProtocol", 13), ("vlanSessionLayer", 14), ("vlanNetBeui", 15), ("vlanLayeredProtocols", 16), ("vlanIPXIIProtocol", 17), ("vlanIPX8022Protocol", 18), ("vlanIPX8023Protocol", 19), ("vlanIPX8022SNAPProtocol", 20))

class A3ComVlanLayer3Type(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("vlanIPProtocol", 1), ("vlanIPXProtocol", 2), ("vlanAppleTalkProtocol", 3), ("vlanXNSProtocol", 4), ("vlanSNAProtocol", 5), ("vlanDECNetProtocol", 6), ("vlanNetBIOSProtocol", 7), ("vlanVINESProtocol", 8), ("vlanX25Protocol", 9), ("vlanIPXIIProtocol", 10), ("vlanIPX8022Protocol", 11), ("vlanIPX8023Protocol", 12), ("vlanIPX8022SNAPProtocol", 13))

class A3ComVlanModeType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vlanUseDefault", 1), ("vlanOpen", 2), ("vlanClosed", 3))

a3ComVlanGlobalMappingTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1), )
if mibBuilder.loadTexts: a3ComVlanGlobalMappingTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingTable.setDescription('This table lists VLAN interfaces that are globally identified. A single entry exists in this list for each VLAN interface in the system that is bound to a global identifier.')
a3ComVlanGlobalMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanGlobalMappingIdentifier"))
if mibBuilder.loadTexts: a3ComVlanGlobalMappingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingEntry.setDescription('An individual VLAN interface global mapping entry. Entries in this table are created by setting the a3ComVlanIfGlobalIdentifier object in the a3ComVlanIfTable to a non-zero value.')
a3ComVlanGlobalMappingIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIdentifier.setDescription('An index into the a3ComVlanGlobalMappingTable and an administratively assigned global VLAN identifier. The value of this object globally identifies the VLAN interface. For VLAN interfaces, on different network devices, which are part of the same globally identified VLAN, the value of this object will be the same.')
a3ComVlanGlobalMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIfIndex.setDescription('The value of a3ComVlanIfIndex for the VLAN interface in the a3ComVlanIfTable, which is bound to the global identifier specified by this entry.')
a3ComVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2), )
if mibBuilder.loadTexts: a3ComVlanIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfTable.setDescription('This table lists VLAN interfaces that exist within a device. A single entry exists in this list for each VLAN interface in the system. A VLAN interface may be created, destroyed and/or mapped to a globally identified vlan.')
a3ComVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComVlanIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfEntry.setDescription('An individual VLAN interface entry. When an NMS wishes to create a new entry in this table, it must obtain a non-zero index from the a3ComNextAvailableVirtIfIndex object. Row creation in this table will fail if the chosen index value does not match the current value returned from the a3ComNextAvailableVirtIfIndex object.')
a3ComVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: a3ComVlanIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfIndex.setDescription("The index value of this row and the vlan's ifIndex in the ifTable. The NMS obtains the index value for this row by reading the a3ComNextAvailableVirtIfIndex object.")
a3ComVlanIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfDescr.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfDescr.setDescription('This is a description of the VLAN interface.')
a3ComVlanIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 3), A3ComVlanType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfType.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfType.setDescription('The VLAN interface type.')
a3ComVlanIfGlobalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfGlobalIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfGlobalIdentifier.setDescription('An administratively assigned global VLAN identifier. For VLAN interfaces, on different network devices, which are part of the same globally identified VLAN, the value of this object will be the same. The binding between a global identifier and a VLAN interface can be created or removed. To create a binding an NMS must write a non-zero value to this object. To delete a binding, the NMS must write a zero to this object.')
a3ComVlanIfInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanIfInfo.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfInfo.setDescription('A TLV encoded information string for the VLAN interface. The information contained within this string corresponds to VLAN information not contained within this table, but contained elsewhere within this MIB module. The purpose of this string is to provide an NMS with a quick read mechanism of all related VLAN interface information. The encoding rules are defined according to: tag = 2 bytes length = 2 bytes value = n bytes The following tags are defined: TAG OBJECT DESCRIPTION 1 a3ComIpVlanIpNetAddress IP Network Address of IP VLAN 2 a3ComIpVlanIpNetMask IP Network Mask of IP VLAN')
a3ComVlanIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfStatus.setDescription('The status column for this VLAN interface. This OBJECT can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notInService(2) notReady(3). Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row and the values are acceptible to the agent, the agent will change the status to active(1). If any of the necessary objects are not available, the agent will reject the creation request. Setting this object to createAndWait(5) causes a row in in this table to be created. The agent sets the status to notInService(2) if all of the information is present in the row and the values are acceptible to the agent; otherwise, the agent sets the status to notReady(3). Setting this object to active(1) is only valid when the current status is active(1) or notInService(2). When the state of the row transitions to active(1), the agent creates the corresponding row in the ifTable.. Setting this object to destroy(6) will remove the corresponding VLAN interface, remove the entry in this table, and the corresponding entries in the a3ComVlanGlobalMappingTable and the ifTable. In order for a set of this object to destroy(6) to succeed, all dependencies on this row must have been removed. These will include any stacking dependencies in the ifStackTable and any protocol specific tables dependencies.')
a3ComVlanIfModeType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 7), A3ComVlanModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfModeType.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfModeType.setDescription(' The VLAN mode type for this interface. This object can be set to: usedefault(1) open(2) closed(3) UseDefault Vlans: uses the bridge Vlan Mode value. The bridge Vlan Mode Value can be set to : Open, Closed or Mixed. Open VLANs: have no requirements about relationship between the bridge port that a frame was received upon and the bridge port(s) that it is transmitted on. All open VLANs within the bridge will share the same address table. Closed VLANs: require that the bridge port that a frame is received on is the same VLAN interface as the bridge port(s) that a frame is transmitted on. Each closed VLAN within the bridge will have its own address table.')
a3ComIpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1), )
if mibBuilder.loadTexts: a3ComIpVlanTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanTable.setDescription('A list of IP VLAN interface information entries. Entries in this table are related to entries in the a3ComVlanIfTable by using the same index.')
a3ComIpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComIpVlanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanEntry.setDescription('A a3ComIpVlanEntry contains layer 3 information about a particular IP VLAN interface. Note entries in this table cannot be deleted until the entries in the ifStackTable that produce overlap are removed.')
a3ComIpVlanIpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanIpNetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanIpNetAddress.setDescription('The IP network number for the IP VLAN interface defined in the a3ComVlanIfTable identified with the same index. The IpNetAdress and the IpNetMask must be set and the the row creation process completed by a NMS before overlapping rows in the ifStackTable can be created. Sets to the ifStackTable that produce overlapping IP IP VLAN interfaces will fail if this object is not set.')
a3ComIpVlanIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanIpNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanIpNetMask.setDescription('The IP network mask corresponding to the IP Network address defined by a3ComIpVlanIpNetAddress. The IpNetAdress and the IpNetMask must be set and the row creation process completed by a NMS before overlapping rows in the ifStackTable can be created. Sets to the ifStackTable that produce overlapping IP VLAN interfaces will fail if this object is not set.')
a3ComIpVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanStatus.setDescription('The status column for this IP VLAN entry. This object can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notInService(2) notReady(3). Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row and the values are acceptible to the agent, the agent will change the status to active(1). If any of the necessary objects are not available, the agent will reject the row creation request. Setting this object to createAndWait(5) causes a row in in this table to be created. The agent sets the status to notInService(2) if all of the information is present in the row and the values are acceptible to the agent; otherwise, the agent sets the status to notReady(3). Setting this object to active(1) is only valid when the current status is active(1) or notInService(2). When the status changes to active(1), the agent applies the IP parmeters to the IP VLAN interface identified by the corresponding value of the a3ComIpVlanIndex object. Setting this object to destroy(6) will remove the IP parmeters from the IP VLAN interface and remove the entry from this table. Setting this object to destroy(6) will remove the layer 3 information from the IP VLAN interface and will remove the row from this table. Note that this action cannot be performed if there are ifStackTable entries that result in overlapping IP VLAN interfaces. Note that these dependencies must be removed first.')
a3ComVlanProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2), )
if mibBuilder.loadTexts: a3ComVlanProtocolTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanProtocolTable.setDescription('This table lists the configured protocols per Vlan. A single entry exists in this list for each protocol configured on a VLAN interface. The a3ComVlanIfType object in a3ComVlanIfTable has to be set to vlanLayeredProtocols in order to use this table.')
a3ComVlanProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanProtocolIfIndex"), (0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanProtocolIndex"))
if mibBuilder.loadTexts: a3ComVlanProtocolEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanProtocolEntry.setDescription('A a3ComVlanProtocolEntry contains a single VLAN to protocol entry.')
a3ComVlanProtocolIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: a3ComVlanProtocolIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanProtocolIfIndex.setDescription("The first indice of this row and the vlan's ifIndex in the ifTable. The value of this object is the same as the corresponding a3ComVlanIfIndex in the a3ComVlanTable.")
a3ComVlanProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1, 2), A3ComVlanLayer3Type())
if mibBuilder.loadTexts: a3ComVlanProtocolIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanProtocolIndex.setDescription('The second indice of this row, which identifies one of possible many protocols associated with the VLAN interface identified by this entries first indice. The values are based on the layer 3 protocols specified in A3ComVlanType')
a3ComVlanProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanProtocolStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanProtocolStatus.setDescription('The status column for this VLAN interface. This OBJECT can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notInService(2) notReady(3). Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row and the values are acceptible to the agent, the agent will change the status to active(1). If any of the necessary objects are not available, the agent will reject the creation request. Setting this object to createAndWait(5) causes a row in this table to be created. The agent sets the status to notInService(2) if all of the information is present in the row and the values are acceptable to the agent; otherwise, the agent sets the status to notReady(3). Setting this object to active(1) is only valid when the current status is active(1) or notInService(2). Row creation to this table is only possible when a corresponding VLAN entry has been created in the a3ComVlanTable with an a3ComVlanType set to vlanLayeredProtocols(16). Setting this object to destroy(6) will remove the corresponding VLAN interface to protocol mapping.')
class A3ComVlanEncapsType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vlanEncaps3ComProprietaryVLT", 1), ("vlanEncaps8021q", 2), ("vlanEncapsPre8021qONcore", 3))

a3ComVlanEncapsIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1), )
if mibBuilder.loadTexts: a3ComVlanEncapsIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfTable.setDescription('This table lists VLAN encapsulation interfaces that exist within a device. A single entry exists in this list for each VLAN encapsulation interface in the system. A VLAN encapsulation interface may be created or destroyed.')
a3ComVlanEncapsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanEncapsIfIndex"))
if mibBuilder.loadTexts: a3ComVlanEncapsIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfEntry.setDescription('An individual VLAN encapsulation interface entry. When an NMS wishes to create a new entry in this table, it must obtain a non-zero index from the a3ComNextAvailableVirtIfIndex object. Row creation in this table will fail if the chosen index value does not match the current value returned from the a3ComNextAvailableVirtIfIndex object.')
a3ComVlanEncapsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: a3ComVlanEncapsIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfIndex.setDescription("The index value of this row and the encapsulation interface's ifIndex in the ifTable. The NMS obtains the index value used for creating a row in this table by reading the a3ComNextAvailableVirtIfIndex object.")
a3ComVlanEncapsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 2), A3ComVlanEncapsType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfType.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfType.setDescription('The encapsulation algorithm used when encapsulating packets transmitted, or de-encapsulating packets received through this interface.')
a3ComVlanEncapsIfTag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfTag.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfTag.setDescription('The tag used when encapsulating packets transmitted, or de-encapsulating packets received through this interface.')
a3ComVlanEncapsIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfStatus.setDescription('The row status for this VLAN encapsulation interface. This OBJECT can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notReady(3). In order for a row to become active, the NMS must set a3ComVlanEncapsIfTagType and a3ComVlanEncapsIfTag to some valid and consistent values. Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row, the agent will create the row and change the status to active(1). If any of the necessary objects are not available, or specify an invalid configuration, the row will not be created and the agent will return an appropriate error. Setting this object to createAndWait(5) causes a row in in this table to be created. If all necessary objects in the row have been assigned values and specify a valid configuration, the status of the row will be set to notInService(2); otherwise, the status will be set to notReady(3). This object may only be set to createAndGo(4) or createAndWait(5) if it does not exist. Setting this object to active(1) when the status is notInService(2) causes the agent to commit the row. Setting this object to active(1) when its value is already active(1) is a no-op. Setting this object to destroy(6) will remove the corresponding VLAN encapsulation interface, remote the entry in this table, and remove the corresponding entry in the ifTable. In order for a set of this object to destroy(6) to succeed, all dependencies on this row must have been removed. These will include any references to this interface in the ifStackTable.')
a3ComNextAvailableVirtIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComNextAvailableVirtIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComNextAvailableVirtIfIndex.setDescription("The value of the next available virtual ifIndex. This object is used by an NMS to select an index value for row-creation in tables indexed by ifIndex. The current value of this object is changed to a new value when the current value is written to an agent's table, that is indexed by ifIndex. Row creation using the current value of this object, allocates a virtual ifIndex. Note the following: 1. A newly created row does not have to be active(1) for the agent to allocate the virtual ifIndex. 2. Race conditions between multiple NMS's end when a row is created. Rows are deemed created when a setRequest is successfully committed (i.e. the errorStats is noError(0)). 3. An agent that exhausts its supply of virual ifIndex values returns zero as the value of this object. This can be used by an NMS as an indication to deleted unused rows and reboot the device.")
mibBuilder.exportSymbols("GENERIC-3COM-VLAN-MIB-1-0-7", a3ComVlanEncapsIfStatus=a3ComVlanEncapsIfStatus, a3ComEncapsulationGroup=a3ComEncapsulationGroup, A3ComVlanLayer3Type=A3ComVlanLayer3Type, a3ComVlanIfTable=a3ComVlanIfTable, generic=generic, a3ComIpVlanTable=a3ComIpVlanTable, a3ComVlanIfModeType=a3ComVlanIfModeType, a3ComVlanProtocolTable=a3ComVlanProtocolTable, a3ComVirtualGroup=a3ComVirtualGroup, A3ComVlanType=A3ComVlanType, a3ComIpVlanIpNetMask=a3ComIpVlanIpNetMask, a3ComVlanGlobalMappingTable=a3ComVlanGlobalMappingTable, a3ComVlanEncapsIfIndex=a3ComVlanEncapsIfIndex, a3ComIpVlanIpNetAddress=a3ComIpVlanIpNetAddress, a3ComVlanProtocolIndex=a3ComVlanProtocolIndex, a3ComVlanGlobalMappingEntry=a3ComVlanGlobalMappingEntry, a3ComVlanEncapsIfTag=a3ComVlanEncapsIfTag, a3ComVlanIfIndex=a3ComVlanIfIndex, a3ComNextAvailableVirtIfIndex=a3ComNextAvailableVirtIfIndex, a3ComVlanIfDescr=a3ComVlanIfDescr, a3ComVlanIfStatus=a3ComVlanIfStatus, a3ComVlanGlobalMappingIfIndex=a3ComVlanGlobalMappingIfIndex, a3ComVlanEncapsIfEntry=a3ComVlanEncapsIfEntry, a3ComVlanEncapsIfTable=a3ComVlanEncapsIfTable, a3ComVlanIfGlobalIdentifier=a3ComVlanIfGlobalIdentifier, a3ComVlanIfInfo=a3ComVlanIfInfo, a3ComVlanProtocolIfIndex=a3ComVlanProtocolIfIndex, genVirtual=genVirtual, RowStatus=RowStatus, a3ComIpVlanEntry=a3ComIpVlanEntry, a3ComVlanIfEntry=a3ComVlanIfEntry, a3ComVlanProtocolEntry=a3ComVlanProtocolEntry, A3ComVlanModeType=A3ComVlanModeType, a3ComIpVlanStatus=a3ComIpVlanStatus, a3Com=a3Com, a3ComVlanGroup=a3ComVlanGroup, a3ComVlanEncapsIfType=a3ComVlanEncapsIfType, a3ComVlanProtocolStatus=a3ComVlanProtocolStatus, a3ComVlanIfType=a3ComVlanIfType, a3ComVlanProtocolsGroup=a3ComVlanProtocolsGroup, A3ComVlanEncapsType=A3ComVlanEncapsType, a3ComVlanGlobalMappingIdentifier=a3ComVlanGlobalMappingIdentifier, genExperimental=genExperimental)
