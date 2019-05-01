#
# PySNMP MIB module VPLS-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPLS-GENERIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
pwIndex, = mibBuilder.importSymbols("PW-STD-MIB", "pwIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, NotificationType, Integer32, MibIdentifier, Counter64, IpAddress, transmission, Gauge32, Unsigned32, ObjectIdentity, Bits, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "MibIdentifier", "Counter64", "IpAddress", "transmission", "Gauge32", "Unsigned32", "ObjectIdentity", "Bits", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, StorageType, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention", "RowStatus", "TruthValue")
VPNIdOrZero, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNIdOrZero")
vplsGenericMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 274))
vplsGenericMIB.setRevisions(('2014-05-19 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vplsGenericMIB.setRevisionsDescriptions(('Initial version published as part of RFC 7257.',))
if mibBuilder.loadTexts: vplsGenericMIB.setLastUpdated('201405191200Z')
if mibBuilder.loadTexts: vplsGenericMIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
if mibBuilder.loadTexts: vplsGenericMIB.setContactInfo(' Thomas D. Nadeau Email: tnadeau@lucidvison.com The L2VPN Working Group (email distribution l2vpn@ietf.org, http://www.ietf.org/wg/l2vpn/charter) ')
if mibBuilder.loadTexts: vplsGenericMIB.setDescription("Copyright (c) 2014 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). The initial version of this MIB module was published in RFC 7257; for full legal notices see the RFC itself. This MIB module contains generic managed object definitions for Virtual Private LAN Service as defined in RFC 4761 and RFC 4762. This MIB module enables the use of any underlying pseudowire network.")
class VplsBgpRouteDistinguisher(TextualConvention, OctetString):
    reference = 'RFC 4364'
    description = 'Syntax for a route distinguisher that matches the definition in RFC 4364. For a complete definition of a route distinguisher, see RFC 4364. For more details on use of a route distinguisher for a VPLS service, see RFC 4761.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VplsBgpRouteTarget(TextualConvention, OctetString):
    reference = 'RFC 4364'
    description = 'Syntax for a Route Target that matches the definition in RFC 4364. For a complete definition of a Route Target, see RFC 4364.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VplsBgpRouteTargetType(TextualConvention, Integer32):
    reference = 'RFC 4364'
    description = 'Used to define the type of a Route Target usage. Route Targets can be specified to be imported, exported, or both. For a complete definition of a Route Target, see RFC 4364.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

vplsNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 274, 0))
vplsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 274, 1))
vplsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 274, 2))
vplsConfigIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 274, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsConfigIndexNext.setStatus('current')
if mibBuilder.loadTexts: vplsConfigIndexNext.setDescription('This object contains an appropriate value to be used for vplsConfigIndex when creating entries in the vplsConfigTable. The value 0 indicates that no unassigned entries are available. To obtain the value of vplsConfigIndex for a new entry in the vplsConfigTable, the manager issues a management protocol retrieval operation to obtain the current value of vplsConfigIndex. After each retrieval operation, the agent should modify the value to reflect the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse.')
vplsConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 274, 1, 2), )
if mibBuilder.loadTexts: vplsConfigTable.setStatus('current')
if mibBuilder.loadTexts: vplsConfigTable.setDescription('This table specifies information for configuring and monitoring Virtual Private LAN Service (VPLS). ')
vplsConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: vplsConfigEntry.setDescription('A row in this table represents a Virtual Private LAN Service (VPLS) in a packet network. It is indexed by vplsConfigIndex, which uniquely identifies a single VPLS. A row is created via SNMP or by the agent if a VPLS service is created by a non-SNMP application or due to the Auto-Discovery process. All of the read-create objects values except vplsConfigSignalingType can be changed when vplsConfigRowStatus is in the active(1) state. Changes for vplsConfigSignalingType are only allowed when the vplsConfigRowStatus is in notInService(2) or notReady(3) states. ')
vplsConfigIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vplsConfigIndex.setStatus('current')
if mibBuilder.loadTexts: vplsConfigIndex.setDescription('Unique index for the conceptual row identifying a VPLS service.')
vplsConfigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigName.setStatus('current')
if mibBuilder.loadTexts: vplsConfigName.setDescription('A textual name of the VPLS. If there is no local name, or this object is otherwise not applicable, then this object MUST contain a zero-length octet string.')
vplsConfigDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigDescr.setStatus('current')
if mibBuilder.loadTexts: vplsConfigDescr.setDescription('A textual string containing information about the VPLS service. If there is no information for this VPLS service, then this object MUST contain a zero-length octet string.')
vplsConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigAdminStatus.setStatus('current')
if mibBuilder.loadTexts: vplsConfigAdminStatus.setDescription('The desired administrative state of the VPLS service. If the administrative status of the VPLS service is changed to enabled, then this service is able to utilize pseudowires to perform the tasks of a VPLS service. The testing(3) state indicates that no operational packets can be passed.')
vplsConfigMacLearning = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigMacLearning.setStatus('current')
if mibBuilder.loadTexts: vplsConfigMacLearning.setDescription('This object specifies if MAC Learning is enabled in this service. If this object is true then MAC Learning is enabled. If false, then MAC Learning is disabled.')
vplsConfigDiscardUnknownDest = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigDiscardUnknownDest.setStatus('current')
if mibBuilder.loadTexts: vplsConfigDiscardUnknownDest.setDescription("If the value of this object is 'true', then frames received with an unknown destination MAC are discarded in this VPLS. If 'false', then the packets are processed.")
vplsConfigMacAging = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigMacAging.setStatus('current')
if mibBuilder.loadTexts: vplsConfigMacAging.setDescription("If the value of this object is 'true', then the MAC aging process is enabled in this VPLS. If 'false', then the MAC aging process is disabled.")
vplsConfigFwdFullHighWatermark = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(95)).setUnits('percentage').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigFwdFullHighWatermark.setStatus('current')
if mibBuilder.loadTexts: vplsConfigFwdFullHighWatermark.setDescription('This object specifies the utilization of the forwarding database for this VPLS instance at which the vplsFwdFullAlarmRaised notification will be sent. The value of this object must be higher than vplsConfigFwdFullLowWatermark.')
vplsConfigFwdFullLowWatermark = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)).clone(90)).setUnits('percentage').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigFwdFullLowWatermark.setStatus('current')
if mibBuilder.loadTexts: vplsConfigFwdFullLowWatermark.setDescription('This object specifies the utilization of the forwarding database for this VPLS instance at which the vplsFwdFullAlarmCleared notification will be sent. The value of this object must be less than vplsConfigFwdFullHighWatermark.')
vplsConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: vplsConfigRowStatus.setDescription('For creating, modifying, and deleting this row. All other objects in this row must be set to valid values before this object can be set to active(1). None of the read-create objects in the conceptual rows may be changed when this object is in the active(1) state. If this object is set to destroy(6) or deleted by the agent, all associated entries in the vplsPwBindTable, vplsBgpRteTargetTable, and vplsBgpVETable shall be deleted.')
vplsConfigMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(64, 9192)).clone(1518)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigMtu.setStatus('current')
if mibBuilder.loadTexts: vplsConfigMtu.setDescription('The value of this object specifies the MTU of this VPLS instance. This can be used to limit the MTU to a value lower than the MTU supported by the associated pseudowires.')
vplsConfigVpnId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 14), VPNIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigVpnId.setStatus('current')
if mibBuilder.loadTexts: vplsConfigVpnId.setDescription('This objects indicates the IEEE 802-1990 VPN ID of the associated VPLS service.')
vplsConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 15), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: vplsConfigStorageType.setDescription('This variable indicates the storage type for this row.')
vplsConfigSignalingType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ldp", 1), ("bgp", 2), ("none", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigSignalingType.setStatus('current')
if mibBuilder.loadTexts: vplsConfigSignalingType.setDescription('Desired signaling type of the VPLS service. If the value of this object is ldp(1), then a corresponding entry in vplsLdpConfigTable is required. If the value of this object is bgp(2), then a corresponding entry in vplsBgpConfigTable is required. If the value of this object is none(3), then it indicates a static configuration of PW labels.')
vplsStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 274, 1, 3), )
if mibBuilder.loadTexts: vplsStatusTable.setStatus('current')
if mibBuilder.loadTexts: vplsStatusTable.setDescription('This table provides information for monitoring Virtual Private LAN Service (VPLS). ')
vplsStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 274, 1, 3, 1), )
vplsConfigEntry.registerAugmentions(("VPLS-GENERIC-MIB", "vplsStatusEntry"))
vplsStatusEntry.setIndexNames(*vplsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: vplsStatusEntry.setStatus('current')
if mibBuilder.loadTexts: vplsStatusEntry.setDescription('A row in this table represents a Virtual Private LAN Service (VPLS) in a packet network. It is indexed by vplsConfigIndex, which uniquely identifies a single VPLS. A row in this table is automatically created by the agent when a VPLS service is first set to active. ')
vplsStatusOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("other", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsStatusOperStatus.setStatus('current')
if mibBuilder.loadTexts: vplsStatusOperStatus.setDescription('The current operational state of this VPLS service.')
vplsStatusPeerCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsStatusPeerCount.setStatus('current')
if mibBuilder.loadTexts: vplsStatusPeerCount.setDescription('This objects specifies the number of peers (pseudowires) present in this VPLS instance.')
vplsPwBindTable = MibTable((1, 3, 6, 1, 2, 1, 10, 274, 1, 4), )
if mibBuilder.loadTexts: vplsPwBindTable.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindTable.setDescription('This table provides an association between a VPLS service and the corresponding pseudowires. A service can have more than one pseudowire association. Pseudowires are defined in the pwTable')
vplsPwBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: vplsPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindEntry.setDescription('Each row represents an association between a VPLS instance and a pseudowire defined in the pwTable. Each index is unique in describing an entry in this table. However, both indexes are required to define the one to many association of service to pseudowire. Entries in this table may be created or deleted through SNMP, as side effects of console or other non-SNMP management commands, or upon learning via autodiscovery. It is optional for the agent to allow entries to be created that point to nonexistent entries in vplsConfigTable.')
vplsPwBindConfigType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("autodiscovery", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindConfigType.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindConfigType.setDescription('The value of this object indicates whether the pseudowire Binding was created via SNMP/Console or via Auto-Discovery. The value of this object must be specified when the row is created and cannot be changed while the row status is active(1)')
vplsPwBindType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mesh", 1), ("spoke", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindType.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindType.setDescription('The value of this object indicates whether the pseudowire Binding is of type mesh or spoke. The value of this object must be specified when the row is created and cannot be changed while the row status is active(1)')
vplsPwBindRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindRowStatus.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindRowStatus.setDescription('For creating, modifying, and deleting this row. All other objects in this row must be set to valid values before this object can be set to active(1). None of the read-create objects in the conceptual rows may be changed when this object is in the active(1) state. If autodiscovered entries are deleted they would likely re-appear in the next autodiscovery interval.')
vplsPwBindStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindStorageType.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindStorageType.setDescription('This variable indicates the storage type for this row.')
vplsBgpADConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 274, 1, 5), )
if mibBuilder.loadTexts: vplsBgpADConfigTable.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigTable.setDescription('This table specifies information for configuring BGP Auto-Discovery parameters for a given VPLS service. ')
vplsBgpADConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsBgpADConfigEntry.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigEntry.setDescription('A row in this table indicates that BGP based Auto- Discovery is in use for this instance of VPLS. A row in this table is indexed by vplsConfigIndex, which uniquely identifies a single VPLS. Entries in this table may be created or deleted through SNMP, as side effects of console or other non-SNMP management commands, or upon learning via autodiscovery. All of the read-create objects can be changed when vplsBGPADConfigRowStatus is in active(1) state.')
vplsBgpADConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 1), VplsBgpRouteDistinguisher()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigRouteDistinguisher.setDescription('The route distinguisher for this VPLS. See RFC 4364 for a complete definition of a route distinguisher. For more details on use of a route distinguisher for a VPLS service, see RFC 4761. When not configured, the value is derived from the lower 6 bytes of vplsBgpADConfigVplsId. ')
vplsBgpADConfigPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigPrefix.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigPrefix.setDescription('In case of auto-discovery, the default prefix advertised is the IP address of the loopback. In case the user wants to override the loopback address, vplsBgpADConfigPrefix should be set. When this value is non-zero, this value is used along with vplsBgpADConfigRouteDistinguisher in the Network Layer Reachability Information (NLRI), see RFC 6074. ')
vplsBgpADConfigVplsId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 3), VplsBgpRouteDistinguisher()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigVplsId.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigVplsId.setDescription('VplsId is a unique identifier for all Virtual Switch Instances (VSIs) belonging to the same VPLS. It is advertised as an extended community. ')
vplsBgpADConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigRowStatus.setDescription('For creating, modifying, and deleting this row. All other objects in this row must be set to valid values before this object can be set to active(1). None of the read-create objects in the conceptual rows may be changed when this object is in the active(1) state.')
vplsBgpADConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: vplsBgpADConfigStorageType.setDescription('This variable indicates the storage type for this row.')
vplsBgpRteTargetTable = MibTable((1, 3, 6, 1, 2, 1, 10, 274, 1, 6), )
if mibBuilder.loadTexts: vplsBgpRteTargetTable.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetTable.setDescription('This table specifies the list of Route Targets imported or exported by BGP during auto-discovery of VPLS. ')
vplsBgpRteTargetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "VPLS-GENERIC-MIB", "vplsBgpRteTargetIndex"))
if mibBuilder.loadTexts: vplsBgpRteTargetEntry.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetEntry.setDescription('An entry in this table specifies the value of the Route Target being used by BGP. Depending on the value of vplsBgpRteTargetType, a Route Target might be exported, imported, or both. Every VPLS that uses auto-discovery for finding peer nodes can import and export multiple Route Targets. This representation allows support for hierarchical VPLS. Entries in this table may be created or deleted through SNMP, as side effects of console or other non-SNMP management commands, or upon learning via autodiscovery. It is optional for the agent to allow entries to be created that point to nonexistent entries in vplsConfigTable.')
vplsBgpRteTargetIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: vplsBgpRteTargetIndex.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetIndex.setDescription('This index, along with vplsConfigIndex, identifies one entry in the vplsBgpRteTargetTable. By keeping vplsConfigIndex constant and using a new value of vplsBgpRteTargetIndex, users can configure multiple Route Targets for the same VPLS. ')
vplsBgpRteTargetRTType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 2), VplsBgpRouteTargetType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpRteTargetRTType.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetRTType.setDescription('Used to define the type of a Route Target usage. Route Targets can be specified to be imported, exported, or both. For a complete definition of a Route Target, see RFC 4364.')
vplsBgpRteTargetRT = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 3), VplsBgpRouteTarget()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpRteTargetRT.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetRT.setDescription('The Route Target associated with the VPLS service. For more details on use of Route Targets for a VPLS service, see RFC 4761. ')
vplsBgpRteTargetRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpRteTargetRowStatus.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table. All other objects in this row must be set to valid values before this object can be set to active(1). When a row in this table is in active(1) state, no objects in that row can be modified. If autodiscovered entries are deleted they would likely re-appear in the next autodiscovery interval.')
vplsBgpRteTargetStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpRteTargetStorageType.setStatus('current')
if mibBuilder.loadTexts: vplsBgpRteTargetStorageType.setDescription('This variable indicates the storage type for this row.')
vplsStatusNotifEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 274, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsStatusNotifEnable.setReference('See also RFC 3413 for explanation that notifications are under the ultimate control of the MIB module in this document.')
if mibBuilder.loadTexts: vplsStatusNotifEnable.setStatus('current')
if mibBuilder.loadTexts: vplsStatusNotifEnable.setDescription('If this object is set to true(1), then it enables the emission of a vplsStatusChanged notification; otherwise, this notification is not emitted.')
vplsNotificationMaxRate = MibScalar((1, 3, 6, 1, 2, 1, 10, 274, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsNotificationMaxRate.setStatus('current')
if mibBuilder.loadTexts: vplsNotificationMaxRate.setDescription('This object indicates the maximum number of notifications issued per second. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or it may queue them until an appropriate time. A value of 0 means no throttling is applied and events may be notified at the rate at which they occur.')
vplsStatusChanged = NotificationType((1, 3, 6, 1, 2, 1, 10, 274, 0, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("VPLS-GENERIC-MIB", "vplsConfigAdminStatus"), ("VPLS-GENERIC-MIB", "vplsStatusOperStatus"))
if mibBuilder.loadTexts: vplsStatusChanged.setStatus('current')
if mibBuilder.loadTexts: vplsStatusChanged.setDescription('The vplsStatusChanged notification is generated when there is a change in the administrative or operating status of a VPLS service. The object instances included in the notification are the ones associated with the VPLS service whose status has changed.')
vplsFwdFullAlarmRaised = NotificationType((1, 3, 6, 1, 2, 1, 10, 274, 0, 2)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"), ("VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"))
if mibBuilder.loadTexts: vplsFwdFullAlarmRaised.setStatus('current')
if mibBuilder.loadTexts: vplsFwdFullAlarmRaised.setDescription('The vplsFwdFullAlarmRaised notification is generated when the utilization of the Forwarding database is above the value specified by vplsConfigFwdFullHighWatermark. The object instances included in the notification are the ones associated with the VPLS service that has exceeded the threshold.')
vplsFwdFullAlarmCleared = NotificationType((1, 3, 6, 1, 2, 1, 10, 274, 0, 3)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"), ("VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"))
if mibBuilder.loadTexts: vplsFwdFullAlarmCleared.setStatus('current')
if mibBuilder.loadTexts: vplsFwdFullAlarmCleared.setDescription('The vplsFwdFullAlarmCleared notification is generated when the utilization of the Forwarding database is below the value specified by vplsConfigFwdFullLowWatermark. The object instances included in the notification are the ones associated with the VPLS service that has fallen below the threshold.')
vplsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 274, 2, 1))
vplsModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 274, 2, 1, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsGroup"), ("VPLS-GENERIC-MIB", "vplsPwBindGroup"), ("VPLS-GENERIC-MIB", "vplsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsModuleFullCompliance = vplsModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: vplsModuleFullCompliance.setDescription('Compliance requirement for implementations that provide full support for VPLS-GENERIC-MIB. Such devices can then be monitored and configured using this MIB module.')
vplsModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 274, 2, 1, 2)).setObjects(("VPLS-GENERIC-MIB", "vplsGroup"), ("VPLS-GENERIC-MIB", "vplsPwBindGroup"), ("VPLS-GENERIC-MIB", "vplsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsModuleReadOnlyCompliance = vplsModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: vplsModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only provide read-only support for VPLS-GENERIC-MIB. Such devices can then be monitored but cannot be configured using this MIB modules.')
vplsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 274, 2, 2))
vplsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 274, 2, 2, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigName"), ("VPLS-GENERIC-MIB", "vplsBgpADConfigRouteDistinguisher"), ("VPLS-GENERIC-MIB", "vplsBgpRteTargetRTType"), ("VPLS-GENERIC-MIB", "vplsBgpRteTargetRT"), ("VPLS-GENERIC-MIB", "vplsBgpRteTargetRowStatus"), ("VPLS-GENERIC-MIB", "vplsBgpRteTargetStorageType"), ("VPLS-GENERIC-MIB", "vplsBgpADConfigPrefix"), ("VPLS-GENERIC-MIB", "vplsBgpADConfigVplsId"), ("VPLS-GENERIC-MIB", "vplsBgpADConfigRowStatus"), ("VPLS-GENERIC-MIB", "vplsBgpADConfigStorageType"), ("VPLS-GENERIC-MIB", "vplsConfigDescr"), ("VPLS-GENERIC-MIB", "vplsConfigAdminStatus"), ("VPLS-GENERIC-MIB", "vplsConfigMacLearning"), ("VPLS-GENERIC-MIB", "vplsConfigDiscardUnknownDest"), ("VPLS-GENERIC-MIB", "vplsConfigMacAging"), ("VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"), ("VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"), ("VPLS-GENERIC-MIB", "vplsConfigRowStatus"), ("VPLS-GENERIC-MIB", "vplsConfigIndexNext"), ("VPLS-GENERIC-MIB", "vplsConfigMtu"), ("VPLS-GENERIC-MIB", "vplsConfigStorageType"), ("VPLS-GENERIC-MIB", "vplsConfigSignalingType"), ("VPLS-GENERIC-MIB", "vplsStatusOperStatus"), ("VPLS-GENERIC-MIB", "vplsStatusPeerCount"), ("VPLS-GENERIC-MIB", "vplsStatusNotifEnable"), ("VPLS-GENERIC-MIB", "vplsNotificationMaxRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsGroup = vplsGroup.setStatus('current')
if mibBuilder.loadTexts: vplsGroup.setDescription('The group of objects supporting management of L2VPN VPLS services')
vplsPwBindGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 274, 2, 2, 2)).setObjects(("VPLS-GENERIC-MIB", "vplsPwBindConfigType"), ("VPLS-GENERIC-MIB", "vplsPwBindType"), ("VPLS-GENERIC-MIB", "vplsPwBindRowStatus"), ("VPLS-GENERIC-MIB", "vplsPwBindStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsPwBindGroup = vplsPwBindGroup.setStatus('current')
if mibBuilder.loadTexts: vplsPwBindGroup.setDescription('The group of objects supporting management of pseudowire (PW) Binding to VPLS.')
vplsNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 274, 2, 2, 3)).setObjects(("VPLS-GENERIC-MIB", "vplsStatusChanged"), ("VPLS-GENERIC-MIB", "vplsFwdFullAlarmRaised"), ("VPLS-GENERIC-MIB", "vplsFwdFullAlarmCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsNotificationGroup = vplsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vplsNotificationGroup.setDescription('The group of notifications supporting the Notifications generated for VPLS services.')
mibBuilder.exportSymbols("VPLS-GENERIC-MIB", vplsConfigIndexNext=vplsConfigIndexNext, vplsBgpADConfigRowStatus=vplsBgpADConfigRowStatus, vplsModuleFullCompliance=vplsModuleFullCompliance, PYSNMP_MODULE_ID=vplsGenericMIB, vplsConfigMtu=vplsConfigMtu, vplsConfigSignalingType=vplsConfigSignalingType, vplsConfigAdminStatus=vplsConfigAdminStatus, VplsBgpRouteTargetType=VplsBgpRouteTargetType, vplsStatusTable=vplsStatusTable, vplsBgpRteTargetRT=vplsBgpRteTargetRT, vplsConfigIndex=vplsConfigIndex, vplsStatusChanged=vplsStatusChanged, vplsObjects=vplsObjects, vplsBgpADConfigStorageType=vplsBgpADConfigStorageType, vplsPwBindGroup=vplsPwBindGroup, vplsConfigMacAging=vplsConfigMacAging, vplsNotifications=vplsNotifications, vplsBgpADConfigVplsId=vplsBgpADConfigVplsId, vplsConfigRowStatus=vplsConfigRowStatus, vplsConfigStorageType=vplsConfigStorageType, vplsPwBindConfigType=vplsPwBindConfigType, vplsPwBindRowStatus=vplsPwBindRowStatus, vplsBgpADConfigTable=vplsBgpADConfigTable, vplsConfigEntry=vplsConfigEntry, vplsPwBindType=vplsPwBindType, vplsBgpRteTargetRowStatus=vplsBgpRteTargetRowStatus, vplsFwdFullAlarmRaised=vplsFwdFullAlarmRaised, vplsGroup=vplsGroup, vplsPwBindTable=vplsPwBindTable, vplsConfigName=vplsConfigName, vplsBgpRteTargetIndex=vplsBgpRteTargetIndex, vplsStatusPeerCount=vplsStatusPeerCount, vplsConfigTable=vplsConfigTable, vplsConfigVpnId=vplsConfigVpnId, vplsStatusEntry=vplsStatusEntry, vplsGenericMIB=vplsGenericMIB, vplsConfigDiscardUnknownDest=vplsConfigDiscardUnknownDest, vplsBgpRteTargetStorageType=vplsBgpRteTargetStorageType, VplsBgpRouteDistinguisher=VplsBgpRouteDistinguisher, vplsBgpRteTargetTable=vplsBgpRteTargetTable, vplsBgpRteTargetRTType=vplsBgpRteTargetRTType, vplsPwBindEntry=vplsPwBindEntry, vplsConfigMacLearning=vplsConfigMacLearning, vplsBgpADConfigRouteDistinguisher=vplsBgpADConfigRouteDistinguisher, vplsBgpADConfigPrefix=vplsBgpADConfigPrefix, vplsNotificationMaxRate=vplsNotificationMaxRate, vplsFwdFullAlarmCleared=vplsFwdFullAlarmCleared, vplsConfigDescr=vplsConfigDescr, vplsStatusNotifEnable=vplsStatusNotifEnable, vplsStatusOperStatus=vplsStatusOperStatus, vplsConfigFwdFullLowWatermark=vplsConfigFwdFullLowWatermark, vplsCompliances=vplsCompliances, vplsModuleReadOnlyCompliance=vplsModuleReadOnlyCompliance, vplsBgpRteTargetEntry=vplsBgpRteTargetEntry, vplsNotificationGroup=vplsNotificationGroup, VplsBgpRouteTarget=VplsBgpRouteTarget, vplsPwBindStorageType=vplsPwBindStorageType, vplsGroups=vplsGroups, vplsConfigFwdFullHighWatermark=vplsConfigFwdFullHighWatermark, vplsConformance=vplsConformance, vplsBgpADConfigEntry=vplsBgpADConfigEntry)