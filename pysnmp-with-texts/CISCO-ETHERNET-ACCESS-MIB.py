#
# PySNMP MIB module CISCO-ETHERNET-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHERNET-ACCESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
managementDomainIndex, vtpVlanIndex = mibBuilder.importSymbols("CISCO-VTP-MIB", "managementDomainIndex", "vtpVlanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Bits, IpAddress, NotificationType, TimeTicks, iso, Gauge32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "IpAddress", "NotificationType", "TimeTicks", "iso", "Gauge32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEthernetAccessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 466))
ciscoEthernetAccessMIB.setRevisions(('2007-09-14 00:00', '2005-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setRevisionsDescriptions(('Added ENI as a new port type to the ceaPortType and ceaPortCapability objects.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setLastUpdated('200709140000Z')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-dsbu@cisco.com')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setDescription("The tables defined by this MIB module contain a collection of managed objects that are general in nature and apply to an edge device in an organizations network, e.g. a Metro Ethernet network. An edge device, is a customer located equipment, this is the first device which will connect the Service Provider's network and map subscriber traffic into the next layer. The access media could be either CAT5 or fiber. The access device (edge device) can be designed for DSL, Ethernet or other technologies, however, this MIB is designed for Ethernet. Terminology: UNI - User to Network Interface NNI - Network to Network Interface. ENI - Enhanced Network Interface. Enhanced UNI port. module/device - In an environment (specifically, in an SNMP context) consisting of a single chassis which can contain multiple cards, the term 'module' refers to a card and the term 'device' refers to the whole chassis. In an environment where multiple chassis are 'stacked' together, the term 'module' refers to a chassis and the term 'device' refers to the whole stack. In an environment containing only a single chassis without removable cards, the terms 'device' and 'module' both refer to the chassis and its contents.")
ciscoEthernetAccessMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1))
ciscoEthernetAccessMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2))
ceaGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1))
ceaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2))
class CeaVlanUNIType(TextualConvention, Integer32):
    description = "The type of a VLAN. 'other' -- this VLAN is not a UNI VLAN 'isolated' -- this VLAN is a UNI isolated VLAN. UNI ports that are members of a UNI isolated VLAN can not communicate with other ports in that VLAN, however NNI ports can communicate with UNI and NNI ports in the same VLAN. 'community' -- this VLAN is a UNI community VLAN. UNI and NNI ports that are members of the community VLAN can communicate with all other UNI and NNI ports in the same VLAN."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("isolated", 2), ("community", 3))

ceaMaxNNIPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaMaxNNIPorts.setStatus('current')
if mibBuilder.loadTexts: ceaMaxNNIPorts.setDescription("The max number of interfaces per module for which the ceaPortType can have the value 'nni'. The value of 0 is returned by this object if there is no limitation to the number of NNI ports.")
ceaMaxUNIVlanCommunityPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaMaxUNIVlanCommunityPorts.setStatus('current')
if mibBuilder.loadTexts: ceaMaxUNIVlanCommunityPorts.setDescription("The maximum number of ports on this device for which the ceaUNIVlanType object can have the value 'community'. The value of 0 is returned by this object if there is no limitation to the number of UNI VLAN Communities.")
ceaPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1), )
if mibBuilder.loadTexts: ceaPortTable.setStatus('current')
if mibBuilder.loadTexts: ceaPortTable.setDescription('This table contains Ethernet port specific information. There exists an entry for each Ethernet port with an ifType of 6 (ethernetCsmacd) in this table. Note that the maximum number of NNI ports that can be configured per module on this device is given by the value of ceaMaxNNIPorts.')
ceaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ceaPortEntry.setStatus('current')
if mibBuilder.loadTexts: ceaPortEntry.setDescription('A set of Ethernet port specific parameters for a device which can be configured with a mixture of port types defined by the ceaPortType object.')
ceaPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unspecified", 1), ("uni", 2), ("nni", 3), ("eni", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceaPortType.setStatus('current')
if mibBuilder.loadTexts: ceaPortType.setDescription('The current configuration of the port. Only ports that are supported by the ceaPortCapability object can be set. Unspecified port type is any other port type than NNI, UNI or ENI. unspecified = Not UNI, or NNI, or ENI uni = User to Network Interface port type. nni = Network to Network Interface port type. eni = Enhanced UNI port type.')
ceaPortCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("nni", 0), ("uni", 1), ("eni", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaPortCapability.setStatus('current')
if mibBuilder.loadTexts: ceaPortCapability.setDescription("Types supported by the Ethernet port. If a port doesn't support the port type the ceaPortType will not allow set of the unsupported type. nni = Port supports NNI. uni = Port supports UNI. eni = Port supports ENI.")
ceaUNIVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2), )
if mibBuilder.loadTexts: ceaUNIVlanTable.setStatus('current')
if mibBuilder.loadTexts: ceaUNIVlanTable.setDescription("This table contains UNI VLAN information for all the VLANs which currently exist on this device. The number of UNI ports that can belong to a VLAN type 'community' is limited by the ceaMaxUNIVlanCommunityPorts object.")
ceaUNIVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-VTP-MIB", "managementDomainIndex"), (0, "CISCO-VTP-MIB", "vtpVlanIndex"))
if mibBuilder.loadTexts: ceaUNIVlanEntry.setStatus('current')
if mibBuilder.loadTexts: ceaUNIVlanEntry.setDescription('There is an entry in this table for each VLAN that exist on this device.')
ceaUNIVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1, 1), CeaVlanUNIType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceaUNIVlanType.setStatus('current')
if mibBuilder.loadTexts: ceaUNIVlanType.setDescription('Indicates the VLAN type defined for the UNI VLAN.')
cEthernetAccessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1))
cEthernetAccessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2))
cEthernetAccessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1, 1)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaPortGroup"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEthernetAccessMIBCompliance = cEthernetAccessMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cEthernetAccessMIBCompliance.setDescription('The compliance statement for entities that implement the CISCO-ETHERNET-ACCESS-MIB. Implementation of this MIB is mandatory for any platform that have Ethernet UNI/NNI capable interfaces.')
ceaPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 1)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxNNIPorts"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortType"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceaPortGroup = ceaPortGroup.setStatus('current')
if mibBuilder.loadTexts: ceaPortGroup.setDescription('A collection of managed objects defining port types.')
ceaVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 2)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxUNIVlanCommunityPorts"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaUNIVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceaVlanGroup = ceaVlanGroup.setStatus('current')
if mibBuilder.loadTexts: ceaVlanGroup.setDescription('A collection of managed objects defining VLAN types.')
mibBuilder.exportSymbols("CISCO-ETHERNET-ACCESS-MIB", CeaVlanUNIType=CeaVlanUNIType, ceaConfig=ceaConfig, ciscoEthernetAccessMIB=ciscoEthernetAccessMIB, ceaPortTable=ceaPortTable, ceaVlanGroup=ceaVlanGroup, cEthernetAccessMIBGroups=cEthernetAccessMIBGroups, ceaPortEntry=ceaPortEntry, ceaMaxNNIPorts=ceaMaxNNIPorts, PYSNMP_MODULE_ID=ciscoEthernetAccessMIB, ceaMaxUNIVlanCommunityPorts=ceaMaxUNIVlanCommunityPorts, ciscoEthernetAccessMIBObjects=ciscoEthernetAccessMIBObjects, cEthernetAccessMIBCompliance=cEthernetAccessMIBCompliance, ceaPortGroup=ceaPortGroup, ceaPortType=ceaPortType, ceaUNIVlanType=ceaUNIVlanType, ciscoEthernetAccessMIBConform=ciscoEthernetAccessMIBConform, ceaGlobals=ceaGlobals, ceaUNIVlanEntry=ceaUNIVlanEntry, ceaPortCapability=ceaPortCapability, cEthernetAccessMIBCompliances=cEthernetAccessMIBCompliances, ceaUNIVlanTable=ceaUNIVlanTable)
