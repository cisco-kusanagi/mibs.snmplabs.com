#
# PySNMP MIB module ARISTA-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-PFC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Gauge32, IpAddress, ModuleIdentity, ObjectIdentity, Counter64, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Bits, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Counter64", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Bits", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaPfcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 11))
aristaPfcMIB.setRevisions(('2014-08-15 00:00', '2013-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaPfcMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses.', 'Initial version.',))
if mibBuilder.loadTexts: aristaPfcMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaPfcMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaPfcMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaPfcMIB.setDescription('Extensions for managing IEEE 802.1Qbb Priority-based Flow Control on Arista devices. This module extends IEEE8021-PFC-MIB by providing per class-of-service information for the supported Arista platforms.')
aristaPfc = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1))
aristaPfcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2))
class AristaPfcCOSIndex(TextualConvention, Integer32):
    description = 'A unique value for each Ethernet class-of-service priority'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

aristaPfcPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1), )
if mibBuilder.loadTexts: aristaPfcPriorityTable.setStatus('current')
if mibBuilder.loadTexts: aristaPfcPriorityTable.setDescription('This table contains the per class-of-service priority-flow-control information of an interface.')
aristaPfcPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1), ).setIndexNames((0, "ARISTA-PFC-MIB", "aristaPfcIfIndex"), (0, "ARISTA-PFC-MIB", "aristaPfcPriorityIndex"))
if mibBuilder.loadTexts: aristaPfcPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: aristaPfcPriorityEntry.setDescription('A list of attributes of each ingress class-of-service of an interface.')
aristaPfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaPfcIfIndex.setStatus('current')
if mibBuilder.loadTexts: aristaPfcIfIndex.setDescription('The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
aristaPfcPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 2), AristaPfcCOSIndex())
if mibBuilder.loadTexts: aristaPfcPriorityIndex.setStatus('current')
if mibBuilder.loadTexts: aristaPfcPriorityIndex.setDescription('The Ethernet class-of-service index for accessing the per-priority information of an interface.')
aristaPfcPriorityRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 3), Counter64()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcPriorityRequests.setStatus('current')
if mibBuilder.loadTexts: aristaPfcPriorityRequests.setDescription('A count of the invoked PFC M_CONTROL.request primitives with this priority class asserted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.')
aristaPfcPriorityIndications = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 4), Counter64()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcPriorityIndications.setStatus('current')
if mibBuilder.loadTexts: aristaPfcPriorityIndications.setDescription('A count of the received PFC M_CONTROL.indication primitives with this priority class asserted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.')
aristaPfcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1))
aristaPfcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2))
aristaPfcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1, 1)).setObjects(("ARISTA-PFC-MIB", "aristaPfcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPfcCompliance = aristaPfcCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaPfcCompliance.setDescription('The compliance statement for Arista switches that support Priority Flow Control (PFC).')
aristaPfcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2, 1)).setObjects(("ARISTA-PFC-MIB", "aristaPfcPriorityRequests"), ("ARISTA-PFC-MIB", "aristaPfcPriorityIndications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPfcGroup = aristaPfcGroup.setStatus('current')
if mibBuilder.loadTexts: aristaPfcGroup.setDescription('The group of required PFC objects.')
mibBuilder.exportSymbols("ARISTA-PFC-MIB", aristaPfcPriorityIndications=aristaPfcPriorityIndications, aristaPfcGroup=aristaPfcGroup, aristaPfcGroups=aristaPfcGroups, aristaPfcMIB=aristaPfcMIB, aristaPfcCompliance=aristaPfcCompliance, aristaPfc=aristaPfc, aristaPfcPriorityTable=aristaPfcPriorityTable, aristaPfcCompliances=aristaPfcCompliances, aristaPfcPriorityIndex=aristaPfcPriorityIndex, aristaPfcIfIndex=aristaPfcIfIndex, AristaPfcCOSIndex=AristaPfcCOSIndex, PYSNMP_MODULE_ID=aristaPfcMIB, aristaPfcPriorityRequests=aristaPfcPriorityRequests, aristaPfcPriorityEntry=aristaPfcPriorityEntry, aristaPfcConformance=aristaPfcConformance)
