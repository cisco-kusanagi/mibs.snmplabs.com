#
# PySNMP MIB module CISCO-IETF-VPLS-BGP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-VPLS-BGP-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cvplsPwBindIndex, cvplsConfigIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex", "cvplsConfigIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, MibIdentifier, ObjectIdentity, IpAddress, Unsigned32, Gauge32, Counter64, Counter32, iso, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibIdentifier", "ObjectIdentity", "IpAddress", "Unsigned32", "Gauge32", "Counter64", "Counter32", "iso", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
ciscoIetfVplsBgpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 140))
ciscoIetfVplsBgpExtMIB.setRevisions(('2008-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setLastUpdated('200810240000Z')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-l2vpn@cisco.com')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setDescription('This MIB module enables the use of any underlying Pseudo Wire network. This MIB extends the MIB module published in the RFC 4188 to manage object definitions for BGP signalled VPLS. GLOSSARY PE The term PE refers to Provider-Edge devices. Pseudo Wire An emulation of a native service over a Packet Switched Network. RD (Route Distinguisher) They are used to create VPN-IPv4 addresses, as specified in [RFC4364]. RT (Route Target) A Route Target attribute can be thought of as identifying a set of sites. More description specified in [RFC4364]. u-PE A Layer 2 PE device used for Layer 2 aggregation. The notion of u-PE is described further in [RFC4761]. VE The term VE refers to a VPLS Edge device, which could be either a PE or a u-PE. VPLS Virtual private LAN service. A type of layer 2 VPN.')
class CiVplsBgpExtRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = 'This textual convention represents a Route Distinguisher. Please refer to RFC 4364 for more details about the Route Distinguisher. Please refer to draft-ietf-l2vpn-vpls-bgp-08 on the use of a Route Distinguisher for a VPLS.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = 'This textual convention represents a Route Target. Please refer to RFC 4364 for more details about the Route Target. Please refer to draft-ietf-l2vpn-vpls-bgp-08 on the use of a Route Target for a VPLS.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC 4364]'
    description = 'This textual convention represents the type of a route target usage. Route targets can be specified to be imported, exported, or both.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

class CiVplsBgpExtVEID(TextualConvention, Unsigned32):
    description = 'This textual convention represents a VE id.'
    status = 'current'

ciscoIetfVplsBgpExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 0))
ciscoIetfVplsBgpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 1))
ciscoIetfVplsBgpExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2))
ciVplsBgpExtConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1), )
if mibBuilder.loadTexts: ciVplsBgpExtConfigTable.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigTable.setDescription('This table specifies information for configuring and monitoring BGP-specific parameters for VPLS. A row is automatically created when a VPLS is configured using BGP signalling. None of the read-write objects values can be changed when cvplsConfigRowStatus is in the active(1) state. Changes are allowed when the cvplsConfigRowStatus is in notInService(2) or notReady(3) states only. If the operator need to change one of the values for an active row the cvplsConfigRowStatus should be first changed to notInService(2), the objects may be changed now, and later to active(1) in order to re-initiate the signaling process with the new values in effect.')
ciVplsBgpExtConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigEntry.setDescription('Each Entry represents a conceptual row in ciVplsBgpExtConfigTable and provides the information about BGP-specific information for VPLS in a packet network.')
ciVplsBgpExtConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 1), CiVplsBgpExtRouteDistinguisher()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigRouteDistinguisher.setDescription('This object represents the Route Distingiusher for this VPLS.')
ciVplsBgpExtConfigVERangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigVERangeSize.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigVERangeSize.setDescription('This object represents the size of the range of VE identifiers in this VPLS. This number controls the size of the label block advertised for this VE by the PE. A value of 0 indicates that the range is not configured and the PE derives the range value from received advertisements from other PEs.')
civplsBgpExtRTTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2), )
if mibBuilder.loadTexts: civplsBgpExtRTTable.setStatus('current')
if mibBuilder.loadTexts: civplsBgpExtRTTable.setDescription('This table specifies information for the list of RTs imported or exported by BGP during auto-discovery of VPLS.')
civplsBgpExtRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"))
if mibBuilder.loadTexts: civplsBgpExtRTEntry.setStatus('current')
if mibBuilder.loadTexts: civplsBgpExtRTEntry.setDescription('Each Entry represents a conceptual row in civplsBgpExtRTTable and provides the information about the value of the RT being used by BGP. Depending on the value of civplsBgpExtRTType, an RT might be exported or imported or both. Every VPLS, which uses auto-discovery for finding peer nodes, can import and export multiple RTs. This representation allows support for hierarchical VPLS. A row is created by the operator or agent prior to autodiscovery.')
ciVplsBgpExtRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 1), CiVplsBgpExtRouteTargetType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTType.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTType.setDescription('This object represents the type of a RT usage. RTs can be specified to be imported, exported, or both.')
ciVplsBgpExtRT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 2), CiVplsBgpExtRouteTarget().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRT.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRT.setDescription('The RT associated with the VPLS service.')
ciVplsBgpExtRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTStorageType.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTStorageType.setDescription('This object indicates the storage type for this row.')
ciVplsBgpExtRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTRowStatus.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTRowStatus.setDescription('This object is used to create, modify, and/or delete a row in this table. When a row in this table is in active(1) state, no objects in that row can be modified.')
ciVplsBgpExtVETable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3), )
if mibBuilder.loadTexts: ciVplsBgpExtVETable.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVETable.setDescription('This table associates VPLS Edge devices to a VPLS. The VEs assigned to a VPLS can be configured on a PE. This table has an expansion dependant relationship with cvplsConfigTable. For each row identified by cvplsConfigIndex, there may exist one or more rows in this table. ciVplsBgpExtVEId is the expansion index. None of the read-create objects values can be changed when ciVplsBgpExtVERowStatus is in the active(1) state. Changes are allowed when the ciVplsBgpExtVERowStatus is in notInService(2) or notReady(3) states only. If the operator need to change one of the values for an active row the ciVplsBgpExtVERowStatus should be first changed to notInService(2), the objects may be changed now, and later to active(1) in order to re-initiate the signaling process with the new values in effect.')
ciVplsBgpExtVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEId"))
if mibBuilder.loadTexts: ciVplsBgpExtVEEntry.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEEntry.setDescription('Each Entry represents a conceptual row in ciVplsBgpExtVETable and provides the information about VPLS Edge devices.')
ciVplsBgpExtVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 1), CiVplsBgpExtVEID())
if mibBuilder.loadTexts: ciVplsBgpExtVEId.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEId.setDescription('This object identifies a VE associated with a VPLS.')
ciVplsBgpExtVEName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEName.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEName.setDescription('This object represents the name of the site or u-PE associated with this VE.')
ciVplsBgpExtVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEPreference.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEPreference.setDescription('This object represents the preference of the VE if the site is multi-homed and VE Id is used.')
ciVplsBgpExtVEStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEStorageType.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEStorageType.setDescription('This object indicates the storage type for this row.')
ciVplsBgpExtVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVERowStatus.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVERowStatus.setDescription('This object is used to create, modify, and/or delete a row in this table. When a row in this table is in active(1) state, no objects in that row can be modified.')
ciVplsBgpExtPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4), )
if mibBuilder.loadTexts: ciVplsBgpExtPwBindTable.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindTable.setDescription('This table provides BGP-specific information for an association between a VPLS and the corresponding Pseudo Wires. A service can have more than one Pseudo Wire association. Pseudo Wires are defined in the cpwvcTable. Each row represents an association between a VPLS instance and one or more Pseudo Wires defined in the cpwVcTable in CISCO-IETF-PW-MIB. An Entry in this table in instantiated only when BGP signalling is used to configure VPLS.')
ciVplsBgpExtPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindEntry.setDescription('Each Entry represents a conceptual row in ciVplsBgpExtPwBindTable and provides the information about BGP-specific information for an association between a VPLS and the corresponding Pseudo Wires.')
ciVplsBgpExtPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 1), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindLocalVEId.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindLocalVEId.setDescription('This object represents the local VE this Pseudo Wire is associated with.')
ciVplsBgpExtPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 2), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindRemoteVEId.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindRemoteVEId.setDescription('This object represents the remote VE this Pseudo Wire is associated with.')
ciscoIetfVplsBgpExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1))
ciscoIetfVplsBgpExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2))
ciscoIetfVplsBgpExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfVplsBgpExtMIBCompliance = ciscoIetfVplsBgpExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIBCompliance.setDescription('Compliance statement for the entities that implement the ciscoIetfVplsBgpExtMIB module.')
ciVplsBgpExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigRouteDistinguisher"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigVERangeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtConfigGroup = ciVplsBgpExtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigGroup.setDescription('This group of objects help to configure L2VPN VPLS using BGP.')
ciVplsBgpExtRTGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 2)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTStorageType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtRTGroup = ciVplsBgpExtRTGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTGroup.setDescription('The group of objects help to manage RTs for L2VPN VPLS using BGP.')
ciVplsBgpExtVEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 3)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEName"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEPreference"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVERowStatus"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtVEGroup = ciVplsBgpExtVEGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEGroup.setDescription('The group of objects help to manage VE devices for L2VPN VPLS using BGP.')
ciVplsBgpExtPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 4)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindLocalVEId"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindRemoteVEId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtPwBindGroup = ciVplsBgpExtPwBindGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindGroup.setDescription('The group of objects help to manage Pseudo Wires for L2VPN VPLS using BGP.')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-BGP-EXT-MIB", ciVplsBgpExtConfigGroup=ciVplsBgpExtConfigGroup, ciscoIetfVplsBgpExtMIBCompliance=ciscoIetfVplsBgpExtMIBCompliance, ciVplsBgpExtVEStorageType=ciVplsBgpExtVEStorageType, CiVplsBgpExtRouteTarget=CiVplsBgpExtRouteTarget, ciVplsBgpExtConfigRouteDistinguisher=ciVplsBgpExtConfigRouteDistinguisher, ciVplsBgpExtRTStorageType=ciVplsBgpExtRTStorageType, ciVplsBgpExtVERowStatus=ciVplsBgpExtVERowStatus, ciVplsBgpExtVEGroup=ciVplsBgpExtVEGroup, ciVplsBgpExtVEName=ciVplsBgpExtVEName, ciscoIetfVplsBgpExtMIBGroups=ciscoIetfVplsBgpExtMIBGroups, ciVplsBgpExtConfigEntry=ciVplsBgpExtConfigEntry, ciVplsBgpExtPwBindTable=ciVplsBgpExtPwBindTable, ciVplsBgpExtPwBindLocalVEId=ciVplsBgpExtPwBindLocalVEId, ciVplsBgpExtPwBindGroup=ciVplsBgpExtPwBindGroup, ciVplsBgpExtVETable=ciVplsBgpExtVETable, PYSNMP_MODULE_ID=ciscoIetfVplsBgpExtMIB, civplsBgpExtRTEntry=civplsBgpExtRTEntry, ciscoIetfVplsBgpExtMIBNotifs=ciscoIetfVplsBgpExtMIBNotifs, ciVplsBgpExtRTRowStatus=ciVplsBgpExtRTRowStatus, ciVplsBgpExtVEId=ciVplsBgpExtVEId, civplsBgpExtRTTable=civplsBgpExtRTTable, ciscoIetfVplsBgpExtMIB=ciscoIetfVplsBgpExtMIB, CiVplsBgpExtRouteDistinguisher=CiVplsBgpExtRouteDistinguisher, ciscoIetfVplsBgpExtMIBConform=ciscoIetfVplsBgpExtMIBConform, ciVplsBgpExtVEPreference=ciVplsBgpExtVEPreference, ciVplsBgpExtPwBindRemoteVEId=ciVplsBgpExtPwBindRemoteVEId, ciscoIetfVplsBgpExtMIBObjects=ciscoIetfVplsBgpExtMIBObjects, ciVplsBgpExtRT=ciVplsBgpExtRT, ciscoIetfVplsBgpExtMIBCompliances=ciscoIetfVplsBgpExtMIBCompliances, ciVplsBgpExtVEEntry=ciVplsBgpExtVEEntry, ciVplsBgpExtRTType=ciVplsBgpExtRTType, ciVplsBgpExtPwBindEntry=ciVplsBgpExtPwBindEntry, ciVplsBgpExtConfigTable=ciVplsBgpExtConfigTable, CiVplsBgpExtRouteTargetType=CiVplsBgpExtRouteTargetType, ciVplsBgpExtRTGroup=ciVplsBgpExtRTGroup, ciVplsBgpExtConfigVERangeSize=ciVplsBgpExtConfigVERangeSize, CiVplsBgpExtVEID=CiVplsBgpExtVEID)
