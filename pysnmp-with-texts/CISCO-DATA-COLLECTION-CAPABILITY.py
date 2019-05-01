#
# PySNMP MIB module CISCO-DATA-COLLECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DATA-COLLECTION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, NotificationType, MibIdentifier, Integer32, Counter64, Gauge32, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "Gauge32", "ModuleIdentity", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDataCollectionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 425))
cDataCollectionCapability.setRevisions(('2007-08-07 00:00', '2005-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDataCollectionCapability.setRevisionsDescriptions(('Added Agent-Capability support for IOS 12.2SR.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cDataCollectionCapability.setLastUpdated('200708070000Z')
if mibBuilder.loadTexts: cDataCollectionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDataCollectionCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel:+1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: cDataCollectionCapability.setDescription('Agent capabilities for CISCO-DATA-COLLECTION-MIB')
cDataCollectionCapabilityV12R0S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setStatus('current')
if mibBuilder.loadTexts: cDataCollectionCapabilityV12R0S.setDescription('cisco-data-collection mib capabilities')
cDataCollectionCapabilityV12R1S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setStatus('current')
if mibBuilder.loadTexts: cDataCollectionCapabilityV12R1S.setDescription('cisco-data-collection mib capabilities')
mibBuilder.exportSymbols("CISCO-DATA-COLLECTION-CAPABILITY", cDataCollectionCapabilityV12R0S=cDataCollectionCapabilityV12R0S, cDataCollectionCapabilityV12R1S=cDataCollectionCapabilityV12R1S, cDataCollectionCapability=cDataCollectionCapability, PYSNMP_MODULE_ID=cDataCollectionCapability)
