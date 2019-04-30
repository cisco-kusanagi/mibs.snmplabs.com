#
# PySNMP MIB module ARISTA-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-PFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Gauge32, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, iso, TimeTicks, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "iso", "TimeTicks", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaPfcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 11))
aristaPfcMIB.setRevisions(('2014-08-15 00:00', '2013-02-28 00:00',))
if mibBuilder.loadTexts: aristaPfcMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaPfcMIB.setOrganization('Arista Networks, Inc.')
aristaPfc = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1))
aristaPfcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2))
class AristaPfcCOSIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

aristaPfcPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1), )
if mibBuilder.loadTexts: aristaPfcPriorityTable.setStatus('current')
aristaPfcPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1), ).setIndexNames((0, "ARISTA-PFC-MIB", "aristaPfcIfIndex"), (0, "ARISTA-PFC-MIB", "aristaPfcPriorityIndex"))
if mibBuilder.loadTexts: aristaPfcPriorityEntry.setStatus('current')
aristaPfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaPfcIfIndex.setStatus('current')
aristaPfcPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 2), AristaPfcCOSIndex())
if mibBuilder.loadTexts: aristaPfcPriorityIndex.setStatus('current')
aristaPfcPriorityRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 3), Counter64()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcPriorityRequests.setStatus('current')
aristaPfcPriorityIndications = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 4), Counter64()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcPriorityIndications.setStatus('current')
aristaPfcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1))
aristaPfcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2))
aristaPfcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1, 1)).setObjects(("ARISTA-PFC-MIB", "aristaPfcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPfcCompliance = aristaPfcCompliance.setStatus('current')
aristaPfcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2, 1)).setObjects(("ARISTA-PFC-MIB", "aristaPfcPriorityRequests"), ("ARISTA-PFC-MIB", "aristaPfcPriorityIndications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPfcGroup = aristaPfcGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-PFC-MIB", aristaPfcConformance=aristaPfcConformance, aristaPfcIfIndex=aristaPfcIfIndex, aristaPfcCompliance=aristaPfcCompliance, aristaPfcPriorityEntry=aristaPfcPriorityEntry, aristaPfcMIB=aristaPfcMIB, AristaPfcCOSIndex=AristaPfcCOSIndex, aristaPfcPriorityIndex=aristaPfcPriorityIndex, aristaPfcGroup=aristaPfcGroup, aristaPfcPriorityTable=aristaPfcPriorityTable, aristaPfcPriorityIndications=aristaPfcPriorityIndications, PYSNMP_MODULE_ID=aristaPfcMIB, aristaPfcGroups=aristaPfcGroups, aristaPfc=aristaPfc, aristaPfcPriorityRequests=aristaPfcPriorityRequests, aristaPfcCompliances=aristaPfcCompliances)
