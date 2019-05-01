#
# PySNMP MIB module CISCO-QINQ-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QINQ-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Bits, MibIdentifier, TimeTicks, NotificationType, Integer32, Gauge32, Unsigned32, IpAddress, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibIdentifier", "TimeTicks", "NotificationType", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoQinqVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 445))
ciscoQinqVlanMIB.setRevisions(('2004-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQinqVlanMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setLastUpdated('200411290000Z')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-7600@cisco.com')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setDescription("This MIB defines configuration and monitoring capabilities relating to 802.1QinQ interfaces. QinQ interfaces are capable of terminating QinQ traffic and translating QinQ tags. IEEE 802.1Q VLAN specification provides for an option to tag Ethernet frames with two VLAN tags: - An inner tag that specifies the customer's VLAN ID. This tag is called the 'CE VLAN'. - An outer tag that specifies the service provider's VLAN ID. This tag is called the 'metro tag', or the 'PE VLAN'. The combination of inner and outer VLAN tags is used to uniquely identify a particular customer's service flow.")
ciscoQinqVlanMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 0))
ciscoQinqVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1))
ciscoQinqVlanMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2))
cqvTermination = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1))
cqvTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2))
class CqvVlanIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC-2674, Bridge MIB Extensions, August 1999, Q-BRIDGE-MIB, E. Bell.'
    description = 'This textual convention is an extension of the VlanId convention. The VlanId convention defines a greater than zero value to identify a VLAN ID in the managed system. The CqvVlanIdOrZero convention defines the additional value of zero. The value zero is object specific and must therefore be defined as part of the description of any object that uses this syntax. An example of the usage of zero might include situations where the VLAN ID is unknown.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class CqvEncapsulationType(TextualConvention, Integer32):
    description = 'This textual convention defines the different types of VLAN trunking. isl - Inter Switch Link, the Cisco proprietary trunking protocol. dot1Q - IEEE 802.1Q trunking standard.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isl", 1), ("dot1Q", 2))

cqvTerminationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1), )
if mibBuilder.loadTexts: cqvTerminationTable.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationTable.setDescription("This table contains attributes pertaining to QinQ terminated interfaces. The ifIndex in the INDEX clause identifies the interface that terminates QinQ traffic. A management application can create a conceptual row in this table by setting the cqvTerminationRowStatus to 'createAndWait' or 'createAndGo'. A conceptual row in this table cannot be modified while cqvTerminationRowStatus is set to 'active'.")
cqvTerminationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationCeVlanId"))
if mibBuilder.loadTexts: cqvTerminationEntry.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationEntry.setDescription('An entry in this table defines a QinQ terminated interface.')
cqvTerminationPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setDescription('The VLAN ID of the outer tag of a QinQ frame.')
cqvTerminationCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 2), VlanId())
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setDescription('The VLAN ID of the inner tag of a QinQ frame.')
cqvTerminationPeEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 3), CqvEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationPeEncap.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationPeEncap.setDescription('The encapsulation type of the PE VLAN (cqvTerminationPeVlanId) of a QinQ frame.')
cqvTerminationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationRowStatus.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationRowStatus.setDescription('This object facilitates the creation, modification, or deletion of a conceptual row in this table.')
cqvTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1), )
if mibBuilder.loadTexts: cqvTranslationTable.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationTable.setDescription("This table defines the translations performed on QinQ capable interfaces. The ifIndex in the INDEX clause identifies the QinQ interface. A QinQ interface performs the following translations: - Double Tagged to Single Tagged - the inner and outer tags of the frames internal to the switch are replaced with a single trunk VLAN tag when the outgoing frame is transmitted. - Double Tagged to Double Tagged - the outer tag of the frames internal to the switch are replaced with an outer trunk VLAN tag when the outgoing frame is transmitted. The inner tag remains unchanged in the transmitted frame. The following picture illustrates QinQ translations. <----- Provider Side -----|----- Customer Side -----> Switch +--------------------------------+ | | | +---------------+ +-------| +------------------+ | | Double Tagged | | QinQ | | Single or Double | | | Frames | --> | Intf | --> | Tagged Frames | | +---------------+ +-------| +------------------+ | | +--------------------------------+ Also, the QinQ interface sets the IEEE 802.1P prioritization bits (P bits) in the outgoing frames by copying the P bits either from the internal frame's outer or inner VLAN tag. A management application can create a conceptual row in this table by setting the cqvTranslationRowStatus to 'createAndWait' or 'createAndGo'. A conceptual row in this table cannot be modified while cqvTranslationRowStatus is set to 'active'.")
cqvTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalCeVlanId"))
if mibBuilder.loadTexts: cqvTranslationEntry.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationEntry.setDescription('An entry in this table contains translation information for a particular QinQ interface.')
cqvTranslationInternalPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 1), CqvVlanIdOrZero())
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setDescription('The QinQ outer VLAN ID of an internal double tagged frame. This object will have the value of zero as described in the cqvTranslationType object.')
cqvTranslationInternalCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 2), CqvVlanIdOrZero())
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setDescription('The QinQ inner VLAN ID of an internal double tagged frame. This object will have the value of zero as described in the cqvTranslationType object.')
cqvTranslationTrunkPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 3), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setDescription('The QinQ outer VLAN ID of a trunk VLAN frame. This object will have the value of zero as described in the cqvTranslationType object.')
cqvTranslationTrunkCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 4), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setDescription('The QinQ inner VLAN ID of a trunk VLAN frame. This object will have the value of zero as described in the cqvTranslationType object.')
cqvTranslationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("doubleToSingle", 1), ("doubleToDouble", 2), ("doubleToDoubleOutOfRange", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationType.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationType.setDescription("The QinQ translation type being performed on the interface. 'doubleToSingle' - Double tagged to single tagged traffic. The value of cqvTranslationTrunkPeVlanId will be zero. This indicates that the PE VLAN tag will be absent in the trunk interface. 'doubleToDouble' - Double tagged to double tagged traffic. The value of the internal PE and CE, and the trunk PE and CE VLAN IDs are non-zero. 'doubleToDoubleOutOfRange' - Double tagged to double tagged traffic that does not have a defined translation. The value of cqvTranslationInternalCeVlanId will be zero. This indicates that the CE VLAN tag is being used as a wildcard.")
cqvTranslationCosPBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copyFromOuterTag", 1), ("copyFromInnerTag", 2))).clone('copyFromOuterTag')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationCosPBits.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationCosPBits.setDescription("This object indicates how the IEEE 802.1P bits (P bits) in the IEEE 802.1Q header of the trunk VLAN are to be set. The P bits in the trunk VLAN can be set by copying the P bits of the outer PE tag or the inner CE tag. 'copyFromOuterTag' - Copy the P bits from the outer PE tag. 'copyFromInnerTag' - Copy the P bits from the inner CE tag.")
cqvTranslationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationRowStatus.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationRowStatus.setDescription('This object facilitates the creation, modification, or deletion of a conceptual row in this table.')
ciscoQinqVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1))
ciscoQinqVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2))
ciscoQinQVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTerminationGroup"), ("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinQVlanMIBCompliance = ciscoQinQVlanMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoQinQVlanMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco QinQ MIB.')
ciscoQinqVlanTerminationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTerminationPeEncap"), ("CISCO-QINQ-VLAN-MIB", "cqvTerminationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTerminationGroup = ciscoQinqVlanTerminationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoQinqVlanTerminationGroup.setDescription('Objects for providing configuration for QinQ termination.')
ciscoQinqVlanTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 2)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkPeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkCeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationType"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationCosPBits"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTranslationGroup = ciscoQinqVlanTranslationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoQinqVlanTranslationGroup.setDescription('Objects for providing configuration for QinQ translation.')
mibBuilder.exportSymbols("CISCO-QINQ-VLAN-MIB", cqvTerminationEntry=cqvTerminationEntry, cqvTerminationRowStatus=cqvTerminationRowStatus, cqvTranslationTrunkPeVlanId=cqvTranslationTrunkPeVlanId, cqvTerminationPeVlanId=cqvTerminationPeVlanId, ciscoQinqVlanMIBCompliances=ciscoQinqVlanMIBCompliances, ciscoQinqVlanMIB=ciscoQinqVlanMIB, cqvTranslationInternalCeVlanId=cqvTranslationInternalCeVlanId, cqvTranslationInternalPeVlanId=cqvTranslationInternalPeVlanId, PYSNMP_MODULE_ID=ciscoQinqVlanMIB, cqvTranslationEntry=cqvTranslationEntry, cqvTermination=cqvTermination, ciscoQinqVlanMIBConform=ciscoQinqVlanMIBConform, cqvTranslationCosPBits=cqvTranslationCosPBits, ciscoQinQVlanMIBCompliance=ciscoQinQVlanMIBCompliance, cqvTranslationType=cqvTranslationType, cqvTranslationRowStatus=cqvTranslationRowStatus, cqvTranslationTrunkCeVlanId=cqvTranslationTrunkCeVlanId, ciscoQinqVlanTerminationGroup=ciscoQinqVlanTerminationGroup, cqvTranslation=cqvTranslation, ciscoQinqVlanTranslationGroup=ciscoQinqVlanTranslationGroup, ciscoQinqVlanMIBObjects=ciscoQinqVlanMIBObjects, cqvTranslationTable=cqvTranslationTable, ciscoQinqVlanMIBNotifs=ciscoQinqVlanMIBNotifs, cqvTerminationCeVlanId=cqvTerminationCeVlanId, ciscoQinqVlanMIBGroups=ciscoQinqVlanMIBGroups, cqvTerminationPeEncap=cqvTerminationPeEncap, CqvVlanIdOrZero=CqvVlanIdOrZero, cqvTerminationTable=cqvTerminationTable, CqvEncapsulationType=CqvEncapsulationType)
