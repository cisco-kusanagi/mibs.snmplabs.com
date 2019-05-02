#
# PySNMP MIB module TOKENRING-STATION-SR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOKENRING-STATION-SR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:23:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, mib_2, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter32, iso, Counter64, NotificationType, ObjectIdentity, Gauge32, MibIdentifier, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "mib-2", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter32", "iso", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress")
RowStatus, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TextualConvention")
dot5SrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 42))
if mibBuilder.loadTexts: dot5SrMIB.setLastUpdated('9412161000Z')
if mibBuilder.loadTexts: dot5SrMIB.setOrganization('IETF Interfaces MIB Working Group')
if mibBuilder.loadTexts: dot5SrMIB.setContactInfo(' Keith McCloghrie Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 US Phone: +1 408 526 5260 Email: kzm@cisco.com')
if mibBuilder.loadTexts: dot5SrMIB.setDescription('The MIB module for managing source routes in end-stations on IEEE 802.5 Token Ring networks.')
dot5SrMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 1))
class SourceRoute(TextualConvention, OctetString):
    reference = 'Annex C of ISO/IEC 10038: 1993, [ANSI/IEEE Std 802.1D, 1993]'
    description = "Represents a Source Route, containing an embedded sequence of bridge and ring ID's, as used by 802.5 Source Routing."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

dot5SrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 42, 1, 1), )
if mibBuilder.loadTexts: dot5SrRouteTable.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteTable.setDescription('The table of source-routing routes. This represents the 802.5 RIF database.')
dot5SrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 42, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TOKENRING-STATION-SR-MIB", "dot5SrRouteDestination"))
if mibBuilder.loadTexts: dot5SrRouteEntry.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteEntry.setDescription("Information on a specific route. An entry is created whenever a 'Single Path Explorer' or an 'All Paths Explorer' discovers a route to a neighbor not currently in the table, or whenever an 'All Paths Explorer' discovers a better (e.g., shorter) route than the route currently stored in the table. This is done on behalf of any network layer client. The ifIndex value in the INDEX clause refers to the value of MIB-II's ifIndex object for the interface on which the route is in effect.")
dot5SrRouteDestination = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: dot5SrRouteDestination.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteDestination.setDescription('The destination of this route.')
dot5SrRouteControl = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteControl.setReference('Annex C of ISO/IEC 10038: 1993, [ANSI/IEEE Std 802.1D, 1993]')
if mibBuilder.loadTexts: dot5SrRouteControl.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteControl.setDescription('The value of Routing Control field for this route.')
dot5SrRouteDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 4), SourceRoute()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteDescr.setReference('Annex C of ISO/IEC 10038: 1993, [ANSI/IEEE Std 802.1D, 1993]')
if mibBuilder.loadTexts: dot5SrRouteDescr.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteDescr.setDescription("The embedded sequence of bridge and ring ID's for this route. For destinations on the local ring, the value of this object is the zero-length string.")
dot5SrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteStatus.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteStatus.setDescription("The status of this row. Values of the instances of dot5SrRouteControl and dot5SrRouteDescr can be modified while the row's status is 'active.")
dot5SrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2))
dot5SrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 1))
dot5SrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 2))
dot5SrCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 42, 2, 2, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrCompliance = dot5SrCompliance.setStatus('current')
if mibBuilder.loadTexts: dot5SrCompliance.setDescription('The compliance statement for SNMPv2 entities which implement the IEEE 802.5 Station Source Route MIB.')
dot5SrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 42, 2, 1, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteControl"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteDescr"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrRouteGroup = dot5SrRouteGroup.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteGroup.setDescription('A collection of objects providing for the management of source routes in stations on IEEE 802.5 source-routing networks.')
mibBuilder.exportSymbols("TOKENRING-STATION-SR-MIB", dot5SrCompliances=dot5SrCompliances, dot5SrRouteDestination=dot5SrRouteDestination, dot5SrMIBObjects=dot5SrMIBObjects, dot5SrRouteControl=dot5SrRouteControl, dot5SrRouteGroup=dot5SrRouteGroup, dot5SrMIB=dot5SrMIB, dot5SrRouteDescr=dot5SrRouteDescr, dot5SrGroups=dot5SrGroups, dot5SrRouteStatus=dot5SrRouteStatus, dot5SrConformance=dot5SrConformance, SourceRoute=SourceRoute, dot5SrRouteTable=dot5SrRouteTable, dot5SrRouteEntry=dot5SrRouteEntry, PYSNMP_MODULE_ID=dot5SrMIB, dot5SrCompliance=dot5SrCompliance)
