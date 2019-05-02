#
# PySNMP MIB module WWP-EGRESS-PORT-RESTRICTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-EGRESS-PORT-RESTRICTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, Counter64, ObjectIdentity, TimeTicks, Gauge32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Counter64", "ObjectIdentity", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "ModuleIdentity", "IpAddress")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpEgressPortRestrictionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 34))
wwpEgressPortRestrictionMIB.setRevisions(('2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setDescription('The MIB module for the WWP EGRESS-PORT-RESTRICTION cobjects.')
class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class VlanId(TextualConvention, Integer32):
    description = 'A 12-bit VLAN ID used in the VLAN Tag header.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpEgressPortRestrictionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1))
wwpEgressPortRestriction = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1))
wwpEgressPortRestrictionNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 2))
wwpEgressPortRestrictionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 2, 0))
wwpEgressPortRestrictionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3))
wwpEgressPortRestrictionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 1))
wwpEgressPortRestrictionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 2))
wwpEgressPortRestrictionTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: wwpEgressPortRestrictionTable.setStatus('current')
if mibBuilder.loadTexts: wwpEgressPortRestrictionTable.setDescription('A Table of EgressPortRestriction Entries.')
wwpEgressPortRestrictionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestVlanId"), (0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestPortId"))
if mibBuilder.loadTexts: wwpEgressPortRestrictionEntry.setStatus('current')
if mibBuilder.loadTexts: wwpEgressPortRestrictionEntry.setDescription('The EgressPortRestriction per vlan per source port Entry in the Table.')
wwpERestVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpERestVlanId.setStatus('current')
if mibBuilder.loadTexts: wwpERestVlanId.setDescription('Vlan ID for this instance of EgressPortRestrictionEntry. This Vlan Id should refer to the wwpVlanId in the WwpVlanEntry.')
wwpERestPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpERestPortId.setStatus('current')
if mibBuilder.loadTexts: wwpERestPortId.setDescription("The source port Id for this instance of EgressPortRestrictionEntry. Port ID's start at 1, and are consecutive for each additional port. This port Id should refer to the dot1dBasePort in the Dot1dBasePortEntry.")
wwpERestEgreesPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 3), PortList().clone(hexValue="0000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpERestEgreesPorts.setStatus('current')
if mibBuilder.loadTexts: wwpERestEgreesPorts.setDescription('The allowed egress ports on which Egress Port Restriction (EPR) allows for the configuration, on a per-port/per-Vlan basis.')
wwpERestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpERestStatus.setStatus('current')
if mibBuilder.loadTexts: wwpERestStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo'.")
mibBuilder.exportSymbols("WWP-EGRESS-PORT-RESTRICTION-MIB", wwpEgressPortRestrictionNotificationPrefix=wwpEgressPortRestrictionNotificationPrefix, wwpEgressPortRestrictionNotifications=wwpEgressPortRestrictionNotifications, wwpEgressPortRestrictionTable=wwpEgressPortRestrictionTable, wwpERestVlanId=wwpERestVlanId, wwpEgressPortRestriction=wwpEgressPortRestriction, VlanId=VlanId, wwpEgressPortRestrictionMIBCompliances=wwpEgressPortRestrictionMIBCompliances, wwpEgressPortRestrictionMIBGroups=wwpEgressPortRestrictionMIBGroups, PYSNMP_MODULE_ID=wwpEgressPortRestrictionMIB, wwpERestPortId=wwpERestPortId, wwpEgressPortRestrictionMIBObjects=wwpEgressPortRestrictionMIBObjects, wwpERestStatus=wwpERestStatus, PortList=PortList, wwpEgressPortRestrictionMIB=wwpEgressPortRestrictionMIB, wwpEgressPortRestrictionEntry=wwpEgressPortRestrictionEntry, wwpEgressPortRestrictionMIBConformance=wwpEgressPortRestrictionMIBConformance, wwpERestEgreesPorts=wwpERestEgreesPorts)
