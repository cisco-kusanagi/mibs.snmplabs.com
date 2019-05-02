#
# PySNMP MIB module ARISTA-VRF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-VRF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, ObjectIdentity, IpAddress, iso, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, Integer32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "IpAddress", "iso", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "Integer32", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaVrfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 18))
aristaVrfMIB.setRevisions(('2015-01-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaVrfMIB.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: aristaVrfMIB.setLastUpdated('201501110000Z')
if mibBuilder.loadTexts: aristaVrfMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaVrfMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaVrfMIB.setDescription('This MIB contains information related to Virtual Routing and Forwarding (VRF). VRF is a mechanism by which a single device can provide independent routing instances. This allows customers to virtually isolate network traffic, and also use overlapping IP addresses. Layer3 or routed interfaces in the system will belong to one VRF at a time. The datapath forwarding logic uses the VRF membership of the input interface to determine a specific forwarding table to use for routing the traffic. VRF can also be used to isolate management traffic from the rest of the data plane traffic. This MIB module provides the following pieces of information: * A table of all VRFs configured in the system * A table that contains the VRF membership information for all routed interfaces in the system by sparsely augmenting the ifTable.')
aristaVrfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1))
aristaVrfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2))
class VrfName(TextualConvention, OctetString):
    description = 'A human-readable identifier assigned to every VRF. The identifier is unique across all VRFs in the system.'
    status = 'current'
    displayHint = '100t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 100)

class VrfRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = "A route distinguisher as defined in [RFC4364], in the form '<admin>:<local>', where <admin> is the administrator ID (e.g., an AS number) and <local> is the locally assigned number."
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VrfState(TextualConvention, Integer32):
    description = 'The state of a specific VRF. When the administrator configures a VRF on the system, it stays inactive until a route distinguisher is assigned to it. Also, when the administrator deletes a VRF, there can be a small delay before the VRF is completely unconfigured from the system, during which time its status becomes inactive.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

aristaVrfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1), )
if mibBuilder.loadTexts: aristaVrfTable.setStatus('current')
if mibBuilder.loadTexts: aristaVrfTable.setDescription('This table contains information about VRFs currently configured in the system.')
aristaVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1), ).setIndexNames((0, "ARISTA-VRF-MIB", "aristaVrfName"))
if mibBuilder.loadTexts: aristaVrfEntry.setStatus('current')
if mibBuilder.loadTexts: aristaVrfEntry.setDescription('A single row containing information for one VRF that is configured in the system.')
aristaVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 1), VrfName())
if mibBuilder.loadTexts: aristaVrfName.setStatus('current')
if mibBuilder.loadTexts: aristaVrfName.setDescription('The name of the VRF that is represented by this row.')
aristaVrfRoutingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("ipv4", 0), ("ipv6", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfRoutingStatus.setStatus('current')
if mibBuilder.loadTexts: aristaVrfRoutingStatus.setDescription('The current status of data path routing in this VRF. Routing for IPv4 and IPv6 packets can be independently enabled by the administrator for a given VRF. This object carries the routing status for both the protocol versions. If data path routing is enabled for a protocol, the bit for the protocol is 1.')
aristaVrfRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 3), VrfRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: aristaVrfRouteDistinguisher.setDescription('The route distinguisher for this VRF.')
aristaVrfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 4), VrfState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfState.setStatus('current')
if mibBuilder.loadTexts: aristaVrfState.setDescription('The state of the VRF.')
aristaVrfIfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2), )
if mibBuilder.loadTexts: aristaVrfIfTable.setStatus('current')
if mibBuilder.loadTexts: aristaVrfIfTable.setDescription('This table augments the ifTable and contains the VRF membership information for every routed interface in the system. A row is present only for each active routed (or layer3) interface.')
aristaVrfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaVrfIfEntry.setStatus('current')
if mibBuilder.loadTexts: aristaVrfIfEntry.setDescription('VRF membership information for a single routed interface.')
aristaVrfIfMembership = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1, 1), VrfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfIfMembership.setStatus('current')
if mibBuilder.loadTexts: aristaVrfIfMembership.setDescription('The name of the VRF that this routed interface is currently part of.')
aristaVrfMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1))
aristaVrfMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2))
aristaVrfMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1, 1)).setObjects(("ARISTA-VRF-MIB", "aristaVrfInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaVrfMibCompliance = aristaVrfMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaVrfMibCompliance.setDescription('The compliance statement for Arista switches that implement the ARISTA-VRF-MIB.')
aristaVrfInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2, 1)).setObjects(("ARISTA-VRF-MIB", "aristaVrfRoutingStatus"), ("ARISTA-VRF-MIB", "aristaVrfRouteDistinguisher"), ("ARISTA-VRF-MIB", "aristaVrfState"), ("ARISTA-VRF-MIB", "aristaVrfIfMembership"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaVrfInformationGroup = aristaVrfInformationGroup.setStatus('current')
if mibBuilder.loadTexts: aristaVrfInformationGroup.setDescription('The collection of objects that provide VRF information in the system.')
mibBuilder.exportSymbols("ARISTA-VRF-MIB", aristaVrfMibGroups=aristaVrfMibGroups, aristaVrfIfMembership=aristaVrfIfMembership, aristaVrfIfTable=aristaVrfIfTable, aristaVrfMibCompliances=aristaVrfMibCompliances, VrfState=VrfState, aristaVrfRoutingStatus=aristaVrfRoutingStatus, aristaVrfMibObjects=aristaVrfMibObjects, VrfName=VrfName, aristaVrfIfEntry=aristaVrfIfEntry, aristaVrfTable=aristaVrfTable, VrfRouteDistinguisher=VrfRouteDistinguisher, PYSNMP_MODULE_ID=aristaVrfMIB, aristaVrfState=aristaVrfState, aristaVrfMIB=aristaVrfMIB, aristaVrfInformationGroup=aristaVrfInformationGroup, aristaVrfRouteDistinguisher=aristaVrfRouteDistinguisher, aristaVrfName=aristaVrfName, aristaVrfEntry=aristaVrfEntry, aristaVrfMibCompliance=aristaVrfMibCompliance, aristaVrfMibConformance=aristaVrfMibConformance)
